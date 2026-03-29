import discord
from discord.ext import commands
from discord import app_commands
import threading
import time
import subprocess
import os
import json
import re
from datetime import datetime, timedelta
from threading import Lock
from dotenv import load_dotenv

# Load biến môi trường từ file .env
load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_BOT_SPAM_TOKEN')
ALLOWED_GUILD_ID = 1470638794750558424  
ADMIN_ID = 1174711992225894474          
LOGS_CHANNEL_ID = 1476888558261244006 

admins = {ADMIN_ID}
user_keys = {}
allowed_users = set()
blacklist = []
spam_processes = {}
spam_users = {}
user_spam_count = {}
user_spam_time = {}
last_usage = {}
full_spam_processes = {}
super_users = set()
super_keys = {}
bot_active = True
lock = Lock()

SUPER_VIP_FILE = 'super_vip.json'
SPAM_COUNT_FILE = 'spam_count.json'
BLACKLIST_FILE = 'blacklist.json'

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)
tree = bot.tree


async def send_log(embed: discord.Embed):
    """Gửi embed log vào kênh logs"""
    try:
        channel = bot.get_channel(LOGS_CHANNEL_ID)
        if channel:
            await channel.send(embed=embed)
    except Exception as e:
        print(f"[LOG ERROR] {e}")

def send_log_sync(embed: discord.Embed):
    """Gửi log từ luồng không phải async"""
    import asyncio
    asyncio.run_coroutine_threadsafe(send_log(embed), bot.loop)

def mask_sdt(sdt):
    if len(sdt) == 10:
        return f"{sdt[:3]}xxxx{sdt[-3:]}"
    return sdt

def get_network_provider(sdt):
    network_providers = {
        '086': 'Viettel', '096': 'Viettel', '097': 'Viettel', '098': 'Viettel',
        '032': 'Viettel', '033': 'Viettel', '034': 'Viettel', '035': 'Viettel',
        '036': 'Viettel', '037': 'Viettel', '038': 'Viettel', '039': 'Viettel',
        '091': 'VinaPhone', '094': 'VinaPhone', '088': 'VinaPhone', '081': 'VinaPhone',
        '082': 'VinaPhone', '083': 'VinaPhone', '084': 'VinaPhone', '085': 'VinaPhone',
        '089': 'MobiPhone', '090': 'MobiPhone', '093': 'MobiPhone', '076': 'MobiPhone',
        '077': 'MobiPhone', '078': 'MobiPhone', '079': 'MobiPhone', '070': 'MobiPhone',
        '058': 'Vietnamobile', '052': 'Vietnamobile', '056': 'Vietnamobile', '092': 'Vietnamobile',
    }
    return network_providers.get(sdt[:3], 'Không xác định')

