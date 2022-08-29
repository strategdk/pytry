#! python3
# from markdownify import markdownify

from markdownify import markdownify

import sys, os

print(__file__)
print(os.path.abspath(__file__));
print(os.path.dirname(__file__));
print(os.path.dirname(os.path.abspath(__file__)));

print('***')
print(sys.path)

for i in range(3):
    print('Hello Py!')


html = markdownify("<h1>Hello, World!</h1>")

print(html)
