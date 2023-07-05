import telebot
from extensions import APIException, ValuteConvert
from name import  keys, TOKEN


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start','help'])
def help (message :telebot .types. Message):
    text = "Чтобы начать работу введите комманду боту в слудеющем формате: \n <имя валюты>\n " \
           "<в какую валюту, перевести>\n " \
           "<количество переводимой валюты>\n" \
           "Увидеть список всех доступых валют: /values"
    bot.reply_to(message,text)


@bot.message_handler(commands=['values'])
def values (message :telebot .types. Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text ='\n'.join((text, key, ))
    bot.reply_to(message,text)

@bot.message_handler(content_types=['text' ,])
def get_price (message :telebot .types. Message):
    try:
        values = message.text.split(' ')
        if len(values) != 3:
            raise APIException("Слишком много параметров ")

        quote, base, amount = values
        total_base = ValuteConvert.convert(quote, base, amount)
    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя \n{e}')

    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду \n{e}')
    else:
        text = f'Цена {amount} {quote} в {base} - {total_base}'
        bot.send_message(message.chat.id, text)


bot.polling()