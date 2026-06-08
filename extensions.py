extension=input("file name-").strip().lower()
if extension.endswith(".jpg") or extension.endswith(".jpeg") or extension.endswith(".png"):
    print("image/jpeg")
elif extension.endswith(".gif"):
    print("image/gif")
elif extension.endswith(".pdf"):
    print("application/pdf")
elif extension.endswith(".txt"):
    print("text/text")
elif extension.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")

