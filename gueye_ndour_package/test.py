from Gueye_Ndour.bisextiles import annee_bissextile
from Gueye_Ndour.multiplication import *

print("TEST DE GUEYE_NDOUR")
print("Veuillez choisir un nombre dans la liste ci-dessous")
print("1 – TABLE DE MULTIPLICATION")
print("2 – ANNEE BISSEXTILE")
print("0 – Quitter")
choix = int(input("Votre choix "))
while(choix<0 or choix>2):
    print("Veuillez saisir un nombre valide : 0, 1 ou 2 ")
    choix = int(input("Votre choix : "))

if(choix==0):
    print("Au revoir")
else:
    if(choix==1):
        base = int(input("Saisissez une base (nombre entier positif) : "))
        table(base);
    elif(choix==2):
        message="L'année n'est pas bissextile";
        annee = int(input("Saisissez une année : "))
        if(annee_bissextile(annee)):
            message=" L'année est bissextile";
        print(f"{annee_bissextile(annee)} : {message}");
