import random

# Намерения = Intents
# Поздароваться, спросить как дела, спросить имя или чем занимаешься
# Заказать пиццу, отменить заказ, добавить больше сыра

# Конфигурация бота
BOT_CONFIG = {
    # Все намерения которые поддерживает наш бот
    "intents": {
        "hello": {
            "examples" : ["Привет", "Здарова", "Йо", "Приветос", "Хеллоу"],
            "responses": ["Здравстсвтсвтвтвуй человек", "И тебе не хворать", "Здоровее видали"],
        },
        "how_are_you": {
            "examples" : ["Как дела", "Чо каво", "Как поживаешь"],
            "responses": ["Маюсь Фигней", "Веду интенсивы", "Учу Пайтон"],
        }
    },
    # Фразы когда бот не может ответить
    "failure_phrases": ["Даже не знаю что сказать", "Поставлен в тупик", "Перефразируйте, я всего лишь бот"],
}

def printAnswer(text, examples, responses):
  for example in examples:  # Для каждого элемента списка examples
    if isMatch(text, example):  # Если пример совпадает с текстом пользователя
      print(random.choice(responses))  # Выводим на экран случайный элемент списка responses

text = input()

# Для каждого намерения, пытаемся напечатать ответ
for intent in BOT_CONFIG["intents"].values():
    printAnswer(text, intent["examples"], intent["responses"])


