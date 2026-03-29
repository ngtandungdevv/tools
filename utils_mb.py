import os
import base64
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO
import datetime

# ===========================
# DANH SÁCH PHÔI (nền ảnh)
# ===========================
PHOI_LIST = {
    "1": "https://i.imgur.com/PxAvv1c.png",
    "2": "https://i.imgur.com/rTJ5ETf.png",
    "3": "https://i.imgur.com/qTCMUtq.png",
    "4": "https://i.imgur.com/s09skKS.png",
    "5": "https://i.imgur.com/LeT3Kda.png",
    "6": "https://i.imgur.com/y2hAIV7.png",
    "7": "https://i.imgur.com/U5W9HaR.png",
    "8": "https://i.imgur.com/jmCD60P.png",
    "9": "https://i.imgur.com/dRxiFNh.png",
    "10": "https://i.imgur.com/iu7Vfqr.png",
    "11": "https://i.imgur.com/57j1W8S.png",
    "12": "https://i.imgur.com/1cwo7yO.png",
    "13": "https://i.imgur.com/K1JVXaK.png",
    "14": "https://i.imgur.com/htXWkry.png",
    "15": "https://i.imgur.com/1GK1mlM.jpeg",
    "16": "https://i.imgur.com/2iCnlaj.jpeg",
    "17": "https://i.imgur.com/4n7PaQW.jpeg",
    "18": "https://i.imgur.com/S0gQ5Bf.jpeg",
    "19": "https://i.imgur.com/Eq5eK9q.jpeg",
    "20": "https://i.imgur.com/8W7Ss1E.jpeg",
    "21": "https://i.imgur.com/4K0jjEj.jpeg"
}

# ===========================
# DANH SÁCH NỀN (Tên)
# ===========================
NEN_NAMES = {
    "1": "MB Mặc định",
    "2": "MB Cánh én mùa xuân",
    "3": "MB Dịu dàng",
    "4": "MB Mèo thần tài",
    "5": "MB Monday Mood",
    "6": "MB Năm mới rực rỡ",
    "7": "MB Nhịp đập sân cỏ",
    "8": "MB Tiến bước vững vàng",
    "9": "MB Tự hào Việt Nam",
    "10": "MB Hi Green",
    "11": "MB Khát vọng vươn cao",
    "12": "MB Bình an",
    "13": "MB Be The Sky",
    "14": "MB Sweet Love",
    "15": "MB Khám phá",
    "16": "MB Phố làng",
    "17": "MB Chinh phục đỉnh cao",
    "18": "MB Pickleball",
    "19": "MB Dream Big",
    "20": "MB Trẻ trung",
    "21": "MB Trường Sa xanh"
}

# ===========================
# CẤU HÌNH TOẠ ĐỘ + MÀU RIÊNG CHO TỪNG PHÔI
# ===========================
PHOI_CONFIG = {
    "1": {"money": (370, 460), "time": (50, 45), "pin": (835, 45), "money_color": "white", "time_color": "white"},
    "2": {"money": (370, 460), "time": (50, 45), "pin": (835, 45), "money_color": "white", "time_color": "white"},
    "3": {"money": (370, 460), "time": (50, 45), "pin": (835, 45), "money_color": "#331725", "time_color": "#222222"},
    "4": {"money": (370, 460), "time": (50, 45), "pin": (835, 45), "money_color": "#222222", "time_color": "#222222"},
    "5": {"money": (370, 460), "time": (50, 45), "pin": (835, 45), "money_color": "white", "time_color": "#222222"},
    "6": {"money": (370, 460), "time": (50, 45), "pin": (835, 45), "money_color": "white", "time_color": "white"},
    "7": {"money": (370, 460), "time": (50, 45), "pin": (835, 45), "money_color": "white", "time_color": "white"},
    "8": {"money": (370, 460), "time": (50, 45), "pin": (835, 45), "money_color": "white", "time_color": "white"},
    "9": {"money": (370, 460), "time": (50, 45), "pin": (835, 45), "money_color": "white", "time_color": "white"},
    "10": {"money": (370, 460), "time": (50, 45), "pin": (835, 45), "money_color": "#222222", "time_color": "#222222"},
    "11": {"money": (370, 460), "time": (50, 45), "pin": (835, 45), "money_color": "#222222", "time_color": "#222222"},
    "12": {"money": (370, 460), "time": (50, 45), "pin": (835, 45), "money_color": "#222222", "time_color": "#222222"},
    "13": {"money": (370, 460), "time": (50, 45), "pin": (835, 45), "money_color": "#222222", "time_color": "#222222"},
    "14": {"money": (370, 460), "time": (50, 45), "pin": (835, 45), "money_color": "#222222", "time_color": "#222222"},
    "15": {"money": (370, 460), "time": (50, 45), "pin": (835, 45), "money_color": "#222222", "time_color": "#222222"},
    "16": {"money": (370, 460), "time": (50, 45), "pin": (835, 45), "money_color": "white", "time_color": "white"},
    "17": {"money": (370, 460), "time": (50, 45), "pin": (835, 45), "money_color": "white", "time_color": "white"},
    "18": {"money": (370, 460), "time": (50, 45), "pin": (835, 45), "money_color": "#222222", "time_color": "#222222"},
    "19": {"money": (370, 460), "time": (50, 45), "pin": (835, 45), "money_color": "white", "time_color": "white"},
    "20": {"money": (370, 460), "time": (50, 45), "pin": (835, 45), "money_color": "#222222", "time_color": "#222222"},
    "21": {"money": (370, 460), "time": (50, 45), "pin": (835, 45), "money_color": "#222222", "time_color": "#222222"}
}

