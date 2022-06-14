import csv

words = []

with open('word_list.csv') as file:
    words_collection = csv.reader(file)
    for row in words_collection:
        if len(row[1]) >= 3:
            words.append(row[1].lower())
