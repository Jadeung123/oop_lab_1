# Lab Overview

This lab focuses on **loading data** from the `Cities.csv` file, placing it into a **table** that includes **filter** and **aggregation** functions, and then using that table for various tasks.

```
oop_lab_1/
│
├── Cities.csv            # dataset_1
├── Countries.csv         # dataset_2
├── README.md             # This file
└── data_processing.py    # The analysis code
 
```

---

# Design Overview

## DataLoader Class

### `__init__` Function
- **Key:** `base_path`  
- **Description:**  
  Stores the base path in `self.base_path`.  
  - If `base_path` is `None`, it defaults to the current directory.  
  - Otherwise, it uses the provided `base_path` via `Path()` from the `pathlib` library.

### `load_csv` Function
- **Key:** `filename`  
- **Variables:**
  1. `filepath` — contains the path of the file (`self.base_path / filename`).  
  2. `data` — a list of dictionaries containing the CSV data read using `csv.DictReader`.

---

## DB Class

### '__init__' Function
- `self.tables` — an empty list.

### 'insert' Function
- **Keys:** `table`
- **Description:**
Add table to `self.tables` list.

### 'search' Function
- **Keys:** `table_name`
- **Description:**
Loop through self.tables to and return the table that have the same name as `table_name`.

---
## Table Class

### `__init__` Function
- **Keys:** `table_name`, `table`  
  - `self.table_name` — stores the table name.  
  - `self.table` — stores the table data.

### `filter` Function
- **Key:** `condition`  
- **Variable:**  
  - `temps` — a nested list of dictionaries containing only the data that meets the given condition.  
- **Return:**  
  A new `Table` object with `temps` as the argument.

### `aggregate` Function
- **Keys:** `aggregation_function`, `aggregation_key`  
- **Variable:**  
  - `temps` — a list of data values corresponding to the given `aggregation_key`.  
    - The function attempts to convert data to `float`; if conversion fails, it appends the raw value.  
- **Return:**  
  The result of applying `aggregation_function` to `temps`.

### `join` Function
- **Keys:** `table2`, `key`
- **Variables:** `joined`
- **Description:** This function will merge the current table with table2 by nested for loop through both table and find the row with the same key as `key` then make a temporary variable called `combined` then assign the current row1 to it then use the `.update` to merch `combined` with row2 then append `combined` to `joined`
- **Return:** Table of `joined`

### `__str__`
- **Return:** `self.table_name` with `self.table` joined using `:`  

---

# How to Run

The program includes **7 test cases**.  
You can run the `data_processing.py` using the `py` command.