# ===========================
# FONT
# ===========================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FONT_MONEY = os.path.join(BASE_DIR, 'bot_vip', 'handlers', 'fonts', 'SF-Pro-Rounded-Bold.otf')
FONT_TIME = os.path.join(BASE_DIR, 'bot_vip', 'handlers', 'fonts', 'SF-Pro-Rounded-Bold.otf')
FONT_SIZE_MONEY = 50
FONT_SIZE_VND = 30
FONT_SIZE_TIME = 38

# ===========================
# ICON PIN
# ===========================
PIN_ICONS = {
    "100": "https://i.imgur.com/8sZpcNS.png",
    "80": "https://i.imgur.com/1sOMWFG.png",
    "60": "https://i.imgur.com/yNRzY1J.png",
    "40": "https://i.imgur.com/35UiCk0.png",
    "35": "https://i.imgur.com/RBjkxE2.png",
    "22": "https://i.imgur.com/iCy35zv.png",
    "10": "https://i.imgur.com/utEDaj5.png",
}

# ===========================
# HÀM HỖ TRỢ
# ===========================
def load_image_from_url(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    img = Image.open(BytesIO(response.content))
    return img.convert("RGBA")

def format_money(value: str) -> str:
    try:
        value = int(value)
        return f"{value:,}"
    except:
        return str(value)

def draw_text(draw, text, font, coords, color, image_width=None, center=False):
    if center and image_width:
        y = coords[1]
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        x = (image_width - text_width) // 2
        draw.text((x, y), text, font=font, fill=color)
    else:
        draw.text(coords, text, font=font, fill=color)

def draw_phoi(phoi_id, phoi_url, money, time_text, pin_level):
    base = load_image_from_url(phoi_url).convert("RGBA")
    draw = ImageDraw.Draw(base)

    if not os.path.exists(FONT_MONEY):
         raise FileNotFoundError(f"Font missing: {FONT_MONEY}")
    
    font_money = ImageFont.truetype(FONT_MONEY, FONT_SIZE_MONEY)
    font_vnd = ImageFont.truetype(FONT_TIME, FONT_SIZE_VND)
    font_time = ImageFont.truetype(FONT_TIME, FONT_SIZE_TIME)

    coords = PHOI_CONFIG.get(str(phoi_id), PHOI_CONFIG["1"])
    image_width = base.width
    money_color = coords.get("money_color", "#222222")

    money_x, money_y = coords["money"]
    draw.text((money_x, money_y), money, font=font_money, fill=money_color)

    money_width = draw.textlength(money, font=font_money)
    draw.text((money_x + money_width + 10, money_y + 20), "VND", font=font_vnd, fill=money_color)

    time_color = coords.get("time_color", "#222222")
    draw_text(draw, time_text, font_time, coords["time"], time_color, image_width, center=False)

    pin_url = PIN_ICONS.get(str(pin_level), PIN_ICONS["100"])
    pin_icon = load_image_from_url(pin_url).resize((55, 30))
    base.paste(pin_icon, coords["pin"], pin_icon)

    return base

def generate_mb_bank_base64(data):
    """Generates MB Bank Bill and returns Base64 string."""
    try:
        money = data.get("money", "100000")
        pin = str(data.get("pin", "100"))
        time_text = data.get("time", datetime.datetime.now().strftime("%H:%M"))
        nen_val = str(data.get("bg_id", "1"))

        phoi_url = PHOI_LIST.get(nen_val, PHOI_LIST["1"])
        formatted_money = format_money(money)

        img = draw_phoi(nen_val, phoi_url, formatted_money, time_text, pin)

        img_io = BytesIO()
        img.save(img_io, format="PNG")
        img_io.seek(0)
        img_b64 = "data:image/png;base64," + base64.b64encode(img_io.read()).decode('utf-8')

        return {
            "success": True,
            "image": img_b64
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }
