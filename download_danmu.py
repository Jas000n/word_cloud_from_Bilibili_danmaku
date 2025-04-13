import re
import requests

def download_danmaku(video_url, output_file="danmaku.xml"):
    """
    根据传入的视频 URL 下载 B 站弹幕并保存到本地文件
    :param video_url: B 站视频链接
    :param output_file: 弹幕数据保存的文件名（默认 danmaku.xml）
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }

    try:
        # 下载视频页面
        response = requests.get(video_url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print("获取视频页面失败:", e)
        return

    # 提取 cid，通常在页面源码中以 "cid":数字 的形式存在
    cid_match = re.search(r'"cid":(\d+)', response.text)
    if not cid_match:
        print("未能找到 cid，请检查视频链接是否正确或页面格式是否发生变化。")
        return

    cid = cid_match.group(1)
    print("检测到视频 cid:", cid)

    # 构造弹幕 XML 的下载链接
    danmaku_url = f"https://comment.bilibili.com/{cid}.xml"
    try:
        danmaku_response = requests.get(danmaku_url, headers=headers, timeout=10)
        danmaku_response.raise_for_status()
        # 强制设置编码为 utf-8，防止因自动推断错误导致乱码
        danmaku_response.encoding = 'utf-8'
    except requests.RequestException as e:
        print("获取弹幕失败:", e)
        return

    # 将弹幕写入本地文件
    output_file = cid+"_danmu.xml"
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(danmaku_response.text)
        print(f"弹幕已成功保存到 {output_file}")
        return output_file
    except IOError as e:
        print("写入文件失败:", e)

if __name__ == "__main__":
    video_url = input("请输入B站视频链接：")
    download_danmaku(video_url)
