user1=input("What are you going to say to me- ").split().lower()

if user1.startwith("hello"):
    print("$0")
elif user1.startwith("h"):
    print("$20")
else:
    print("$100")
