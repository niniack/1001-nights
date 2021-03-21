#!/usr/bin/env python

import re
import sys
import string

male_patterns = [
    "he",
    "him",
    "his",
    "boys",
    "man",
    "men",
    "husbands",
    "kings",
    "princes",
    "wizards",
    "males",
    "sons",
    "brothers",
    "fathers",
    "masculine",
    "gentleman",
    "dervish",
    "dervishes",
    "porters",
    "masters",
]
female_patterns = [
    "she",
    "her",
    "hers",
    "girls",
    "woman",
    "women",
    "wife",
    "wives",
    "queens",
    "princess",
    "princesses",
    "witch",
    "witches",
    "females",
    "daughters",
    "sisters",
    "mothers",
    "feminine",
    "lady",
    "ladies",
    "mistress",
    "mistresses",
]

print()

document_text = open(sys.argv[1], "r")
text_string = document_text.read().lower()

male_frequency = {}
female_frequency = {}

male_count = 0
female_count = 0


def find_frequency(pattern_list, text_string, frequency_list):

    for p in pattern_list:
        # regex = r"\b(?=\w)" + re.escape(p) + r"\b(?!\w)"

        # regex = r"\b(?=\w)" + re.escape(p) + r"?\b"

        if p[-1] == "s":
            regex = r"\b(?=\w)" + re.escape(p) + r"?\b"
        else:
            regex = r"\b(?=\w)" + re.escape(p) + r"\b(?!\w)"

        match_pattern = re.findall(regex, text_string)

        # if match_pattern:
        #     word = match_pattern[0]
        #     count = len(match_pattern)
        #     frequency_list[word] = count

        for word in match_pattern:
            count = frequency_list.get(word, 0)
            frequency_list[word] = count + 1

    return frequency_list.keys()


female_words = find_frequency(female_patterns, text_string, female_frequency)

male_words = find_frequency(male_patterns, text_string, male_frequency)

for words in female_words:
    female_count += female_frequency[words]
    print(words, female_frequency[words])

for words in male_words:
    male_count += male_frequency[words]
    print(words, male_frequency[words])

print("Total Mentions of Female Pronouns/Nouns: " + str(female_count))
print("Total Mentions of Male Pronouns/Nouns: " + str(male_count))

if female_count > male_count:
    print("Female Dominant Story")
else:
    print("Male Dominant Story")