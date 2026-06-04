# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Setup

```bash
pip install -r requirements.txt
curl -o input.txt https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt
```

## Run

```bash
python gpt.py
```

## Architecture

This project builds a character-level GPT language model from scratch, following [Andrej Karpathy's tutorial](https://www.youtube.com/watch?v=kCc8FmEb1nY).

- `gpt.py` — the full model implementation and training script
- `gpt_dev.ipynb` — development notebook for experimentation
- `input.txt` — tinyshakespeare training data (not committed, download via curl above)

The model is a decoder-only transformer trained on character-level tokenization of the Shakespeare dataset.
