"""main file to collect all patterns to send/recieve from printer"""

# strings to recieve some data
REQUEST_CONTROLL = '~M601 S1\r\n'
REQUEST_INFO = '~M115\r\n'
REQUEST_POSITION = '~M114\r\n'
REQUEST_TEMPERATURE = '~M105\r\n'
REQUEST_PROGRESS = '~M27\r\n'
REQUEST_STATUS = '~M119\r\n'

REQUESTS = {
			"controll": REQUEST_CONTROLL,
			"info": REQUEST_INFO, 
			"position": REQUEST_POSITION, 
			"temperature": REQUEST_TEMPERATURE, 
			"progress": REQUEST_PROGRESS,
			"status": REQUEST_STATUS
}

# regex fields for responses
TEMPS = ['T0', 'T1', 'B']
TEMPS_LONG = [item + '_actual' for item in TEMPS] + [item + '_target' for item in TEMPS]
INFOS = ['Type', 'Name', 'Firmware', 'SN', 'X', 'Y', 'Z', 'Count']
INFOS_LONG = ['Type', 'Name', 'Firmware', 'SN', 'X_max', 'Y_max', 'Z_max', 'Count']
AXIS = ['X', 'Y', 'Z', 'A', 'B']
STATUS = ['MachineStatus', 'MoveMode', 'Endstop']
PROGRESS = ['Printed', 'Total', 'Percentage']

NAMES = {
			"controll": None,
			"info": INFOS,
			"position": AXIS,
			"temperature": TEMPS,
			"progress": PROGRESS,
			"status": STATUS
		 }



def re_temp(field:str) -> str:
	'''T0:200 /200 T1:47 /0 B:49 /50'''

	return field + ':([0-9].*?) '


def re_temp_target(field:str) -> str:
	'''T0:200 /200 T1:47 /0 B:49 /50'''

	return field + r':[0-9].*? /([0-9].*?)[ \r\n]'


def re_pos(field:str) -> str:
	'''X:147.993 Y:74.9949 Z:150 A:0 B:0'''

	return field + ':(.+?)[ \\r\\n]'


def re_field(field:str) -> str:
    '''Machine Type: T-REX'''

    return field + ': ?(.+?)\\r\\n'


def re_pro(field:str) -> str:
	'''SD printing byte 12738825/12738824'''

	return r'([0-9].*)/([0-9].*?)\r'


PATTERN_LIST = {"controll": [],
				"info": [re_field],
				"position": [re_pos],
				"temperature": [re_temp, re_temp_target],
				"progress": [re_pro],
				"status": [re_field],
				}

assert PATTERN_LIST.keys() == REQUESTS.keys()
assert REQUESTS.keys() == NAMES.keys()
