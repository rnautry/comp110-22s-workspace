"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730244043"
word = input("Enter a 5-character word: hello")
chosen_one = input("Enter a single charaacter: e")
print(word)
print(chosen_one)
print("Searching for e in hello")

s = "hello"
character = "e"
for e in s:
    if (e == character):
        print("c found at index ", s.index(character))