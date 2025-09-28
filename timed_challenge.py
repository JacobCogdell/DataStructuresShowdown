# Pick one question from timed_challenge.txt
# Paste the question as a comment below
# Set a timer for 30 minutes and complete the question!

# Group 2: Fast Lookup / Uniqueness
# 5. Unique Word Count
# Count how many distinct words are in the collection.
# Input: ""
# Output: 5

def unique_word_count(text):
    words = text.split()
    unique_words = set(words)
    return len(unique_words)

# Testing
input_text = "one fish two fish red fish blue fish"
print("Sample Text:" ,input_text)
print("Unique Word Count:", unique_word_count(input_text))

input_text = "How much wood would a woodchuck chuck if a woodchuck could chuck wood"
print("Sample Text:" ,input_text)
print("Unique Word Count:", unique_word_count(input_text))

input_text = ""
print("Sample Text:" ,input_text)
print("Unique Word Count:", unique_word_count(input_text))

input_text = "Jacob Jacob Jacob Jacob Jacob"
print("Sample Text:" ,input_text)
print("Unique Word Count:", unique_word_count(input_text))


