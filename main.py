import time

from telegrambot import TelegramBot
from robot import SepRobot


robots = [SepRobot()]
last_message_id = 0

while True:
    # 1 обращаемся к телеграм за поседними сообщениями
    bot = TelegramBot()
    messages = bot.get_messages_as_json(last_message_id + 1)

    # 2 обработка ответа от телеграм

    for message in messages:
        # TODO
        last_message_id = max(last_message_id, message["update_id"])

        text = message["message"]["text"]
        chat_id = message["message"]["chat"]["id"]
        user = message["message"]["chat"]["first_name"]
        answer = ''
        for robot in robots:
            if robot.check(text):
                answer = f'{robot.do_command(text)}'
        result = bot.post_message_to_user(chat_id, answer)
        print(result)
        # 3 отправить ответ в телеграм
    time.sleep(1)
