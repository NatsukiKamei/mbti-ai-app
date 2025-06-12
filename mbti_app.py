import streamlit as st

# タイトルを2段に表示
st.markdown("""
# MBTIタイプ別  
## AI活用アドバイスツール
""")

mbti_type = st.selectbox("あなたのMBTIタイプは？", 
                         ['INTJ', 'INFP', 'ENFP', 'ISTJ', 'ENTP', 'ISFJ', 'INFJ', 'ESFP'])

if mbti_type == 'ENFP':
    st.write("🎨 ENFPタイプには、画像生成やアイデア拡張系AIがおすすめ！")
elif mbti_type == 'ISTJ':
    st.write("📑 ISTJタイプには、文書作成や整理系のAIがぴったり！")
else:
    st.write("🧭 他のタイプへのアドバイスは順次更新中…！お楽しみに✨")