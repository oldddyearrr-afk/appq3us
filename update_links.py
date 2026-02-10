import requests

# الروابط الخاصة بك
links = [
    "http://line.dream-4k.cc:80/live/9142DC/107CC6/1440477.ts",
    "http://tornado-pro.com:80/live/alhomaidirashid@gmail.com/HOrashid1/160239.ts"
]

content = "#EXTM3U\n"
for i, link in enumerate(links):
    # إضافة خيار التكرار للمشغلات (خدعة بسيطة)
    content += f"#EXTINF:-1, Channel {i+1}\n{link}\n"

with open("playlist.m3u", "w") as f:
    f.write(content)
