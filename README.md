# Quoridor

## Description

Quoridor est un jeu de société classique où les joueurs doivent atteindre le côté opposé du plateau tout en plaçant des murs pour bloquer leurs adversaires. Ce projet implémente une API pour gérer les parties de Quoridor, ainsi qu'une interface en ligne de commande pour interagir avec le jeu.

## Installation

1. Clonez le dépôt :

   ```bash
   git clone https://votre-repo-url.git
   cd quoridor
   ```

2. Installez les dépendances nécessaires :
   ```bash
   pip install requests
   ```

## Utilisation

### Lancer le jeu

Pour démarrer le jeu, exécutez le fichier `main.py` avec votre IDUL et, si nécessaire, l'option pour lister les parties existantes :

```bash
python main.py <IDUL> [-p]
```

- `<IDUL>` : Votre identifiant d'utilisateur.
- `-p` : Option pour lister les parties existantes.

### Fonctions principales

- `lister_parties(idul, secret)`: Récupère la liste des parties en cours.
- `debuter_partie(idul, secret)`: Crée une nouvelle partie et retourne son état.
- `recuperer_partie(id_partie, idul, secret)`: Récupère l'état d'une partie spécifique.
- `jouer_coup(id_partie, type_coup, position, idul, secret)`: Exécute un coup et retourne le nouvel état du jeu.

### Tests

Des tests unitaires sont fournis dans le fichier `tests.py`. Pour exécuter les tests, utilisez la commande suivante :

```bash
python tests.py
```

## Contribuer

Les contributions sont les bienvenues ! Veuillez soumettre une demande de tirage (pull request) pour toute amélioration ou correction.

## Auteurs

- [Votre Nom](https://votre-site-web.com)

## License

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.
