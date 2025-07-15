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

# 기업명 수정
df.loc[df["CompanyName"] == "Company 1", "CompanyName"] = "Accor"

st.title("\ud83d\udcd8 1. \uae30\uc5c5 \uac1c\uc694 \ubc0f ESG \uc810\uc218")
st.markdown("#### \uae30\uc5c5\uc758 ESG \ud574\uc0c1 \uc815\ubcf4\ub97c \uc694\uc57d\ud569\ub2c8\ub2e4.")

st.markdown(f"""
- **기업명**: `{df['CompanyName'].iloc[0]}`
- **산업군**: `{df['Industry'].iloc[0]}`
- **지역**: `{df['Region'].iloc[0]}`
""")

st.markdown("#### \ud83d\udcca \uc5f0\ub3cc\ubcc4 ESG \uc810\uc218 \ubc0f \ub4f1\uae09")
st.dataframe(df[[
    "Year", "ESG_Environmental", "Environmental_Grade",
    "ESG_Social", "Social_Grade",
    "ESG_Governance", "Governance_Grade",
    "ESG_Overall", "ESG_Grade"
]])

