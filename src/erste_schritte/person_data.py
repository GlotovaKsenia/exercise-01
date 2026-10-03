name = input("Name:")
alter = input ("Alter:")
studiengang = input("Studiengang")

print(f"{name} ist {alter} Jahre alt und studiert {studiengang}")
print(name,"ist" , alter, "Jahre alt und studiert", studiengang)

#Syntaxfehler: Klammer nicht schließen; SyntaxError: '(' was never closed
#Laufzeitfehler: während programm ausgeführt wird; NameError: name 'studium' is not defined
#logische Fehler: Satz macht keinen sinn.