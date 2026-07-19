import inflect
p=inflect.engine()
users = []
while True:
    try:
        user=input("Name: ")
        users.append(user)

    except EOFError:

     output=p.join(users)
     print()
     print(f"Adieu, adieu, to {output}" )


     break



