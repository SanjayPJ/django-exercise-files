
import re

patterns = ['pattern_term0', 'pattern_term1']

text = "This is a text with pattern pattern_term0 and not the other one"

for pattern in patterns:
    print("i'm searching for " + pattern)
    match = re.search(pattern,text);
    if match:
        print("Match")
        print("Match started at : " , match.start())
    else:
        print("Not Match")

split_term = "@"

email = "sanjaypjayan@gmail.com"

print(re.split(split_term, email))

print(re.findall("pattern", "this is some patterns and it have alot of patterns"))

def find_all_re(patterns, text_phrase):

    for pattern in patterns:

        print("Searching for pattern {}".format(pattern))

        matches = re.findall(pattern, text_phrase)

        print(matches , "\n")


test_phrase = "sddd..s..sdd..sd...sdddd..sd...sdddd"
test_phrase_str = "This is a string! but is has punctuation. How can we remove it?"
test_phrase_str0 = "this is a string with numbers 12345 and a symbol #hashtag"

test_patterns = ["sd*","sd+","sd?", "sd{3}", "sd{2,3}", "s[sd]+"]
test_patterns_str = ["[^!.?]+", "[a-z]+", "[A-Z]+"]
test_patterns_str0 = [r'\d+',r'\D+',r'\s+',r'\S+',r'\w+',r'\W+']

find_all_re(test_patterns, test_phrase)
find_all_re(test_patterns_str, test_phrase_str)
find_all_re(test_patterns_str0,test_phrase_str0)
