import os

class Config(object):

      BOT_TOKEN = os.environ.get("BOT_TOKEN", "6065321925:AAE447qFGOZBhMJeDr413xE1d1_C8Jbbqno")
      API_ID = int(os.environ.get("API_ID", 16743442))
      API_HASH = os.environ.get("API_HASH", "12bbd720f4097ba7713c5e40a11dfd2a")
      
