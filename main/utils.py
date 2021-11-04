from .models import Account
def extract_user_data(data):
	if "callback_query" in data:
		user = data["callback_query"]["message"]["from"]
	else:
		user = data["message"]["from"]
	return {
	 "user_id":user["id"],
	 "first_name":user.get("first_name",""),
	 "last_name":user.get("last_name",""),

	}

def get_user(data):
	user_data = extract_user_data(data)
	account = Account.objects.filter(user_id=user_data.get("user_id"))

	if account.exists():
		account = account.first()
		for key,value in user_data.items():
			if hasattr(account,key):
				setattr(account,key,value)

		account.save()
	else:
		account = Account(**user_data)
		account.save()
	return account


def update_bot_step(account,step):
	account.bot_steps = step 
	account.save()
	return account


def get_message_text(data):
	if "callback_query" in data:
		text = data["callback_query"]["message"]["text"]
	else:
		text = data["message"]["text"]

	return text

def get_user_id(data):
	if "callback_query" in data:
		user_id = data["callback_query"]["from"]["id"]
	else:
		user_id = data["message"]["from"]["id"]
	return user_id


def get_callback_data(data):
	if "callback_query" in data:
		callback_data = data["callback_query"]["data"]
	else:
		callback_data = ""

	return callback_data