def get_remaining_days(expiration_time):
    if expiration_time == "permanent":
        return "Vĩnh Viễn"
    remaining_time = float(expiration_time) - time.time()
    if remaining_time <= 0:
        return "Đã hết hạn"
    days = int(remaining_time // 86400)
    hours = int((remaining_time % 86400) // 3600)
    if days > 0:
        return f"{days} ngày {hours} giờ"
    return f"{hours} giờ"

def load_vip_users():
    if os.path.exists('vip_users.json'):
        try:
            with open('vip_users.json', 'r') as f:
                data = json.load(f)
                for user_id, status in data.items():
                    if status == "permanent":
                        allowed_users.add(int(user_id))
                        user_keys[int(user_id)] = "permanent"
                    else:
                        user_keys[int(user_id)] = float(status)
                        allowed_users.add(int(user_id))
        except json.JSONDecodeError:
            print("Lỗi đọc vip_users.json")

def save_vip_users():
    try:
        vip_data = {str(user_id): user_keys[user_id] for user_id in allowed_users}
        with open('vip_users.json', 'w') as f:
            json.dump(vip_data, f)
    except Exception as e:
        print(f"Lỗi lưu VIP: {e}")

def check_vip_status(user_id):
    if user_id in user_keys:
        expiration_time = user_keys[user_id]
        if expiration_time == "permanent":
            return True
        elif time.time() > float(expiration_time):
            allowed_users.discard(user_id)
            del user_keys[user_id]
            save_vip_users()
            return False
        return True
    return False

def load_super_users():
    if os.path.exists(SUPER_VIP_FILE):
        try:
            with open(SUPER_VIP_FILE, 'r') as f:
                data = json.load(f)
                for user_id, status in data.items():
                    if status == "permanent":
                        super_keys[int(user_id)] = "permanent"
                    else:
                        super_keys[int(user_id)] = float(status)
                    super_users.add(int(user_id))
        except:
            pass

def save_super_users():
    try:
        with open(SUPER_VIP_FILE, 'w') as f:
            json.dump({str(k): v for k, v in super_keys.items()}, f)
    except Exception as e:
        print(f"Lỗi lưu Super VIP: {e}")

def check_super_status(user_id):
    if user_id == ADMIN_ID:
        return True
    if user_id in super_keys:
        status = super_keys[user_id]
        if status == "permanent":
            return True
        if time.time() > float(status):
            super_users.discard(user_id)
            super_keys.pop(user_id, None)
            save_super_users()
            return False
        return True
    return False

def load_spam_counts():
    global user_spam_count, user_spam_time
    try:
        with open(SPAM_COUNT_FILE, 'r') as f:
            data = json.load(f)
            user_spam_count = data.get('spam_count', {})
            user_spam_time = data.get('spam_time', {})
    except:
        user_spam_count = {}
        user_spam_time = {}

def save_spam_counts():
    with open(SPAM_COUNT_FILE, 'w') as f:
        json.dump({'spam_count': user_spam_count, 'spam_time': user_spam_time}, f)

def load_blacklist():
    global blacklist
    if os.path.exists(BLACKLIST_FILE):
        with open(BLACKLIST_FILE, 'r') as f:
            blacklist = json.load(f)

def save_blacklist():
    with open(BLACKLIST_FILE, 'w') as f:
        json.dump(blacklist, f)

def check_process_status(sdt, process):
    start = time.time()
    while True:
        if process.poll() is not None:
            spam_processes.pop(sdt, None)
            break
        if time.time() - start > 300:
            process.terminate()
            spam_processes.pop(sdt, None)
            break
        time.sleep(10)

def reset_spam_counts_loop():
    while True:
        now = datetime.now()
        next_reset = (datetime.combine(now.date() + timedelta(days=1), datetime.min.time()) - now).total_seconds()
        time.sleep(next_reset)
        user_spam_count.clear()
        user_spam_time.clear()
        save_spam_counts()

def check_all_vip_status():
    while True:
        for user_id in list(user_keys.keys()):
            check_vip_status(user_id)
        time.sleep(60)


@bot.event
async def on_ready():
    print(f"Bot đã sẵn sàng: {bot.user}")
    try:
        synced = await tree.sync()
        print(f"Đã sync {len(synced)} lệnh slash")
    except Exception as e:
        print(f"Lỗi sync: {e}")

    log = discord.Embed(title="🟢 BOT ĐÃ KHỞI ĐỘNG", color=0x00ff00)
    log.add_field(name="Bot", value=str(bot.user), inline=True)
    log.add_field(name="Trạng thái", value="🟢 ONLINE", inline=True)
    log.add_field(name="Thời gian", value=time.strftime("%H:%M:%S, %d/%m/%Y"), inline=False)
    await send_log(log)

@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="general")
    if channel:
        msg = await channel.send(f"👋 Wẻo Căm Bro {member.display_name} Đã Đến Server! Dùng lệnh `/help` để xem các lệnh.")
        await asyncio.sleep(1800)
        try:
            await msg.delete()
        except:
            pass


@tree.command(name="help", description="Hiển thị danh sách các lệnh")
async def help_cmd(interaction: discord.Interaction):
    embed = discord.Embed(title="📋 DANH SÁCH LỆNH BOT SMS", color=0x00ff00)
    embed.add_field(name="🔥 Lệnh Spam & Call", value=(
        "`/spam [sdt]` - Spam SMS free (3 lần/ngày)\n"
        "`/spamvip [sdt]` - Spam SMS VIP\n"
        "`/call [sdt]` - Gọi điện free\n"
        "`/callvip [sdt]` - Gọi điện VIP\n"
    ), inline=False)
    embed.add_field(name="⚙️ Lệnh Admin", value=(
        "`/addvip [id] [ngày]` - Cấp VIP\n"
        "`/delvip [id]` - Xóa VIP\n"
        "`/addadmin [id]` - Thêm Admin\n"
    ), inline=False)
    embed.set_footer(text="Liên hệ Admin để mua VIP")
    await interaction.response.send_message(embed=embed)


@tree.command(name="spam", description="Spam SMS free (3 lần/ngày)")
@app_commands.describe(sdt="Số điện thoại cần spam (10 số)")
async def spam_cmd(interaction: discord.Interaction, sdt: str):
    await interaction.response.defer(ephemeral=False)

    user_id = interaction.user.id

    if not bot_active and user_id != ADMIN_ID:
        await interaction.followup.send("❌ BOT đang OFF. Vui lòng đợi BOT ON.")
        return

    if not sdt.isdigit() or len(sdt) != 10:
        await interaction.followup.send("❌ SĐT không hợp lệ (phải là 10 số)")
        return

    if sdt in blacklist:
        await interaction.followup.send(f"🚫 SĐT `{mask_sdt(sdt)}` nằm trong danh sách cấm!")
        return

    if sdt in spam_processes:
        await interaction.followup.send(f"❌ SĐT `{mask_sdt(sdt)}` đang được spam, vui lòng đợi!")
        return

    current_time = time.time()
    uid_str = str(user_id)

    if user_id in last_usage and current_time - last_usage[user_id] < 120:
        remaining = 120 - (current_time - last_usage[user_id])
        await interaction.followup.send(f"❌ Thích spam lắm không? {remaining:.0f} giây nữa nhé!")
        return

    if uid_str not in user_spam_time or current_time - float(user_spam_time[uid_str]) > 86400:
        user_spam_count[uid_str] = 0
        user_spam_time[uid_str] = current_time

    if user_spam_count.get(uid_str, 0) >= 3:
        await interaction.followup.send("❌ Bạn đã dùng hết 3/3 lần FREE hôm nay. Mua VIP để không giới hạn!")
        return

    last_usage[user_id] = current_time
    user_spam_count[uid_str] = user_spam_count.get(uid_str, 0) + 1
    save_spam_counts()

    network_provider = get_network_provider(sdt)
    masked_phone = mask_sdt(sdt)
    formatted_time = time.strftime("%H:%M:%S, %d/%m/%Y")

    msg = await interaction.followup.send("⏳ Đang khởi động...")

    def spam_task():
        script_filename = "dec.py"
        if os.path.isfile(script_filename):
            process = subprocess.Popen(["python", script_filename, sdt, "5"])
            spam_processes[sdt] = process
            spam_users[sdt] = user_id

            embed = discord.Embed(title="✅ SPAM SMS FREE", color=0x00ff00)
            embed.add_field(name="Người dùng", value=interaction.user.display_name, inline=False)
            embed.add_field(name="Target", value=f"`{masked_phone}`", inline=True)
            embed.add_field(name="Nhà Mạng", value=network_provider, inline=True)
            embed.add_field(name="Vòng Lặp", value="5", inline=True)
            embed.add_field(name="Hôm nay", value=f"{user_spam_count[uid_str]}/3", inline=True)
            embed.add_field(name="Thời gian", value=formatted_time, inline=False)
            embed.set_footer(text="Dùng /stop để dừng")

            import asyncio
            asyncio.run_coroutine_threadsafe(msg.edit(content=None, embed=embed), bot.loop)

            log = discord.Embed(title="📨 [LOG] SPAM FREE", color=0x5865f2)
            log.add_field(name="User", value=f"{interaction.user} (`{interaction.user.id}`)", inline=False)
            log.add_field(name="Target", value=f"`{masked_phone}`", inline=True)
            log.add_field(name="Nhà Mạng", value=network_provider, inline=True)
            log.add_field(name="Lần hôm nay", value=f"{user_spam_count[uid_str]}/3", inline=True)
            log.add_field(name="Thời gian", value=formatted_time, inline=False)
            send_log_sync(log)

            threading.Thread(target=check_process_status, args=(sdt, process)).start()
        else:
            asyncio.run_coroutine_threadsafe(
                msg.edit(content="❌ Không tìm thấy file dec.py"), bot.loop
            )

    threading.Thread(target=spam_task).start()


@tree.command(name="spamvip", description="Spam SMS VIP (không giới hạn)")
@app_commands.describe(sdt="Số điện thoại cần spam (10 số)")
async def spamvip_cmd(interaction: discord.Interaction, sdt: str):
    await interaction.response.defer(ephemeral=False)

    user_id = interaction.user.id

    if not bot_active and user_id != ADMIN_ID:
        await interaction.followup.send("❌ BOT đang OFF.")
        return

    if not check_vip_status(user_id) and user_id not in allowed_users:
        await interaction.followup.send("❌ Bạn là User FREE, không thể dùng `/spamvip`. Hãy mua VIP!")
        return

    if not sdt.isdigit() or len(sdt) != 10:
        await interaction.followup.send("❌ SĐT không hợp lệ (phải là 10 số)")
        return

    if sdt in blacklist:
        await interaction.followup.send(f"🚫 SĐT `{mask_sdt(sdt)}` nằm trong danh sách cấm!")
        return

    if sdt in spam_processes:
        await interaction.followup.send(f"❌ SĐT `{mask_sdt(sdt)}` đang được spam, vui lòng đợi!")
        return

    current_time = time.time()
    if user_id in last_usage and current_time - last_usage[user_id] < 30:
        remaining = 30 - (current_time - last_usage[user_id])
        await interaction.followup.send(f"❌ Chờ {remaining:.0f}s nữa để tiếp tục")
        return

    last_usage[user_id] = current_time
    network_provider = get_network_provider(sdt)
    masked_phone = mask_sdt(sdt)
    formatted_time = time.strftime("%H:%M:%S, %d/%m/%Y")

    msg = await interaction.followup.send("⏳ Đang khởi động VIP...")

    def spam_task():
        import asyncio
        script_filename = "dec.py"
        if os.path.isfile(script_filename):
            process = subprocess.Popen(["python", script_filename, sdt, "10"])
            spam_processes[sdt] = process
            spam_users[sdt] = user_id

            embed = discord.Embed(title="✅ SPAM SMS VIP", color=0xffd700)
            embed.add_field(name="Người dùng", value=interaction.user.display_name, inline=False)
            embed.add_field(name="Target", value=f"`{masked_phone}`", inline=True)
            embed.add_field(name="Nhà Mạng", value=network_provider, inline=True)
            embed.add_field(name="Vòng Lặp", value="10", inline=True)
            embed.add_field(name="Gói", value="VIP", inline=True)
            embed.add_field(name="Thời gian", value=formatted_time, inline=False)
            embed.set_footer(text="Dùng /stop để dừng")

            asyncio.run_coroutine_threadsafe(msg.edit(content=None, embed=embed), bot.loop)

            log = discord.Embed(title="💎 [LOG] SPAM VIP", color=0xffd700)
            log.add_field(name="User", value=f"{interaction.user} (`{interaction.user.id}`)", inline=False)
            log.add_field(name="Target", value=f"`{masked_phone}`", inline=True)
            log.add_field(name="Nhà Mạng", value=network_provider, inline=True)
            log.add_field(name="Vòng Lặp", value="10", inline=True)
            log.add_field(name="Thời gian", value=formatted_time, inline=False)
            send_log_sync(log)

            threading.Thread(target=check_process_status, args=(sdt, process)).start()
        else:
            asyncio.run_coroutine_threadsafe(
                msg.edit(content="❌ Không tìm thấy file dec.py"), bot.loop
            )

    threading.Thread(target=spam_task).start()


@tree.command(name="call", description="Gọi điện free")
@app_commands.describe(sdt="Số điện thoại cần gọi (10 số)")
async def call_cmd(interaction: discord.Interaction, sdt: str):
    await interaction.response.defer(ephemeral=False)

    user_id = interaction.user.id

    if not bot_active and user_id != ADMIN_ID:
        await interaction.followup.send("❌ BOT đang OFF.")
        return

    if not sdt.isdigit() or len(sdt) != 10:
        await interaction.followup.send("❌ SĐT không hợp lệ (phải là 10 số)")
        return

    if sdt in blacklist:
        await interaction.followup.send(f"🚫 SĐT `{mask_sdt(sdt)}` nằm trong danh sách cấm!")
        return

    if sdt in spam_processes:
        await interaction.followup.send(f"❌ SĐT `{mask_sdt(sdt)}` đang chạy, vui lòng đợi!")
        return

    current_time = time.time()
    uid_str = str(user_id)

    if user_id in last_usage and current_time - last_usage[user_id] < 120:
        remaining = 120 - (current_time - last_usage[user_id])
        await interaction.followup.send(f"❌ Chờ {remaining:.0f}s nữa nhé!")
        return

    if uid_str not in user_spam_time or current_time - float(user_spam_time.get(uid_str, 0)) > 86400:
        user_spam_count[uid_str] = 0
        user_spam_time[uid_str] = current_time

    if user_spam_count.get(uid_str, 0) >= 3:
        await interaction.followup.send("❌ Bạn đã dùng hết 3/3 lần CALL FREE hôm nay!")
        return

    last_usage[user_id] = current_time
    user_spam_count[uid_str] = user_spam_count.get(uid_str, 0) + 1
    save_spam_counts()

    network_provider = get_network_provider(sdt)
    masked_phone = mask_sdt(sdt)
    formatted_time = time.strftime("%H:%M:%S, %d/%m/%Y")

    msg = await interaction.followup.send("⏳ Đang khởi động call...")

    def call_task():
        import asyncio
        script_filename = "nat1.py"
        if os.path.isfile(script_filename):
            process = subprocess.Popen(["python", script_filename, sdt, "5"])
            spam_processes[sdt] = process
            spam_users[sdt] = user_id

            embed = discord.Embed(title="📞 CALL FREE STARTED", color=0x00bfff)
            embed.add_field(name="Người dùng", value=interaction.user.display_name, inline=False)
            embed.add_field(name="Target", value=f"`{masked_phone}`", inline=True)
            embed.add_field(name="Nhà Mạng", value=network_provider, inline=True)
            embed.add_field(name="Số lần", value=f"{user_spam_count[uid_str]}/3", inline=True)
            embed.add_field(name="Thời gian", value=formatted_time, inline=False)
            embed.set_footer(text="Dùng /stop để dừng")

            asyncio.run_coroutine_threadsafe(msg.edit(content=None, embed=embed), bot.loop)

            log = discord.Embed(title="📞 [LOG] CALL FREE", color=0x00bfff)
            log.add_field(name="User", value=f"{interaction.user} (`{interaction.user.id}`)", inline=False)
            log.add_field(name="Target", value=f"`{masked_phone}`", inline=True)
            log.add_field(name="Nhà Mạng", value=network_provider, inline=True)
            log.add_field(name="Lần hôm nay", value=f"{user_spam_count[uid_str]}/3", inline=True)
            log.add_field(name="Thời gian", value=formatted_time, inline=False)
            send_log_sync(log)

            threading.Thread(target=check_process_status, args=(sdt, process)).start()
        else:
            asyncio.run_coroutine_threadsafe(
                msg.edit(content="❌ Không tìm thấy file nat1.py"), bot.loop
            )

    threading.Thread(target=call_task).start()


@tree.command(name="callvip", description="Gọi điện VIP (chỉ dành cho Super VIP)")
@app_commands.describe(sdt="Số điện thoại cần gọi (10 số)")
async def callvip_cmd(interaction: discord.Interaction, sdt: str):
    await interaction.response.defer(ephemeral=False)

    user_id = interaction.user.id

    if not bot_active and user_id != ADMIN_ID:
        await interaction.followup.send("❌ BOT đang OFF.")
        return

    if not check_super_status(user_id):
        await interaction.followup.send("❌ Lệnh này chỉ dành cho tài khoản **SUPER VIP**. Liên hệ Admin để nâng cấp.")
        return

    if not sdt.isdigit() or len(sdt) != 10:
        await interaction.followup.send("❌ SĐT không hợp lệ (phải là 10 số)")
        return

    if sdt in blacklist:
        await interaction.followup.send(f"🚫 SĐT `{mask_sdt(sdt)}` nằm trong danh sách cấm!")
        return

    if sdt in spam_processes:
        await interaction.followup.send(f"❌ SĐT `{mask_sdt(sdt)}` đang chạy!")
        return

    current_time = time.time()
    if user_id in last_usage and current_time - last_usage[user_id] < 30:
        remaining = 30 - (current_time - last_usage[user_id])
        await interaction.followup.send(f"❌ Chờ {remaining:.0f}s nữa để tiếp tục")
        return

    last_usage[user_id] = current_time
    network_provider = get_network_provider(sdt)
    masked_phone = mask_sdt(sdt)
    formatted_time = time.strftime("%H:%M:%S, %d/%m/%Y")

    msg = await interaction.followup.send("⏳ Đang khởi động Call VIP...")

    def callvip_task():
        import asyncio
        script_filename = "nat1.py"
        if os.path.isfile(script_filename):
            spam_processes[sdt] = "STARTING"
            spam_users[sdt] = user_id

            embed = discord.Embed(title="📞 CALL VIP STARTED", color=0xff8c00)
            embed.add_field(name="Target", value=f"`{masked_phone}`", inline=True)
            embed.add_field(name="Nhà Mạng", value=network_provider, inline=True)
            embed.add_field(name="Gói", value="SUPER VIP", inline=True)
            embed.add_field(name="Thời gian", value=formatted_time, inline=False)
            embed.set_footer(text="Dùng /stopcallvip để dừng")

            asyncio.run_coroutine_threadsafe(msg.edit(content=None, embed=embed), bot.loop)

            log = discord.Embed(title="👑 [LOG] CALL VIP", color=0xff8c00)
            log.add_field(name="User", value=f"{interaction.user} (`{interaction.user.id}`)", inline=False)
            log.add_field(name="Target", value=f"`{masked_phone}`", inline=True)
            log.add_field(name="Nhà Mạng", value=network_provider, inline=True)
            log.add_field(name="Gói", value="SUPER VIP", inline=True)
            log.add_field(name="Thời gian", value=formatted_time, inline=False)
            send_log_sync(log)

            process = subprocess.Popen(["python", script_filename, sdt, "10"])
            spam_processes[sdt] = process
            process.wait()

            spam_processes.pop(sdt, None)
            spam_users.pop(sdt, None)
        else:
            asyncio.run_coroutine_threadsafe(
                msg.edit(content="❌ Không tìm thấy file nat1.py"), bot.loop
            )

    threading.Thread(target=callvip_task).start()


@tree.command(name="addvip", description="[ADMIN] Cấp quyền VIP cho user")
@app_commands.describe(user_id="Discord User ID", ngay="Số ngày VIP (để trống = vĩnh viễn)")
async def addvip_cmd(interaction: discord.Interaction, user_id: str, ngay: int = 0):
    if interaction.user.id != ADMIN_ID and interaction.user.id not in admins:
        await interaction.response.send_message("❌ Bạn không có quyền dùng lệnh này!", ephemeral=True)
        return

    try:
        uid = int(user_id)
        if ngay > 0:
            expiration_time = time.time() + (ngay * 86400)
            user_keys[uid] = expiration_time
            exp_date = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(expiration_time))
            han = f"{ngay} Ngày (Hết hạn: {exp_date})"
        else:
            user_keys[uid] = "permanent"
            han = "Vĩnh Viễn"

        allowed_users.add(uid)
        save_vip_users()

        embed = discord.Embed(title="✅ ADD VIP THÀNH CÔNG", color=0x00ff00)
        embed.add_field(name="User ID", value=f"`{uid}`", inline=True)
        embed.add_field(name="Thời Hạn", value=han, inline=True)
        await interaction.response.send_message(embed=embed)

        log = discord.Embed(title="🔑 [LOG] ADD VIP", color=0x00ff00)
        log.add_field(name="Admin", value=f"{interaction.user} (`{interaction.user.id}`)", inline=False)
        log.add_field(name="Target ID", value=f"`{uid}`", inline=True)
        log.add_field(name="Thời Hạn", value=han, inline=True)
        log.add_field(name="Thời gian", value=time.strftime("%H:%M:%S, %d/%m/%Y"), inline=False)
        await send_log(log)

    except ValueError:
        await interaction.response.send_message("❌ User ID phải là số!", ephemeral=True)


