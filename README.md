plp_python_week7
Week 7 Assignment: my notes and the report builder
Python Week 7 Assignment

my_notes.py: Creates, appends to, reads, and counts lines in a text file safely.
my_notes.txt: Text file storing the generated notes.
report_builder.py: Reads learner data from a CSV, calculates pass/fail statistics, and outputs a summary report with error handling.
hubs.csv: Source dataset containing learner names, hubs, and scores.
report.txt: Generated summary text report.
 Reflection
If you changed `"a"` (append mode) to `"w"` (write mode) when adding the fourth note in Question 1, Python would truncate and overwrite the file immediately. This would wipe out the first three notes you originally wrote, leaving only the final note in the file.
