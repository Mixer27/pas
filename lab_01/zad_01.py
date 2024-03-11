print("Podaj nazwę pliku: ")
path = input()


fin = open(path , "r")
buff = fin.read()
fin.close()

fout = open("lab1zad1.txt", "w")
fout.write(buff)
fout.close()