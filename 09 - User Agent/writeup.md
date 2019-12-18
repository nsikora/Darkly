### 9 - USER AGENT

FLAG: f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188
URL:  http://10.13.0.127/?page=e43ad1fdc54babe674da7c7b8f0127bde61de3fbe01def7d00f151c2fcca6d1c

En inspectant les elements de la page, on peut trouver dissemine un peu partout des informations pour trouver un flag, notamment:

- Disposer du navigateur ft_bornTosec
- Venir du site https://www.nsa.gov/

Pour se connecter de cette manière, on va utiliser curl pour effectuer une requête sur cette page en utilisqnt les paramètres cités précédemment.

En utilisant la commande suivante, on trouve alors le flag.

curl -A "ft_bornToSec" --referer "https://www.nsa.gov/" http://10.12.1.129/\?page=e43ad1fdc54babe674da7c7b8f0127bde61de3fbe01def7d00f151c2fcca6d1c
