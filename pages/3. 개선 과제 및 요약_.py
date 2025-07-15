import streamlit as st
import pandas as pd

st.set_page_config(page_title="3. 개선 과제 및 기대 효과", layout="centered")
df = pd.read_csv("esg_data.csv")

def get_grade(score):
    if score >= 80: return "A (우수)"
    elif score >= 60: return "B (보통)"
    elif score >= 40: return "C (주의)"
    else: return "D (위험)"

latest = df.iloc[-1]

st.title("🛠️ 3. 개선 과제 및 기대 효과")
st.markdown("#### ESG 각 항목에 대한 개선방안과 기대효과를 제안합니다.")

problems = []

if latest["ESG_Environmental"] < 60:
    problems.append({
        "분야": "환경 (E)",
        "과제": "탄소배출 과다, 에너지 효율 낮음",
        "해결책": [
            "친환경 설비 도입 (고효율 보일러, 폐열 회수 등)",
            "재생에너지 확대 (태양광, 수력)",
            "탄소배출권 거래 참여"
        ],
        "기대효과": "에너지 비용 절감, 글로벌 친환경 인증 획득",
        "그래프컬럼": "ESG_Environmental"
    })

if latest["ESG_Social"] < 60:
    problems.append({
        "분야": "사회 (S)",
        "과제": "직원 만족도 및 사회적 책임 부족",
        "해결책": [
            "유연근무제, 복지 확대",
            "다양성/포용성 확대",
            "지역사회 연계 프로그램 실행"
        ],
        "기대효과": "직원 유지율 개선, 대외 이미지 향상",
        "그래프컬럼": "ESG_Social"
    })

if latest["ESG_Governance"] < 60:
    problems.append({
        "분야": "지배구조 (G)",
        "과제": "이사회 다양성 부족, 투명성 낮음",
        "해결책": [
            "외부 감사 및 윤리경영 강화",
            "이사회 다양성 확대",
            "리스크 평가 체계 도입"
        ],
        "기대효과": "투명성 제고, 투자자 신뢰 향상",
        "그래프컬럼": "ESG_Governance"
    })

for p in problems:
    st.markdown(f"### 🔍 {p['분야']}")
    st.markdown(f"- **📌 과제**: {p['과제']}")
    st.markdown("**🧩 해결책**")
    for s in p["해결책"]:
        st.markdown(f"  - {s}")
    st.markdown(f"**🎯 기대효과**: {p['기대효과']}")
    st.line_chart(df.set_index("Year")[[p["그래프컬럼"]]])
    st.markdown("---")

if not problems:
    st.success("모든 ESG 항목이 양호한 수준입니다. 🎉")

# 요약 등급
st.markdown("#### 📊 최신 ESG 등급 요약")
st.markdown(f"""
- **환경 (E)**: `{get_grade(latest['ESG_Environmental'])}`
- **사회 (S)**: `{get_grade(latest['ESG_Social'])}`
- **지배구조 (G)**: `{get_grade(latest['ESG_Governance'])}`
- **종합 ESG**: `{get_grade(latest['ESG_Overall'])}`
""")
