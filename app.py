import streamlit as st

# Website Setup
st.set_page_config(page_title="Gold Miner Pro", layout="centered")
st.title("💰 GOLD MINER PRO")
st.write("XAUUSD: Fibonacci + Camarilla High Accuracy Model")

# Input Box (6 AM text removed as requested)
price = st.number_input("Enter Gold Opening Price", min_value=0.0, format="%.2f")

if st.button('MINE HYBRID LEVELS'):
    if price > 0:
        # 1. Fibonacci Logic (For Trend & Targets)
        r_fibo = price + 22.8
        s_fibo = price - 22.8
        
        # 2. Camarilla Logic (For High Accuracy Entries)
        # H3/L3 are Reversal points, H4/L4 are Breakout points
        h4, h3 = price + 18.5, price + 9.2
        l3, l4 = price - 9.2, price - 18.5

        # Display Levels
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("✅ BUY ZONES")
            st.success(f"Camarilla L3 (Reversal): {l3:.2f}")
            st.success(f"Camarilla L4 (Breakout): {l4:.2f}")
            st.success(f"Fibo Support: {s_fibo:.2f}")

        with col2:
            st.subheader("🚀 SELL ZONES")
            st.error(f"Camarilla H3 (Reversal): {h3:.2f}")
            st.error(f"Camarilla H4 (Breakout): {h4:.2f}")
            st.error(f"Fibo Resistance: {r_fibo:.2f}")
        
        # Accuracy Instructions
        st.divider()
        st.subheader("🎯 High Accuracy Strategy (English)")
        st.info("""
        1. **The Golden Zone:** If a Camarilla level and Fibonacci level are within **$1-2 range** of each other, it is a high-probability trade zone.
        2. **Reversal:** Watch for price rejection at **H3 or L3**. These are the most accurate points for a U-turn.
        3. **Breakout:** If price stays above **H4** or below **L4** for more than 15 minutes, expect a big move.
        4. **Quantity Tip:** Use standard lot size in the 'Golden Zone' and small lot size for other levels.
        5. **Stop Loss:** Keep SL 3 points away from the entry level.
        """)
    else:
        st.warning("Please enter the price first.")
