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

if sys.argv[1] == "tarixide":
    print("Tarix:", today)
elif sys.argv[1] == "ilide":
    print("Il:", today.year)
elif sys.argv[1] == "ayide":
    print("Ay:", ayy.strftime("%B"))
elif sys.argv[1] == "gunude":
    print("Gun:", ayy.strftime("%A"))
elif sys.argv[1] == "saatide":
    print("Saat:", time)

# - - - - - - - - - - - - - - - - 

# qovluq funksyalari basladi

cwd = os.getcwd()
if sys.argv[1] == "yerigoster":
    print("Yeriniz:", cwd)



if sys.argv[1] == "qovluqyarat":
    directory = input("Qovluq adını qeyd et: ") 
    parent_dir = "/Users/hcyevelnur/Desktop/py/botpy/"
    path = os.path.join(parent_dir, directory) 
    os.mkdir(path)
    print(directory + ": adlı qovluqunuz yaradıldı.")
elif sys.argv[1] == "qovluqsil":
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

