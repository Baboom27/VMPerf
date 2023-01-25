#!/usr/bin/env python3

import os
import fileinput
import time

while True :


    Commande=""
    with open("../../../Documents/netplan.txt", "r") as Netplan :
        x=list()
        for line in Netplan:
            data=line.split()
            if len(data)>0:
                if data[0]=="interfaces:":
                    x.append(data[1])

    d=[]

    for i in range(len(x)):
        d.append([x[i][1:-1]])

    l=[]

    for i in range(len(d)):
        l.append(d[i][0].split(","))


    for interface in l:
        Commande+='<li> ' + interface[0] + ' - ' + interface[1] + ' </li> '

    # Ouvrir le fichier en mode lecture
    with open("../GUI_static/templates/main.html", "r") as f:
        # Lire toutes les lignes du fichier
        lines = f.readlines()

    # Modifier la 15ème ligne avec la variable Commande
    lines[14] = Commande + "\n"

    # Ouvrir le fichier en mode écriture
    with open("../GUI_static/templates/main.html", "w") as f:
        # Écrire toutes les lignes modifiées dans le fichier
        f.writelines(lines)

    time.sleep(30)