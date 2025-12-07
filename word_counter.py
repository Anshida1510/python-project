def count_words(sentence):
    """Count characters, words, and vowels in a sentence."""
    chars = len(sentence)
    words = len(sentence.split())
    vowels = sum(1 for char in sentence.lower() if char in 'aeiou')
    return chars, words, vowels

sentence = input("Enter a sentence: ")
chars, words, vowels = count_words(sentence)

print("\n=== Word Counter Results ===")
print(f"Characters: {chars}")
print(f"Words: {words}")
print(f"Vowels: {vowels}")
