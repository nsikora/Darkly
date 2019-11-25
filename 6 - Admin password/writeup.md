###6 - ADMIN PASSWORD

FLAG: d19b4823e0d5600ceed56d5e896ef328d7a2b9e7ac7e80f4fcdb9b10bcb3e7ff
URL:  http://10.13.0.11

Pour ce flag, on va devoir utiliser dirb, un scanner d'architecture de site web.
Pour scanner notre site, il suffit de lancer dirb avec une liste de mots cles a chercher. La commande se lance de la facon suivante:

./dirb http://10.13.0.11 wordlists/small.txt

On trouve alorss deux resultats qui nosu interessent:

==> DIRECTORY: http://10.13.0.11/whatever/
---- Entering directory: http://10.13.0.11/admin/ ----

En allant dans notre premiere url, on a acces a un fichiier de mot de passe, avec un nom d'utilisateur "root"
et une chaine de caractere hashee en md5 "8621ffdbc5698829397d97767ac13db3".
Apres avoir decrypte la chaine md5, on sait que le mot de passe est "dragon"

On se connecte alors a notre seconde URL pour se connecter en tant qu'admin avec cet identifiant mot de passe.
