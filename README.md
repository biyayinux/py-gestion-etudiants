# py-gestion-etudiants 🐍🎓

**py-gestion-etudiants** est une application Python pour gérer les étudiants 👨‍🎓👩‍🎓, les cours 📚, les notes 📝 et les moyennes 📊 via un menu interactif 🔁💻.  
Elle propose également la recherche 🔍, les statistiques 📈, le classement 🏆 et les décisions académiques ✅.

## Fonctionnalités ✨🎓

- 📝 **Enregistrer** des étudiants avec leurs informations personnelles  
- 📚 **Créer et gérer** la liste des cours  
- ✏️ **Saisir et modifier** les notes d’un étudiant  
- 📊 **Calculer** les moyennes et décisions  
- 👀 **Afficher** tous les étudiants de manière lisible  
- 🔍 **Rechercher** un étudiant par matricule  
- 📈 **Statistiques** de la promotion  
- 🏆 **Classement** des étudiants (top et derniers)

## Prérequis ⚙️🐍

- 🐍 Python 3.13 ou supérieur  
- 📦 Aucun module externe nécessaire (bibliothèques standard)

## Installation 🚀🐍

Pour éviter les **conflits de dépendances**, nous allons créer un **environnement virtuel**.  
Il permet d’**isoler les paquets** nécessaires à notre projet, sans toucher au système global. 💡

> ⚠️ **Note :**  
> Réservé aux utilisateurs sous **Debian ou dérivés** (Ubuntu, Linux Mint, etc.).

```bash
  # Crée le venv sans pip
  python3.13 -m venv --without-pip venv

  # Active le venv
  source venv/bin/activate

  # Installer pip
  curl -sS https://bootstrap.pypa.io/get-pip.py -o get-pip.py
  python3.13 get-pip.py

  # Vérifie
  python --version
  pip --version
```

## Exécuter localement 🚀💻

Cloner ou télécharger le projet

```bash
  git clone https://github.com/biyayinux/py-gestion-etudiants.git
```

📂 Accédez au répertoire du projet

```bash
  cd py-gestion-etudiants
```

▶️ Démarrer le projet

```bash
  python main.py
```