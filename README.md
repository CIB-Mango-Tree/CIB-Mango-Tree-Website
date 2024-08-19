# CIB-Mango-Tree-Repo

A series of tests for researchers to use to identify
Coordinated Inauthentic Behavior (CIB).

# Ngrams

The first, simple, test is identifying identical ngrams across
different bodies of text from different users.

## Output Schema

```ts
type Post = {
  id: string;
  username: string;
  text: string;
};

type NgramAndFreq = {
  tokens: string; // space delimited tokens of ngrams
  frequency: number;
};

type OutputPerUsername = {
  [_: string] /* Username */ : {
    freqs: NgramAndFreq[];
    /* foundIn: { ngram: Post[] }; */
  };
};
```
