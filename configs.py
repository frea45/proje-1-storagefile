# (c) @FarshidBand

import os


class Config(object):
	API_ID = int(os.environ.get("API_ID"))
	API_HASH = os.environ.get("API_HASH")
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	BOT_USERNAME = os.environ.get("BOT_USERNAME")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER"))
	DATABASE_URL = os.environ.get("DATABASE_URL")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", None)
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
🤖 **نام ربات :** [ذخیره ساز انواع فایل](https://t.me/{BOT_USERNAME})

🧑🏻‍💻 **سازنده ربات :** @FarshidBand

👥 **گروه پشتیبانی :** [Group](https://t.me/dlchinhub)

📢 **کانال پشتیبانی :** [Channel](https://t.me/SeriesPlus1)
"""
	ABOUT_DEV_TEXT = f"""
ابتدا در کانال خواسته شده عضو شوید‌.

سپس روی لینک درج شده داخل کانال 
کلیک کنید.

سپس به ربات هدایت میشوید روی start کلیک کنید فایل مورد نظر براتون ارسال میشه.


"""
	HOME_TEXT = """
**سلام [{}](tg://user?id={}) عزیز خوش آمدید ❤**\n\n**• من ربات ذخیره ساز انواع فایل هستم**.

**🎭 جهت دریافت فایل روی لینک های داخل کانال سریزپلاس کلیک کنید.

"""
