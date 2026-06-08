user1=str(input("What are you going to say to me-")).lower().strip()
if user1.startswith("hello"):
    print("$0")
elif user1.startswith("h"):
    print("$20")
else:
    print("$100")
