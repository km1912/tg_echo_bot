import asyncio
from aiogram import Dispatcher, Bot
from config_data.config import Config, load_config

# async func main statement to make config and start bot
async def main() -> None:
    
    # load config
    config: Config = load_config()

    # initialization bot and dispatcher
    dp: Dispatcher = Dispatcher()
    bot: Bot = Bot(token=config.tg_bot.token)

    # missing accuumulated updates and start polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
