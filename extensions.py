user1=input("File name- ").strip().lower()
extension=input("Enter the extension-").strip().lower()
if extension==".jpg" or extension==".jpeg" or extension==".png":
    print("image/jpeg")
elif extension==".gif":
    print("image/gif")
elif extension==".pdf":
    print("image/pdf")
elif extension==".txt":
    print("image/txt")
else:
    print("image/zip")
