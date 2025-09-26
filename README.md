# 📊 extract_numb.py

A simple Python utility to parse **GROMACS `.xvg` files** and extract numeric data (time vs. measurement). The script ignores comments and metadata lines, then computes the **minimum, maximum, and average** values from the second column.

---

## ✨ Features

* Reads one or more `.xvg` files.
* Skips comments (`@` and `#`) automatically.
* Extracts **time values** (first column) and **measurement values** (second column).
* Reports:

  * Total number of data points
  * Minimum value
  * Maximum value
  * Average value
* Handles malformed or empty lines gracefully.

---

## 🛠 Requirements

* Python 3.6+
* No external dependencies (only uses built-in modules: `os`, `sys`, `re`).

---

## 🚀 Usage

### Run for a single file:

```bash
python extract_numb.py data.xvg
```

### Run for multiple files:

```bash
python extract_numb.py file1.xvg file2.xvg file3.xvg
```

---

## 📂 Example Output

```text
File: data.xvg
  Data points: 500
  Minimum numb: 0.123
  Maximum numb: 1.876
  Average numb: 0.957
```

MIT License — feel free to use and modify. Contributions are welcome! 🚀
