def count_word(text):
    """Count the occurrences of each word in a given text and display them sorted alphabetically"""
    words = text.split()
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    sorted_word_counts = sorted(word_counts.items())
    longest_word_length = max(len(word) for word, _ in sorted_word_counts)
    for word, count in sorted_word_counts:
        print(f'{word:{longest_word_length}} : {count}')

"""Ask the user input"""
input_text = input("Text: ")
count_word(input_text)