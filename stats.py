def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    # Create an empty dictionary to store character counts
    char_counts = {}
    
    # Loop through each character in the text
    for char in text:
        # Convert to lowercase
        char = char.lower()
        if char in char_counts:
            char_counts[char] +=1 
        else: 
            char_counts[char] = 1 
        #Updates the character count 
        # Also checks if the character is already in the dictionary
        
    # Return the dictionary
    return char_counts


def sort_on(dict):
    return dict["num"]
def sort_dictionary(char_counts):
    dictionary_list = []   
    for char, num in char_counts.items():
        char_dict = {"char": char, "num" : num}
        dictionary_list.append(char_dict)
    dictionary_list.sort(reverse=True, key=sort_on)
    return dictionary_list