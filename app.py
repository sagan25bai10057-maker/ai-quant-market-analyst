import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
import pandas as pd
import os
from google import genai
from dotenv import load_dotenv
load_dotenv()
st.set_page_config(page_title="AI Market Quant Alpha",layout="wide")
st.title("📈 AI-Powered Market Quant & Chat Ecosystem")
st.markdown("An advanced technical backtesting engine fused with an interactive Gemini conversation matrix.")
st.sidebar.header("Control Matrix")
ticker=st.sidebar.text_input("Asset Ticker (e.g., AAPL, GC=F, SI=F)", value="AAPL").upper()
period=st.sidebar.selectbox("Time Horizon", options=["3mo", "6mo", "1y", "2y"], index=2)
try:
    api_key=st.secrets.get("GEMINI_API_KEY")
except Exception:
    api_key=None
if not api_key:
    api_key=os.getenv("GEMINI_API_KEY")
if not api_key:
    api_key=st.sidebar.text_input("Gemini API Key Keyway", type="password", help="Input your key from Google AI Studio")
if ticker:
    try:
        stock_data=yf.Ticker(ticker)
        df=stock_data.history(period=period)
        info=stock_data.info
        if df.empty:
            st.error("Engine mismatch: Invalid ticker identifier or empty timeline.")
        else: 
            current_price=df['Close'].iloc[-1]
            prev_price=df['Close'].iloc[-2]
            price_change=current_price - prev_price
            pct_change=(price_change / prev_price)*100
            col1, col2, col3, col4=st.columns(4)
            col1.metric("Current Price",f"${current_price:.2f}",f"{price_change:+.2f} ({pct_change:+.2f}%)")
            col2.metric("52 Week High",f"${info.get('fiftyTwoWeekHigh','N/A')}")
            col3.metric("Market Cap",f"${info.get('marketCap',0):,}")
            col4.metric("Forward P/E",f"{info.get('forwardPE','N/A')}")
            df['MA20']=df['Close'].rolling(window=20).mean()
            df['MA50']=df['Close'].rolling(window=50).mean()
            df['Signal']=0.0
            df.loc[df['MA20']>df['MA50'],'Signal']=1.0
            df['Position']=df['Signal'].diff()
            tab1,tab2=st.tabs(["📊 Strategy Analytics & Charts","💬 Live AI Quant Chatroom"])
            with tab1:
                st.subheader("Interactive Strategy Chart & Signals")
                fig=go.Figure()
                fig.add_trace(go.Candlestick(
                    x=df.index,open=df['Open'],high=df['High'],
                    low=df['Low'],close=df['Close'],name="Price Candles"
                ))
                fig.add_trace(go.Scatter(x=df.index,y=df['MA20'],name='Fast MA (20D)',line=dict(color='orange',width=1.5)))
                fig.add_trace(go.Scatter(x=df.index,y=df['MA50'],name='Slow MA (50D)',line=dict(color='cyan',width=1.5)))
                buys=df[df['Position']==1.0]
                fig.add_trace(go.Scatter(
                    x=buys.index,y=buys['MA20'],mode='markers',name='Golden Cross (Buy)',
                    marker=dict(symbol='triangle-up',size=13,color='lime',line=dict(width=1,color='black'))
                ))
                sells=df[df['Position']==-1.0]
                fig.add_trace(go.Scatter(
                    x=sells.index,y=sells['MA20'],mode='markers',name='Death Cross (Sell)',
                    marker=dict(symbol='triangle-down',size=13,color='red',line=dict(width=1,color='black'))
                ))
                fig.update_layout(xaxis_rangeslider_visible=False,template="plotly_dark",height=550)
                st.plotly_chart(fig, width='stretch')
                with st.expander("View Underlying Core Fundamentals Data"):
                    st.json({
                        "Asset Name":info.get('longName',ticker),
                        "Sector/Industry":f"{info.get('sector','N/A')}/{info.get('industry','N/A')}",
                        "Trailing P/E":info.get("trailingPE","N/A"),
                        "Price-to-Book":info.get("priceToBook","N/A"),
                        "Profit Margin":f"{info.get('profitMargins',0)*100:.2f}%"if info.get('profitMargins') else"N/A",
                        "ROA": f"{info.get('returnOnAssets',0)*100:.2f}%" if info.get('returnOnAssets') else"N/A"
                    })
            with tab2:
                st.subheader("Conversational Quantitative Chatroom")
                if not api_key:
                    st.warning("Establish a secure Gemini API Key connection in the control sidebar to open chat lines.")
                else:
                    market_context = f"""
                    You are an elite, active Wall Street Quant. You have full awareness of the asset context below:
                    - Target Asset Ticker: {ticker} ({info.get('longName','N/A')})
                    - Horizon Selected: {period}
                    - Current Valuation: ${current_price:.2f}
                    - Moving Averages status: 20-Day is ${df['MA20'].iloc[-1]:.2f}, 50-Day is ${df['MA50'].iloc[-1]:.2f}.
                    Recent data arrays:\n{df[['Close', 'Volume', 'MA20', 'MA50']].tail(5).to_string()}
                    Always provide crisp, institutional answers with key figures highlighted in bold.
                    """
                    if "messages" not in st.session_state:
                        st.session_state.messages=[
                            {"role":"assistant","content": f"System active.I am your specialized algorithmic assistant for **{ticker}**. Ask me about its valuation metrics, technical entry triggers, or trend reversals."}
                        ]
                    for msg in st.session_state.messages:
                        with st.chat_message(msg["role"]):
                            st.markdown(msg["content"])
                    if user_input := st.chat_input(f"Inquire details regarding {ticker}..."):
                        with st.chat_message("user"):
                            st.markdown(user_input)
                        st.session_state.messages.append({"role": "user", "content": user_input})
                        with st.spinner("Calculating quantitative projections..."):
                            try:
                                client=genai.Client(api_key=api_key)
                                prompt_payload=f"{market_context}\n\nConversation Timeline:\n"
                                for previous_msg in st.session_state.messages[-5:]:
                                    prompt_payload+=f"{previous_msg['role']}: {previous_msg['content']}\n"
                                prompt_payload+=f"user: {user_input}\nassistant:"
                                response = client.models.generate_content(
                                    model='gemini-2.5-flash',
                                    contents=prompt_payload
                                )
                                with st.chat_message("assistant"):
                                    st.markdown(response.text)
                                st.session_state.messages.append({"role":"assistant","content":response.text})
                                
                            except Exception as chat_err:
                                st.error(f"Ecosystem connection fault:{chat_err}")
    except Exception as general_err:
        st.error(f"Critical execution error:{general_err}")