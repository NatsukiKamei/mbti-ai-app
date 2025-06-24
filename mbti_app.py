import streamlit as st
import os

# アップロード画像をMBTIと紐付けて管理（ローカル or cloudディレクトリ構成に応じて調整）
mbti_images = {
    "ENTP": "https://github.com/NatsukiKamei/mbti-ai-app/blob/main/ENTP.png?raw=true",
    # 他も追加していってね
}


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
mbti_type = st.selectbox("あなたのMBTIは？", [
    'ENFJ(主人公)', 'ENFP(運動家)', 'ENTJ(指揮官)', 'ENTP(討論者)',
    'INFJ(提唱者)', 'INFP(仲介者)', 'INTJ(建築家)', 'INTP(論理学者)',
    'ESFJ(領事)', 'ESFP(エンターテイナー)', 'ESTJ(幹部)', 'ESTP(起業家)',
    'ISFJ(擁護者)', 'ISFP(冒険家)', 'ISTJ(ロジスティシャン)', 'ISTP(巨匠)'
])

# MBTIごとのアドバイス辞書
recommendations = {
    'INTJ': '戦略立案や企画設計など、構造的に物事を考える職務。研究職や経営企画も◎',
    'INTP': 'システム設計・分析・AI分野など、独創性が求められる開発・研究向き',
    'ENTJ': 'マネジメント・経営幹部・プロジェクト統括などリーダーシップが活きる',
    'ENTP': '新規事業やイノベーション領域、柔軟な発想が求められる営業企画など',

    'INFJ': '教育、コーチング、HRなど、内省と共感を活かす支援的ポジション',
    'INFP': 'クリエイティブ、編集、福祉系など、価値観重視の個人ワークに適性',
    'ENFJ': '人事・広報・ファシリテーターなど、対人関係を重視する調整役に最適',
    'ENFP': 'マーケ・PR・イベント・スタートアップ系など自由度の高い環境◎',

    'ISTJ': '経理・法務・総務など、手続きとルール遵守が求められる職務に適性',
    'ISFJ': '医療・事務・秘書など、人に寄り添い正確な対応が求められる配置',
    'ESTJ': '現場管理・営業統括・マネジメントなど、実務型リーダーに向いている',
    'ESFJ': '接客・CS・サポート部門など、共感と気配りが活かせる環境が◎',

    'ISTP': 'ITエンジニア・整備・モノづくり系など、実践的な技術職が得意',
    'ISFP': '介護・アート・空間設計など、五感や美的感性を活かす業務に適性',
    'ESTP': '営業・起業家・イベント企画など、行動力と社交性を活かせる分野',
    'ESFP': 'タレント系、接客、クリエイティブ現場など、感覚的なパフォーマンス職',
}

mbti_code = mbti_type[:4]  # 'ENFP(運動家)' → 'ENFP'


    # 🧭 人員配置レコメンドも表示
    recommend = mbti_recommendations.get(mbti_type[:4])  # 例: 'ENFP(運動家)' → 'ENFP'
    if recommend:
        st.markdown(f"""
        <div class="card">
            <h3>🧭 あなたに向いている人員配置</h3>
            <p>{recommend}</p>
        </div>
        """, unsafe_allow_html=True)
