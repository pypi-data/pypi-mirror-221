"""main module to get helper functions"""

try:
    from .patterns import PATTERN_LIST, REQUESTS, NAMES, TEMPS, TEMPS_LONG, INFOS_LONG
except ImportError:
    from patterns import PATTERN_LIST, REQUESTS, NAMES, TEMPS, TEMPS_LONG, INFOS_LONG

import socket
import asyncio
import re

import logging

from typing import Any, Callable

TIMEOUT_CONNECT = 10
TIMEOUT_TEST = 5
BUFFER = 1024
MAX_RETRY = 5
MAX_TESTS = 10
TIMEOUT_AWAIT = 30
UNAVAILABLE = None

_LOGGER = logging.getLogger(__name__)


async def printer_check(ip:str, port:int) -> bool:
    "returns True if printer currently recieves data. Else returns False"
    printer = socket.socket()
    printer.settimeout(TIMEOUT_TEST)
    loop = asyncio.get_event_loop()

    try:
        await loop.sock_connect(printer, (ip, port))
        recv = await loop.sock_recv(printer, BUFFER)

        _LOGGER.debug("recieved for test: %s", recv)

        clear = recv.decode().split('\r\n')
        for string in clear:
            if "ok" in string and "N" in string:
                _LOGGER.info("Printer currently recieving data. Skip connection to printer")
                return True
        _LOGGER.info("printer currently connected to another program")

    except OSError as err:
        _LOGGER.error("Something wrong happend with the OS while testing the connection. We got errormsg: %s" ,err)
    
    except TimeoutError:
        _LOGGER.info("Timeout while testing the printer, probably printer not connected to any other program")

    except ConnectionRefusedError:
        _LOGGER.warn("Could not connect to Server, probably a wrong ip or port or the printer is not running")

    finally:
        printer.close()

    return False



async def printer_call(ip:str, 
                       port:int, 
                       msg:list[str]) -> dict[str:str]:
    """sends a massage to the printer and awaits the return"""

    data = dict()

    printer = socket.socket()
    printer.settimeout(TIMEOUT_CONNECT)
    loop = asyncio.get_event_loop()

    try:
        await loop.sock_connect(printer, (ip, port))
        
        for message in msg:
            cmd = message[1:5]
            if not cmd[-1] in "0123456789":
                cmd = cmd[:-1]
            retry = 1
            broken = False
            while retry < MAX_RETRY:
                await loop.sock_sendall(printer, message.encode())
                recv = await loop.sock_recv(printer, BUFFER)
                _LOGGER.debug("Try %s, for command %s. Recieved: ", str(retry), str(cmd))
                _LOGGER.debug(recv)
                retry += 1
                rec_de = recv.decode()
                if "CMD " + cmd in rec_de:
                    broken = True
                    break
            if not broken:
                _LOGGER.warning("Could not get the desired result. Going on with empty string")
                rec_de = ""

            data[message] = rec_de

        _LOGGER.debug("Printer call ended")
        _LOGGER.debug("recieved data %s", str(data))

    except OSError as err:
        _LOGGER.error("Something wrong happend with the OS. We got errormsg: %s" ,err)
    
    except TimeoutError:
        _LOGGER.warning("Timeout while connecting to printer")

    except ConnectionRefusedError:
        _LOGGER.warn("Could not connect to Server, probably a wrong ip or port or the printer is not running")

    finally:
        printer.close()

    return data


async def printer_recv(ip:str, 
                       port:int, 
                       msg:list[str] ) -> dict[str:str]:
    """function to ensure that the connection responds in a reasonable time frame"""
    try:
        test = await asyncio.wait_for(printer_check(ip, port), timeout=TIMEOUT_AWAIT)
    except asyncio.exceptions.TimeoutError:
        _LOGGER.debug("Could not recieve data in given time. If this is the only message the printer is just not connected to any other program")
        test = False

    try:        
        if not test:
            data = await asyncio.wait_for(printer_call(ip, port, msg), timeout=TIMEOUT_AWAIT)
        else:
            data = {}
    except asyncio.exceptions.TimeoutError:
        _LOGGER.warning('Time out reached, probably printer is offline or a wrong message was send')
        data = {}

    return data

    
def decode_data(msg:str, key:list[str], fun:Callable[[str], str]) -> str:
    """encodes a string with a given pattern"""

    data = {}

    for field in key:
        re_string = fun(field)
        group = re.search(re_string, msg)

        if not group is None:
            data[field] = group.groups()[0]

            if len(group.groups()) > 1:
                data[field + "2"] = group.groups()[1]

        else:
            data[field] = UNAVAILABLE
            _LOGGER.info("Data of field %s could not be fetched. Used standart None.", field)

    return data


