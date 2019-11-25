###1 - FAILLE SURVEY

FLAG: 03a944b434d5baff05f46c4bede5792551a2595574bcafc9a6e25f67c382ccaa
URL:  http://10.13.0.127/index.php?page=survey#

En inspectant les elements de la page, on peut modifier les valeurs des notes a rentrer en modifiant le HTML du retour des valeur du champ.
Un select va s'effectUer a partir de la valeur modifiee dans le champ. On peut donc entrer 400000 comme valeur directement dans le tableau,
alors que le resultat attendu est compris entre 1 et 10.
