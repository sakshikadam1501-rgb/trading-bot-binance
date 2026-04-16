# Binance Futures Trading Bot (Testnet / Mock)

## 📌 Overview

A Python CLI-based trading bot that simulates placing MARKET and LIMIT orders on Binance Futures Testnet.

Due to API restrictions (KYC requirement), this project uses a **mocked API response**, while maintaining real-world architecture and structure.

---

## 🚀 Features

* MARKET & LIMIT orders
* BUY / SELL support
* CLI input using argparse
* Input validation
* Logging (requests, responses, errors)
* Modular code structure

---

## 🛠 Setup

```bash
git clone https://github.com/your-username/trading_bot.git
cd trading_bot
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

---

## 🔑 Environment Setup

Create `.env` file:

```env
API_KEY=your_key
API_SECRET=your_secret
```

---

## ▶️ Run Examples

### MARKET Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### LIMIT Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 60000
```

---

## 📄 Logs

Check:

```
trading_bot.log
```

---

## ⚠️ Note

Due to Binance Testnet requiring identity verification for API usage, this project simulates API responses.

The architecture allows easy replacement with real API by modifying `orders.py`.

---

## 📌 Assumptions

* User provides valid CLI inputs
* Mock response simulates successful execution

---

## 📷 Sample Output

```
Order ID: 123456
Status: FILLED
Executed Qty: 0.001
Avg Price: 65000
```
