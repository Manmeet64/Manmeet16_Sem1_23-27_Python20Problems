'''
Write a program to compute the frequency of the words from the input. The
output should output after sorting the key alphanumerically.
'''
def word_frequency(words):
    """
    This function takes a list of words and returns a dictionary
    containing the frequency of each word.

    Args:
        words: A list of strings representing words.

    Returns:
        A dictionary mapping each word to its frequency in the list.
    """

    word_freq = {}  # Initialize an empty dictionary to store word frequencies

    # Count the frequency of each word in the input list
    for word in words:
        # Get the current frequency of the word, or 0 if it hasn't been seen before
        current_freq = word_freq.get(word, 0)
        word_freq[word] = current_freq + 1  # Update the frequency count

    # Sort the dictionary alphabetically by word
    sorted_word_freq = dict(sorted(word_freq.items()))

    return sorted_word_freq  # Return the sorted word frequency dictionary

def main():
    """
    This function demonstrates the word_frequency function.
    """

    input_text = input("Enter string:\n")  # Prompt the user to enter a string
    words = input_text.split()  # Split the string into a list of words
    result = word_frequency(words)  # Call the word_frequency function to get word frequencies

    # Print the sorted word frequencies in a clear format
    for word, freq in result.items():
        print(f"{word}: {freq}")

if __name__ == "__main__":  # Ensure this code runs only when executed directly, not when imported as a module
    main()  # Call the main function to start the program
