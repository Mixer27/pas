print("Podaj nazwę pliku graficznego: ")
path = input()


fin = open(path , "rb")
buff = fin.read()
fin.close()

fout = open("lab1zad1.png", "wb")
fout.write(buff)
fout.close()