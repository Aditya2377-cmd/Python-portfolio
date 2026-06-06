def convert(tto):
    tto=tto.replace(":)" , "🙂")
    tto=tto.replace(":(" , "🙁")
    return tto
def main():
    user=input("What is your input- ")
    process= convert(user)
    print(process)


main()


