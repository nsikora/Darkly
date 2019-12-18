### 11 - SQL INJECTION MEMBERS

Flag: 10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5
Url:  http://192.168.0.19/?page=member

En testant un id de 1, par exemple, on peut voir que l'on interagit directement avec la base de donnee SQL,
que l'on a besoin d'un numero d'id pour lance rune requete, et que systematiquement, deux colonnes nous sont retournées.

Nous allons donc devoir utiliser un UNION pour demander un numéro d'id bidon et surtout pour effectuer une requete nous renvoyant deux résultats.
Nous allons lister dans un premier temps les tables de la base de donnée avec la commande suivante:

0 UNION SELECT table_schema, table_name FROM information_schema.tables

Nous pouvons lire par rapport à ce qui semble être des tables par défaut, les tables suivantes:

"db_default", "users", "guestbook", "list_image", "vote_db"

Comme on regarde dans la page members, la table qui semble la plus proche de ce sujet semble être users.
On va maitenant lister les colonnes et les tables à laquelle elles appartiennent avec la commande suivante:

0 UNION SELECT table_name, column_name FROM information_schema.columns

On a alors une page avec 3 tonnes de données, mais pas de soucis, grace à la commande precedente, il suffit d'effectuer un ctrl + f pour trouver tout les  columns en rapport avec la table users.
On a donc les colonnes suivantes qui nous intéressent:

"user_id", "first_name", "last_name", "town", "country", "planet", "Commentaire", "countersign"

Il nous suffit donc de les observer deux par deux avec la commande:

0 UNION SELECT user_id, firstname FROM users

En arrivant sur la commande suivante:

0 UNION SELECT Commentaire, countersign FROM users

On trouve alors une réponse qui pique notre intérêt:

ID: 0 UNION SELECT Commentaire, countersign FROM users 
First name: Decrypt this password -> then lower all the char. Sh256 on it and it's good !
Surname : 5ff9d0165b4f92b14994e5c685cdce28

Le mot de passe contient 32 caractères, c'est donc très certainement du md5.
Sur le site https://md5decrypt.net/, on trouve que ce hash correspond à "FortyTwo"

On va alors chiffrer ce mot de passe en sha256, en utilisant uniquement des miniscules, comme indiqué sur notre dernière réponse SQL.
Sur le site https://md5decrypt.net/Sha256/, on trouve alors le hash de "fortytwo", étant:

"10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5"

On a donc notre flag.

