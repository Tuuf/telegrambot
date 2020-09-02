import telebot

from veri import amerika,sterlin,frank,kanada,kuveytdinar,norveckron,sudiriyal,japyen,bulgarleva,romenleyi,ruble,riyaliran,yuan,katarriyali,pakistanrubi
yazı="123"
token='1308347668:AAHEdpzCbc9He_PH-VnnFxdpQ73U0vm-WYg'
#grupli
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "merhaba ben bir Döviz botuyum daha fazla bilgi için ve komut bilgileri için  /bilgi komutunu uygulamanızı rica edeceğim . düşüncelerinizi hasario@protonmail.com adresine yazabilirsiniz")
#ne yazarsan / ıle gonderıyor
#veris=requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id': id, 'text': yazı}).json()

döviz_veri='''
 /döviz komutu ile döviz bilgilerine ulaşabilirsiniz
 /isviçrefrankı komutu ile İsviçre Frankı  bilgilerine ulaşabilirsiniz
 /ingilizsterlin komutu ile ingiliz Sterlini bilgilerine ulaşabilirsiniz
 /abddoları komutu ile Amerikan Doları  bilgilerine ulaşabilirsiniz
  .
'''
@bot.message_handler(commands=['bilgi' ])
def send_welcome(message):
    bot.reply_to(message,text=döviz_veri)



@bot.message_handler(commands=['döviz' ])
def send_welcome(message):

    bot.reply_to(message,text=str("Amerikan Doları:") + str(amerika))
    bot.reply_to(message,text=str("İngiliz Sterlini: ") + str(sterlin))
    bot.reply_to(message,text=str("İsviçre Frankı: ")+str(frank))
    bot.reply_to(message,text=str("Kanada Doları: ")+str(kanada))
    bot.reply_to(message,text=str("Kuveyt Dinarı: ")+str(kuveytdinar))
    bot.reply_to(message,text=str("Norvec Kronu: ")+str(norveckron))
    bot.reply_to(message,text=str("Suudi Arabistan Riyali ")+str(sudiriyal))
    bot.reply_to(message,text=str("Japon Yeni: ")+str(japyen))
    bot.reply_to(message,text=str("Bulgar Levası:")+str(bulgarleva))
    bot.reply_to(message,text=str("Romen Leyi:")+str(romenleyi))
    bot.reply_to(message,text=str("Rus Rublesi:")+str(ruble))
    bot.reply_to(message,text=str("İran Riyali:")+str(riyaliran))
    bot.reply_to(message,text=str("Çin Yuanı:")+str(yuan))
    bot.reply_to(message,text=str("Katar Riyali:")+str(katarriyali))
    bot.reply_to(message,text=str("Pakistan Rupisi:")+str(pakistanrubi))
    bot.reply_to(message,text="beklettim sanırım neyse çay kahve ? " )



@bot.message_handler(commands=['abddoları'])
def send_welcome(message):
    bot.reply_to(message, text=str("Amerikan Doları:") + str(amerika))


@bot.message_handler(commands=['ingilizsterlini'])
def send_welcome(message):
    bot.reply_to(message, text=str("İngiliz Sterlini: ") + str(sterlin))


@bot.message_handler(commands=['isviçrefrankı'])
def send_welcome(message):
    bot.reply_to(message, text=str("İsviçre Frankı: ") + str(frank))











#send_message(chat_id=id,text="Merhaba Dünya")

bot.polling()
