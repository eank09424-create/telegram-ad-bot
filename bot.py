from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor

TOKEN = "8574531684:AAGfuLYkRkvRilIG8wc6EuVdBlChdycAmvc"
CHANNEL = "@vip_deals_here"
ADSTERRA_LINK = "https://www.effectivegatecpm.com/ybh3jtc9w?key=d2d0de24d378fcbb8c8ec854f6450563"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

async def is_joined(user_id):
    try:
        member = await bot.get_chat_member(CHANNEL, user_id)
        return member.status in ["member", "administrator", "creator"]
    except:
        return False

@dp.message_handler(commands=["start"])
async def start(msg):
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(
        InlineKeyboardButton("📢 Join Channel", url="https://t.me/vip_deals_here"),
        InlineKeyboardButton("✅ Check Join", callback_data="check"),
        InlineKeyboardButton("▶ Play (Locked)", callback_data="locked")
    )
    await msg.answer("Bot use karne ke liye pehle channel join karo 👇", reply_markup=kb)

@dp.callback_query_handler(lambda c: c.data == "check")
async def check(call):
    if await is_joined(call.from_user.id):
        kb = InlineKeyboardMarkup()
        kb.add(InlineKeyboardButton("▶ Play", callback_data="play"))
        await call.message.edit_text("Play unlocked ✅", reply_markup=kb)
    else:
        await call.answer("❌ Pehle join karo!", show_alert=True)

@dp.callback_query_handler(lambda c: c.data == "play")
async def play(call):
    if not await is_joined(call.from_user.id):
        await call.answer("Join first!", show_alert=True)
        return

    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("👉 Watch Ad", url=ADSTERRA_LINK))
    await call.message.answer("Click below 👇", reply_markup=kb)

executor.start_polling(dp)