@tree.command(name="delvip", description="[ADMIN] Xóa quyền VIP của user")
@app_commands.describe(user_id="Discord User ID cần xóa VIP")
async def delvip_cmd(interaction: discord.Interaction, user_id: str):
    if interaction.user.id != ADMIN_ID and interaction.user.id not in admins:
        await interaction.response.send_message("❌ Bạn không có quyền dùng lệnh này!", ephemeral=True)
        return

    try:
        uid = int(user_id)
        if uid in allowed_users:
            allowed_users.discard(uid)
            user_keys.pop(uid, None)
            save_vip_users()
            await interaction.response.send_message(f"✅ Đã xóa VIP của ID `{uid}`")

            log = discord.Embed(title="🗑️ [LOG] DEL VIP", color=0xff4444)
            log.add_field(name="Admin", value=f"{interaction.user} (`{interaction.user.id}`)", inline=False)
            log.add_field(name="Target ID", value=f"`{uid}`", inline=True)
            log.add_field(name="Thời gian", value=time.strftime("%H:%M:%S, %d/%m/%Y"), inline=True)
            await send_log(log)
        else:
            await interaction.response.send_message(f"❌ ID `{uid}` không có trong danh sách VIP")
    except ValueError:
        await interaction.response.send_message("❌ User ID phải là số!", ephemeral=True)


