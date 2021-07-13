import requests
import telebot
import random
import os
from telebot import types
bot = telebot.TeleBot("1862214466:AAHuF6ULZhH_t3cLafKJg5HuwNoADVnNDMs")
c = 0
g = 0
ch = 0
@bot.message_handler(commands=["start"])
def start(message):
	bot.send_message(message.chat.id,f"*Welcome @{message.chat.username}* To MF4 BOT\n\n/help => If You Need Help\n\n/startbruting => To Start Bruting Users",parse_mode="markdown")
	k = open("users.txt","r").read().splitlines()
	if message.chat.id in k:		
		pass
	else:
		f = open("users.txt","a")
		f.write(str(message.chat.id)+"\n")
		f.close
@bot.message_handler(commands=["help"])
def help(message):
	bot.send_message(message.chat.id,"*This Bot Maked By MF4\nDeveloper Username : @FFQ_Q*",parse_mode="markdown")
@bot.message_handler(commands=["startbruting"])
def brute(message):
	keyboard = telebot.types.ReplyKeyboardMarkup()
	keyboard.row('api','web')
	bot.send_message(message.chat.id,"*Choose From Buttons Below :*",parse_mode="markdown", reply_markup=keyboard)
@bot.message_handler(commands=["stop"])
def msg(message):
    bot.send_message(message.chat.id,"*Done Stopped !*",parse_mode="markdown")
    exit()
    os.system("python users.py")
@bot.message_handler(func=lambda message:True)
def check(message):
    global c , ch , g
    if message.text == "api":
    	keyboard1 = telebot.types.ReplyKeyboardMarkup()
    	keyboard1.row('Start Checking 50 users ...')
    	bot.send_message(message.chat.id,"*Checking 50 users ...*",parse_mode="markdown", reply_markup=keyboard1)
    	for i in range(50):
	    		user = "".join(random.choice("AAABBBCCCWWWNNNIIIMMMQQQ")for k in range(5))
	    		r = requests.get(f"https://cvcbnhfuu.ml/HMD/api/telegram.php/?User={user}")
	    		if "The Username is Available or Banned" in r.text:
	    			bot.send_message(message.chat.id,f"*New User \n@{user}*",parse_mode="markdown")
	    			g +=1
	    			ch +=1
	    			print(f"\r Error Users {c} Good Users {g} Checked {ch}",end="")
	    		else:
	    			c +=1
	    			ch +=1
	    			print(f"\r Error Users {c} Good Users {g} Checked {ch}",end="")
	    			pass
    	bot.send_message(message.chat.id,"*Done Checked 50 users ... !*",parse_mode="markdown")
    elif message.text == "web":
	    	bot.send_message(message.chat.id,"*Not Supported In This Time !*",parse_mode="markdown")
    else:
     		bot.send_message(message.chat.id,"*Please Send Valid Word !*",parse_mode="markdown")
	    			
	   
bot.polling()