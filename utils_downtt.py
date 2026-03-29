import requests
import time
from datetime import datetime

API_URL_TIKWM = "https://www.tikwm.com/api/"

def process_downtt(url: str) -> dict:
    try:
        response = requests.get(f"{API_URL_TIKWM}?url={url}", timeout=15)
        response.raise_for_status()
        data = response.json()

        if data.get('code') != 0:
            return {"success": False, "error": data.get('msg', 'URL không hợp lệ hoặc video đã bị xóa')}

        item = data['data']
        
        # Trích xuất thông tin chi tiết
        title = item.get('title') or "Không có tiêu đề"
        username = item.get('author', {}).get('unique_id', 'unknown')
        nickname = item.get('author', {}).get('nickname', 'Không rõ')
        video_id = item.get('id', 'unknown')
        
        region = item.get('region', 'N/A')
        duration = item.get('duration', 0)
        size_mb = item.get('size', 0) / 1048576 if item.get('size', 0) > 0 else 0
        created_time = datetime.fromtimestamp(item.get('create_time', 0)).strftime('%Y-%m-%d %H:%M:%S') if item.get('create_time') else "N/A"
        
        # Thống kê
        play_count = item.get('play_count', 0)
        digg_count = item.get('digg_count', 0)
        comment_count = item.get('comment_count', 0)

        # Media links
        video_url = item.get('play') if duration > 0 else None
        images = item.get('images', [])
        music_url = item.get('music_info', {}).get('play')

        return {
            "success": True,
            "data": {
                "title": title,
                "author": f"{nickname} (@{username})",
                "region": region,
                "created_time": created_time,
                "stats": {
                    "views": play_count,
                    "likes": digg_count,
                    "comments": comment_count
                },
                "media": {
                    "type": "video" if video_url else ("slideshow" if images else "unknown"),
                    "size_mb": round(size_mb, 2),
                    "video_url": video_url,
                    "images": images,
                    "music_url": music_url
                }
            }
        }
    except Exception as e:
        return {"success": False, "error": str(e)}
