#!/bin/bash

# Récupération des informations sur les interfaces en bridge
interfaces=$(brctl show | tail -n +2)

# Création de la page web
echo "<html>"
echo "<head>"
echo "<title>Interfaces en bridge</title>"
echo "<style>"
echo "table, th, td {"
echo "border: 1px solid black;"
echo "border-collapse: collapse;"
echo "}"
echo "th, td {"
echo "padding: 5px;"
echo "}"
echo "</style>"
echo "</head>"
echo "<body>"
echo "<h1>Interfaces en bridge</h1>"
echo "<table>"
echo "<tr>"
echo "<th>Bridge</th>"
echo "<th>Interface</th>"
echo "</tr>"

# Remplissage de la table avec les informations sur les interfaces en bridge
while read -r line; do
  bridge=$(echo $line | awk '{print $1}')
  interface=$(echo $line | awk '{print $4}')
  echo "<tr>"
  echo "<td>$bridge</td>"
  echo "<td>$interface</td>"
  echo "</tr>"
done <<< "$interfaces"

echo "</table>"
echo "</body>"
echo "</html>"

