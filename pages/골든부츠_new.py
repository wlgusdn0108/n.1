import streamlit as st
import pandas as pd
import plotly.express as px

# 페이지 설정
st.set_page_config(page_title="프리미어리그 골든부츠", layout="centered")
st.title("⚽ 프리미어리그 역대 골든부츠 수상자")

# 데이터: 시즌별 골든부츠 수상자
data = [
    ["1992-93", "Teddy Sheringham", 22],
    ["1993-94", "Andy Cole", 34],
    ["1994-95", "Alan Shearer", 34],
    ["1995-96", "Alan Shearer", 31],
    ["1996-97", "Alan Shearer", 25],
    ["1997-98", "Dion Dublin, Michael Owen, Chris Sutton", 18],
    ["1998-99", "Jimmy Floyd Hasselbaink, Michael Owen, Dwight Yorke", 18],
    ["1999-00", "Kevin Phillips", 30],
    ["2000-01", "Jimmy Floyd Hasselbaink", 23],
    ["2001-02", "Thierry Henry", 24],
    ["2002-03", "Ruud van Nistelrooy", 25],
    ["2003-04", "Thierry Henry", 30],
    ["2004-05", "Thierry Henry", 25],
    ["2005-06", "Thierry Henry", 27],
    ["2006-07", "Didier Drogba", 20],
    ["2007-08", "Cristiano Ronaldo", 31],
    ["2008-09", "Nicolas Anelka", 19],
    ["2009-10", "Didier Drogba", 29],
    ["2010-11", "Carlos Tevez, Dimitar Berbatov", 20],
    ["2011-12", "Robin van Persie", 30],
    ["2012-13", "Robin van Persie", 26],
    ["2013-14", "Luis Suárez", 31],
    ["2014-15", "Sergio Agüero", 26],
    ["2015-16", "Harry Kane", 25],
    ["2016-17", "Harry Kane", 29],
    ["2017-18", "Mohamed Salah", 32],
    ["2018-19", "Salah, Aubameyang, Mané", 22],
    ["2019-20", "Jamie Vardy", 23],
    ["2020-21", "Harry Kane", 23],
    ["2021-22", "Mohamed Salah, Son Heung-min", 23],
    ["2022-23", "Erling Haaland", 36],
]

df = pd.DataFrame(data, columns=["Season", "Winner(s)", "Goals"])

# 시즌 선택
selected_season = st.selectbox("시즌을 선택하세요", df["Season"].tolist()[::-1])

# 해당 시즌 정보 출력
row = df[df["Season"] == selected_season].iloc[0]
st.subheader(f"🏆 {row['Season']} 시즌 골든부츠")
st.markdown(f"**수상자**: {row['Winner(s)']}")
st.markdown(f"**득점 수**: {row['Goals']}골")

# 전체 테이블 보기
with st.expander("📋 전체 시즌별 수상자 보기"):
    st.dataframe(df[::-1].reset_index(drop=True), use_container_width=True)

# 바 차트
st.subheader("📊 시즌별 최고 득점 수")
fig = px.bar(df[::-1], x="Season", y="Goals", text="Winner(s)", height=500)
fig.update_layout(xaxis_tickangle=-45)
fig.update_traces(textposition="outside")
st.plotly_chart(fig, use_container_width=True)

st.caption("※ 데이터 출처: 프리미어리그 공식 기록. 공동 수상자는 쉼표로 구분되어 있습니다.")
