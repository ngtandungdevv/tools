from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO
import datetime
import base64
import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PHOI_URL = "https://i.imgur.com/R0qWfzv.jpeg"

FONT_BOLD = os.path.join(CURRENT_DIR, "bot_vip", "handlers", "fonts", "Arial Bold.ttf")
FONT_REGULAR = os.path.join(CURRENT_DIR, "bot_vip", "handlers", "fonts", "SF-Pro-Rounded-Regular.otf")

BANK_INFO = {  
    "MB": {"logo": "https://i.imgur.com/dJXJiMz.png", "name": "MBBank (MB)"},  
    "VCB": {"logo": "https://i.imgur.com/elWpyWR.png", "name": "Vietcombank (VCB)"},  
    "TCB": {"logo": "https://i.imgur.com/Pjn8MYL.png", "name": "Techcombank (TCB)"},  
    "BIDV": {"logo": "https://i.imgur.com/30zY8oB.png", "name": "BIDV"},  
    "TPBANK": {"logo": "https://i.imgur.com/Hz4Q2wm.png", "name": "TP Bank (VPB)"},  
    "OCB": {"logo": "https://i.imgur.com/JBgN9yl.png", "name": "OCB"},  
    "AGB": {"logo": "https://i.imgur.com/h8E7kuk.png", "name": "Agribank (AGB)"},  
    "SHB": {"logo": "https://i.imgur.com/6J3HHG7.png", "name": "SHB"},  
    "VPBANK": {"logo": "https://i.imgur.com/HrgjHZ6.png", "name": "VP BANK (VPB)"},  
    "ACB": {"logo": "https://i.imgur.com/VyhnvZZ.png", "name": "ACB"},  
    "VTB": {"logo": "https://i.imgur.com/GwdNaXo.png", "name": "Viettinbank (CTG)"},  
}  

PIN_ICONS = {
    "100": "https://i.imgur.com/8sZpcNS.png",
    "80": "https://i.imgur.com/1sOMWFG.png",
    "60": "https://i.imgur.com/yNRzY1J.png",
    "40": "https://i.imgur.com/35UiCk0.png",
    "35": "https://i.imgur.com/RBjkxE2.png",
    "22": "https://i.imgur.com/iCy35zv.png",
    "10": "https://i.imgur.com/utEDaj5.png",
}

WEEKDAY_MAP = {
    "Monday": "Thứ Hai", "Tuesday": "Thứ Ba", "Wednesday": "Thứ Tư",
    "Thursday": "Thứ Năm", "Friday": "Thứ Sáu", "Saturday": "Thứ Bảy", "Sunday": "Chủ Nhật"
}

def format_money(value: str) -> str:
    try: return "{:,}".format(int(value))
    except: return value

def format_time(time_str: str) -> str:
    try:
        dt = datetime.datetime.strptime(time_str, "%H:%M %d/%m/%Y")
        weekday_vi = WEEKDAY_MAP.get(dt.strftime("%A"), dt.strftime("%A"))
        return dt.strftime(f"%H:%M {weekday_vi} %d/%m/%Y")
    except: return time_str

def load_image_from_url(url, size=None):
    try:
        res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
        res.raise_for_status()
        img = Image.open(BytesIO(res.content)).convert("RGBA")
        if size: img = img.resize(size)
        return img
    except: return None

def draw_text_right(draw, y, text, font, fill, x_end):
    if not text: return
    bbox = draw.textbbox((0, 0), text, font=font)
    draw.text((x_end - (bbox[2] - bbox[0]), y), text, font=font, fill=fill)

def generate_vcb_base64(data: dict) -> dict:
    try:
        bg = load_image_from_url(PHOI_URL)
        if bg is None: return {"success": False, "error": "Khong tai duoc phoi bill"}
        
        draw = ImageDraw.Draw(bg)
        try:
            font_mid = ImageFont.truetype(FONT_BOLD, 23)
            font_small = ImageFont.truetype(FONT_REGULAR, 50)
            font_vnd = ImageFont.truetype(FONT_REGULAR, 20)
            font_gio = ImageFont.truetype(FONT_REGULAR, 18)
        except OSError:
            return {"success": False, "error": f"Font file not found at {FONT_BOLD} or {FONT_REGULAR}"}

        # Pin
        pin_percent = str(data.get("pin", "100"))
        if pin_percent in PIN_ICONS:
            pin_icon = load_image_from_url(PIN_ICONS[pin_percent], size=(35, 35))
            if pin_icon:
                bg.paste(pin_icon, (bg.width - pin_icon.width - 25, 25), pin_icon)

        # So tien
        sotien = format_money(data.get("sotien", "0"))
        bbox_full = draw.textbbox((0, 0), sotien, font=font_small)
        x_money = (bg.width - (bbox_full[2] - bbox_full[0])) // 2
        draw.text((x_money, 302), sotien, font=font_small, fill="#0D472F")
        draw.text((x_money + (bbox_full[2] - bbox_full[0]) + 10, 312), "VND", font=font_vnd, fill="#555555")

        # Thoi gian
        thoigian_fmt = format_time(data.get("thoigian", datetime.datetime.now().strftime("%H:%M %d/%m/%Y")))
        bbox_time = draw.textbbox((0, 0), thoigian_fmt, font=font_gio)
        draw.text(((bg.width - (bbox_time[2] - bbox_time[0])) // 2, 370), thoigian_fmt, font=font_gio, fill="#555555")

        # Text list
        X_END = bg.width - 50
        draw_text_right(draw, 470, data.get("taikhoan", ""), font_mid, "black", X_END)
        draw_text_right(draw, 550, data.get("ten", "").upper(), font_mid, "black", X_END)

        bank = BANK_INFO.get(data.get("bank", "VCB").upper(), {})
        draw_text_right(draw, 625, bank.get("name", ""), font_mid, "black", X_END)
        
        if bank.get("logo"):
            bank_logo = load_image_from_url(bank["logo"], size=(50, 50))
            if bank_logo: bg.paste(bank_logo, (265, 615), bank_logo)

        draw_text_right(draw, 750, data.get("noidung", "CHUYEN TIEN"), font_mid, "black", X_END)
        draw_text_right(draw, 840, data.get("phi", "Miễn phí"), font_mid, "black", X_END)
        hinh_thuc = "Chuyển tiền trong Vietcombank" if data.get("bank","").upper() == "VCB" else "Chuyển tiền nhanh Napas 247"
        draw_text_right(draw, 945, data.get("hinhthuc", hinh_thuc), font_mid, "black", X_END)
        
        import random
        magd = data.get("magd", "") or str(random.randint(10000000000, 99999999999))
        draw_text_right(draw, 1020, magd, font_mid, "black", X_END)

        buffered = BytesIO()
        bg.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
        
        return {"success": True, "base64": f"data:image/png;base64,{img_str}"}
        
    except Exception as e:
        return {"success": False, "error": str(e)}
