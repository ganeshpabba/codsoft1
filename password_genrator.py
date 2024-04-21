import random

password = (
    "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRESTUVWXYZ1234567890!@#$%^&*)(}{+_:"
)
len_password = int(input("enter the length of the password :"))
l = "".join(random.sample(password, len_password))
print(f"your password is {l}")
