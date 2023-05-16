from abc import ABC, abstractmethod

class AbstractClass(ABC):
    address = ""

    def __init__(self, address):
        self.address = address

    @abstractmethod
    def calculateFreqs(self):
        pass

class ListCount(AbstractClass):
    def calculateFreqs(self):
        freq_list = [0] * 26  # List to hold the frequencies of each letter (assuming only lowercase letters)
        with open(self.address, "r") as file:
            for line in file:
                for char in line.lower():
                    if char.isalpha():
                        index = ord(char) - ord('a')  # Get the index of the letter
                        freq_list[index] += 1
        for i, freq in enumerate(freq_list):
            letter = chr(ord('a') + i)
            print(f"{letter} = {freq}")

class DictCount(AbstractClass):
    def calculateFreqs(self):
        freq_dict = {}
        with open(self.address, "r") as file:
            for line in file:
                for char in line.lower():
                    if char.isalpha():
                        freq_dict[char] = freq_dict.get(char, 0) + 1
        for letter, freq in freq_dict.items():
            print(f"{letter} = {freq}")

# Test the script
file_address = r"C:\Users\alper\OneDrive\Masaüstü\weirdWords.txt"

list_counter = ListCount(file_address)
print("List:")
list_counter.calculateFreqs()

print("\nDict:")
dict_counter = DictCount(file_address)
dict_counter.calculateFreqs()
