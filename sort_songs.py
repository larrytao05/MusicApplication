import codecs
import csv

with open("songs.csv", "r") as f:
    data = csv.DictReader((line.replace('��name', '#').replace('\0','') for line in f), delimiter=',')
    
    dict = {}

    for song in data:
        print(song)