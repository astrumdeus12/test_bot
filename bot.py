from config import dp, bot
from main_bot.handlers.main_handler import chatbot_router
import logging
import asyncio

async def main() -> None:
    
    dp.include_router(chatbot_router)
    
    await dp.start_polling(bot)
    


    
logging.basicConfig(level=logging.INFO)
asyncio.run(main())