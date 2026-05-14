from pyrogram import filters

from config import (
    ADMIN_ID,
    STORAGE_CHANNEL_ID
)

import os
import json

# ==========================================
# GLOBAL VARIABLES
# ==========================================

SETWELCOME_MODE = False

WELCOME_MESSAGES = []

# ==========================================
# LOAD HANDLER
# ==========================================

def load_setwelcome_handler(app):

    # ==========================================
    # START SETWELCOME
    # ==========================================

    @app.on_message(
        filters.command("setwelcome") &
        filters.user(ADMIN_ID)
    )
    async def setwelcome_command(client, message):

        global SETWELCOME_MODE
        global WELCOME_MESSAGES

        SETWELCOME_MODE = True

        WELCOME_MESSAGES = []

        os.makedirs("data", exist_ok=True)

        print("WELCOME SETUP STARTED")

        await message.reply_text(
            "Send all welcome messages.\n\nWhen finished send /done"
        )

    # ==========================================
    # DONE COMMAND
    # ==========================================

    @app.on_message(
        filters.command("done") &
        filters.user(ADMIN_ID)
    )
    async def done_command(client, message):

        global SETWELCOME_MODE
        global WELCOME_MESSAGES

        if not SETWELCOME_MODE:

            return await message.reply_text(
                "No active setup."
            )

        SETWELCOME_MODE = False

        if len(WELCOME_MESSAGES) == 0:

            return await message.reply_text(
                "No messages saved."
            )

        try:

            with open("data/welcome.json", "w") as f:

                json.dump(
                    WELCOME_MESSAGES,
                    f,
                    indent=4
                )

            print("WELCOME SYSTEM SAVED")

            print(WELCOME_MESSAGES)

            await message.reply_text(
                f"Welcome system saved ✅\n\nMessages: {len(WELCOME_MESSAGES)}"
            )

        except Exception as e:

            print(f"SAVE ERROR: {e}")

    # ==========================================
    # SAVE MESSAGES
    # ==========================================

    @app.on_message(filters.user(ADMIN_ID))
    async def save_welcome_message(client, message):

        global SETWELCOME_MODE
        global WELCOME_MESSAGES

        # Setup Mode Check
        if not SETWELCOME_MODE:
            return

        # Ignore Commands
        if message.text and message.text.startswith("/"):

            return

        try:

            copied = await message.copy(
                STORAGE_CHANNEL_ID
            )

            data = {

                "chat_id": copied.chat.id,
                "message_id": copied.id

            }

            WELCOME_MESSAGES.append(data)

            print(f"MESSAGE SAVED: {data}")

            print(WELCOME_MESSAGES)

            await message.reply_text(
                "Message added ✅"
            )

        except Exception as e:

            print(f"SAVE MESSAGE ERROR: {e}")
