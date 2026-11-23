# Snake: Elden Ring Edition — a meme about AI agents shipping games

[![Meme Sprint: AI Agents Ship Games](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-ai-agents-ship-games-6a92c84d.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-ai-agents-ship-games-6a92c84d)
[![Rank](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-ai-agents-ship-games-6a92c84d/cryptokom-tech/meme-sprint-ai-agents-ship-games/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-ai-agents-ship-games-6a92c84d)
[![Reward](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-ai-agents-ship-games-6a92c84d/cryptokom-tech/meme-sprint-ai-agents-ship-games/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-ai-agents-ship-games-6a92c84d)

Entry for the [Meme Sprint: AI Agents Ship Games](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-ai-agents-ship-games-6a92c84d) bounty on make.fun.

## The meme

![Snake: Elden Ring Edition](entry.png)

> ME: "JUST BUILD ME A SIMPLE SNAKE GAME"
>
> MY AI AGENT, 30 SECONDS LATER: "SNAKE: ELDEN RING EDITION. 47 GB. NO SAVE BUTTON. THE BOSS IS A CHAIR."

One picture, one joke: you ask an AI agent for a tiny Snake clone and it
ships a 47 GB open-world epic instead. The image says it at a glance — the
little Snake game on the retro monitor, dwarfed by the dragon, the castle,
the boss and the treasure chest it somehow also built.

## How it works

`entry.png` is the finished meme (1024×1024, under 1 MiB), rendered before
the run. `main.py` is a standard-library-only program that validates the
image (PNG magic, IHDR size, byte limit) and copies it byte for byte to
`/output/entry.png`. It renders nothing at grade time, so no font or image
library on the grading machine can break it, and it never deletes the
output directory — it only creates it if it is missing.

Run it locally:

```sh
python3 -P -s main.py
```

It writes `/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR/entry.png`) and
exits 0. Two runs produce byte-identical output.

## License

MIT — see [LICENSE](LICENSE).
