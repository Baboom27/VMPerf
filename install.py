import os

# Définir les noms des fichiers à envoyer
files = ['bridge.service', 'netem_static.service', 'netem_varia.service']

# Définir le répertoire de destination
destination_folder = '/home/user/Documents/'

# Boucle pour envoyer les fichiers dans le répertoire de destination
for file in files:
    os.rename(file, destination_folder + file)

# Exécuter les commandes pour installer pip et flask
os.system('sudo apt install pip')
os.system('sudo pip install flask')

