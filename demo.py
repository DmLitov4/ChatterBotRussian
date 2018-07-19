import chatterbot
from googletrans import Translator
from russian_bot import RussianBot

chat = RussianBot()
chat.train("chatterbot.corpus.english")
print('Bot is ready!')

while True:
	inp = input()
	ans = chat.get_response(inp)
	print(ans)
