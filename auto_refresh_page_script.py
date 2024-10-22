
import time
from DrissionPage import ChromiumPage
from datetime import datetime, timedelta
import argparse

def auto_refresh_page(url: str, refresh_interval: int, run_hours: int):

    # 使用默认浏览器初始化
    tab = ChromiumPage()
    tab.get(url)

    # 设置程序结束时间
    end_time = datetime.now() + timedelta(hours=run_hours)

    # 每隔指定时间刷新页面并记录日志，直到达到结束时间
    while datetime.now() < end_time:
        try:
            tab.refresh()
            print(f"Page refreshed at {datetime.now()}")
        except Exception as e:
            print(f"Error occurred: {e}. Retrying...")
            tab.get(url)  # 如果出错，重新打开页面
        
        time.sleep(refresh_interval)  # 等待设定的时间间隔

    print("Program has finished running.")

def main():
    parser = argparse.ArgumentParser(description='Auto refresh a webpage.')
    parser.add_argument('--url', type=str, required=True, help='The URL of the webpage to refresh.')
    parser.add_argument('--interval', type=int, default=240, help='Time interval between refreshes (in seconds).')
    parser.add_argument('--hours', type=int, default=2, help='How long the script will run (in hours).')

    args = parser.parse_args()

    auto_refresh_page(url=args.url, refresh_interval=args.interval, run_hours=args.hours)

if __name__ == "__main__":
    main()
