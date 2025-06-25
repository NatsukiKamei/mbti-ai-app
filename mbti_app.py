import streamlit as st
import pandas as pd
import datetime
import os

st.set_page_config(page_title="MBTI診断フィードバック", page_icon="💬")

st.markdown("""
<style>
body {
    background: linear-gradient(to bottom, #e0f7fa, #ffffff);
    color: #4A4A4A;
}
.card {
    background: rgba(255, 255, 255, 0.95);
    padding: 2rem;
    border-radius: 20px;
    box-shadow: 0 10px 20px rgba(0,0,0,0.1);
    margin: 2rem 0;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("## 💬 あなたのフィードバックを聞かせてください！")

# --- ユーザー入力 ---
mbti = st.selectbox("あなたのMBTIタイプ", [
    'ENFJ', 'ENFP', 'ENTJ', 'ENTP',
    'INFJ', 'INFP', 'INTJ', 'INTP',
    'ESFJ', 'ESFP', 'ESTJ', 'ESTP',
    'ISFJ', 'ISFP', 'ISTJ', 'ISTP'
])

match = st.radio("診断結果はあなたに合っていましたか？", [
    "とても合っていた", "まあまあ合っていた", "ちょっと違った", "全然違った"
])

satisfaction = st.slider("満足度（1〜5）", 1, 5, 3)

comment = st.text_area("📓 ご意見・ご感想・今後の希望などあればどうぞ", "")

submit = st.button("📩 フィードバックを送信")

# --- 保存処理 ---
if submit:
    feedback = {
        "timestamp": datetime.datetime.now(),
        "mbti": mbti,
        "match": match,
        "satisfaction": satisfaction,
        "comment": comment
    }

    # ファイルに追記（初回は作成）
    file_path = "feedback_log.csv"
    df_new = pd.DataFrame([feedback])

    if os.path.exists(file_path):
        df_old = pd.read_csv(file_path)
        df_all = pd.concat([df_old, df_new], ignore_index=True)
    else:
        df_all = df_new

    df_all.to_csv(file_path, index=False)

    st.success("🎉 フィードバックありがとうございました！")
    st.balloons()

st.markdown("</div>", unsafe_allow_html=True)
