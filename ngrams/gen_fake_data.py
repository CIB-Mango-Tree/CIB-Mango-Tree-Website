import pandas as pd
import random

alphabet = 'abcdefghijklmnopqrstuvwxyz'


def make_fake_dataset():
    records = []
    usernames = ["jesus69", "spaniardfarmer", "kisheater", "thugfest"]

    def get_random_username():
        return random.choice(usernames)

    for i in range(100):
        words = []
        for _ in range(10):
            num_of_letters = random.randint(3, 4)

            word = ""
            for _ in range(num_of_letters):
                random_num = random.randint(0, 25)
                generated_letter = alphabet[random_num]
                word += generated_letter
            words.append(word)

        text = " ".join(words)
        record = {'id': i, "username": get_random_username(),
                  'text': text}
        records.append(record)
    return records


data_frame = pd.DataFrame(make_fake_dataset())
data_frame.to_csv("ngrams/fake_data.csv", index=False)
