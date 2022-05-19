import aminofix, pyfiglet, json
from colored import fore, style, attr
from os import listdir as ld, remove as rm
attr(0)
print(fore.BLUE + style.BOLD)
client = aminofix.Client()
print(""" 
Made by Xsarz
GitHub: https://github.com/xXxCLOTIxXx
Telegram Group: https://t.me/DxsarzUnion
Telegram: @DXsarz
YouTube: https://www.youtube.com/channel/UCNKEgQmAvt6dD7jeMLpte9Q/
""")
print(pyfiglet.figlet_format("AminoSave", font="slant"))
try:
	client.login(email='Почта', password='Пароль')

	print("Аккаунт авторизован")
except Exception as error:
	print(f"\nОшибка входа\n{error}\n");exit()
@client.event("on_text_message")
def text_handler(data):
	try:
		sub_client = aminofix.SubClient(comId=data.comId, profile=client.profile)
		comId = data.comId
		chatId = data.message.chatId
		author_n = data.message.author.nickname
		author_u = data.message.author.userId
		id = data.message.messageId
		ct = data.message.content
		content = ct.lower().split(" ")
		if content[0][0] == '/':
			if content[0][1:] == 'сохранить':
				try:
					fold = ld()
					chat = sub_client.get_chat_thread(chatId=chatId).json
					try:chatContent = chat['content']
					except:chatContent = None
					try:chatBackground= chat['extensions']['bm'][1]
					except:chatBackground = None

					chat_save = {'chatName': chat['title'], 'chatContent': chatContent, 'chatBackground': chatBackground, 'chatIcon': chat['icon']}
					with open(f'{chatId}_save.json', 'w') as file:
						json.dump(chat_save, file)
					if f'{chatId}_save.json' in fold:
						sub_client.send_message(chatId=chatId, message='Сохранение чата перезаписано✔')
					else:
						sub_client.send_message(chatId=chatId, message='Оформление чата сохранено✔')
				except Exception as error:
					print(error)
					sub_client.send_message(chatId=chatId, message='Произошла ошибка❌')
			elif content[0][1:] == 'восстановить':
				if f'{chatId}_save.json' not in ld():
					sub_client.send_message(chatId=chatId, message='Сохранение чата не найдено🧶')
				else:
					try:
						with open(f'{chatId}_save.json','r') as file:
							load_chat = json.load(file)
						sub_client.edit_chat(chatId=chatId, title=load_chat['chatName'], content=load_chat['chatContent'])
						try:
							sub_client.edit_chat(chatId=chatId, icon=load_chat['chatIcon'])
							sub_client.edit_chat(chatId=chatId, backgroundImage=load_chat['chatBackground'])
						except:
							sub_client.send_message(chatId=chatId, message='Оформление чата восстановлено✔')
					except Exception as error:
						print(error)
						sub_client.send_message(chatId=chatId, message='Произошла ошибка❌')
			elif content[0][1:] == 'удалить':
				try:
					if f'{chatId}_save.json' not in ld():
						sub_client.send_message(chatId=chatId, message='Сохранение чата не найдено🧶')
					else:
						rm(f'{chatId}_save.json')
						sub_client.send_message(chatId=chatId, message='Сохранение чата удалено✔')
				except:
					sub_client.send_message(chatId=chatId, message='Произошла ошибка❌')
			elif content[0][1:] == 'помощь':
				sub_client.send_message(chatId=chatId, message='[BC]Все команды\n/сохранить - сохранить оформление чата\n/восстановить - восстановить оформление чата по последнему сохранению\n/удалить - удалить сохранение этого чата')
	except Exception as ex:print(ex)
