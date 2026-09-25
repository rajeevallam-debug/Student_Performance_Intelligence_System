# Student Performance Intelligence System

A beginner-friendly NumPy notebook that analyzes a small, in-memory table of student marks and demonstrates array-based performance summaries, pass-threshold checks, and rankings.

## Overview

This project uses a 5 × 3 NumPy array containing marks for five students in three subjects: Python, Statistics, and Data Visualization. The notebook walks through the shape and indexing of the array, then applies NumPy operations to summarize performance. No external dataset or file is required; the sample marks are written directly in the notebook.

This is an educational demonstration, not a production student-information or predictive system. The data is a small sample and the notebook does not establish grading policy, infer causes, or make predictions.

## Objectives

- Represent tabular marks as a two-dimensional NumPy array.
- Practice array shape, dimensions, size, and indexing.
- Calculate per-student totals and averages.
- Identify the highest- and lowest-average students and rank students by average.
- Flag subject marks below 50 and identify students with at least one such mark.
- Calculate subject averages, maximum marks, and standard deviations.

## Dataset and inputs

The notebook defines this sample directly in code:

| Student | Python | Statistics | Data Visualization |
|---|---:|---:|---:|
| 1 | 85 | 78 | 92 |
| 2 | 65 | 72 | 68 |
| 3 | 95 | 91 | 89 |
| 4 | 45 | 52 | 48 |
| 5 | 76 | 81 | 79 |

There are 15 marks in total. A mark under 50 is treated as a failed subject for the notebook's Boolean demonstration. That threshold is an example encoded in the notebook, not a general grading recommendation.

## Technologies

- Python 3
- NumPy
- Jupyter Notebook or Google Colab

## Methodology and workflow

1. Create a NumPy array with five rows and three subject columns.
2. Inspect `shape`, `ndim`, and `size`, then access selected values by row and column.
3. Sum and average across each student's subject marks (`axis=1`).
4. Use `argmax` and `argmin` to locate the highest and lowest student averages.
5. Apply a `< 50` comparison and `any(..., axis=1)` to find students with at least one mark below the example threshold.
6. Select each subject column and calculate subject averages, maximum marks, and standard deviations (`axis=0`).
7. Sort the student averages in descending order with `argsort` to produce the ranking.

## Key analysis and results

The included outputs show:

- Student averages: **85.00, 68.33, 91.67, 48.33, 78.67** for Students 1–5.
- Highest average: **Student 3 (91.67)**.
- Lowest average: **Student 4 (48.33)**.
- Student 4 is the only student with at least one subject mark below 50.
- Subject averages: **Python 73.2**, **Statistics 74.8**, **Data Visualization 75.2**.
- Highest mark per subject: **Python 95**, **Statistics 91**, **Data Visualization 92**.
- Standard deviations by subject, as calculated by NumPy's default population standard deviation: approximately **17.23, 12.95, 15.99**.
- Ranking: **Student 3, Student 1, Student 5, Student 2, Student 4**.

## Project structure

```text
student-performance-intelligence-system/
├── README.md
└── Student_Performance_Intelligence_System.ipynb
```

## Run in Google Colab

1. Create a GitHub repository and upload the notebook, or download the ZIP linked below and extract it.
2. In Colab, choose **File → Open notebook → GitHub** and select the repository/notebook, or use **File → Upload notebook** to upload the `.ipynb` file.
3. Choose **Runtime → Run all**. The notebook only requires NumPy, which is normally available in Colab.

## Run in Jupyter

### Installation

Python 3 and Jupyter are needed. In a terminal, install the dependencies:

```bash
python -m pip install numpy notebook
```

### Usage

From the project directory, start Jupyter:

```bash
jupyter notebook
```

Open `Student_Performance_Intelligence_System.ipynb` and run the cells from top to bottom. No separate dataset download or configuration is needed.

## Screenshots and results

No screenshots are included yet. Add notebook screenshots here after capturing the array, summary outputs, and ranking in Jupyter or Colab. Keep the images in an `images/` directory and link them with relative paths, for example:

```markdown
![Student ranking output](images/student-ranking.png)
```

## Future improvements

- Read student marks from a CSV file instead of defining them in the notebook.
- Add column and student labels using a pandas DataFrame for clearer tabular output.
- Make the pass threshold configurable and validate input ranges and missing values.
- Add visual summaries such as subject-average and student-average charts.
- Expand the dataset and compare results across classes or terms, while documenting data provenance and privacy safeguards.

## Author

Add your name, GitHub profile, and any preferred contact or portfolio link here.

## License recommendation

**MIT License** is a simple choice for a small educational code repository if you own the notebook and intend to allow reuse. Before adding it, confirm you have rights to license all included material. The sample values are embedded in the notebook; if any came from real students, remove or anonymize them and confirm permission before publishing. If you do not want to grant reuse rights, omit a license file; without a license, GitHub users do not receive explicit permission to reuse the code.

To apply MIT, create a `LICENSE` file in the repository root using the standard MIT License text and replace `[year]` and `[fullname]` with your details.
