import inflect
p=inflect.engine()
users = []
while True:
    try:
        user=input("Enter the names: ")


    except EOFError:

        break
    users.append(user)
    output=p.join(users)
    print(f"Adieu, Adieu to {output}" )


