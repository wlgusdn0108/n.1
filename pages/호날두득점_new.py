import streamlit as st
import pandas as pd
import plotly.express as px

# 페이지 기본 설정
st.set_page_config(page_title="호날두 연도별 골 수", layout="centered")
st.title("⚽ 크리스티아누 호날두 연도별 골 수 + 소속팀")

# 데이터: 연도별 득점 수 + 소속팀
data = [
    [2002, 5, "Sporting CP"],
    [2003, 1, "Manchester United"],
    [2004, 9, "Manchester United"],
    [2005, 12, "Manchester United"],
    [2006, 23, "Manchester United"],
    [2007, 34, "Manchester United"],
    [2008, 35, "Manchester United"],
    [2009, 27, "Real Madrid"],
    [2010, 48, "Real Madrid"],
    [2011, 60, "Real Madrid"],
    [2012, 63, "Real Madrid"],
    [2013, 69, "Real Madrid"],
    [2014, 61, "Real Madrid"],
    [2015, 57, "Real Madrid"],
    [2016, 55, "Real Madrid"],
    [2017, 53, "Real Madrid"],
    [2018, 49, "Juventus"],
    [2019, 39, "Juventus"],
    [2020, 44, "Juventus"],
    [2021, 47, "Manchester United"],
    [2022, 23, "Al Nassr"],
    [2023, 54, "Al Nassr"]
]

# 데이터프레임 생성
df = pd.DataFrame(data, columns=["Year", "Goals", "Team"])

# 연도 슬라이더로 필터링
year_range = st.slider("조회할 연도 범위", min_value=2002, max_value=2023, value=(2010, 2023))
filtered_df = df[(df["Year"] >= year_range[0]) & (df["Year"] <= year_range[1])]

# 표 출력
st.subheader("📋 연도별 득점 & 소속팀")
st.dataframe(filtered_df.reset_index(drop=True), use_container_width=True)

# 팀별 색상 매핑 (선택사항)
team_colors = {
    "Sporting CP": "#2E8B57",
    "Manchester United": "#DA291C",
    "Real Madrid": "#FEBE10",
    "Juventus": "#000000",
    "Al Nassr": "#002060"
}

# 시각화
st.subheader("📊 연도별 득점 (소속팀 색상 표시)")
fig = px.bar(
    filtered_df,
    x="Year",
    y="Goals",
    color="Team",
    text="Goals",
    color_discrete_map=team_colors
)
fig.update_layout(xaxis_title="연도", yaxis_title="골 수", xaxis_tickangle=-45)
fig.update_traces(textposition="outside")
st.plotly_chart(fig, use_container_width=True)

# 설명
st.caption("※ 클럽 및 국가대표 골 포함. 일부 수치는 추정된 비공식 통계입니다.")
