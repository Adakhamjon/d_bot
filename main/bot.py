from django.conf import settings
import json
import requests as r
def bot(method,data):
	try:
		response = r.post(settings.BASE_URL + method,json = data)
	except Exception as e :
		print(e)

	return json.loads(response.text)

def send_message(text,chat_id,menu=None,parse_mode="html"):
	data = {
	"text":text,
	"chat_id":chat_id,
	"parse_mode":parse_mode
	}
	if menu:
		data["reply_markup"] = menu 

	return bot("sendMessage",data)