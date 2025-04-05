#try,except,else,finally
# try:
#     x=10/0
#     print(x)
# except ZeroDivisionError:
#     print("Division by zero is not possible")
# finally:
#     print("completed execution ")

# try:
#     num=int(input("enter the num:"))
#     result=num/0
# except ZeroDivisionError as e:
#     print("Division by zero is not possible")
# except ValueError as e:
#     print("invalid input",e)
# except Exception as e:
#     print("An Unexcepted")
# else:
#     print("result:",result)
# finally:
#     print("completed execution ")

# def checkage(age):
#     if age<18:
#         raise ValueError("age must be 18")
#     else:
#         print("you are eligible")
# try:
#     checkage(18)
# except ValueError as e:
#     print(e)

# class UserNotFound(Exception):
#     pass
# def checkage(age):
#     if age<18:
#         raise UserNotFound("age must be 18")
#     else:
#         print("you are eligible")
# try:
#     checkage(16)
# except UserNotFound as e:
#     print("error")