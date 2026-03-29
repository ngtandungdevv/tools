from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO
import textwrap
from datetime import datetime
import base64
import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PHOI_URL = "https://i.imgur.com/alus95l.png"

# Font handling relative to bot_vip structure
FONT_BOLD = os.path.join(CURRENT_DIR, "bot_vip", "handlers", "fonts", "SVN-Arial 3 bold.ttf")
FONT_REGULAR = os.path.join(CURRENT_DIR, "bot_vip", "handlers", "fonts", "SVN-Arial Regular.ttf")

WEEKDAY_VI = {
    0: "THỨ HAI", 1: "THỨ BA", 2: "THỨ TƯ",
    3: "THỨ NĂM", 4: "THỨ SÁU", 5: "THỨ BẢY", 6: "CHỦ NHẬT"
}

COORDS = {
    "ngay_thang": (450, 450), "name": (89, 281), "code": (327, 375),
    "flight": (115, 609), "from_kh": (685, 545), "to_kh": (1105, 545),
    "from": (685, 600), "to": (1105, 600), "depart_time": (685, 715),
    "arrive_time": (1105, 715), "congve": (685, 890), "plane": (1520, 597),
    "duration": (115, 725), "seat": (115, 822), "ticket": (1385, 1110),
    "quang_duong": (1520, 760),
}

def format_date_vi(date_str: str, to: str):
    date_obj = datetime.strptime(date_str, "%d/%m/%Y")
    weekday = WEEKDAY_VI[date_obj.weekday()]
    day = date_obj.strftime("%d")
    month = date_obj.strftime("%m")
    year = date_obj.strftime("%Y")
    with_weekday = f"{weekday}, NGÀY {day}, THÁNG {month}"
    without_weekday = f"NGÀY {day}, THÁNG {month}, {year}     NGÀY {day}, THÁNG {month}, {year} CHUYẾN ĐI ĐẾN {to}"
    return with_weekday, without_weekday

def generate_vebay_base64(data: dict) -> dict:
    try:
        response = requests.get(PHOI_URL, headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()
        img = Image.open(BytesIO(response.content)).convert("RGBA")
        draw = ImageDraw.Draw(img)

        # Ensure fonts exist, fallback to default if missing
        try:
            font_bold = ImageFont.truetype(FONT_BOLD, 50)
            font_bold_4 = ImageFont.truetype(FONT_BOLD, 35)
            font_bold_2 = ImageFont.truetype(FONT_BOLD, 45)
            font_bold_3 = ImageFont.truetype(FONT_BOLD, 48)
            font_reg = ImageFont.truetype(FONT_REGULAR, 30)
            font_kh = ImageFont.truetype(FONT_REGULAR, 50)
            font_code = ImageFont.truetype(FONT_REGULAR, 35)
        except OSError:
            return {"success": False, "error": f"Font file not found at {FONT_BOLD} or {FONT_REGULAR}"}

        date_obj = datetime.strptime(data["ngay_thang"], "%d/%m/%Y")
        day = date_obj.strftime("%d")
        month = date_obj.strftime("%m")
        day_thg = f"(ngày {day}, tháng {month})"

        draw.text((685, 770), day_thg, font=font_bold_4, fill="black")
        draw.text((1105, 770), day_thg, font=font_bold_4, fill="black")

        ngay_with, ngay_without = format_date_vi(data["ngay_thang"], data["to"])
        draw.text(COORDS["ngay_thang"], ngay_with, font=font_bold_3, fill="black")

        wrapped_text = textwrap.fill(ngay_without, width=70)
        draw.text((89, 100), wrapped_text, font=font_bold_2, fill="black")

        draw.text(COORDS["name"], data["name"].upper(), font=font_bold, fill="black")
        draw.text((115, 1110), data["name"].upper(), font=font_code, fill="black")
        draw.text(COORDS["code"], data["code"].upper(), font=font_code, fill="black")
        draw.text(COORDS["flight"], f"VN {data['flight']}", font=font_bold, fill="black")
        draw.text(COORDS["from_kh"], data["from_kh"].upper(), font=font_kh, fill="black")
        draw.text(COORDS["to_kh"], data["to_kh"].upper(), font=font_kh, fill="black")

        from_text = "\n".join(textwrap.wrap(data["from"].upper(), width=17))
        draw.multiline_text(COORDS["from"], from_text, font=font_reg, fill="black", spacing=5)

        to_text = "\n".join(textwrap.wrap(data["to"].upper(), width=16))
        draw.multiline_text(COORDS["to"], to_text, font=font_reg, fill="black", spacing=5)

        draw.text(COORDS["depart_time"], data["depart_time"], font=font_kh, fill="black")
        draw.text(COORDS["arrive_time"], data["arrive_time"], font=font_kh, fill="black")

        congve = f"TERMINAL {data['congve']}"
        draw.text(COORDS["congve"], congve, font=font_code, fill="black")
        draw.text((1105, 890), congve, font=font_code, fill="black")
        draw.text(COORDS["quang_duong"], str(data["quang_duong"]), font=font_code, fill="black")

        plane_text = "\n".join(textwrap.wrap(data["plane"], width=17))
        draw.multiline_text(COORDS["plane"], plane_text, font=font_code, fill="black", spacing=5)

        draw.text(COORDS["duration"], data["duration"], font=font_reg, fill="black")
        draw.text(COORDS["seat"], data["seat"], font=font_reg, fill="black")
        draw.text(COORDS["ticket"], str(data["ticket"]), font=font_reg, fill="black")

        buffered = BytesIO()
        img.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
        
        return {"success": True, "base64": f"data:image/png;base64,{img_str}"}

    except Exception as e:
        return {"success": False, "error": str(e)}
