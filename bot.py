# Write a bot:

# 	bot functions:
		
# 		tarixi de => Indiki tariff qaytarmalidi
# 		ili de => Indiki ili qaytarmalidi
# 		Ayi de => Indiki Ayi qaytarmalidi
# 		saati de => Indiki saati qaytarmalidi
		
# 		"Flan" adli folder yarat => olduğumuz qovluqda verilen adla Folder yaratsın
# 		"Flan" adli folderi sil => olduğumuz qovluqda verilen adla Folderi silsin

# 		Hesabla (misal) => cavab


from datetime import datetime, date
import os
import sys
 
#  tarixlerin funksyalari basladi

now = datetime.now()
today = date.today()
time = now.strftime("%H:%M:%S")
ayy = datetime.now()
gun = datetime.now()

# tarixlerin funksyalari bitdi

if (sys.argv[1] == "tarixi" and sys.argv[2] == "de"):
    print("Tarix:", today)
elif (sys.argv[1] == "ili" and sys.argv[2] == "de"):
    print("Il:", today.year)
elif (sys.argv[1] == "ayi" and sys.argv[2] == "de"):
    print("Ay:", ayy.strftime("%B"))
elif (sys.argv[1] == "gunu" and sys.argv[2] == "de"):
    print("Gun:", ayy.strftime("%A"))
elif (sys.argv[1] == "saati" and sys.argv[2] == "de"):
    print("Saat:", time)

# - - - - - - - - - - - - - - - - 

# qovluq funksyalari basladi

cwd = os.getcwd()
if (sys.argv[1] == "yeri" and sys.argv[2] == "goster"):
    print("Yeriniz:", cwd)



if (sys.argv[1] == "qovluq" and sys.argv[2] == "yarat"):
    directory = input("Qovluq adını qeyd et: ") 
    parent_dir = "/Users/hcyevelnur/Desktop/py/botpy/"
    path = os.path.join(parent_dir, directory) 
    os.mkdir(path)
    print(directory + ": adlı qovluqunuz yaradıldı.")
elif (sys.argv[1] == "qovluqu" and sys.argv[2] == "sil"):
    directory = input("Qovluq adını qeyd et: ") 
    parent_dir = "/Users/hcyevelnur/Desktop/py/botpy/"
    path = os.path.join(parent_dir, directory) 
    os.rmdir(path)
    print(directory + ": adlı qovluqunuz silindi.")

# qovluq funksyalari bitdi

# - - - - - - - - - - - - - - - - 

if sys.argv[1] =="+":
    X = int(input('Ilk Reqem: '))
    Y = int(input('Ikinci Reqem: '))
    print(X, "+", Y, "=", X + Y)
elif sys.argv[1] == "-":
    X = int(input('Ilk Reqem: '))
    Y = int(input('Ikinci Reqem: '))
    print(X, "-", Y, "=", X - Y)
elif sys.argv[1] == "*":
    X = int(input('Ilk Reqem: '))
    Y = int(input('Ikinci Reqem: '))
    print(X, "*", Y, "=", X * Y)
elif sys.argv[1] == "/":
    X = int(input('Ilk Reqem: '))
    Y = int(input('Ikinci Reqem: '))
    print(X, "/", Y,"=", X / Y)

