import csv
import random

#Charge le fichier passé en commentaire
def fileLoader(path):
    ret = [[],[],[],[]] #Liste qui va représenter tout les étudiants selon leur promo
    with open(path, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in csvreader:
            if(row[2] == "INFO 1"):
                ret[0].append(row[0]+" "+row[1])
            elif(row[2] == "INFO 2"):
                ret[1].append(row[0]+" "+row[1])
            elif(row[2] == "MMI 1"):
                ret[2].append(row[0]+" "+row[1])
            elif(row[2] == "MMI 2"):
                ret[3].append(row[0]+" "+row[1])
        csvfile.close()
    return ret
#Crée les binomes selon les listes passée en paramètres
def binomesMaker(_godfather, _godson):
    binomes = [] #Permet d'enregistrer les binomes déjà fait
    alreadyPick = [] #Permet d'enregistrer les étudiants qui ont déjà été pick

    #Première boucle pour attribuer aux parrains un filleul pour être sur qu'ils ont tous au moins 1 filleul
    for i in range(len(_godfather)):
        godson = random.choice(_godson) #Pick un parrain aléatoire dans la liste des parrains
        _godson.remove(godson)
        binomes.append([_godfather[i], godson])
    alreadyPick.clear() #On clear la liste pour le deuxième passage pour être sur que tout les filleuls ont des parrains
    for i in range(len(_godson)):
        godfather = random.choice(_godfather)
        alreadyPick.append(godfather)
        binomes.append([godfather, _godson[i]])
    return binomes
#ouvre le fichier avec le chemin passé en paramètre pour enregistrer les binomes dans un fichier
def saveBinomes(binomes, path):
    with open (path, 'w') as file:
        for i in binomes:
            for j in i:
                file.write(j[0].upper()+';'+j[1].upper()+'\n')
    
    file.close()
def main():
    #Je charge le fichier csv // model = {"nom", "prénom", "filière"}
    csv = fileLoader("students.csv")

    #Je séparer chaque étudiants pour la suite du programme
    info_1  = csv[0]
    info_2  = csv[1]
    mmi_1   = csv[2]
    mmi_2   = csv[3]

    #Je randomise les listes afin de faire une première couche d'aléatoire
    random.shuffle(info_1)
    random.shuffle(info_2)
    random.shuffle(mmi_1)
    random.shuffle(mmi_2)

    #Je crée les différents binomes et les enregistre dans deux fichiers différents
    binomes_info = [binomesMaker(info_2, info_1)]
    binomes_mmi = [binomesMaker(mmi_2, mmi_1)]
    saveBinomes(binomes_info,"binomes_info.csv")
    saveBinomes(binomes_mmi,"binomes_mmi.csv")

main()
