# Function to read a text file and count unique word occurrences
def count_word_occurrences(file_path):
    word_count = {}
    
    try:
        with open(file_path, 'r') as file:
            for line in file:
                words = line.split()
                for word in words:
                    word = word.strip('.,!?()[]{}"\'')
                    word = word.lower()
                    if word not in word_count:
                        word_count[word] = 1
                    else:
                        word_count[word] += 1
    
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    
    return word_count

while True:
    file_path = input("Enter the path of the text file: ")
    
    word_occurrences = count_word_occurrences(file_path)
    
    if word_occurrences is not None:
        break  

for word, count in sorted(word_occurrences.items()):
    print(f"{word}: {count} times")
