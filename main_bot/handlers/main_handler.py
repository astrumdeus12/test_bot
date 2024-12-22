from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram import Router
from ..chatbot.functions import get_bot_answer
from ..dao.functions.request_functions import create_request
from ..dto.request_model import RequestSchema
chatbot_router = Router()



@chatbot_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Приветствую! \n Чтобы начать пользоваться нейросетью просто отправьте запрос.')
    
@chatbot_router.message()
async def make_request(message : Message):
    user_message = message.text
    bot_answer = get_bot_answer(user_message)
    
    new_request = RequestSchema(user_tg_id=str(message.from_user.id), message=user_message, answer=bot_answer)
    
    await create_request(new_request)
    
    await message.reply(bot_answer, parse_mode='Markdown')
    



