import re

# search
# x="The rain in spain"
# y=re.search("^The.*in$",x)
# if y:
#     print("yes the match is correct")
# else:
#     print("not matching with the pattern")

#findall
# x="The rain in spain"
# y=re.findall("ai",x)
# print(y)
# z=re.search("\s",x) #searches no of white spaces
# print(z)
# # z=re.split("\s",x) #splits 
# # print(z)
# a=re.sub("\s","$",x) #replacement 
# print(a)

# to find numbers in text
# pattern=r"\d+"
# text="There are 123 apples"
# match=re.search(pattern,text)
# if match:
#     print("match found",match.group())
# else:
#     print("match not found")

# pattern=r"\d+"
# text="There are 123 apples and 45 oranges"
# match=re.findall(pattern,text)
# print(match)

# pattern=r"(\d+)-(\d+)-(\d+)"
# text="The event is on 2025-10-06"
# match=re.search(pattern,text)
# if match:
#     print("year:",match.group(1))
#     print("month:",match.group(2))
#     print("day:",match.group(3))
    
# pattern=r"(\d+)-(\d+)-(\d+)"
# text="The event is on 2025-10-06"
# match=re.findall(pattern,text)
# print(match)

# email
# email = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
# text = "my email id is mani@123.com"
# match = re.search(email, text)
# if match:
#     print("Email found:", match.group())

