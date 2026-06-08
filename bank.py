user1=input("What are you going to say to me- ").lower().split()
if user1.startswith("h"):
    print("$20")
elif user1==("Hello"):
    print("$0")
else:
    print("$100")
