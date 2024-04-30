import logging
from telegram import ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, ConversationHandler

from config import BOT_TOKEN1


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.DEBUG
)
logger = logging.getLogger(__name__)
#Все что связано с кнопками на клавиатуре пользователя
markup=ReplyKeyboardMarkup([['/where'],['/meny'],['/what_is_this'],['/vk'],['/help'],['/stop']],one_time_keyboard=False)

#старт бота с использованием имени пользователя
async def start(update, context):
    user = update.effective_user
    await update.message.reply_text(
        f'Здравствуте, {user.first_name}! Я бот, который ответит на все часто задаваемые вопросы о нашем проекте.Сколько вас? Что вы хотите узнать?',reply_markup=markup
        )
#помощник-справочкник с описанием команд
async def help(update,context):
    await update.message.reply_text('Для того чтобы узнать ответы на ваши вопросы, воспользуйтесь кнопками')
    await update.message.reply_text('"/where"-где начинается квест')
    await update.message.reply_text('"/meny"- о наших продуктах')
    await update.message.reply_text('"/what_is_this"- информация о нашем проекте')
    await update.message.reply_text('"/vk"-наше VK сообщество')
    await update.message.reply_text('"/stop"-окончание общения с ботом')
#функиция с расположением начальной точки
async def where_were_you(update,context):
    static_api_request = f"http://static-maps.yandex.ru/1.x/?ll=36.249187,54.511284&spn=0.001,0.001&l=map"
    await context.bot.send_photo(
            update.message.chat_id,
            static_api_request,
            caption="Наш квест начинается с 73 дома. Так что вперед к прохождению квеста. Незабываемы эмоции обеспечены."
        )
#функция с описанием продукции
async  def meny(update,context):
    await update.message.reply_text('И что же мы можем Вам предложит? Ну, пока что немного. Сейчас вы можете пройти только один квест, но мы не стоим на месте)')
#функция с описанием организации
async def what(update,context):
    await update.message.reply_photo('leg.png')
    await update.message.reply_text('Что же такое "Путешествие без компаса"? Это проект школьников одной из калужской школ, которые решили привлечь внимание сверстников к истории родного края. А сделали они это необычным спосаобом, создав квест.')
# дополнительный мессенджер
async def find(update, context):
    await update.message.reply_text('Ты спросишь: где нас найти? Ну, что лови ссылку?')
    await update.message.reply_text('https://vk.com/interestingkaluga')
#команда стоп
async def stop(update,context):
    await update.message.reply_text('До свидание! Ждем вас еще!')
    return ConversationHandler.END

def main():
    application = Application.builder().token('6344870568:AAHKg4y5jWc7twUCQ3HoIaBsjC_rCdBN0g0').build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help))
    application.add_handler(CommandHandler('where',where_were_you))
    application.add_handler(CommandHandler('meny',meny))
    application.add_handler(CommandHandler('what_is_this',what))
    application.add_handler(CommandHandler('vk',find))
    application.add_handler(CommandHandler('stop',stop))
    application.run_polling()


if __name__ == '__main__':
    main()
