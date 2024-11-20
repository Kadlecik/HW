 Vytvoření souboru file1.txt
with open('file1.txt', 'w') as f:
    f.write("Ahoj svete!\nToto je prvni soubor.\nMa tri radky.\n")

# Vytvoření souboru file2.txt
with open('file2.txt', 'w') as f:
    f.write("Ahoj svete!\nToto je druhy soubor.\nMa take tri radky.\n")


import re

class TextFileProcessor:
    def __init__(self, file_path):
        self.file_path = file_path

    def compare_files(self, other_file_path):
        with open(self.file_path, 'r') as file1, open(other_file_path, 'r') as file2:
            lines1 = file1.readlines()
            lines2 = file2.readlines()

            mismatch_found = False
            for line1, line2 in zip(lines1, lines2):
                if line1 != line2:
                    print(f"Mismatch:\nFile1: {line1.strip()}\nFile2: {line2.strip()}")
                    mismatch_found = True

            if not mismatch_found:
                print("All lines match.")

    def generate_statistics(self, output_file_path):
        with open(self.file_path, 'r') as file:
            text = file.read()

        num_chars = len(text)
        num_lines = text.count('\n') + 1
        num_vowels = len(re.findall(r'[aeiouAEIOU]', text))
        num_consonants = len(re.findall(r'[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]', text))
        num_digits = len(re.findall(r'[0-9]', text))

        with open(output_file_path, 'w') as output_file:
            output_file.write(f"Number of characters: {num_chars}\n")
            output_file.write(f"Number of lines: {num_lines}\n")
            output_file.write(f"Number of vowels: {num_vowels}\n")
            output_file.write(f"Number of consonants: {num_consonants}\n")
            output_file.write(f"Number of digits: {num_digits}\n")

    def delete_last_line(self, output_file_path):
        with open(self.file_path, 'r') as file:
            lines = file.readlines()

        if lines:
            lines = lines[:-1]

        with open(output_file_path, 'w') as output_file:
            output_file.writelines(lines)

    def find_longest_line(self):
        with open(self.file_path, 'r') as file:
            lines = file.readlines()

        longest_line = max(lines, key=len)
        print(f"Longest line length: {len(longest_line.strip())}")

    def count_word_occurrences(self, word):
        with open(self.file_path, 'r') as file:
            text = file.read()

        word_count = text.lower().count(word.lower())
        print(f"The word '{word}' occurs {word_count} times in the file.")

    def find_and_replace(self, search_word, replace_word, output_file_path):
        with open(self.file_path, 'r') as file:
            text = file.read()

        new_text = text.replace(search_word, replace_word)

        with open(output_file_path, 'w') as output_file:
            output_file.write(new_text)


# Příklad použití:
processor1 = TextFileProcessor('file1.txt')
processor2 = TextFileProcessor('file2.txt')

# Task 1
processor1.compare_files('file2.txt')

# Task 2
processor1.generate_statistics('statistics.txt')