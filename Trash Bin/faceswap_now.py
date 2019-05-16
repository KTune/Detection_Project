{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import telebot   #импортируем телеграмную библиотеку\n",
    "bot = telebot.TeleBot('895248757:AAH7tjGZjkiRSyAOCInlSn4F0auuaqD55XE')     #подключаем токен бота"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "@bot.message_handler(content_types=['text'])   #объявляем слушателя для текстовых сообщений и метод их обработки\n",
    "def get_text_messages(message):\n",
    "    if message.text == \"Привет\":\n",
    "        bot.send_message(message.from_user.id, \"Привет, я бот Face Swap now! Чем могу помочь? :)\")\n",
    "    elif message.text == \"/help\":\n",
    "        bot.send_message(message.from_user.id, \"Давай-ка напиши мне привет.\")\n",
    "    else:\n",
    "        bot.send_message(message.from_user.id, \"Что-то непонятное говоришь. Напиши /help"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "bot.polling(none_stop=True, interval=0)    #постоянная аутенфикация с телеграмом"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
