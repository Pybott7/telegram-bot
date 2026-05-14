from pyrogram import Client

from config import (
    API_ID,
    API_HASH,
    BOT_TOKEN
)

from handlers.join import load_join_handler
from handlers.start import load_start_handler
from handlers.users import load_users_handler
from handlers.broadcast import load_broadcast_handler
from handlers.setwelcome import load_setwelcome_handler

# ==========================================
# CREATE BOT CLIENT
# ==========================================

app = Client(
    "bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# ==========================================
# LOAD HANDLERS
# ==========================================

load_join_handler(app)
load_start_handler(app)
load_users_handler(app)
load_broadcast_handler(app)
load_setwelcome_handler(app)

# ==========================================
# START BOT
# ==========================================

print("BOT RUNNING ✅")

app.run()
