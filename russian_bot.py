from chatterbot import ChatBot
from googletrans import Translator

class RussianBot:

	def __init__(self):
		self.translator = Translator()
		self.chatbot = ChatBot(
    		'GraphGrail',
    		filters=["chatterbot.filters.RepetitiveResponseFilter"],
    		trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
		)

	def train(self, corpus):
		self.chatbot.train(corpus)

	def get_response(self, question):
		question = self.translator.translate(question, src='ru', dest='en').text
		answer = self.chatbot.get_response(question)
		answer = self.translator.translate(str(answer), src='en', dest='ru').text
		return answer