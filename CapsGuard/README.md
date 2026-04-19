# 🛡️ CapsGuard – Capital Usage Validator

A beginner-friendly Python project to validate correct usage of capital letters in a word.

---

## 🚀 Features

- Checks if word follows valid capitalization rules
- Simple CLI interface
- Includes test cases
- Clean and minimal Python implementation

---

## ✅ Valid Cases

- "USA" → All uppercase
- "hello" → All lowercase
- "Google" → First letter uppercase

## ❌ Invalid Case

- "FlaG" → Incorrect capitalization

---

## 💻 Usage

### Run Main Program

```bash
python detect_capital.py
```
Run Test Cases
```
python test_cases.py
```


## 🧠 Core Logic
```
def detectCapitalUse(word):
    return word.isupper() or word.islower() or word.istitle()
```
    
## 🎯 Learning Goals

- Python string methods
- Writing clean functions
- Basic testing structure
- GitHub project setup

## ⭐ Support

If you like this project, give it a star ⭐
