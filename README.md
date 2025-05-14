# 💱 UdemyLessonCurrencyConversion

This is a simple Python script that converts a specified amount of **EUR** into another currency using historical exchange rates. It uses the [ExchangeRatesAPI.io](https://exchangeratesapi.io/) service and is built with `requests` for API calls and basic input handling.

---

## 🚀 Features

- Convert EUR to another currency (e.g., CAD, USD, GBP) on a specific date  
- Uses the free-tier of ExchangeRatesAPI (base EUR only)  
- Handles API errors gracefully  
- Lightweight and beginner-friendly

---

## 🧰 Requirements

- Python 3.6+
- `requests` library

Install dependencies with:

```bash
pip install -r requirements.txt
```

---

## 🔑 API Key Setup

This script requires an API key from [https://exchangeratesapi.io/](https://exchangeratesapi.io/).

1. Sign up for a free account.
2. Create a `.env` file in the root of the project directory.
3. Add your key like this:

```bash
API_KEY=your_api_key_here
```

Alternatively, set it as an environment variable in your system.

---

## 📝 Usage

Run the script in your terminal:

```bash
python ExchangeRateCurrencyConverter.py
```

You’ll be prompted to enter:
- A date (`YYYY-MM-DD`)
- The 3-letter currency code you want to convert EUR to
- The amount in EUR

Example:
```
Please enter the date in the format of "YYYY-MM-DD": 2020-03-10
What currency do you wish to convert EUR to? Use the 3-letter currency code: CAD
How much EUR do you want to convert: 100
```

---

## 📁 Project Structure

```
UdemyLessonCurrencyConversion/
├── ExchangeRateCurrencyConverter.py
├── .env.example         # Template for environment variables
├── requirements.txt     # Python dependencies
└── README.md
```

---

## ⚠️ Notes

- Free-tier accounts on ExchangeRatesAPI only support EUR as the base currency.
- If the currency code is invalid or the date is unsupported, the script will return a helpful error message.
- API calls may fail if rate limits are hit or the key is invalid.

---

## 💡 Future Enhancements

- Support more flexible base currencies (with paid API)
- Build a GUI (Tkinter, Streamlit, or web-based)
- Output results to CSV or database

---

## 📜 License

MIT — feel free to use, modify, or fork this project. Just don’t use it to power a global financial empire without sending coffee.