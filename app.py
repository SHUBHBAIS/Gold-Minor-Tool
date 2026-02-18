import streamlit as st

# Website Setup
st.set_page_config(page_title="Gold Miner Pro", layout="centered")
st.title("💰 GOLD MINER PRO (FIBO)")
st.write("XAUUSD Advanced Fibonacci Levels (6:00 AM Logic)")

# Input Box
price = st.number_input("Enter 6:00 AM Gold Price", min_value=0.0, format="%.2f")

if st.button('MINE ADVANCED LEVELS'):
    if price > 0:
        # Advanced Fibonacci Ratios
        r1, r2, r3 = price + 12.5, price + 22.8, price + 35.0
        s1, s2, s3 = price - 12.5, price - 22.8, price - 35.0

        # UI Design for Levels
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("✅ Support (BUY)")
            st.success(f"S1 (Minor): {s1:.2f}")
            st.success(f"S2 (Major): {s2:.2f}")
            st.success(f"S3 (Strong): {s3:.2f}")

        with col2:
            st.subheader("🚀 Resistance (SELL)")
            st.error(f"R1 (Minor): {r1:.2f}")
            st.error(f"R2 (Major): {r2:.2f}")
            st.error(f"R3 (Strong): {r3:.2f}")
        
        # Trading Instructions Section in English
        st.divider()
        st.subheader("📝 Trading Rule Book")
        st.info("""
        1. **Reversal Trade:** If price hits **S2 or R2** and forms a rejection candle (Hammer or Shooting Star), look for a reversal entry.
        2. **Breakout Trade:** If a 15-minute candle closes with a **Full Body** above R2 or below S2, follow the trend.
        3. **Retest Strategy:** The safest entry is waiting for the price to break a level and then **Retest** it before continuing the move.
        4. **Stop Loss (SL):** Always maintain a Stop Loss 3-4 points behind the entry level to manage risk.
        5. **Confirmation:** Never jump into a trade immediately; wait for the candle to **Close** for confirmation.
        """)
    else:
        st.warning("Please enter the opening price first.")
