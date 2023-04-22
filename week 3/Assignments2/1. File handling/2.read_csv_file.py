# Write a Python program that reads a CSV file and converts
# it into a dictionary. Each row of the CSV file should be
# a key-value pair in the dictionary.
import csv

with open("files/file.csv", "r", encoding='utf-8-sig') as file:
    people = {}
    csv_reader = csv.DictReader(file)

    for line in csv_reader:
        people[line["name"]] = {line["email"], line["age"]}

    print(people)



