import random


def unique(string):
    """Checks if the given string is unique (each character is never repeated)"""
    lst = list(string)  # Change the string that is given into a list of characters.
    new_lst = []  # Empty list we will be adding stuff to.
    for char in lst:  # Loop through each element in the lst list.
        if char in new_lst:  # check if the element is in new_lst, if it is, the string is not unique.
            return False
        new_lst.append(char)  # append the char to this new list.

    return True  # If it goes through the for loop without running false, it is true.


def gen_unique(chars, length):
    """Generates a unique string with the given chars list and length."""
    if len(chars) < length:  # Basically if the length of the string they want is longer the char array, we cannot make a unique string out of it.
        print("The length you want the string is longer than the list of characters you provided, this means we cannot make a unique string out of it.")
        return None
    if not unique("".join(chars)):  # checks if the chars list is unique and only contains 1 of each character.
        print("The list that you provided contains duplicate characters making it not unique. Please do not do that.")
        return None

    unique_string = ""  # The unique string we generate
    modified_chars = chars[:]  # Duplicate of the chars list, we use this because we want to modify the list
    for x in range(0, length):  # This is what makes the string the length we want, we loop the number of times "length" is set to.
        rand_char = random.choice(modified_chars)  # Gets a random character/element from the modified_chars list.
        modified_chars.remove(rand_char)  # Removes the character that was picked from the modified_chars list so it cannot be repeated (keeping the string unique)
        unique_string += rand_char  # Adding the random character we generated to the unique string.

    return unique_string  # Returning the unique string to the user.


def words_unique(sentence):
    """Gets the number of words in a sentence that are unique."""
    words = sentence.split(" ")  # gets each word in the sentence into a list.
    uniques = 0  # Variable for the number of unique words.
    for word in words:  # Goes through eahc word in the words list.
        if unique(word):  # Checks if the word is unique with our prebuilt function.
            uniques += 1  # If it is unique, we add one to the uniques counter.

    return uniques  # Returning the number of unique words.


def sentence_unique(sentence):
    """Checks if this is a unique sentence (no duplicated characters), MINUS space."""
    words = sentence.split(" ")  # gets each word in the sentence into a list.
    chars = []
    for word in words:  # Go through each word in the sentence.
        for char in list(word):
            if char in chars:  # Checks if the character is in the chars list, if it is, the sentence is not unique.
                return False
            chars.append(char)  # Adds the character to the character list.
    return True  # If the loop never returns false, then the sentence is unique.


def remove_nonunique_elements(lst):
    """With the list lst, return the same list with non unique elements removed (like if there is two of the same element in the list)"""
    new_lst = []  # Our new list
    cannot_add = []  # Elements we cannot add because they are dupes.
    for element in lst:
        if element in new_lst or element in cannot_add:
            if element in cannot_add:
                continue
            else:
                cannot_add.append(element)
                while element in new_lst:
                    new_lst.remove(element)
                continue
        else:
            new_lst.append(element)
    return new_lst


def remove_nonunique(lst):
    """With the list lst, we return the list with elements removed that are not unique objects."""
    new_lst = []  # Our new list
    for element in lst:
        if unique(element):
            new_lst.append(element)
    return new_lst

