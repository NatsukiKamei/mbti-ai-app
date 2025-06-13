import streamlit as st

# カスタムCSSでエモい水色カードスタイル
st.markdown("""
<style>
.card {
    background: rgba(255, 255, 255, 0.9);
    padding: 1.5rem;
    border-radius: 20px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    margin: 2rem 0;
    font-family: 'Helvetica Neue', sans-serif;
}
body {
    background: linear-gradient(to bottom, #cceeff, #e0f7fa);
}
</style>
""", unsafe_allow_html=True)

# MBTI選択
mbti_type = st.selectbox("あなたのMBTIは？", ['ENFP', 'ISTJ', 'INTP', 'ISFJ'])

# カード内容定義（ここを増やしていく）
recommendations = {
    'ENFP': {
        'desc': '🎨 好奇心旺盛なアイデアマンタイプ',
        'use': '画像生成・企画アイデア出し・SNS投稿づくり',
        'tools': 'Midjourney, ChatGPT, Canva',
        'prompt': '「◯◯の面白いアイデアを5つ提案して」',
        'scene': '企画・プレゼン・ポートフォリオ'
    }
}

# 表示（1枚カード）
if mbti_type in recommendations:
    r = recommendations[mbti_type]
    st.markdown(f"""
    <div class="card">
        <h2>{mbti_type} タイプ ✨</h2>
        <p>{r['desc']}</p>
        <p><b>🚀 おすすめ活用法:</b> {r['use']}</p>
        <p><b>🔧 ツール:</b> {r['tools']}</p>
        <p><b>💬 プロンプト例:</b> <code>{r['prompt']}</code></p>
        <p><b>🎯 活用シーン:</b> {r['scene']}</p>
    </div>
    """, unsafe_allow_html=True)
