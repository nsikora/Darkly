### 4 - COOKIE ADMINISTRATEUR

FLAG: df2eb4ba34ed059a1e3e89ff4dfc13445f104a1a52295214def1c4fb1693a5c3
URL:  http://10.13.0.127/index.php

En inspectant l'element de la page d'accueil sous firefox, on peut voir dans l'onglet stockage un cookie nomme "i-am-admin",
avec pour valeur "68934a3e9455fa72420237eb05902327", qui une fois dechiffre sur le site "https://md5decrypt.net/" , donne le mot "false".
On sait alors que c'es un booleen.
Pour trouver ce flag, ila  juste fallut remplacer la valeur md5 de false par la valeur md5 de true, soit "b326b5062b2f0e69046810717534cb09".
