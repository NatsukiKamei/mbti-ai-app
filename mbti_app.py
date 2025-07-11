import streamlit as st
import os
import pandas as pd
from datetime import datetime

# ✅ MBTI画像リンク（必要に応じて追加）
mbti_images = {
    "ENTP": "https://github.com/NatsukiKamei/mbti-ai-app/blob/main/ENTP.png?raw=true",
    "ESTP": "https://github.com/NatsukiKamei/mbti-ai-app/blob/main/ESTP.png?raw=true",
    "INFP": "https://github.com/NatsukiKamei/mbti-ai-app/blob/main/INFP.png?raw=true",
    # 他のMBTI画像も同様に追加可
}

# ✅ カスタムCSS（水色背景＋カード）
st.markdown("""
<style>
body {
    background: linear-gradient(to bottom, #b3d9ea, #e0f7fa); /* ブルー系グラデ */
    color: #4A4A4A;
}
.card {
    background: rgba(255, 255, 255, 0.95);
    padding: 1.5rem;
    border-radius: 20px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    margin: 2rem 0;
    font-family: 'Helvetica Neue', sans-serif;
}
</style>
""", unsafe_allow_html=True)

# ✅ MBTIタイプ選択（デフォルトに注意！）
mbti_type = st.selectbox("あなたのMBTIは？", [
    '--- 選択してください ---',
    'ENFJ(主人公)', 'ENFP(運動家)', 'ENTJ(指揮官)', 'ENTP(討論者)',
    'INFJ(提唱者)', 'INFP(仲介者)', 'INTJ(建築家)', 'INTP(論理学者)',
    'ESFJ(領事)', 'ESFP(エンターテイナー)', 'ESTJ(幹部)', 'ESTP(起業家)',
    'ISFJ(擁護者)', 'ISFP(冒険家)', 'ISTJ(ロジスティシャン)', 'ISTP(巨匠)'
])

