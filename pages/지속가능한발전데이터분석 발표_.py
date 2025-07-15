import streamlit as st

st.set_page_config(page_title="지속가능발전데이터분석 발표", layout="centered")

# 스타일 CSS 직접 삽입
st.markdown("""
<style>
    .title {
        font-size: 48px;
        font-weight: bold;
        color: #2E86C1;
        text-align: center;
        margin-bottom: 30px;
    }
    .subtitle {
        font-size: 24px;
        font-weight: 600;
        color: #117A65;
        text-align: center;
        margin-bottom: 40px;
    }
    .card {
        background: #D6EAF8;
        border-radius: 15px;
        padding: 20px;
        margin: 10px auto;
        max-width: 400px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .card h3 {
        margin: 0;
        color: #1B4F72;
    }
    .card p {
        font-size: 18px;
        margin: 5px 0 0 0;
        color: #154360;
    }
    .footer {
        margin-top: 50px;
        font-size: 14px;
        color: #7D7D7D;
        text-align: center;
        font-style: italic;
    }
</style>
""", unsafe_allow_html=True)

# 제목
st.markdown('<div class="title">📊 지속가능발전데이터분석</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">발표자 소개</div>', unsafe_allow_html=True)

# 발표자 카드
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
        <h3>21331 지현우</h3>
        <p>팀원</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h3>21309 노우현</h3>
        <p>팀원</p>
    </div>
    """, unsafe_allow_html=True)

# 발표 내용 자리
st.markdown("---")
st.write("여기에 발표 내용을 추가하세요.")

# 하단 푸터
st.markdown('<div class="footer">© 2025 지속가능발전 프로젝트</div>', unsafe_allow_html=True)
