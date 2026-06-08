user1=str(input("What are you going to say to me-")).lower().split()
if user1.startswith("h"):
    print("$20")
elif user1==("hello"):
    print("$0")
else:
    print("$100")
