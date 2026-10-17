def greet(name: str, greeting: str = "Hallo", ending: str = ""):
    return greeting, name, ending

a, b , c= greet("Jonas","Willkommen","!")
print(a,b,c)