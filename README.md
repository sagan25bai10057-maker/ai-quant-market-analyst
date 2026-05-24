# 📈 AI-Powered Market Quant & Contextual Chat Matrix

An advanced, enterprise-grade technical analysis dashboard and interactive quantitative ecosystem. This application bridges programmatic backtesting with generative AI—calculating moving average crossover indicators, charting strategy signals on structural canvas graphs, and hosting a context-aware chat assistant fueled by **Gemini 2.5 Flash**.

---

## ✨ Core Engineering Capabilities

* **Multi-Asset Compatibility:** Seamlessly parses global equities (e.g., `AAPL`, `NVDA`), index tracking funds (`SPY`, `QQQ`), and Indian commodities from the Multi Commodity Exchange (e.g., `GC=F` for Gold, `SI=F` for Silver in INR metrics).
* **Algorithmic Strategy Backtesting:** Programmatically calculates **20-Day (Fast)** and **50-Day (Slow)** Moving Averages over historical intervals.
* **Visual Trajectory Signal Markers:** Automatically highlights structural inflection points directly onto Plotly candlestick layouts:
  * 🟩 **Triangle Up:** Golden Cross (Bullish Momentum Buy Signal)
  * 🟥 **Triangle Down:** Death Cross (Bearish Trend Reversal Sell Signal)
* **Persistent Session State Chat Matrix:** Features a built-in conversational LLM model interface that retains multi-turn context memory across UI re-renders, enabling you to deep-dive interrogate specific asset datasets.

---

## 🛠️ Architecture & Tech Stack

* **Frontend Framework:** [Streamlit](https://streamlit.io/) (Reactive Python Web Canvas Engine)
* **Data Pipelines:** [yFinance](https://github.com/ranaroussi/yfinance) (Market historical arrays parsing engine)
* **Charting Core:** [Plotly Graph Objects](https://plotly.com/python/) (Interactive, high-frequency vector charts)
* **Artificial Intelligence Engine:** [Google GenAI SDK](https://github.com/google/generative-ai-python) (`gemini-2.5-flash` infrastructure framework)

---

## 📖 Comprehensive Step-by-Step Implementation Guide

To understand how this application was built or to set it up from absolute scratch, follow this comprehensive blueprint detailing every functional step:

### Step 1: Local Development Workspace Setup
Before writing any code, your local environment needs to be properly configured to process Python libraries without conflicts.
* Create a dedicated root directory on your computer named `STOCK AI`.
* Open your terminal inside this folder and run `python -m pip install -r requirements.txt`. This commands your Python package installer to download the necessary software frameworks: `streamlit` for the UI, `yfinance` to grab market tables, `plotly` for rich charts, and `google-genai` to manage the AI connection.

### Step 2: Formulating the Financial Data Pipeline
The application engine uses the `yfinance` library to bridge a background connection to Yahoo Finance's historical data APIs. 
* When you input a ticker symbol (like `AAPL` or `GC=F` for Indian Gold), the code triggers `yf.Ticker(ticker).history(period=period)`.
* This pulls a structured Pandas DataFrame into memory containing the standard daily pricing indexes: Open, High, Low, Close, and Trading Volume. Failsafe checks (`if df.empty:`) are written right below this to catch typos and prevent application crashes.

### Step 3: Engineering the Algorithmic Backtesting Strategy
Once raw numbers are successfully parsed into rows and columns, the code runs automated algorithms to spot market trends:
* **Moving Averages Calculation:** It processes `.rolling(window=20).mean()` and `.rolling(window=50).mean()` on historical closing points to create smooth tracking trend lines.
* **Crossover Logic Generation:** The program evaluates conditions where the fast 20-Day trendline passes through the slow 50-Day baseline. A differential step math tracker (`df['Signal'].diff()`) filters the exact dates when these structural crossings occur.
* **Plotly Marker Mapping:** It flags a buying signal as a bright green up-facing triangle marker (`triangle-up`) and a selling signal as a dark red down-facing triangle (`triangle-down`), placing them directly onto your interactive candle canvas layout.

### Step 4: Establishing Secret Environment Variables & Safeties
Security is the most critical pillar when engineering public software repositories. Hardcoding API credentials directly inside code text leaves them vulnerable to automated scrapers.
* **The Layered Verification Flow:** The code utilizes an advanced conditional chain (`api_key = os.getenv("GEMINI_API_KEY") or st.secrets.get("GEMINI_API_KEY")`). It looks for local computer system parameters first, looks inside cloud vault secrets second, and drops down to a manual sidebar web form input third if nothing else is found.
* **The Repository Shield:** A specialized `.gitignore` instruction file is introduced. It blocks git version tracking systems from picking up private local text configurations (like `.env`), keeping your live active credentials safe from public repository history.

### Step 5: Structuring the Persistent Context AI Chat Matrix
Unlike standard AI scripts that forget everything the moment you hit a button, this framework utilizes Streamlit's structural session history tracking (`st.session_state.messages`).
* **Background Context Feeding:** Whenever you switch tabs to text the AI model, the application automatically builds a comprehensive data text block behind the scenes. This block compresses current stock valuation metrics, industry domains, and a raw 10-day log history array.
* **Multi-Turn Conversation Memory:** It appends your current question to this background dataset alongside the last 5 active message exchanges. The entire context packet is dispatched cleanly through the modern `google-genai` SDK using `client.models.generate_content(model='gemini-2.5-flash', contents=prompt_payload)`. This enables the AI model to respond like a veteran Wall Street quant who knows the exact charts you are looking at.

### Step 6: Deploying Global Cloud Production
To transform this local file tracker into an open-source web application, you push the code files into your public GitHub space.
* Go live on the web by linking the public code repository over to [Streamlit Community Cloud](https://share.streamlit.io/).
* Open the **Advanced Settings** toggle during configuration, choose **Secrets**, paste your live Google AI Studio API credential (`GEMINI_API_KEY = "your_key"`), and launch. Streamlit handles hosting tasks, provisions infrastructure, reads your text dependency manifests, and spins out a permanent web address for users worldwide.

---

## 🚀 Local Deployment Quickstart

1. Clone this project repository:
   ```bash
   git clone [https://github.com/sagan25bai10057-maker/ai-quant-market-analyst.git](https://github.com/sagan25bai10057-maker/ai-quant-market-analyst.git)
   cd ai-quant-market-analyst
   Establish local parameter files:
2. Create a new file named .env in your root folder:

Plaintext
GEMINI_API_KEY=enter your key by creating from gemini studio ai
Initialize the application engine:

3. Bash
python -m streamlit run app.py
🤝 Special Thanks & Authorship
A very special thank you to everyone exploring, testing, and reviewing this algorithmic financial matrix dashboard!

This system was designed, engineered, and developed from concept to deployment by:

Sagan (sagan25bai10057-maker) Lead Developer & Quantitative Project Architect

If you found this software useful, encountered bug anomalies, or wish to contribute advanced charting metrics to the ecosystem, feel free to open a public issue or fork the repository structure for further pull requests!

⚖️ Disclaimer
This system is an open-source data analytics modeling tool built for experimental prototyping. None of the charts, technical indicator overlaps, or generative AI summaries constitute formal financial or investment advice.
