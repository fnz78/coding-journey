## 📦 Column Deletion Problem (LeetCode Style)

A beginner-friendly Python project that solves the "Delete Columns to Make Sorted" problem.

## 🚀 Problem Statement

You are given an array of strings where all strings have the same length.

Your task is to count how many columns must be deleted so that each remaining column is sorted lexicographically (top to bottom).

## 🧠 Example
Input:
strs = ["abc", "bce", "cae"]

Grid:
a b c
b c e
c a e

Column 0 → a, b, c ✅ sorted
Column 1 → b, c, a ❌ not sorted
Column 2 → c, e, e ✅ sorted

Output:
1

## 📁 Project Structure

```text
column-deletion-project/
│
├── main.py             
├── solution.py         
├── test_cases.py        
├── README.md           
└── requirements.txt    
|──problem statement.txt

```


## 🛠️ How to Run
1. Clone the repo
   ```
   git clone https://github.com/your-username/column-deletion-project.git
   
   cd column-deletion-project
   ```
3. Run main program
   ```
   python main.py
   ```
3. Run tests
```
   python test_cases.py
```
   ## 🌟 Features
. Beginner-friendly implementation
. Clean and modular code
. Includes test cases
. Easy to extend for similar problems


