import json

# numbers = [2, 3, 5, 7, 11, 13]

def writeFile(filename, numbers):
    with open(filename, 'w') as f:
        json.dump(numbers, f)

def readFile(filename, numbers):
    with open(filename, 'r') as f:
        numbers = json.load(f)
    print(numbers)

arr = []
readFile('numbers.json', arr)
