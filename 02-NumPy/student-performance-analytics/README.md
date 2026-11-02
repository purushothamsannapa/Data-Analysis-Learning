# Student Performance Analytics using NumPy

## Project Overview

Student Performance Analytics is a Python project developed using NumPy to analyze student marks and generate useful academic performance reports.

The project reads student records from a CSV file, performs numerical calculations using NumPy arrays, and identifies student performance through averages, rankings, pass/fail results, and subject-wise analysis.

## Objectives

- Load student records from a CSV dataset.
- Analyze student marks using NumPy.
- Calculate total and average marks.
- Identify the class topper.
- Separate pass and fail students.
- Calculate subject-wise averages.
- Generate student rankings.
- Categorize students based on their academic performance.

## Technologies Used

- Python
- NumPy
- CSV dataset
- Visual Studio Code

## Project Structure

```text
student-performance-analytics/
│
├── data/
│   └── students.csv
│
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Dataset Description

The project uses a CSV dataset containing 10 student records.

The dataset includes the following columns:

- Name
- Python
- Java
- SQL
- Maths

Each student has marks for four subjects.

## Features and Analysis

### 1. Dataset Loading
Uses NumPy's `genfromtxt()` function to read student names, subject names, and marks from the CSV file.

### 2. Dataset Information
Displays the dimensions, shape, number of students, number of subjects, and data types of the arrays.

### 3. Total and Average Marks
Calculates each student's total and average marks using NumPy functions.

### 4. Class Topper
Identifies the student with the highest total marks using `np.argmax()`.

### 5. Pass and Fail Analysis
Classifies students with an average of 50 or above as pass and those below 50 as fail.

### 6. Subject-wise Analysis
Calculates the average marks for each subject using `np.mean()`.

### 7. Overall Analysis
Finds the highest mark, lowest mark, and overall average of the dataset.

### 8. Student Ranking
Uses `np.argsort()` to arrange students in descending order of average marks.

### 9. Performance Categorization
Uses `np.select()` to categorize student performance:

| Average Marks | Category |
|---|---|
| 90 and above | Excellent |
| 75–89.99 | Very Good |
| 60–74.99 | Good |
| 50–59.99 | Average |
| Below 50 | Fail |

## NumPy Concepts Used

- NumPy arrays
- `np.genfromtxt()`
- Array dimensions and shape
- Data types
- `np.sum()`
- `np.mean()`
- `np.argmax()`
- `np.max()` and `np.min()`
- `np.argsort()`
- `np.select()`
- Boolean conditions
- Array indexing and slicing

## Installation and Execution

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the project folder

```bash
cd student-performance-analytics
```

### 3. Install the required package

```bash
pip install -r requirements.txt
```

### 4. Run the project

```bash
python main.py
```

## Expected Output

The program displays:

- Student names and marks
- Dataset information
- Total and average marks
- Class topper
- Pass and fail student lists
- Subject-wise averages
- Overall analysis
- Student rankings
- Student performance categories

## Conclusion

This project demonstrates how NumPy can be used to perform numerical analysis on student performance data. It provides practical experience with array operations, calculations, sorting, filtering, and data analysis using Python.