async def collect_data(ip:str, 
                 port:int,
                 msg:list[str]) -> dict[str:str]:

    data_dict = await printer_recv(ip, port, msg)#
    all_data = {}

    for command in data_dict:
        key = [k for k, v in REQUESTS.items() if v == command][0]

        for pattern in PATTERN_LIST[key]:

            data = decode_data(data_dict[command], 
                               NAMES[key],
                               pattern)

            if key == "progress":
                val1 = data[NAMES[key][0]]
                if not val1 is None:
                    val2 = data[NAMES[key][0]+"2"]
                else:
                    data[NAMES[key][0]] = UNAVAILABLE
                    data[NAMES[key][1]] = UNAVAILABLE
                    data[NAMES[key][2]] = UNAVAILABLE

                    _LOGGER.debug(str(data))
                    all_data = {**all_data, **data}
                    continue

                data = {}
                data[NAMES[key][0]] = val1
                data[NAMES[key][1]] = val2
                if val2 == "0":
                    data[NAMES[key][2]] = "0"
                else:
                    data[NAMES[key][2]] = f"{int(val1) / int(val2) * 100.0 :6.2f}"

            if key == "temperature":
                if pattern == PATTERN_LIST[key][0]:
                    s = "_actual"
                else:
                    s = "_target"

                data["T0" + s] = data.pop("T0")
                data["T1" + s] = data.pop("T1")
                data["B" + s] = data.pop("B")

            if key == "info":
                if not data["X"] is None:
                    data['X_max'] = data.pop("X").split(" ")[0]
                    data["Y_max"] = data.pop("Y").split(" ")[0]
                    data["Z_max"] = data.pop("Z")
                else:
                    data['X_max'] = data.pop("X", UNAVAILABLE)
                    data["Y_max"] = data.pop("Y", UNAVAILABLE)
                    data["Z_max"] = data.pop("Z", UNAVAILABLE)
   

            _LOGGER.debug(str(data))
            all_data = {**all_data, **data}

    return all_data


def purify_data(data:dict[str:str]) -> dict[str:dict[str:str]]:

    keys = list(NAMES.keys())[1:]
    beau_data = {}

    for key in keys:
        if "temperature" in key:
            sub_keys = TEMPS_LONG
        elif "info" in key:
            sub_keys = INFOS_LONG
        else:
            sub_keys = NAMES[key]

        sub_dict = {}
        for s_key in sub_keys:
            if not s_key in data:
                sub_dict[s_key] = None
            else:
                sub_dict[s_key] = data[s_key]

        beau_data[key] = sub_dict
    return beau_data


async def get_data(ip: str, port:int) -> dict:
    """base function to collect data from printer"""
    
    commands = list(REQUESTS.values())

    data = await collect_data(ip, port, commands)

    for value in NAMES.values():
        if value == TEMPS:
            value = TEMPS_LONG
        if value is None:
            continue
        for elm in value:
            if not elm in data:
                data[elm] = UNAVAILABLE
                _LOGGER.info("Could not get key %s in data, Using standart None instead", elm)

    return purify_data(data)




if __name__ == '__main__':
    ip = "192.168.178.98"
    port = 8899

    print( asyncio.run( get_data( ip, port ) ) )


    """{'~M601 S1\r\n': 'CMD M601 Received.\r\nControl Success.\r\nok\r\n', 
    '~M115\r\n': 'CMD M115 Received.\r\nMachine Type: T-REX\r\nMachine Name: My 3D Printer\r\nFirmware: V1.0.0 20200821\r\nSN: 400040-414e5019-20303347\r\nX: 227  Y: 148  Z: 150\r\nTool Count: 2\r\nok\r\n', 
    '~M114\r\n': 'CMD M114 Received.\r\nX:0 Y:0 Z:0 A:0 B:0\r\nok\r\n', 
    '~M105\r\n': 'CMD M105 Received.\r\nT0:23 /0 T1:23 /0 B:18 /0\r\nok\r\n', 
    '~M27\r\n': 'CMD M27 Received.\r\nSD printing byte 0/0\r\nok\r\n', 
    '~M119\r\n': 'CMD M119 Received.\r\nEndstop: X-max: 0 Y-max: 0 Z-min: 0\r\nMachineStatus: READY\r\nMoveMode: READY\r\nok\r\n'} """