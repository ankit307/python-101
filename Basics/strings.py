# Ask user for their name
name = input("What's Your name? ")

#Say Hello to User
print("Hello, "+name)
print(f"Hello, {name}")

# Removes Whitespaces from str
name = name.strip()
print(f"Hello, {name}")

# Capitalize user's name first char
name = name.capitalize()
print(f"Hello, {name}")

# Capitalize user's name all char
name = name.title()
print(f"Hello, {name}")