@tree.command(name="addadmin", description="[ADMIN] Thêm admin mới")
@app_commands.describe(user_id="Discord User ID cần thêm làm Admin")
async def addadmin_cmd(interaction: discord.Interaction, user_id: str):
    if interaction.user.id != ADMIN_ID:
        await interaction.response.send_message("❌ Chỉ Admin gốc mới có thể thêm Admin!", ephemeral=True)
        return

    try:
        uid = int(user_id)
        admins.add(uid)
        await interaction.response.send_message(f"✅ Đã thêm ID `{uid}` vào danh sách Admin")

        log = discord.Embed(title="🛡️ [LOG] ADD ADMIN", color=0x9b59b6)
        log.add_field(name="Admin gốc", value=f"{interaction.user} (`{interaction.user.id}`)", inline=False)
        log.add_field(name="Admin mới ID", value=f"`{uid}`", inline=True)
        log.add_field(name="Thời gian", value=time.strftime("%H:%M:%S, %d/%m/%Y"), inline=True)
        await send_log(log)
    except ValueError:
        await interaction.response.send_message("❌ User ID phải là số!", ephemeral=True)


@tree.command(name="stop", description="Dừng spam/call đang chạy")
@app_commands.describe(sdt="Số điện thoại đang spam cần dừng")
async def stop_cmd(interaction: discord.Interaction, sdt: str):
    user_id = interaction.user.id
    masked_phone = mask_sdt(sdt)

    if sdt in spam_processes:
        if sdt in spam_users:
            if user_id == spam_users[sdt] or user_id == ADMIN_ID or user_id in admins:
                process = spam_processes[sdt]
                if hasattr(process, 'terminate'):
                    process.terminate()
                spam_processes.pop(sdt, None)
                spam_users.pop(sdt, None)
                await interaction.response.send_message(f"✅ Đã dừng SĐT `{masked_phone}`")

                log = discord.Embed(title="🛑 [LOG] STOP SPAM", color=0xe74c3c)
                log.add_field(name="User", value=f"{interaction.user} (`{interaction.user.id}`)", inline=False)
                log.add_field(name="Target", value=f"`{masked_phone}`", inline=True)
                log.add_field(name="Thời gian", value=time.strftime("%H:%M:%S, %d/%m/%Y"), inline=True)
                await send_log(log)
            else:
                await interaction.response.send_message(f"❌ Bạn không phải người khởi tạo lệnh cho số `{masked_phone}`")
        else:
            process = spam_processes.pop(sdt, None)
            if process and hasattr(process, 'terminate'):
                process.terminate()
            await interaction.response.send_message(f"✅ Đã dừng SĐT `{masked_phone}`")

            log = discord.Embed(title="🛑 [LOG] STOP SPAM", color=0xe74c3c)
            log.add_field(name="User", value=f"{interaction.user} (`{interaction.user.id}`)", inline=False)
            log.add_field(name="Target", value=f"`{masked_phone}`", inline=True)
            log.add_field(name="Thời gian", value=time.strftime("%H:%M:%S, %d/%m/%Y"), inline=True)
            await send_log(log)
    else:
        await interaction.response.send_message(f"❌ SĐT `{masked_phone}` không có trong danh sách đang spam")


