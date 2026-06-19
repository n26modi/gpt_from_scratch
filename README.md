# GPT from Scratch

Character-level GPT language model from scratch, in PyTorch, trained on the [tinyshakespeare](https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt) dataset. Built to deepen my understanding of the transformer architecture. Inspiration: [Andrej Karpathy's tutorial](https://www.youtube.com/watch?v=kCc8FmEb1nY).

## Setup

```bash
pip install -r requirements.txt
```

## Data

Download the tinyshakespeare dataset:

```bash
curl -o input.txt https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt
```

## Run

```bash
python gpt.py
```

## Config

The default config in gpt.py is tuned for CPU (small n_embd, block_size, n_layer). Training runs ~5000 steps and takes
~5 minutes on CPU. To scale up, increase n_embd, n_head, n_layer, and block_size, but a GPU is recommended for larger
configs.
  
## Sample output (val loss ~2.07)

He basten makeck great; as loved you? This wherio I not! 

And a to Would thy rene, deston me, heath it, empardm!


