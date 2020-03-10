Flag: 46910d9ce35b385885a9f7e2b336249d622f29b267a1771fbacf52133beddba8
Url:  http://10.12.1.107/?page=upload#

On sait que l'on peut uploader une image sur cette url, donc de la donnee. On va d'abord determiner quel format est supporte.
Apres quelques tests, on se rend compte que le format jpeg est potentiellement utilisable.

Pour injecter du code en PHP, on peut utiliser un fichier a double extension (exploit.jpeg.php) poru executer du code, soit utiliser curl.
Il y a une protection sur les extensions, donc il nous reste la tentative avec curl.

On va creer un fichier exploit.php qui va contenir un grep de flag, que l'on va executer avec la commande curl -F qui va tout simplement
envoyer un formulaire contenant les valeurs voulues, vers notre url d'upload, et faire passer notre fichier php pour une image jpeg
en modifiant son header pour obtenir uen page de reponse contenant notre flag. 

Traduit en code, cela donne:

"touch exploit.php && curl -F "uploaded=@exploit.php;type=image/jpeg" -F "Upload=ok" "http://10.12.1.107/?page=upload" | grepp flag"
