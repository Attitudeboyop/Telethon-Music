import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "26282779"))
    API_HASH = os.environ.get("API_HASH", "29a23eeb9974492a8fa89ba4e7e1efae")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5541240122:AAF09QOOU2NNpmtKw1wqM3SdtRkeWi0_kFM")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOH4BuxJBmQI-I5qXN8MI_4w6t-pdu813qq5SJm105KuigE-hFgrcLVU0TrXXh16cgj5ojf2q5iRGFXqUC2ryCMwKGvbQXCvUZ6g7aW1nX0orcEfGrJAFFH3d5Pwkb61JnkdEzWOoUPt8zfgfIylEne9dleyEaNt4L2eqiBcTdRbTWVuITG0qPm1GQx37CAEYADGYXCk0yfLOTBfzN0itCWZHodsxTvZYGPTbcLAZStsd_WEolE-DioUE_InKxhtj4L0SAbXBk4EOhBtMuh5eWTE85woX-p4ykwz-GRxsmCkwf97uYNRaTSydzPKcE1SeAUEVclvCsYbAXq0QvJg5q8d_Ao8=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "YKY_musicy_bot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "6075413841")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
