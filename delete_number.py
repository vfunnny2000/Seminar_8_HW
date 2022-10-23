import csv
import json

def delete(number):
    number = int(number - 1)
    with open("phone_data.csv", "r+", encoding='utf-8') as f:
        lines = f.read().splitlines()
        lines.pop(number)

    with open("phone_data.json", "w", encoding='utf-8') as f:
        # f.write('\n'.join(lines) +'\n')
        f.write(json.dump(lines) + '\n')
        # print('\n'.join(lines))