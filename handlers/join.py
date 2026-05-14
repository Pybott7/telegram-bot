from pyrogram.handlers import ChatJoinRequestHandler
from pyrogram.types import ChatJoinRequest

from utils.database import save_user

import json
import os
import asyncio

# ==========================================
# JOIN REQUEST HANDLER
# ==========================================

async def join_request(client, request: ChatJoinRequest):

    user_id = request.from_user.id

    print(f"JOIN REQUEST: {user_id}")

    # ==========================================
    # APPROVE REQUEST
    # ==========================================

    try:

        await request.approve()

        print("APPROVED")

    except Exception as e:

        print(f"APPROVE ERROR: {e}")

        return

    # ==========================================
    # SAVE USER
    # ==========================================

    save_user(user_id)

    # ==========================================
    # CHECK WELCOME FILE
    # ==========================================

    if not os.path.exists("data"):

        os.makedirs("data")

    if not os.path.exists("data/welcome.json"):

        print("WELCOME NOT SET")

        return

    # ==========================================
    # LOAD WELCOME DATA
    # ==========================================

    try:

        with open("data/welcome.json", "r") as f:

            messages = json.load(f)

    except Exception as e:

        print(f"WELCOME LOAD ERROR: {e}")

        return

    # ==========================================
    # SEND ALL MESSAGES
    # ==========================================

    for msg in messages:

        try:

            await client.copy_message(
                chat_id=user_id,
                from_chat_id=msg["chat_id"],
                message_id=msg["message_id"]
            )

            await asyncio.sleep(1)

        except Exception as e:

            print(f"SEND ERROR: {e}")

    print("WELCOME SENT")

# ==========================================
# LOAD HANDLER
# ==========================================

def load_join_handler(app):

    app.add_handler(
        ChatJoinRequestHandler(join_request)
    )