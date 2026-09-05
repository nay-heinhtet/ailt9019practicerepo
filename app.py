import streamlit as st

HKD_TO_USD_RATE = 0.128

st.title("HKD to USD Converter")

hkd = st.number_input("Amount in HKD", min_value=0.0, step=1.0, format="%.2f")
usd = hkd * HKD_TO_USD_RATE

st.write(f"{hkd:.2f} HKD → {usd:.2f} USD")
st.caption(f"Fixed rate used: 1 HKD = {HKD_TO_USD_RATE} USD")
