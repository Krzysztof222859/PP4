x=input("Podaj tekst do dopisania do pliku")

def addingText(text):

    with open ("file1.txt", "a") as file:
        file.write("\n" + text)

addingText(x)