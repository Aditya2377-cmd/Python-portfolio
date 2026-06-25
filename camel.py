# camelcase=input("What is your input- ").lower()
   # if camel=camelcase.isupper():
    #case=camelcase.replace(" ","_")
    #print(f"snakecase-{case}")
    #def main(camelcase):
       # if snake=camelcase.split("_"):
        #return str(snake)
        # else return snake
camel_case = input("camelCase: ")
snake_case = ""
for char in camel_case:
    if char.isupper():
        snake_case += "_" + char.lower()
    else:
        snake_case += char
print("snake_case:", snake_case)



