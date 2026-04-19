## 💡 Bulb Switcher Problem

A clean and beginner-friendly Python project to solve the classic Bulb Switcher problem efficiently.

## 🚀 Problem Statement

There are n bulbs that are initially OFF.

You perform n rounds of toggling:

- Turn ON all bulbs
- Toggle every 2nd bulb
- Toggle every 3rd bulb
- Continue...
- Toggle the nth bulb

👉 Return the number of bulbs that are ON after all rounds.

## 🧠 Key Insight

Each bulb is toggled based on its factors.

- Even number of factors → bulb ends OFF
- Odd number of factors → bulb ends ON

👉 Only perfect squares have an odd number of factors.

So, the answer is:

⌊ √n ⌋

### Visual Example (n = 10)

| Bulb | Factors | Toggles | Final State |
| :--- | :--- | :--- | :--- |
| **1** | 1 | 1 (odd) | ON ✅ |
| **2** | 1, 2 | 2 (even) | OFF ❌ |
| **3** | 1, 3 | 2 | OFF ❌ |
| **4** | 1, 2, 4 | 3 | ON ✅ |
| **5** | 1, 5 | 2 | OFF ❌ |
| **6** | 1, 2, 3, 6 | 4 | OFF ❌ |
| **7** | 1, 7 | 2 | OFF ❌ |
| **8** | 1, 2, 4, 8 | 4 | OFF ❌ |
| **9** | 1, 3, 9 | 3 | ON ✅ |
| **10** | 1, 2, 5, 10 | 4 | OFF ❌ |

👉 **ON bulbs = 1, 4, 9 → total = 3**




## ▶️ How to Run

Run program
```
python bulb_switcher.py
```
Run tests
```
python -m unittest test_bulb_switcher.py
```


## 🌟 Key Takeaway

Instead of simulating toggles (slow), just count perfect squares.


## 🤝 Contributing

Pull requests are welcome! Feel free to improve explanations or add features.

## ⭐ If you like this project

Give it a star on GitHub ⭐ and share it!
