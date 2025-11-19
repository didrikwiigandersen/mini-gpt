from config import DATA_FILE
import torch

device = 'cuda' if torch.cuda.is_available() else 'cpu'

def main():
    # Read in the dataset
    with open(DATA_FILE, 'r', encoding='utf8') as f:
        text = f.read()

    # Get set of characters
    chars = sorted(list(set(text)))
    vocab_size = len(chars)
    # Encoding
    stoi = { ch:i for i,ch in enumerate(chars) }
    encode = lambda s: [stoi[c] for c in s]

    # Decoding
    itos = {i: ch for i, ch in enumerate(chars)}
    decode = lambda l: ''.join([itos[i] for i in l])

    # Taking all the text in our training data and creating a tensor
    data = torch.tensor(encode(text), dtype=torch.long)

    # Separating dataset into train and validation sets
    n = int(0.9*len(data))
    train_data = data[:n] # 90% is train
    val_data = data[n:] # 10% is validation

    # Sample data
    torch.manual_seed(1337)
    batch_size = 4
    block_size = 8

    def get_batch(split):
        data = train_data if split == 'train' else val_data
        ix = torch.randint(len(data) - block_size, (batch_size,))
        x = torch.stack([data[i:i + block_size] for i in ix])
        y = torch.stack([data[i + 1:i + block_size + 1] for i in ix])
        x, y = x.to(device), y.to(device)
        return x, y

    xb, yb = get_batch('train')
    print(xb)









    

if __name__ == '__main__':
    main()

