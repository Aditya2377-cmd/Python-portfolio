# camelcase=input("What is your input- ").lower()
   # if camel=camelcase.isupper():
    #case=camelcase.replace(" ","_")
    #print(f"snakecase-{case}")
    #def main(camelcase):
       # if snake=camelcase.split("_"):
        #return str(snake)
        # else return snake
# 1. Get the camelCase input from the user
camel_case = input("camelCase: ")

# 2. Create an empty string (our snowball) to build the snake_case version
snake_case = ""

# 3. Loop through the input string character by character
for char in camel_case:

    # 4. If the character is uppercase (e.g., 'N' in firstName)
    if char.isupper():
        # Add an underscore and the lowercase version of the letter
        snake_case += "_" + char.lower()

    # 5. If it's already a lowercase letter, just add it as-is
    else:
        snake_case += char

# 6. Print the final snake_case result
print("snake_case:", snake_case)



