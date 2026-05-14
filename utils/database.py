import os

# ==========================================
# CREATE USERS FILE
# ==========================================

if not os.path.exists("users.txt"):

    with open("users.txt", "w") as f:
        pass

# ==========================================
# SAVE USER
# ==========================================

def save_user(user_id):

    user_id = str(user_id)

    try:

        with open("users.txt", "r") as f:

            users = f.read().splitlines()

    except Exception as e:

        print(f"READ ERROR: {e}")

        users = []

    if user_id not in users:

        try:

            with open("users.txt", "a") as f:

                f.write(f"{user_id}\n")

            print(f"NEW USER SAVED: {user_id}")

        except Exception as e:

            print(f"SAVE ERROR: {e}")

# ==========================================
# GET USERS
# ==========================================

def get_users():

    try:

        with open("users.txt", "r") as f:

            return f.read().splitlines()

    except Exception as e:

        print(f"GET USERS ERROR: {e}")

        return []
