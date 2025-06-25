import streamlit as st
import os

# ✅ MBTI画像リンク
mbti_images = {
    "ENTP": "https://github.com/NatsukiKamei/mbti-ai-app/blob/main/ENTP.png?raw=true",
    "ESTP": "https://github.com/NatsukiKamei/mbti-ai-app/blob/main/ESTP.png?raw=true",
    "INFP": "https://github.com/NatsukiKamei/mbti-ai-app/blob/main/INFP.png?raw=true",
    # 他のMBTI画像も同様に追加可
}

# ✅ カスタムCSS（グラデ背景＆洗練デザイン）
st.markdown("""
<style>
body {
    background: linear-gradient(to bottom, #d0f0ff, #ffffff);
    font-family: 'Segoe UI', sans-serif;
    color: #333333;
}
.card {
    background: #ffffffdd;
    border-radius: 20px;
    padding: 2rem;
    margin: 1.5rem 0;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

# ✅ MBTIタイプ選択 UI
st.markdown("### 💫 あなたのMBTIを選んでください")
mbti_type = st.selectbox("　", [
    'ENFJ(主人公)', 'ENFP(運動家)', 'ENTJ(指揮官)', 'ENTP(討論者)',
    'INFJ(提唱者)', 'INFP(仲介者)', 'INTJ(建築家)', 'INTP(論理学者)',
    'ESFJ(領事)', 'ESFP(エンターテイナー)', 'ESTJ(幹部)', 'ESTP(起業家)',
    'ISFJ(擁護者)', 'ISFP(冒険家)', 'ISTJ(ロジスティシャン)', 'ISTP(巨匠)'
])
mbti_key = mbti_type[:4]  # 例: "ENFP"

# ✅ MBTIアドバイス辞書（省略部分略）
mbti_ai_advice = {
    "ENFP": {"一言": "感性のバクハツ系アイデアマン", "おすすめAI": "ビジュアル系AI", "活用スタイル": "発想のブレストやSNS投稿にも", "特徴": "ひらめき×AIで世界を変えがち"},
    "ESTP": {"一言": "アクティブ挑戦者", "おすすめAI": "動画編集AI、セールス系AI", "活用スタイル": "すぐに試してアウトプット重視", "特徴": "行動してなんぼ！AIはスピード勝負"},
    # 他のタイプも続く...
}

# ✅ 人員配置辞書（省略部分略）
recommendations = {
    "ENFP": "マーケ・PR・イベント・スタートアップ系など自由度の高い環境◎",
    "ESTP": "営業・起業家・イベント企画など、行動力と社交性を活かせる分野",
    # 他のタイプも続く...
}

# ✅ MBTI画像表示（あれば）
if mbti_key in mbti_images:
    st.image(mbti_images[mbti_key], use_container_width=True)

# ✅ カード①：MBTI × AI活用
if mbti_key in mbti_ai_advice:
    info = mbti_ai_advice[mbti_key]
    st.markdown(f"""
    <div class="card">
        <h2>{mbti_type} タイプ ✨</h2>
        <p><b>🌟 一言でいうと:</b> {info['一言']}</p>
        <p><b>🚀 おすすめAI:</b> {info['おすすめAI']}</p>
        <p><b>🎯 活用スタイル:</b> {info['活用スタイル']}</p>
        <p><b>💡 特徴:</b> {info['特徴']}</p>
    </div>
    """, unsafe_allow_html=True)

# ✅ カード②：人員配置レコメンド
if mbti_key in recommendations:
    recommend = recommendations[mbti_key]
    st.markdown(f"""
    <div class="card">
        <h3>🧭 あなたに向いている人員配置</h3>
        <p>{recommend}</p>
    </div>
    """, unsafe_allow_html=True)
