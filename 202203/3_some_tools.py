import collections
import pprint

data = (
    "this is a string",
    [1, 2, 3, 4],
    ("more tuples", 1.0, 2.3, 4.5),
    "this is yet another string"
)

pprint.pprint(data)
print(data)
print("*" * 20)
import glob

print(glob.glob("../*md"))

import string

print(string.punctuation)
print(string.ascii_letters)
print(string.digits)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.printable)
print(string.hexdigits)

from string import punctuation

intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)  # 制作翻译表

sentence1 = "this is string example....wow!!!"
print(trantab)
print(sentence1.translate(trantab))


sentence = "One, two, three, one, two, tree, I come from China."

trantab = str.maketrans(punctuation, ' '*len(punctuation))

words_count = collections.Counter(sentence.translate(trantab).lower().split())

print(words_count)
