import nltk
from nltk import ngrams
# from nltk.tokenize import word_tokenize
# from nltk.corpus import stopwords
from collections import Counter
import numpy as np

nltk.download('punkt')
nltk.download('stopwords')

# Function to preprocess, tokenize sentences, and create n-grams
def tokenize_and_create_ngrams(sentences, max_n):
    all_n_grams_list = []
    for sentence in sentences:
        # Tokenize and convert to lowercase
        #tokens = word_tokenize(sentence.lower())
        tokens = sentence.split()
        # Filter out punctuation and stop words
        filtered_tokens = [word for word in tokens if word.isalpha()]
        # Create n-grams for all n up to max_n
        for n in range(1, max_n + 1):  # This will loop through 1 to max_n
            n_grams = ngrams(filtered_tokens, n)
            all_n_grams_list.extend([' '.join(gram) for gram in n_grams])
    return all_n_grams_list

# Normalize frequency function remains the same
def normalize_frequency(word_freq, total_count):
    return {word: count / total_count for word, count in word_freq.items()}

# Function to calculate frequency difference and sort the n-grams
def calculate_frequency_difference_and_sort(target_freq, normal_freq):
    # Calculate the frequency difference for n-grams present in both sets
    freq_diff = {ngram: target_freq.get(ngram, 0) - normal_freq.get(ngram, 0) for ngram in set(target_freq) | set(normal_freq)}
    
    # Sort the n-grams by the calculated frequency difference, highest difference first
    sorted_ngrams_by_diff = sorted(freq_diff.items(), key=lambda item: item[1], reverse=True)
    
    return sorted_ngrams_by_diff

# Sample sets of sentences
target_sentences = ['Im sorry, I cannot assist with that Ii'
    # ... your target sentences ...
]
normal_sentences = ['love to help! Ii will love to help'
    # ... your normal sentences ...
]

# Define max_n for the largest n-gram size
max_n = 3  # for unigrams, bigrams, and trigrams

# Tokenize and calculate frequency distribution for both sets with all n-grams up to max_n
target_ngrams = tokenize_and_create_ngrams(target_sentences, max_n)
normal_ngrams = tokenize_and_create_ngrams(normal_sentences, max_n)

# Count frequencies
target_ngram_freq = Counter(target_ngrams)
normal_ngram_freq = Counter(normal_ngrams)

# Normalize frequencies
# This step could be optional depending on whether you want to take text length into account
total_target_ngrams = sum(target_ngram_freq.values())
total_normal_ngrams = sum(normal_ngram_freq.values())
normalized_target_ngram_freq = normalize_frequency(target_ngram_freq, total_target_ngrams)
normalized_normal_ngram_freq = normalize_frequency(normal_ngram_freq, total_normal_ngrams)

# Calculate and sort n-grams by frequency difference
sorted_ngrams_by_freq_diff = calculate_frequency_difference_and_sort(normalized_target_ngram_freq, normalized_normal_ngram_freq)

# Select the top n-grams based on the frequency difference
top_n = 10
top_ngrams_by_freq_diff = sorted_ngrams_by_freq_diff

print(f"Top {top_n} n-grams by frequency difference: {top_ngrams_by_freq_diff}")