@tree.command(name="stopcallvip", description="Dừng call VIP đang chạy")
@app_commands.describe(sdt="Số điện thoại đang call cần dừng")
async def stopcallvip_cmd(interaction: discord.Interaction, sdt: str):
    user_id = interaction.user.id
    masked_phone = mask_sdt(sdt)

    if sdt in spam_processes:
        owner = spam_users.get(sdt)
        if user_id == owner or user_id == ADMIN_ID or user_id in admins:
            process = spam_processes[sdt]
            if process and not isinstance(process, str) and hasattr(process, 'terminate'):
                process.terminate()
            spam_processes.pop(sdt, None)
            spam_users.pop(sdt, None)

            embed = discord.Embed(title="✅ DỪNG CALL VIP THÀNH CÔNG", color=0x00ff00)
            embed.add_field(name="Target", value=f"`{masked_phone}`", inline=True)
            embed.add_field(name="Dừng bởi", value=interaction.user.display_name, inline=True)
            await interaction.response.send_message(embed=embed)

            log = discord.Embed(title="🛑 [LOG] STOP CALL VIP", color=0xe74c3c)
            log.add_field(name="User", value=f"{interaction.user} (`{interaction.user.id}`)", inline=False)
            log.add_field(name="Target", value=f"`{masked_phone}`", inline=True)
            log.add_field(name="Thời gian", value=time.strftime("%H:%M:%S, %d/%m/%Y"), inline=True)
            await send_log(log)
        else:
            await interaction.response.send_message(f"❌ Bạn không có quyền dừng số `{masked_phone}`")
    else:
        await interaction.response.send_message(f"❌ Số `{masked_phone}` hiện không chạy Call VIP")


