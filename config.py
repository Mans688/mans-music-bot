from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "19697852")) #لا تغير هاذة القيمة
API_HASH = getenv("API_HASH", "ec1826f77dae9cfaa78bc161b5af05b4")#لا تغير هاذة القيمة
BOT_TOKEN = getenv("BOT_TOKEN", "5351917074:AAHTJYsGjavFjfmFVjAKHr1R0cGZtIxMbnU")
SESSION_NAME = getenv("SESSION_NAME", "BAB8Ec83fsUBoxSb6niVpmYbWg2L87euqH4g8_YyoWtMXLRonFPDZCL1B8nZwiPWJYVHiBGHMFjIZ4QVR4ilBRHJ1U9s19CVOURg_ykJfmpanYXFLayqLHHwP5RqnW-p5OLaxRINn8FTW7zQxeeFdwdFOfDxPwP6VWi5jxE5Qv-Cdg-aECih7U0D8ncVqhHAfjpI0HcA86orO9oG47WNn5abRlPGkR0nyXIQiS0T9G6gVL8HcKLmaRy82KzclQKOlzNpOT-jokozafdesFrG09m2wlVSA2abXQ2VdlUyohvUU8hAAEvYbNUnv8c9UvmczHhafsK_Jyv-pVwrxg91U3dhAAAAATq-NBMA")

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME", "vip_D_A_D") # @ هنا ضع يوزر حسابك بدون 
ALIVE_NAME = getenv("ALIVE_NAME", "frank") # هنا ضع اسم حسابك
BOT_USERNAME = getenv("BOT_USERNAME", "M_A_N_S578BOT") # @ هنا ضع يوزر البوت بدون 
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/X02lx/RrRRR") 
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main") #لا تغير هاذة القيمة
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60")) #لا تغير هاذة القيمة
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "BAR_V_I_P") # @ هنا ضغ يوزر كروبك بدون 
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "M_8_S_H7") # @ هنا ضغ يوزر قناتك بدون

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "").split())
OWNER_ID = list(map(int, getenv("OWNER_ID", "5545885396").split()))
                                             #هنا ضع ايدي المطور فوق و الاعلئ
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5545885396").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.png")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.png")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d70bb6fa92728763c671f.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/430dcf25456f2bb38109f.png")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cd5c96a3c7e8ae1913ef3.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
