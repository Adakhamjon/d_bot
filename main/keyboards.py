from .constants import *
def main_menu():
	keyboard = {
	"keyboard":[
	     [{"text":KB_TIMES},{"text":KB_EXCHANGE}],
	     [{"text":KB_NEWS},{"text":KB_WEATHER}],
	   "resize_keyboard": True,
	   "one_time_keyboard": True
	 ]
	}

	return keyboard