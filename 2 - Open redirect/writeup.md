### 2 - OPEN REDIRECT

FLAG: b9e775a0291fed784a2d9680fcfad7edd6b8cdf87648da647aaf4bba288bcab3
URL:  http://10.13.0.127/index.php

Pour obtenir ce flag, on a juste a inspecter l'element sur les redirections des liens twitter/facebook/instagram
On peut changer les redirections listees sur les icones du style "index.php?page=redirect&site=instagram"
vers une redirection du style "index.php?page=redirect&site=monsitepirate".

Cette attaque nous permet eventuellement de faire du phising en envoyant des mails contenant l'url de ce site pouvant rediriger
des utilisateurs vers une copie de ce site demandant les identifiants et mot de passe du visiteur sans attirer l'attention.
