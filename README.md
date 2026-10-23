# Gumball TP

Petit projet Python qui simule des personnages et des situations chaotiques inspirées de l'univers de Gumball.

## Description

Ce projet permet de créer des personnages, leur attribuer une énergie et une humeur, puis de leur faire réagir face à différentes situations comme :

- incendie
- inondation
- bêtise de Gumball

Le but est de gérer les effets des situations sur le personnage, notamment le coût énergétique et le niveau de réaction.

## Fonctionnalités actuelles

- Création de personnages avec un nom, une énergie et une humeur.
- Vérification et limitation de l'énergie.
- Détection de l'état d'épuisement.
- Création de situations avec gravité et type de danger.
- Calcul du chaos associé à une situation.
- Calcul du coût en énergie et de la réaction du personnage.

## Structure du projet

```text
.
├── main.py
├── personnages.py
├── situations.py
├── simulation.py
├── test_tp.py
├── README.md
└── requirements.txt   (à ajouter si nécessaire)
```

## Lancer le projet

Depuis la racine du projet, exécutez :

```bash
python3 main.py
```

## Préparer l'environnement

Choisissez un environnement Python de votre préférence :

- venv
- Conda / Anaconda
- pyenv + pyenv-virtualenv

### Exemple avec venv

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Exemple avec Conda

```bash
conda create -n gumballtp python=3.11
conda activate gumballtp
```

### Exemple avec pyenv

```bash
pyenv install 3.11.9
pyenv local 3.11.9
python -m venv .venv
source .venv/bin/activate
```

## Installer pytest

Une fois l'environnement activé, installez les dépendances de test :

```bash
pip install pytest
```

Vous pouvez aussi sécuriser la version dans un fichier `requirements.txt` plus tard :

```bash
pip freeze > requirements.txt
```

## Exécuter les tests

```bash
pytest
```

Nous utiliserons `pytest` pour valider le bon fonctionnement des classes et de la logique du projet au fur et à mesure de son évolution.

## État du projet

Le projet est en cours de développement et sera complété progressivement