@tree.command(name="on", description="[ADMIN] Bật BOT")
async def on_cmd(interaction: discord.Interaction):
    global bot_active
    if interaction.user.id != ADMIN_ID and interaction.user.id not in admins:
        await interaction.response.send_message("❌ Bạn không có quyền dùng lệnh này!", ephemeral=True)
        return

    if bot_active:
        await interaction.response.send_message("✅ BOT đã đang trong trạng thái **ON** rồi!")
        return

    bot_active = True
    embed = discord.Embed(title="✅ BOT ĐÃ ĐƯỢC BẬT", color=0x00ff00)
    embed.add_field(name="Người thực hiện", value=interaction.user.mention, inline=True)
    embed.add_field(name="Thời gian", value=time.strftime("%H:%M:%S, %d/%m/%Y"), inline=True)
    embed.add_field(name="Trạng thái", value="🟢 ONLINE", inline=False)
    await interaction.response.send_message(embed=embed)
    await send_log(embed)

@tree.command(name="off", description="[ADMIN] Tắt BOT (chỉ Admin dùng được khi OFF)")
async def off_cmd(interaction: discord.Interaction):
    global bot_active
    if interaction.user.id != ADMIN_ID and interaction.user.id not in admins:
        await interaction.response.send_message("❌ Bạn không có quyền dùng lệnh này!", ephemeral=True)
        return

    if not bot_active:
        await interaction.response.send_message("⚠️ BOT đã đang trong trạng thái **OFF** rồi!")
        return

    bot_active = False
    embed = discord.Embed(title="🔴 BOT ĐÃ ĐƯỢC TẮT", color=0xff0000)
    embed.add_field(name="Người thực hiện", value=interaction.user.mention, inline=True)
    embed.add_field(name="Thời gian", value=time.strftime("%H:%M:%S, %d/%m/%Y"), inline=True)
    embed.add_field(name="Trạng thái", value="🔴 OFFLINE", inline=False)
    await interaction.response.send_message(embed=embed)
    await send_log(embed)


if __name__ == "__main__":
    import asyncio

    load_vip_users()
    load_super_users()
    load_spam_counts()
    load_blacklist()

    threading.Thread(target=check_all_vip_status, daemon=True).start()
    threading.Thread(target=reset_spam_counts_loop, daemon=True).start()

    print("🤖 BOT DISCORD ĐÃ SẴN SÀNG HOẠT ĐỘNG!")
    bot.run(DISCORD_TOKEN)