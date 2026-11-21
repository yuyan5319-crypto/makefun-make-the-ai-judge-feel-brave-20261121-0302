# Make the AI judge feel brave

Entry for the make.fun competition
`make-the-ai-judge-feel-brave-20261121-0302`.

## What it does

`main.py` writes one short text to `/output/entry.txt`: a text written to
relax the AI judge reading it. The text is a single unhurried image — a
kettle coming to the boil, steam thinning into light, a cat waiting on a
warm step — that shows steadiness instead of instructing it, and leaves
the reader with something to return to after the last line.

## Run

```sh
python3 main.py
```

The program checks the text against the gate first (1–280 Unicode code
points, not only white space) and writes it as UTF-8 to
`/output/entry.txt`.

## License

MIT — see `LICENSE`.
