import pyttsx3 as pyttsx3

ConsonantsUnchanged = ['p', 'k', 'h', 'l', 'm', 'n']
Vowels = {
    'a': 'ah-',
    'e': 'eh-',
    'i': 'ee-',
    'o': 'oh-',
    'u': 'oo-'
}
SpecialCases = {
    'ai': 'eye-',
    'ae': 'eye-',
    'ao': 'ow-',
    'au': 'ow-',
    'ei': 'ay-',
    'eu': 'eh-oo-',
    'iu': 'ew-',
    'oi': 'oyo-',
    'ou': 'ow-',
    'ui': 'ooey-'
}


def pronounce(word):
    # validate input
    # check if input contains nothing but Consonants unchanged, 'w', vowels keys, spaces, apostrophes
    valid_chars_list = ConsonantsUnchanged + list(Vowels.keys()) + [' ', 'w', '\'', '’']
    input_string_test = word
    for allowed_char in valid_chars_list:
        input_string_test = input_string_test.replace(allowed_char, '')
    if input_string_test != '':
        for invalid_character in input_string_test:
            print(f"{invalid_character} is not a valid hawaiian character")
        return None
    word_list = list(word)
    if word.find('w') > 0:
        # w is present but it is not a first character
        letter_position = 0
        for letter in word:
            if letter == 'w':
                prev_letter = word[letter_position - 1]
                if prev_letter == 'i' or prev_letter == 'e':  # Pronounced as a v sound.
                    word_list[letter_position] = 'v'
            letter_position += 1

    for v in list(Vowels.keys()):
        letter_position = 0
        for letter in word_list:
            if letter == v:
                # we have a letter to check
                if letter_position < len(word_list) - 1:
                    # if this is not the last letter, get next one to see if there is a special case (2 letter)
                    next_char = word_list[letter_position + 1]
                    two_char = letter + next_char
                    if two_char in list(SpecialCases.keys()):
                        word_list[letter_position] = SpecialCases[two_char]
                        word_list.pop(letter_position + 1)
                    else:
                        # the two chars are not special case. Only replace single vowel.
                        word_list[letter_position] = Vowels[v]
                else:
                    # it is the last character so it can nto be the special case. Only replace single vowel.
                    word_list[letter_position] = Vowels[v]
            letter_position += 1

    if word_list[-1].endswith("-") and not word.endswith("-"):
        last = word_list[-1].rstrip("-")
        word_list.pop(-1)
        word_list.append(last)

    result = ''
    for converted_part in word_list:
        result += converted_part

    result = result.replace("- ", " ")
    # no hyphen before space
    return result


def speak_hawaiian():
    word_to_pronounce = input("Enter a hawaiian word to pronounce: ")
    pronounced = pronounce(word_to_pronounce.lower())
    if pronounced is not None:
        print(f"{word_to_pronounce} is pronounced {pronounced}")
        pyttsx3.speak(pronounced)


if __name__ == '__main__':
    speak_hawaiian()
    while input("Do you want to enter another word? Y/YES/N/NO \n Enter Y, YES, N or NO: ").startswith('Y'):
        speak_hawaiian()
