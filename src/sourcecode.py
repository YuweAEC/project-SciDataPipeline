# src/sourcecode.py

def main():
    print("Processing data files...")
    with open('data/base.dat', 'r') as base_file:
        base_data = base_file.read()
    
    with open('data/data.dat', 'r') as data_file:
        data = data_file.read()
    
    combined_data = base_data + '\n' + data
    
    with open('data/combined.dat', 'w') as combined_file:
        combined_file.write(combined_data)
    
    print("Data files combined.")

if __name__ == '__main__':
    main()
