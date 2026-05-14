from pyrogram import filters

from config import ADMIN_ID
from utils.database import get_users

# ==========================================
# LOAD HANDLER
# ==========================================

def load_users_handler(app):

    # ==========================================
    # USERS COMMAND
    # ==========================================

    @app.on_message(
        filters.command("users") &
        filters.user(ADMIN_ID)
    )
    async def users_command(client, message):

        # Get Users
        users = get_users()

        total_users = len(users)

        print(f"TOTAL USERS: {total_users}")

        # Reply
        await message.reply_text(
            f"📊 Total Users: {total_users}"
        )