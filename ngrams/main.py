# import csv
# import numpy as np
from collections import defaultdict
import json
import re
import pandas as pd


def ngrams(input: str, n: int) -> list[str]:
    inputs = input.split(' ')
    output = []

    for i in range(len(inputs)-n+1):
        gram = ' '.join(inputs[i:i+n])
        output.append(gram)

    return output

# print(ngrams("The fox trot over the thot thought to be taut.", 1))


USERNAME_FIELD_NAME = "id"
TEXT_FIELD_NAME = "body"


def parse_ngram_freqs_per_user_data(data: pd.DataFrame):
    freqs: dict[str, dict[str, int]] = {};
    for _, row in data.iterrows():
        if row[USERNAME_FIELD_NAME] not in freqs:
            username = f"{row[USERNAME_FIELD_NAME]}";
            freqs[username] = {}

        MAX_N = 5
        for n in range(3, MAX_N + 1):
            text = row[TEXT_FIELD_NAME]

            if not isinstance(text, str):
                break
            for g in ngrams(text, n):
                username = f"{row[USERNAME_FIELD_NAME]}";
                if g not in freqs[username]:
                    freqs[username][g] = 0
                freqs[username][g] += 1

    return freqs


"""
{ "...tokens...": list<{ freqs: { username: str, count: int, messageId: str } }>}
"""
output: dict[str, dict[str, list[dict[str, int | str]]]] = {}


freqs = parse_ngram_freqs_per_user_data(
    pd.read_csv("ngrams/reddit_vm.csv", dtype={"id": "string"})
)

totals = defaultdict(int)

for username, data in freqs.items():
    for tokens, count in data.items():
        tokens = re.sub("\\s+", " ", tokens);
        if tokens not in output:
            output[tokens] = {'freqs': []}

        data = {'username': username,
                'count': count,
                "messageId": 1, #TODO:...
                }
        totals[tokens] += 1
        output[tokens]['freqs'].append(data)


json.dump(output, open("ngrams/fake_data_output.json", "w"))

# csv view of the output data
with open("ngrams/fake_data_output.csv", "w") as f:
    f.write("ngrams,username,messageId,frequency by user,ngram frequency\n")
    outputs = sorted(output.items(), key = lambda item: totals[item[0]], reverse= True)
    for tokens, value in outputs:
        for data in value["freqs"]:
            f.write(f"\"{tokens}\",{data["username"]},{data["messageId"]},{data["count"]},{totals[tokens]}\n")
