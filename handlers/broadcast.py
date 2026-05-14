from pyrogram import filters
import asyncio

from config import ADMIN_ID
from utils.database import get_users

# ==========================================
# GLOBAL VARIABLE
# ==========================================

broadcast_mode = False

# ==========================================
# LOAD HANDLER
# ==========================================

def load_broadcast_handler(app):

    # ==========================================
    # START BROADCAST
    # ==========================================

    @app.on_message(
        filters.command("broadcast") &
        filters.user(ADMIN_ID)
    )
    async def broadcast_command(client, message):

        global broadcast_mode

        broadcast_mode = True

        await message.reply_text(
            "Send any message/photo/video for broadcast."
        )

    # ==========================================
    # SEND BROADCAST
    # ==========================================

    @app.on_message(
        filters.user(ADMIN_ID),
        group=1
    )
    async def broadcast_message(client, message):

        global broadcast_mode

        # Check Mode
        if not broadcast_mode:
            return

        # Ignore Commands
        if message.text and message.text.startswith("/"):

            return

        # Stop Broadcast Mode
        broadcast_mode = False

        # Get Users
        users = get_users()

        success = 0
        failed = 0

        # Start Message
        status = await message.reply_text(
            f"Broadcast Started ✅\n\nTotal Users: {len(users)}"
        )

        # ==========================================
        # SEND TO ALL USERS
        # ==========================================

        for user in users:

            try:

                # Copy Exact Message
                await message.copy(
                    int(user)
                )

                success += 1

                print(f"SENT TO: {user}")

                # Anti Flood
                await asyncio.sleep(1)

            except Exception as e:

                failed += 1

                print(f"BROADCAST ERROR ({user}): {e}")

        # ==========================================
        # FINAL STATUS
        # ==========================================

        await status.edit_text(
            f"Broadcast Complete ✅\n\nSuccess: {success}\nFailed: {failed}"
        )