import re

paragraph = "Python is popular in London. Many Developers use Python for Data Science."

capital_words = re.findall(r'\b[A-Z][a-zA-Z]*\b', paragraph)

print("Words starting with uppercase letters:", capital_words)
