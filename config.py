import os


class Config(object):
    API_HASH = os.environ.get("ddc284e5fdc33ef38845f7a5e9142f50")
    BOT_TOKEN = os.environ.get("7869076614:AAGX_Zxet7KTK0_7LauTvWan4h1jaS5B1xk")
    TELEGRAM_API = os.environ.get("22296245")
    OWNER = os.environ.get("5405110137")
    OWNER_USERNAME = os.environ.get("God_Of_Genjutsue")
    PASSWORD = os.environ.get("itachi")
    DATABASE_URL = os.environ.get("mongodb+srv://Outlawbots:Zoro@cluster0.huekk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    LOGCHANNEL = os.environ.get("-1002423590126")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", None)
    IS_PREMIUM = False
    MODES = ["video-video", "video-audio", "video-subtitle", "extract-streams"]
