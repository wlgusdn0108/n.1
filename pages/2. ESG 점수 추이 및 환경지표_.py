import streamlit as st
import pandas as pd

st.set_page_config(page_title="2. ESG 점수 추이 및 환경지표", layout="centered")
df = pd.read_csv("esg_data.csv")

st.title("📉 2. ESG 점수 추이 및 환경지표")
st.markdown("#### ESG 항목별 점수 변화와 환경 데이터를 시각화합니다.")

# ESG 점수 변화
st.markdown("##### ESG 점수 변화")
st.line_chart(df.set_index("Year")[["ESG_Environmental", "ESG_Social", "ESG_Governance", "ESG_Overall"]])

# 환경 성과
st.markdown("##### 🌿 환경 성과 지표 (탄소, 물, 에너지)")
eco1, eco2, eco3 = st.columns(3)

eco1.metric("🌍 탄소배출량", f"{df.iloc[-1]['CarbonEmissions']} tCO₂")
eco1.line_chart(df.set_index("Year")[["CarbonEmissions"]])

eco2.metric("💧 물 사용량", f"{df.iloc[-1]['WaterUsage']} tons")
eco2.line_chart(df.set_index("Year")[["WaterUsage"]])

eco3.metric("⚡ 에너지 소비", f"{df.iloc[-1]['EnergyConsumption']} MWh")
eco3.line_chart(df.set_index("Year")[["EnergyConsumption"]])

