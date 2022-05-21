import csv
villains = [
    ['Doctor','No'],
    ['Rosa','Klebb'],
    ['Mister','Big'],
    ['Auric','Goldfinger'],
    ['Ernst','Blofrld'],
    ]
with open('villains','wt') as fout:
    csvout = csv.writer(fout)
    csvout.writerow(villains)

with open('villains','rt') as fin:
    cin = csv.reader(fin)
    villains = [row for row in cin]
print(villains)

with open('villains','rt') as fin:
    cin = csv.DictReader(fin,fieldnames=['first','last'])
    villains = [row for row in cin]

print(villains)