# ✅ MBTIアドバイス辞書
mbti_ai_advice = {
    "ENFJ": {"一言": "ひらめきリーダータイプ", "おすすめAI": "画像生成AI、アイデア拡張ツール", "活用スタイル": "企画やアイデア出しに活用、チームを鼓舞", "特徴": "流行キャッチが得意で、表現力も◎"},
    "ENFP": {"一言": "感性のバクハツ系アイデアマン", "おすすめAI": "ビジュアル系AI、創造系チャットボット", "活用スタイル": "発想のブレストやSNS投稿にも", "特徴": "ひらめき×AIで世界を変えがち"},
    "ENTJ": {"一言": "戦略脳のパワーリーダー", "おすすめAI": "要約・分析AI、業務効率化ツール", "活用スタイル": "資料作成、プロジェクト管理にフル活用", "特徴": "判断速い×論理的でAIの使いこなし最強"},
    "ENTP": {"一言": "ぶっ飛び発明家タイプ", "おすすめAI": "アイデア発掘・商品企画AI", "活用スタイル": "おもしろコンテンツづくりや企画出しに", "特徴": "常に刺激を求めて試しまくる"},
    "INFJ": {"一言": "静かなる情熱家", "おすすめAI": "文章生成AI、内省系チャットボット", "活用スタイル": "日記、創作、コンセプト整理に◎", "特徴": "深く考える力とビジョンの融合タイプ"},
    "INFP": {"一言": "ロマンチック思考家", "おすすめAI": "ストーリー生成、感性デザイン系AI", "活用スタイル": "創作活動、ポエム、ブログに活用", "特徴": "やさしい感性でAIに命吹き込むタイプ"},
    "INTJ": {"一言": "思考のアーキテクト", "おすすめAI": "戦略設計AI、論文生成や構造化系AI", "活用スタイル": "計画立案、研究支援、裏方で大活躍", "特徴": "静かに最適解を追い求める天才肌"},
    "INTP": {"一言": "知的探求ガチ勢", "おすすめAI": "調査・要約・コード系AI", "活用スタイル": "学習・研究やツール開発にハマる", "特徴": "常に「なんで？」を深掘りしていく"},
    "ESFJ": {"一言": "愛されまとめ役", "おすすめAI": "スケジュール補助・メモ整理AI", "活用スタイル": "みんなのタスク整理・連絡に大活躍", "特徴": "相手のためにAIも気遣い系で使う"},
    "ESFP": {"一言": "エンタメマスター", "おすすめAI": "画像・動画系AI、SNS投稿支援AI", "活用スタイル": "キラキラ投稿やビジュ作成に◎", "特徴": "直感派でビジュと感情の天才✨"},
    "ESTJ": {"一言": "現場仕切る実務派", "おすすめAI": "タスク整理・報告書系AI", "活用スタイル": "進捗管理やマニュアル作成に強い", "特徴": "合理的に成果出すためならAI活用も積極的"},
    "ESTP": {"一言": "アクティブ挑戦者", "おすすめAI": "動画編集AI、セールス系AI", "活用スタイル": "すぐに試してアウトプット重視", "特徴": "行動してなんぼ！AIはスピード勝負"},
    "ISFJ": {"一言": "サポートのプロフェッショナル", "おすすめAI": "翻訳・要約AI、事務補助系ツール", "活用スタイル": "地道に正確な作業を助ける方向で", "特徴": "縁の下の力持ち！コツコツ型"},
    "ISFP": {"一言": "感性のおしゃれ番長", "おすすめAI": "デザイン系AI、配色・素材提案AI", "活用スタイル": "ビジュ作成や作品づくりにピッタリ", "特徴": "センスの良さがAIでさらに引き立つ"},
    "ISTJ": {"一言": "堅実で実直な管理者タイプ", "おすすめAI": "文書管理AI、分析ツール", "活用スタイル": "ルールに沿った作業補助に最適", "特徴": "正確さ×AIで業務最適化職人"},
    "ISTP": {"一言": "技術屋×クールガール", "おすすめAI": "ツール開発・ハンズオンAI", "活用スタイル": "何かを“いじる”作業と相性良し", "特徴": "とりあえず試して動かす派"}
}

# ✅ MBTI人員配置レコメンド辞書
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

# ✅ 「---」以外が選ばれたら処理
if mbti_type != '--- 選択してください ---':
    mbti_key = mbti_type[:4]

    # ✅ 画像表示
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

    # ✅ カード②：人員配置
    if mbti_key in recommendations:
        st.markdown(f"""
        <div class="card">
            <h3>🧭 あなたに向いている人員配置</h3>
            <p>{recommendations[mbti_key]}</p>
        </div>
        """, unsafe_allow_html=True)

    # ✅ フィードバックフォーム表示
    st.markdown("---")
    st.markdown("### 💬 フィードバックをお聞かせください")

    with st.form("feedback_form"):
        feedback_text = st.text_area("アプリを使ってみてどうだった？", placeholder="例：当たりすぎてびっくりした！")
        liked = st.radio("おすすめ度", ["👍 いいね！", "🤔 まあまあ", "😅 改善希望"])
        submitted = st.form_submit_button("送信する")

        if submitted:
            st.success("フィードバックありがとうございます！🙏")
            df = pd.DataFrame([{
            "timestamp": datetime.now().isoformat(),
            "mbti_type": mbti_type,
            "feedback": feedback_text,
            "liked": liked
            }])
            df.to_csv("feedback_log.csv", mode="a", header=not os.path.exists("feedback_log.csv"), index=False)

import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Google Sheets API設定
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("service_account.json", scope)
client = gspread.authorize(creds)

# スプレッドシートを開く
sheet = client.open_by_key("1WQGUcuUBfsdAh6LsNasgOKWPccZ1KpA5qxtsWE4JK3g").sheet1

# 例：フィードバックの追加
sheet.append_row(["ENFP", "めちゃ当たってた！", "👍 いいね！"])
