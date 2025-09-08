import pandas as pd
from aiogram import Bot, Router, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()

# token = os.getenv("BOT_TOKEN")
# path = os.getenv("PATH_TO_TODO_TABLE")
path = "/Users/levakluev/Bot/bot/todo_result/todo_list.csv"
bot = Bot(token="8454391809:AAHGcnfarRcprOxBUMZX23GtJzlb0litfZs")
dp = Dispatcher()
router = Router()


def get_todo_data():
    return pd.read_csv(path)


@router.message(Command("start"))
async def start(message: Message):
    await message.answer("Hello!")


@router.message(Command("all"))
async def all_tasks(payload: Message):
    await payload.reply(f"```{get_todo_data().to_markdown()}```", parse_mode="Markdown")


@router.message(Command("add"))
async def add_task(payload: Message):
    text = payload.text.replace('/add', '').strip()
    new_task = pd.DataFrame({"text": [text], "status": ["active"]})
    updated_tasks = pd.concat([get_todo_data(), new_task], ignore_index=True, axis=0)
    updated_tasks.to_csv(path, index=False)

    await payload.reply(f"Добавил задачу {text}", parse_mode="Markdown")


@router.message(Command("done"))
async def complete_task(payload: Message):
    text = payload.text.replace('/done', '').strip()
    df = get_todo_data()
    df.loc[df.text == text, "status"] = "complete"
    df.to_csv(path, index=False)
    await payload.reply(f"Выполнено {text}", parse_mode="Markdown")


dp.include_router(router)


if __name__ == "__main__":
    dp.run_polling(bot)







