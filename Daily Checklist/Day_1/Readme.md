# 📘 Day 1 — NumPy Basics

> **100 Days of AI Engineer Challenge**
> **Date:** 15 August 2026
> **Topic:** Python NumPy Fundamentals

---

## 🎯 Objective

Learn the foundational building block of numerical computing in Python — **NumPy**.
NumPy's `ndarray` is the backbone of nearly every data science, ML, and deep learning library.

---

## 📂 Folder Structure

```text
Day_1/
├── Codes/
│   ├── arr_basics.py       # Array properties — ndim, shape, dtype, size
│   ├── create_arr.py       # Creating arrays — zeros, ones, linspace, arange, reshape
│   ├── indx_slic.py        # Indexing & slicing (positive + negative)
│   ├── operations.py       # Element-wise arithmetic operations
│   ├── aggregation.py      # Aggregation functions with axis parameter
│   ├── reshaping.py        # reshape() and flatten()
│   ├── broadcasting.py     # Broadcasting — scalar & array combinations
│   └── mini_project.py     # 🏆 Mini Project — Student Marks Analyzer
├── Data/
│   └── sample_marks.csv    # Sample dataset (7 students × 4 subjects)
├── Notebook/
│   └── day_1numpy.py       # All concepts combined in one script (235 lines)
├── Notes.md                # Learning notes & reflections
└── Output/
    └── Readme.md           # ← You are here
```

---

## 📝 Concepts Covered

### 1. Array Basics (`arr_basics.py`)
Created a 1D array and explored its core properties: `ndim`, `shape`, `dtype`, and `size`.

### 2. Array Creation (`create_arr.py`)
Practiced multiple ways to create arrays using `np.zeros()`, `np.ones()`, `np.linspace()`, `np.arange()`, and `reshape()`.

### 3. Indexing & Slicing (`indx_slic.py`)
Learned positive indexing, slicing with step, and negative indexing to access and reverse array elements.

### 4. Arithmetic Operations (`operations.py`)
Performed element-wise addition, subtraction, multiplication, exponentiation, and division between two arrays.

### 5. Aggregation Functions (`aggregation.py`)
Used `sum()`, `mean()`, `min()`, `max()`, and `std()` on a 2D array — with `axis=0` (per column) and `axis=1` (per row).

### 6. Reshaping (`reshaping.py`)
Transformed array dimensions using `reshape()` (1D → 2D) and `flatten()` (any dimension → 1D).

### 7. Broadcasting (`broadcasting.py`)
Explored how NumPy automatically handles operations between arrays of different shapes — array + scalar, 2D + column vector, 2D + row vector, and array × scalar.

---

## 🏆 Mini Project — Student Marks Analyzer (`mini_project.py`)

A practical project that combines **every concept** from Day 1 — all without a single Python loop.

| Concept Used | Application |
|-------------|-------------|
| Arrays & Shape | Stored marks as a 5×4 matrix, extracted dimensions |
| Indexing & Slicing | Retrieved single student's marks and all marks for one subject |
| Aggregation + Axis | Computed per-student and per-subject `mean`, `max`, `min`, `std` |
| Broadcasting | Compared each student's average against the class average |
| Vectorization | Used `np.where()` for pass/fail and `np.argmax()` for top student |

---

## 📊 Dataset (`sample_marks.csv`)

| Name | Math | Science | English | History |
|------|------|---------|---------|---------|
| Asha | 85 | 78 | 92 | 88 |
| Ravi | 72 | 69 | 75 | 80 |
| Meera | 90 | 95 | 89 | 94 |
| Vikram | 60 | 65 | 70 | 68 |
| Neha | 88 | 84 | 91 | 87 |
| Karan | 45 | 38 | 52 | 49 |
| Divya | 95 | 98 | 94 | 96 |

---

## 🔑 Key Takeaways

- **NumPy's `ndarray`** is the foundation of numerical computing in Python
- **Vectorization** replaces slow Python loops with fast C-level operations
- **Broadcasting** automatically handles shape mismatches during operations
- **`axis=0`** = per column, **`axis=1`** = per row
- **`reshape()`** and **`flatten()`** allow flexible dimension transformations

---

## 🧠 Areas to Revise

- [ ] `axis=0` vs `axis=1` with more 2D arrays
- [ ] Broadcasting rules for complex shapes
- [ ] Reshaping multidimensional arrays (3D+)
- [ ] Vectorized conditionals (`np.where`)

---

## ⚙️ How to Run

```bash
pip install numpy
python "Daily Checklist/Day_1/Codes/mini_project.py"
python "Daily Checklist/Day_1/Notebook/day_1numpy.py"
```

---

## 🔗 Resources

- [NumPy Documentation](https://numpy.org/doc/stable/)
- [NumPy Quickstart](https://numpy.org/doc/stable/user/quickstart.html)
- [Broadcasting Rules](https://numpy.org/doc/stable/user/basics.broadcasting.html)

---

> **Day 1 completed. 🚀** — The journey of 100 days begins with a single array.
