# Create a basic sentence checker that takes in a stream of characters and determines whether they form valid sentences.
# If a sentence is valid, the program should print it out.
# We can consider a sentence valid if it conforms to the following rules:
# 1.	The sentence must start with a capital letter, followed by a lowercase letter or a space.
# 2.	All other characters must be lowercase letters, separators (,,;,:) or terminal marks (.,?,!,‽).
# 3.	There must be a single space between each word.
# 4.	The sentence must end with a terminal mark immediately following a word.

#====================================================================================================================
# Solution

def sentence_validation(word_stream):

    terminator = False

    for i in range(len(word_stream)):

        # Checks for case 1
        if i == 0 and not word_stream[i].isupper():
            return

        # Checks for case 2
        if word_stream[i].isupper() and i != 0:
            return
        if not word_stream[i].isalnum() and not word_stream[i].isspace() and i != len(word_stream)-1:
            return

        # Checks for case 3
        if word_stream[i].isspace() and i < len(word_stream)-1:
            if word_stream[i+1].islower() and word_stream[i+1].isalpha():
                continue
            else:
                return

        # Checks for case 4
        if i == len(word_stream)-1:
            if word_stream[i] == '.' or word_stream[i] == '?' or word_stream[i] == '!' or word_stream[i] == '‽':
                terminator = True

    if terminator:
        print(word_stream)


# Tests
sentence_validation("This is a valid sentence.")                # All cases passed
sentence_validation("this is not a valid sentence.")            # Fails capital first
sentence_validation("This is not a valid sentence")             # Fails terminal mark
sentence_validation("Th☺is is no♣t a valid sent☻ence.")        # Fails legal characters
sentence_validation("This is not a vaLid seNtence.")            # Fails all lowercase after start
sentence_validation("This  is  not  a  valid  sentence.")       # Fails single space between word
