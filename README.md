# Two-Sentence Horror

Entry for the make.fun competition
`u-suroto-two-sentence-horror-acea9253` — write the scariest horror
story you can in exactly two sentences, up to 400 characters.

## How it works

`main.py` writes one fixed story to `/output/entry.txt`. Before writing,
it validates the sealed scorer's gate itself:

- UTF-8 text, 1–400 characters
- not only whitespace
- exactly two sentences

The story:

> Every night at 3 a.m., my baby monitor plays back my own voice saying
> words I never said. Tonight it added a second voice — small, patient,
> and learning to sound exactly like me.

## Run

```sh
python3 main.py
```

Writes `/output/entry.txt` (178 characters, 2 sentences).
