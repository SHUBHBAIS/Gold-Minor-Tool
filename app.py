import streamlit as st

st.set_page_config(page_title="Gold Miner", layout="centered")

st.title("💰 GOLD MINER 2.0")
st.write("XAUUSD 6:00 AM Special Levels")

# Input Box (Exactly like your Nifty tool)
price = st.number_input("Enter 6:00 AM Gold Price", min_value=0.0, format="%.2f")

if st.button('MINE LEVELS'):
    if price > 0:
        # Gold Logic
        r2, r1 = price + 15.0, price + 7.5
        s1, s2 = price - 7.5, price - 15.0
        
        # Color Coded Result Boxes
        st.success(f"Support Level 1: {s1:.2f}")
        st.success(f"Support Level 2: {s2:.2f}")
        st.error(f"Resistance Level 1: {r1:.2f}")
        st.error(f"Resistance Level 2: {r2:.2f}")
    else:
        st.info("Please enter the price first.")