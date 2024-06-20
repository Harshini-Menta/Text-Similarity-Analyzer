from difflib import SequenceMatcher

with open("sample1.txt") as file1 ,open("sample2.txt") as file2:
    data_file1 = file1.read()
    data_file2 = file2.read()
    matches = SequenceMatcher(None ,data_file1 ,data_file2).ratio()
    print(f" The Plagiarized Content is {matches*100} ")
    