# import csv
# import numpy as np
import json
import pandas as pd


def ngrams(input: str, n: int) -> list[str]:
    input = input.split(' ')
    output = []

    for i in range(len(input)-n+1):
        gram = ' '.join(input[i:i+n])
        output.append(gram)

    return output

# print(ngrams("The fox trot over the thot thought to be taut.", 1))


def parse_ngram_freqs_per_user_data(data: pd.DataFrame):
    freqs = {}
    for idx, row in data.iterrows():
        if row.username not in freqs:
            freqs[row.username] = {}
        MAX_N = 2
        for n in range(1, MAX_N + 1):
            for g in ngrams(row.text, n):
                if g not in freqs[row.username]:
                    freqs[row.username][g] = 0
                freqs[row.username][g] += 1
    return freqs


"""
listof
{ [username]: { freqs: { tokens: str, count: int } }}
"""
output = {}


freqs = parse_ngram_freqs_per_user_data(
    pd.read_csv("ngrams/fake_data.csv")
)

for username, freq in freqs.items():
    for tokens, count in freq.items():
        if username not in output:
            output[username] = {'freqs': []}
        output[username]['freqs'].append({
            'tokens': tokens,
            'count': count,
        })

print(output)
json.dump(output, open("ngrams/fake_data_output.json", "w"))
