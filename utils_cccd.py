import os
import base64
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import requests
from io import BytesIO
import datetime
import unicodedata

def remove_diacritics(text: str) -> str:
    """
    Xóa dấu tiếng Việt, trả về chuỗi ASCII in hoa
    """
    nfkd_form = unicodedata.normalize('NFKD', text)
    only_ascii = "".join([c for c in nfkd_form if not unicodedata.combining(c)])
    return only_ascii.upper()

# --- Link phôi ---
PHOI_FRONT = "https://i.imgur.com/VyCgafr.jpeg"   # phôi mặt trước
PHOI_BACK  = "https://i.imgur.com/0KbHn7v.jpeg"   # phôi mặt sau

# --- Các đường dẫn Font ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.path.join(BASE_DIR, 'bot_vip', 'handlers', 'fonts')
FONT_BOLD = os.path.join(FONT_DIR, 'Arial Bold.ttf')
FONT_REG  = os.path.join(FONT_DIR, 'Roboto-Regular.ttf')
FONT_MRZ = os.path.join(FONT_DIR, 'font.ttf')

# --- Tọa độ mặt trước ---
COORDS_FRONT = {
    "name": (620,780),
    "ngay_sinh": (620,940),
    "sex": (1440,940),
    "nation": (620,1070),
    "so_cccd": (620,610),
    "anh_the": (175, 475),   # vị trí ảnh thẻ
}

# --- Tọa độ mặt sau ---
COORDS_BACK = {
    "mrz1": (175,820),
    "mrz2": (175,910),
    "mrz3": (175,1000),
    "qr": (1360,75),
    "ngay_cap": (843,460),
    "thuong_tru_1": (140,160),
    "thuong_tru_2": (140,330),
    "ngay_het_han": (843,585),
}

