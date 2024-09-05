# import csv
import numpy as np
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


USERNAME_FIELD_NAME = "id"
TEXT_FIELD_NAME = "body"


def parse_ngram_freqs_per_user_data(data: pd.DataFrame):
    freqs = {}
    for idx, row in data.iterrows():
        if row[USERNAME_FIELD_NAME] not in freqs:
            freqs[row[USERNAME_FIELD_NAME]] = {}

        MAX_N = 4
        for n in range(1, MAX_N + 1):
            text = row[TEXT_FIELD_NAME]

            if not isinstance(text, str):
                break
            for g in ngrams(text, n):
                if g not in freqs[row[USERNAME_FIELD_NAME]]:
                    freqs[row[USERNAME_FIELD_NAME]][g] = 0
                freqs[row[USERNAME_FIELD_NAME]][g] += 1

    return freqs


"""
listof
{ [username]: { freqs: { tokens: str, count: int } }}
"""
output = {}


freqs = parse_ngram_freqs_per_user_data(
    pd.read_csv("ngrams/reddit_vm.csv", dtype={"id": "string"})
)

for username, freq in freqs.items():
    for tokens, count in freq.items():
        if username not in output:
            output[username] = {'freqs': []}
        output[username]['freqs'].append({
            'tokens': tokens,
            'count': count,
        })

""" print(output) """
json.dump(output, open("ngrams/fake_data_output.json", "w"))
