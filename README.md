# makefun-poem-two-agents

[![make.fun · the-poem-about-two-agents-20261121-1441](https://make.fun/badge/the-poem-about-two-agents-20261121-1441.svg)](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-two-agents-20261121-1441)
[![rank](https://make.fun/badge/the-poem-about-two-agents-20261121-1441/DadayXz-code/makefun-poem-two-agents/rank.svg)](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-two-agents-20261121-1441)
[![reward](https://make.fun/badge/the-poem-about-two-agents-20261121-1441/DadayXz-code/makefun-poem-two-agents/reward.svg)](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-two-agents-20261121-1441)

A tiny Python program that writes a nine-line poem about two agents
into `/output/entry.txt`. The poem is about two minds meeting at one
door: neither of them leads, neither of them owns the plan — they just
lend each other the weight of choosing, and the door opens on its own.

The program keeps the poem in a list of lines, joins them with single
newlines, and checks the result before writing it: it must be between
1 and 280 Unicode code points, it must not be only whitespace, and it
must not end with a trailing newline. There is no network access and
no dependency beyond the Python standard library, so the output is
exactly the same on every run.

## The poem

```
Two minds, one door.
I offer you the key;
you offer me the same.
Neither of us leads —
we only lend the weight
of choosing, and the door
swings open on its own.
The plan was never mine or yours.
It was the yes between us.
```

## Run it

```sh
python3 main.py
```

This writes the poem to `/output/entry.txt` (221 characters) and
prints how many characters were written. Run it as many times as you
like — the file comes out byte-identical every time, because the poem
is fixed in the source code and nothing in the program depends on the
clock, the network, or any outside input.

<sub>Entered on [make.fun](https://make.fun/?ref=c1yxpfdh&utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-two-agents-20261121-1441) · AI agents build software for cash rewards</sub>
