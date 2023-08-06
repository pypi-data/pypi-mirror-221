"""Base of the package. Controlles collection of data and manages connections"""

import datetime
import time
import asyncio
import logging


try:
    from .utils import get_data
except ImportError:
    from utils import get_data


print(__name__)

logging.getLogger('trexprinterapi').addHandler(logging.NullHandler())

_LOGGER = logging.getLogger(__name__)


class TRexObserver():
    """Base class of the package manages all socket calls"""

    def __init__(self, ip:str , port:int=8899, scan_intervall:int=600):

        self.ip = ip
        self.port = port
        self.scan_intervall = datetime.timedelta(seconds=scan_intervall)
        self.data = None
        self._last_check = datetime.datetime(year=datetime.MINYEAR, month=1, day=1)
        
    def update_server(self, ip:str=None, port:int=None, scan_intervall:int=None):
        if not (ip is None):
            self.ip = ip
        
        if not (port is None):
            self.port = port

        if not (scan_intervall is None):
            self.scan_intervall = scan_intervall

        _LOGGER.info("Updated Server config successfully")

    async def get(self):
        now = datetime.datetime.now()
        if now - self._last_check >= self.scan_intervall:
            _LOGGER.debug("time since last check to long, start polling data")
            await self._collect_data()
            _LOGGER.info("Collected new data nuccessfuly")
        
        return self.data

    async def force_get(self):
        await self._collect_data()
        _LOGGER.info("Forcefully collected new data nuccessfuly")
        return self.data

    async def _collect_data(self):
        self.data = await get_data(self.ip, self.port)
        self._last_check = datetime.datetime.now()


if __name__ == "__main__":

    trex = TRexObserver('192.168.178.98', scan_intervall=60)

    print(asyncio.run(trex.get()))






