import requests
import os
import sys

def send_discord_message(message):
    webhook_url = os.getenv('DISCORD_WEBHOOK_URL')
    
    if not webhook_url:
        print("Error: DISCORD_WEBHOOK_URL が設定されていません。")
        sys.exit(1)

    payload = {"content": message}
    
    try:
        response = requests.post(webhook_url, json=payload)
        response.raise_for_status()
        print("Discordへの通知に成功しました！")
    except requests.exceptions.RequestException as e:
        print(f"通知に失敗しました: {e}")
        sys.exit(1)

if __name__ == "__main__":
    send_discord_message("🚀 GitHub Actions からのテスト通知です！成功しました。")
