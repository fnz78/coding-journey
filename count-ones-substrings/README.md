# 🔢 Count Substrings with Only 1's

## 📌 Problem
Given a binary string `s`, return the number of substrings that contain only `'1'`.

---

## 💡 Approach

Instead of checking all substrings (slow), we:
- Count consecutive `1`s
- Add them progressively

### Formula:
If a group has length `n`, substrings = `n * (n + 1) / 2`

---

## 🚀 Example

Input:
s = "0110111"


Output:

9


Explanation:
- "1" → 5 times  
- "11" → 3 times  
- "111" → 1 time  

---



## 🧪 Running Tests
Step 1: Install requirements
```
pip install -r requirements.txt
```
Step 2: Run tests
```
python -m unittest discover tests
```

📊 Complexity
Time: O(n)
Space: O(1)

## 🌟 Features
- Beginner-friendly logic
- Optimized solution
- Unit tests included

---
