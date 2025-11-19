# mini-gpt
A small GPT-style Transformer built from scratch in PyTorch

## Features

- Token-level language model trained on a text corpus
- Decoder-only Transformer architecture:
  - Token embeddings + positional embeddings
  - Multi-head self-attention
  - Feed-forward blocks
  - Residual connections and layer normalization
- Simple training loop with configurable hyperparameters
- Script for sampling / text generation from the trained model
- Clean, modular project structure suitable for further experiments

## References
- Let's build GPT: from scratch, in code, spelled out. (Andrej Karpathy, 2023)
