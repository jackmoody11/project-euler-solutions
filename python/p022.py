import csv
from utils import word_score

file = "p022.txt"


with open(file) as f:
    csvreader = csv.reader(f, delimiter=',')
    name_list = list(csvreader)[0]

name_list.sort()
score_list = []
for i in range(len(name_list)):
    score_list.append(word_score(name_list[i]) * (i + 1))

print(sum(score_list))
