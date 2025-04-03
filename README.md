# 📊 Volatility Indicators for Crypto Markets

This repository provides a collection of volatility metrics used to analyze cryptocurrency price behavior. It includes both simple return-based indicators and more advanced statistical models, implemented in Python and demonstrated in Jupyter Notebooks.

The repo is structured to support a series of blog posts hosted on [Substack](#) (coming soon), where each post walks through the theory and implementation of key volatility measures in the context of DeFi and crypto markets.

---

## 🚀 Repository Structure

Volatility-Indicators-Crypto/

├── notebooks/

│   ├── 01_intro_volatility_metrics.ipynb

│   └── 02_advanced_volatility_models.ipynb

├── lib/

│   └── volatility_metrics.py

├── data/                  

│   └── BTCBUSD-1h-data.csv

│   └── ETHBUSD-1h-data.csv

├── README.md

---

## 📘 Covered in Blog Post 1: Intro to Volatility

Implemented in `01_intro_volatility_metrics.ipynb`:

- Log Returns
- Rolling Mean & Std Dev
- Z-Score of Returns
- Normalized Candle Height
- Range Over Price (trend-aware)
- Rate of Change (ROC)
- Average True Range (ATR)
- Efficiency Ratio (ROC / ATR)

Each metric is explained intuitively and visualized using real BTC price data.

---

## 📗 Upcoming in Blog Post 2: Advanced Volatility Models

Planned for future updates:

- Bollinger Bands
- EWMA Volatility
- ARCH / GARCH models
- ARIMA returns
- Drawdown analysis (Off ATH)
- Correlation matrix of indicators
- Yang-Zhang / Garman-Klass (optional extensions)

---

🧠 Author
This repo is maintained by @aguumg, a mathematician and researcher in risk modeling, DeFi, and crypto token engineering. For collaborations or consulting, feel free to reach out!
