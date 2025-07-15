import streamlit as st
import pandas as pd

st.set_page_config(page_title="1. 기업 개요 및 ESG 점수", layout="centered")

CSV_FILE = "esg_data.csv"
df = pd.read_csv(CSV_FILE)

def get_grade(score):
    if score >= 80: return "A (우수)"
    elif score >= 60: return "B (보통)"
    elif score >= 40: return "C (주의)"
    else: return "D (위험)"

# 등급 계산
df["Environmental_Grade"] = df["ESG_Environmental"].apply(get_grade)
df["Social_Grade"] = df["ESG_Social"].apply(get_grade)
df["Governance_Grade"] = df["ESG_Governance"].apply(get_grade)
df["ESG_Grade"] = df["ESG_Overall"].apply(get_grade)

# 최근 연도
latest = df.iloc[-1]

st.title("📘 1. 기업 개요 및 ESG 점수")
st.markdown("#### 기업의 ESG 핵심 정보를 요약합니다.")

st.markdown(f"""
- **기업명**: `{df['CompanyName'].iloc[0]}`
- **산업군**: `{df['Industry'].iloc[0]}`
- **지역**: `{df['Region'].iloc[0]}`
""")

st.markdown("#### 📊 연도별 ESG 점수 및 등급")
st.dataframe(df[[
    "Year", "ESG_Environmental", "Environmental_Grade",
    "ESG_Social", "Social_Grade",
    "ESG_Governance", "Governance_Grade",
    "ESG_Overall", "ESG_Grade"
]])
