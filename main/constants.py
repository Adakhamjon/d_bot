KB_TIMES="Namoz vaqtlari"
KB_EXCHANGE="Pul kurslari"
KB_NEWS="Yangiliklar"
KB_WEATHER="Ob havo"

KB_BACK = "GoBack"

KB_GREETING = "Assalomu Alekum"
# LANG_NO_TASKS = "sizda tasklar yo'q"


STATUS_MAIN_MENU = "MainMenu"
STATUS_TIMES  = "Times"

STATUS_EXCHANGE = "Exchange"

STATUS_NEWS = "News"

STATUS_WEATHER = "Weather"

class StepsMixin:
	BOT_STEPS = [
	(STATUS_MAIN_MENU, STATUS_MAIN_MENU),
	(STATUS_TIMES, STATUS_TIMES),
	(STATUS_EXCHANGE,STATUS_EXCHANGE),
	(STATUS_WEATHER,STATUS_WEATHER),
	 ]