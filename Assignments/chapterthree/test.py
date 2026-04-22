# the code wont pass the turing test
# it ignores user input
# no reasoning awareness
# responses are fixed


input("What is your problem? ")

answer = input("Have you had this problem before (yes or no)? ")

if answer.lower() == "yes":
    print("Well, you have it again.")
else:
    print("Well, you have it now.")
