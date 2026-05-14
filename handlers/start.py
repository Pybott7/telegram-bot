from pyrogram import filters

from utils.database import save_user

# ==========================================
# LOAD HANDLER
# ==========================================

def load_start_handler(app):

    # ==========================================
    # START COMMAND
    # ==========================================

    @app.on_message(filters.command("start"))
    async def start_command(client, message):

        user_id = message.from_user.id

        # Save User
        save_user(user_id)

        print(f"START USER: {user_id}")

        # Reply
        await message.reply_text(
            "Bot Active ✅"
        )
