import gspread
from oauth2client.service_account import ServiceAccountCredentials

# スプレッドシートに接続する関数（毎回呼び出してもOK）
def write_to_gsheet(mbti, liked, feedback):
    try:
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        credentials = ServiceAccountCredentials.from_json_keyfile_name("service_account.json", scope)
        gc = gspread.authorize(credentials)

        # あなたのスプレッドシートに接続
        sh = gc.open_by_key("1WQGUcuUBfsdAh6LsNasgOKWPccZ1KpA5qxtsWE4JK3g")
        worksheet = sh.sheet1

        # フィードバックを書き込み
        worksheet.append_row([mbti, liked, feedback])
    except Exception as e:
        st.error(f"スプレッドシートへの保存に失敗しました😢: {e}")
