import re

email = 'email.address@example.com'
email_parts = re.split('@', email)
print("Email first part is "+email_parts[0])
print("Domain is "+email_parts[1])

term = 'term1'
phrase = "Searching for term1 in this string. There are more than term1 in this string."

match = re.search(term, phrase)

if match:
    print(match.start())
    print(match.end())
    print(phrase[match.start():match.end()])
    print("re.search returns first occurrence of the pattern")
else:
    print(term+" not found")

print(re.findall(term, phrase))
print("re.findall returns list of all occurrences of the pattern")

phrase = "sd sdd sddd sssd ssd sd sss ddd s d ss dd ssssssssd ddddddds ds dds dss dsdsdsd sdsdsds"
print(phrase)
print(re.findall('sd', phrase))
print(re.findall('sd*', phrase))
print("8 gives 0 or any number of occurrence.")
print(re.findall('sd+', phrase))
print("+ gives 1 or more occurrence.")
print(re.findall('sd?', phrase))
print("? gives 0 or 1 occurrence.")

print(re.findall('sd{3}', phrase))
print("{1,3} gives 3 occurrence.")
print(re.findall('sd{1,3}', phrase))
print("{3} gives 1, 2 or 3 occurrence.")
print(re.findall('s[sd]+', phrase))
print("[sd]+ gives any number of s or d or both occurrence.")

phrase = "This is awesome! It has a punctuation mark. How do I remove it? 99239 08880"

pattern = '[^!.?]+'
print(re.findall(pattern, phrase))
print("^ splits by the character in front of it.")
print("+ keeps all letter characters as single string")

pattern = '[a-z]+'
print(re.findall(pattern, phrase))
print("a-z gives back words without spaces and punctuations removing uppercase")

pattern = '[A-Z]+'
print(re.findall(pattern, phrase))
print("A-Z gives back words without spaces and punctuations removing lowercase")

pattern = r'\d+'
print(re.findall(pattern, phrase))
print("r'\d+' returns numbers")

pattern = r'\d'
print(re.findall(pattern, phrase))
print("r'\d' returns digits")

pattern = r'\D+'
print(re.findall(pattern, phrase))
print("r'\D+' returns non-numbers")

pattern = r'\s+'
print(re.findall(pattern, phrase))
print("r'\s+' returns spaces")

pattern = r'\S+'
print(re.findall(pattern, phrase))
print("r'\S+' returns non-spaces")

pattern = r'\w+'
print(re.findall(pattern, phrase))
print("r'\w+' returns alpha-numeric")

pattern = r'\W+'
print(re.findall(pattern, phrase))
print("r'\w+' returns non-alpha-numeric")