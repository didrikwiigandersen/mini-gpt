from config import DATA_FILE

def main():
    # Read in the dataset
    with open(DATA_FILE, 'r', encoding='utf8') as f:
        text = f.read()

    print(text[:1000])

if __name__ == '__main__':
    main()

