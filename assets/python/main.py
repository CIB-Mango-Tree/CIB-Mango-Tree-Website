import csv
import pandas as pd
import numpy as np
import random


def find_ngrams(input, n):
   input = input.split(' ')
   output = {}
   for i in range(len(input)-n+1):
       g = ' '.join(input[i:i+n])
       output.setdefault(g, 0)
       output[g] += 1
   return output


# Make a Text Dataset
alphabet = 'abcdefghijklmnopqrstuvwxyz'
list_to_df = []
concat_text = ""

for i in range(100):
    time = i
    text = ''
    for gen_word_i in range(10):
        word = ''
        num_of_letters = random.randint(3,4)
        for gen_letter_i in range(num_of_letters):
            random_num = random.randint(0,25)
            generated_letter = alphabet[random_num]
            word = word+generated_letter
        text = text+word+' '
        concat_text += text
    output_dict = {'time':i, 'text':text}
    list_to_df.append(output_dict)

output_df = pd.DataFrame(list_to_df)

f = open("random.txt", "w")
f.write(concat_text)

ngrams = find_ngrams(concat_text,4)

gram_df = pd.DataFrame(ngrams.items())

result_dict = {}

for index, row in output_df.iterrows():
    for gramRow in gram_df.iterrows():
        if gramRow[1].to_string() in row.text:
            result_dict = {'timestamp': row.time, 'ngram': gramRow[0]}

print(result_dict)

# for item in output_df.items():
#     print(item)