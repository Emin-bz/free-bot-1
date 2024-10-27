# Simple Moving Average Crossover Trading Bot

This is a basic cryptocurrency trading bot written in Python that uses a **Moving Average Crossover** strategy to determine buy and sell signals. The bot connects to popular crypto exchanges (such as Binance) through the **CCXT** library, which provides a unified interface for multiple exchanges.

---

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [How It Works](#how-it-works)
- [Usage](#usage)
- [Disclaimer](#disclaimer)
- [Get More](#get-more)

---

## Introduction

This bot is ideal for beginners looking to learn algorithmic trading with cryptocurrency. The strategy used here is the **Moving Average Crossover**, which signals a **buy** when the short-term average price is higher than the long-term average and a **sell** when it's lower.

## Features

- Uses the Moving Average Crossover strategy for trading signals
- Connects to multiple crypto exchanges via the CCXT library
- Configurable trading pair, moving average windows, and trade amount
- Easy to customize for more advanced strategies

## Requirements

- Python 3.x
- `ccxt` library (Install with `pip install ccxt`)

## Installation

1. Clone or download this repository.
2. Install the required Python package by running:

    ```bash
    pip install ccxt
    ```

## Configuration

1. Open the bot script (`bot.py`).
2. Add your exchange API keys:

    ```python
    API_KEY = "YOUR_API_KEY"
    API_SECRET = "YOUR_API_SECRET"
    ```

3. Adjust trading parameters as desired:

    - **symbol**: Set the trading pair, e.g., `'BTC/USDT'`.
    - **short_window** and **long_window**: Set the moving average periods.
    - **trade_amount**: Set the amount to trade per order.

## How It Works

1. The bot fetches recent historical prices for the specified trading pair.
2. It calculates the short-term and long-term moving averages.
3. It generates a **buy** signal if the short moving average is above the long moving average, a **sell** signal if the short is below the long, and a **hold** signal if there’s no change.
4. The bot places a market order based on the signal.

## Usage

1. Run the bot:

    ```bash
    python bot.py
    ```

2. Monitor the console for **buy**, **sell**, and **hold** signals.

3. The bot will continuously check prices and place trades every 60 seconds.

## Disclaimer

This is a sample bot for educational purposes. Trading cryptocurrency involves substantial risk and is not suitable for every investor. Use this bot at your own risk, and be cautious with real funds.

---

## Get More

Want to see a step-by-step tutorial on how to properly deploy this bot, along with exclusive content and advanced bot strategies? 

👉 Head over to my [Patreon page](https://www.patreon.com/c/tradingbotswithemin/membership) and choose a subscription plan to unlock access!

As a Patreon member, you’ll get:
- Full deployment tutorials
- Exclusive insights into trading bot strategies
- Access to private discussions and live Q&A sessions

---

Enjoy using the bot, and happy trading!
