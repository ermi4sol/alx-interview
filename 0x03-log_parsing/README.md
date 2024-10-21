## 0x03. Log Parsing

### Description
This project focuses on parsing and processing log data in real-time using Python. The goal is to read from standard input (stdin), process logs with a specific format, compute metrics, and display them every 10 lines or upon keyboard interruption (CTRL + C). It is a great exercise in **data processing**, **signal handling**, and **I/O operations** in Python.

---

### Learning Objectives
In this project, you will apply the following Python concepts:  
- **File I/O:** Reading input from `stdin`.
- **Signal Handling:** Handling keyboard interruptions (CTRL + C).
- **Data Processing:** Parsing strings to extract and aggregate data points.
- **Regular Expressions (optional):** Validating line formats.
- **Dictionaries:** Counting status codes and accumulating file sizes.
- **Exception Handling:** Managing invalid input gracefully.

---

### Requirements
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on **Ubuntu 20.04 LTS** using Python 3 (version 3.4.3)
- Code must follow **PEP 8** style guidelines (version 1.7.x)
- All files should be executable (`chmod +x`)
- Scripts should start with `#!/usr/bin/python3`
- A `README.md` file is mandatory

---

### Input Format
The input is a log entry with the following format:

```
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
```

- If the format does not match, the line is skipped.
- Example input:
  ```
  123.45.67.89 - [2023-05-10 12:34:56] "GET /projects/260 HTTP/1.1" 200 512
  ```

---

### Output
After every 10 lines or on keyboard interruption (CTRL + C), the following statistics are printed:

1. **Total File Size**: The sum of all `<file size>` values processed so far.
   ```
   File size: <total size>
   ```

2. **Status Code Count**: The number of occurrences for specific status codes, printed in ascending order:
   ```
   200: <count>
   301: <count>
   400: <count>
   401: <count>
   403: <count>
   404: <count>
   405: <count>
   500: <count>
   ```

---

### Example Run

```bash
./0-generator.py | ./0-stats.py
```

**Sample Output:**
```
File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3
File size: 11320
200: 3
301: 2
400: 1
401: 2
403: 3
404: 4
405: 2
500: 3
```

If the program is interrupted with `CTRL + C`, it will print the current metrics before exiting:

```
^CFile size: 17146
200: 4
301: 3
400: 4
401: 2
403: 6
404: 6
405: 4
500: 4
```

---

### Script Overview

The `0-stats.py` script:
1. Reads lines from **stdin**.
2. Extracts the status code and file size from each line.
3. Maintains a cumulative total of the file sizes and a count of each status code.
4. Prints the statistics after every 10 lines or when interrupted with `CTRL + C`.

---

### How to Use

1. **Make the script executable:**
   ```bash
   chmod +x 0-stats.py
   ```

2. **Run the generator and the script:**
   ```bash
   ./0-generator.py | ./0-stats.py
   ```

---

### Handling Interruptions

- If the user presses **CTRL + C**, the program will print the collected metrics before exiting.
- Example:
  ```
  ^CFile size: 17146
  200: 4
  301: 3
  400: 4
  401: 2
  403: 6
  404: 6
  405: 4
  500: 4
  ```

---

### Edge Cases Handled
- **Invalid Lines:** Lines with missing or non-integer values for status codes or file sizes are skipped.
- **Unexpected Input Format:** If a line doesn't match the expected format, it is ignored.
- **Graceful Exit:** Metrics are printed even when the script is interrupted with `CTRL + C`.

---

### Author
Ermiyas Solomon
This project is part of the **ALX Interview Preparation** track.