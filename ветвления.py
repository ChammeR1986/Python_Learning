orig_pass = "chammer"
password = input("please enter password: ")

if (password != orig_pass):
    print("try again")
    password = input("please enter password: ")
if (password != orig_pass):
    print("try again")
    password = input("please enter password: ")
if (password != orig_pass):
    print("you are blocked")

else:
    print("well done")
