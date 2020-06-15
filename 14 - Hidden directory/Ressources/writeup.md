### 14 - HIDDEN DIRECTORY

Flag: 99dde1d35d1fdd283924d84e6d9f1d820
Url:  http://10.12.1.107/.hidden/

Bien que l'on ai scanne les differents noms de dossiers communement utilises, 
j'ai remarque que le scan ne semblait pas se faire autour par rapport aux fichiers caches.

On va donc regarder si des fichiers caches supplementaires existent avec les commandes suivante:

"sed -e 's/^/./' wordlists/small.txt > wordlists/small_hidden.txt"
Qui va nous convertir notre check de fichiers en check de fichiers caches, 
en ajoutant un '.' comme prefixe au debut de chaque ligne, donc de chaque mot cle.

"./dirb http://10.11.200.221/ wordlists/small_hidden.txt"
Qui va verifier l'existence de ces dossiers caches.

On tombe alors sur une multitudes de dossiers et de sous dossiers.
Il va falloir utiliser un crawler pour recuperer le flag car une inspection manuelle nous prendrait trop de temps.

Nous l'uiliserons avec la commande suivante, afin de stocker son resultat:
"python3 crawler.py > result.txt"

Une fois notre script lance, on peut voir qu'une multitude de messages repetitifs 
sont presents dans notre fichier result.txt.Pour les ignorer, il suffit d'utiliser la commande:

"cat result.txt | grep -v "Demande" | grep -v "Non" | grep -v "Tu" | grep -v "Retorune" | grep -v "Toujours""
