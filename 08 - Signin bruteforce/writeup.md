### 8 - SIGNIN BRUTEFORCE 

FLAG: b3a6e43ddf8b4bbb4125e5e7d23040433827759d4de1c04ea63907479a80a6b2  
URL:  http://10.13.0.11/?page=signin

En tentent de se connecter avec des identifiants et mots de passe au pif, on est redirige vers une page.
En examinant l'element, sous firefox, dans l'onglet reseau, on peut voir la requete effectuee en clair pour tenter de se connecter, soit:

GET "?page=signin&username=admin&password=lol&Login=Login#"

A partir de la, on peut creer un script qui va automatiser nos requetes pour tester une liste de mots de passe et d'identifiants relativement commun pur pouvoir se connecter.

Apres avoir lance le script, il ne nous reste plus qu'a lire notre fichier d'identifiants/mots de passe valides 
