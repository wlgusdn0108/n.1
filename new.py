import streamlit as st

import streamlit as st
import pandas as pd
import plotly.express as px

# ─── 페이지 설정 ────────────────────────────────
st.set_page_config(page_title="프리미어리그 우승 횟수", layout="wide")
st.title("🏆 프리미어리그 팀별 우승 횟수 대시보드")
st.markdown("1992‑93 시즌부터 **2022‑23 시즌**까지, 시즌 범위를 선택해 팀별 우승 횟수를 확인하세요.")

# ─── 우승 데이터 (정적) ────────────────────────
# 시즌별 챔피언 (92-93 ~ 22-23)
champions = [
    "Man United","Man United","Blackburn Rovers","Man United","Man United",
    "Arsenal","Man United","Man United","Man United","Arsenal",
    "Man United","Arsenal","Chelsea","Chelsea","Man United",
    "Man United","Man United","Chelsea","Man City","Man City",
    "Liverpool","Man City","Man City"
]
seasons = list(range(1992, 1992 + len(champions)))  # 1992 → 1992‑93, …, 2022

df = pd.DataFrame({
    "Season": seasons,
    "Champion": champions
})

# ─── 사용자 입력: 시즌 범위 선택 ─────────────────
start, end = st.slider(
    "분석할 시즌 범위 선택",
    min_value=1992, 
    max_value=1992 + len(champions) - 1,
    value=(1992, 2022),
    format="%d"
)
filtered = df[(df.Season >= start) & (df.Season <= end)]

# ─── 우승 횟수 집계 ─────────────────────────────
count = filtered["Champion"].value_counts().reset_index()
count.columns = ["Team", "Titles"]

# ─── 결과 출력 ─────────────────────────────────
st.subheader(f"{start}‑{end} 시즌 우승 횟수")
st.table(count)

# 차트
fig = px.bar(
    count.sort_values("Titles", ascending=False),
    x="Team", y="Titles",
    title="🏟️ 팀별 우승 횟수",
    text="Titles"
)
fig.update_traces(textposition="outside")
st.plotly_chart(fig, use_container_width=True)

st.caption("※ 데이터: 1992‑93 시즌 ~ 2022‑23 시즌 우승 기록 (예시용 정적 데이터)")

