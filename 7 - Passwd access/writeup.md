### 7 - PASSWD ACCESS

FLAG: b12c4b2cb8094750ae121a676269aa9e2872d07c06e429d25a63196ec1c8c1d0
URL:  http://10.13.0.11

Pour ce flag, on peut se rendre compte que l'url de notre page permet de entrer n'importe quel parametre en utilisant le format d'url suivant:

"http://10.13.0.11?page=URL"

En effet, en utilisant une adresse non valide, le site nous envoie juste une alerte et nous redirige vers la page d'accueil.
A partir de la, on peut tenter de naviguer dans la machine hebergeant ce site pour recuperer des informations,
notablement le fichier contenant le mot de passe de la machine.

Il nous suffit alors d'utiliser l'url suivante pour acceder a ce fichier.

"http://10.13.0.11/?page=/../../../../../../../../../../../../etc/passwd"