# ============================================================
# Hàm cắt ảnh thẻ đúng tỉ lệ + làm mờ viền
# ============================================================
def process_avatar(anh_the_data, size=(380, 560)):
    # Có thể là Data URL dạng base64 (từ canvas upload) hoặc link http
    if anh_the_data.startswith('data:image'):
        header, encoded = anh_the_data.split(",", 1)
        img_data = base64.b64decode(encoded)
        img = Image.open(BytesIO(img_data)).convert("RGBA")
    elif anh_the_data.startswith('http'):
        resp = requests.get(anh_the_data, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
        img = Image.open(BytesIO(resp.content)).convert("RGBA")
    else:
        # Giả định base64 raw
        img_data = base64.b64decode(anh_the_data)
        img = Image.open(BytesIO(img_data)).convert("RGBA")

    # crop giữ tỉ lệ
    target_w, target_h = size
    target_ratio = target_w / target_h
    w, h = img.size
    ratio = w / h

    if ratio > target_ratio:  # quá ngang -> cắt 2 bên
        new_w = int(h * target_ratio)
        offset = (w - new_w) // 2
        img = img.crop((offset, 0, offset + new_w, h))
    elif ratio < target_ratio:  # quá dọc -> cắt trên dưới
        new_h = int(w / target_ratio)
        offset = (h - new_h) // 2
        img = img.crop((0, offset, w, offset + new_h))

    img = img.resize(size)

    # mask làm mờ viền
    mask = Image.new("L", size, 255)
    mask = mask.filter(ImageFilter.GaussianBlur(10))

    result = Image.new("RGBA", size, (0, 0, 0, 0))
    result.paste(img, (0, 0), mask)
    return result

# ============================================================
# Sinh MRZ chuẩn ICAO 9303 TD1
# ============================================================
def build_mrz(data):
    # --- Line 1 ---
    doc_type = "ID"
    country = "VNM"
    doc_number = data.get("so_cccd", "012345678901")
    mrz1 = f"{doc_type}{country}{doc_number}".ljust(30, "<")

    # --- Line 2 ---
    try:
        ngay_sinh = datetime.datetime.strptime(data.get("ngay_sinh", "01/01/2000"), "%d/%m/%Y").strftime("%y%m%d")
    except:
        ngay_sinh = "000101"

    sex_val = data.get("sex", "Nam")
    sex = sex_val.upper()[0] if sex_val else "<"
    
    try:
        ngay_het_han = datetime.datetime.strptime(data.get("ngay_het_han", "01/01/2040"), "%d/%m/%Y").strftime("%y%m%d")
    except:
        ngay_het_han = "400101"

    mrz2 = f"{ngay_sinh}{sex}{ngay_het_han}{country}".ljust(30, "<")

    # --- Line 3 (Name không dấu, upper, thay space bằng <) ---
    clean_name = remove_diacritics(data.get("name", "NGUYEN VAN A"))
    name_parts = clean_name.split()
    surname = name_parts[0] if len(name_parts) > 0 else ""
    given_names = "<".join(name_parts[1:]) if len(name_parts) > 1 else ""
    name_field = f"{surname}<<{given_names}"
    mrz3 = name_field.ljust(30, "<")

    return mrz1, mrz2, mrz3

# ============================================================
# Vẽ mặt trước
# ============================================================
def make_front(data):
    resp = requests.get(PHOI_FRONT, headers={"User-Agent": "Mozilla/5.0"})
    bg = Image.open(BytesIO(resp.content)).convert("RGBA")
    draw = ImageDraw.Draw(bg)

    font_b = ImageFont.truetype(FONT_BOLD, 80)
    font_name = ImageFont.truetype(FONT_REG, 60)
    font_r = ImageFont.truetype(FONT_REG, 50)

    draw.text(COORDS_FRONT["name"], data.get("name", "").upper(), font=font_name, stroke_width=0.5, fill="#17181a")
    draw.text(COORDS_FRONT["ngay_sinh"], data.get("ngay_sinh", ""), font=font_r, stroke_width=0.5, fill="#17181a")
    draw.text(COORDS_FRONT["sex"], data.get("sex", "Nam"), font=font_r, stroke_width=0.5, fill="#17181a")
    draw.text(COORDS_FRONT["nation"], data.get("nation", "Việt Nam"), font=font_r, stroke_width=0.5, fill="#17181a")
    draw.text(COORDS_FRONT["so_cccd"], data.get("so_cccd", ""), font=font_b, stroke_width=0.5, fill="#17181a")

    # ảnh thẻ
    if "anh_the" in data and data["anh_the"]:
        try:
            avatar = process_avatar(data["anh_the"])
            bg.paste(avatar, COORDS_FRONT["anh_the"], avatar)
        except Exception as e:
            print(f"Error processing avatar: {e}")

    return bg

# ============================================================
# Vẽ mặt sau (MRZ + QR)
# ============================================================
def make_back(data):
    resp = requests.get(PHOI_BACK, headers={"User-Agent": "Mozilla/5.0"})
    bg = Image.open(BytesIO(resp.content)).convert("RGBA")
    draw = ImageDraw.Draw(bg)

    font_mrz = ImageFont.truetype(FONT_MRZ, 85)
    font_r   = ImageFont.truetype(FONT_REG, 50)
    font_x  = ImageFont.truetype(FONT_REG, 55)
    
    # MRZ
    mrz1, mrz2, mrz3 = build_mrz(data)
    draw.text(COORDS_BACK["mrz1"], mrz1, font=font_mrz, stroke_width=0.75, fill="#17181a")
    draw.text(COORDS_BACK["mrz2"], mrz2, font=font_mrz, stroke_width=0.75, fill="#17181a")
    draw.text(COORDS_BACK["mrz3"], mrz3, font=font_mrz, stroke_width=0.75, fill="#17181a")

    # Ngày cấp, ngày hết hạn, địa chỉ
    draw.text(COORDS_BACK["ngay_cap"], data.get("ngay_cap", ""), font=font_r, stroke_width=0.5, fill="#17181a")
    draw.text(COORDS_BACK["ngay_het_han"], data.get("ngay_het_han", ""), font=font_r, stroke_width=0.5, fill="#17181a")
    draw.text(COORDS_BACK["thuong_tru_1"], data.get("thuong_tru_1", ""), font=font_x, stroke_width=0.5, fill="#17181a")
    draw.text(COORDS_BACK["thuong_tru_2"], data.get("thuong_tru_2", ""), font=font_x, stroke_width=0.5, fill="#17181a")

    # QR giống PHP
    qr_payload = (
        f'{data.get("so_cccd", "")}||'
        f'{data.get("name", "").upper()}|'
        f'{data.get("ngay_sinh", "").replace("/", "")}|'
        f'{data.get("sex", "Nam")}|'
        f'{data.get("thuong_tru_1", "")}|'
        f'{data.get("ngay_cap", "").replace("/", "")}'
    )

    qr_size = 470
    qr_url = (
        f'https://quickchart.io/qr?text={requests.utils.quote(qr_payload)}'
        f'&dark=000000&light=FFFFFF'
        f'&ecLevel=Q&format=png&size={qr_size}'
    )
    
    try:
        qr_resp = requests.get(qr_url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
        qr_img = Image.open(BytesIO(qr_resp.content)).convert("RGBA")

        # --- tách nền trắng thành trong suốt ---
        datas = qr_img.getdata()
        new_data = []
        for item in datas:
            if item[0] > 240 and item[1] > 240 and item[2] > 240:
                new_data.append((255, 255, 255, 0))
            else:
                new_data.append(item)
        qr_img.putdata(new_data)
        bg.alpha_composite(qr_img, COORDS_BACK["qr"])
    except Exception as e:
        print(f"Error generating QR: {e}")

    return bg

def generate_cccd_base64(data):
    """Generates both front and back CCCD images and returns Base64 representations."""
    try:
        front = make_front(data)
        back = make_back(data)

        # Encode Front
        front_io = BytesIO()
        front.save(front_io, format="PNG")
        front_io.seek(0)
        front_b64 = "data:image/png;base64," + base64.b64encode(front_io.read()).decode('utf-8')

        # Encode Back
        back_io = BytesIO()
        back.save(back_io, format="PNG")
        back_io.seek(0)
        back_b64 = "data:image/png;base64," + base64.b64encode(back_io.read()).decode('utf-8')

        return {
            "success": True,
            "front": front_b64,
            "back": back_b64
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }
