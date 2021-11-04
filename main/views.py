from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
import requests as r 
from django.http.response import JsonResponse
from main.bot import *
from main.utils import *
from main.keyboards import *
from main.models import *
from main.constants import *
@csrf_exempt
def index(request):
	response = {}
	if request.method == "POST":
		data = json.loads(request.body)

		text = get_message_text(data)
		user_id = get_user_id(data)
		callback_data = get_callback_data(data)

		account = get_user(data)


		if text == "/start":
			menu = main_menu()
			send_message(KB_GREETING,user_id,menu)
			update_bot_steps(account,STATUS_MAIN_MENU)


	return JsonResponse(response)

		
		
