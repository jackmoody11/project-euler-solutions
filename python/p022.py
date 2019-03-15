import csv
import string


file = "p022.txt"


def calc_name_score(name):
    c_scores = {string.ascii_uppercase[i]: i + 1 for i in range(26)}
    score = 0
    for c in name:
        score += c_scores[c]
    return score


with open(file) as f:
    csvreader = csv.reader(f, delimiter=',')
    name_list = list(csvreader)[0]

name_list.sort()
score_list = []
for i in range(len(name_list)):
    score_list.append(calc_name_score(name_list[i]) * (i + 1))

print(sum(score_list))
