# file=open('new.txt','r')
# content=file.read()
# print(content)

# print(file.readline())
# print(file.readlines())

# file.write("new content")
# file.close()

# import os 

# if os.path.exists("new.txt"):
#     with open('new.txt','r') as file:
#         content=file.read()
#         print(content)
# else:
#     print("file does not exist  ")

# import os
# try:
#     with open('new.txt','r') as file:
#         data=file.read()
#     with open('new1.txt','w') as file:
#         file.write()
#     print("file copied successfully")

# except FileNotFoundError:
#     print('input or output file operation')
# except IOError as e:
#     print("IO exception",e)
# except Exception as e:
#     print("an unexcepted error")

# f=open('example3.txt','x')
# import os
# os.remove('example3.txt')
