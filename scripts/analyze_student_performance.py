import csv
from pathlib import Path

import numpy as np

DATA_FILE = Path(__file__).resolve().parent.parent / 'data' / 'student_marks.csv'


def load_data():
    with DATA_FILE.open(newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)


def main():
    rows = load_data()
    students = np.array([row['Student'] for row in rows], dtype=object)
    subjects = ['Maths', 'Science', 'English', 'History']
    marks = np.array([
        [int(row[subject]) for subject in subjects]
        for row in rows
    ], dtype=float)

    averages = marks.mean(axis=0)
    totals = marks.sum(axis=1)
    ranking = np.argsort(totals)[::-1]
    threshold = 75
    below_threshold = np.where(totals < threshold)[0]

    print('Subject Averages:')
    for subject, avg in zip(subjects, averages):
        print(f'  {subject}: {avg:.2f}')

    print('\nPerformance Ranking:')
    for rank_pos, idx in enumerate(ranking, start=1):
        print(f'  {rank_pos}. {students[idx]} -> Total: {totals[idx]:.0f}')

    print('\nStudents below threshold (score < 75 total):')
    if len(below_threshold) == 0:
        print('  None')
    else:
        for idx in below_threshold:
            print(f'  {students[idx]} -> Total: {totals[idx]:.0f}')


if __name__ == '__main__':
    main()
