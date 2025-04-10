
# 🍕 PizzeriaApp

Une application de gestion des produits d'une pizzeria avec une interface graphique intuitive, développée en Python.  
Les données sont stockées dans une base de données MySQL locale via MAMP.

---

## 🖥️ Fonctionnalités

- Interface graphique moderne avec `customtkinter`
- Affichage de la liste des pizzas (id, nom, prix)
- Ajout de nouvelles pizzas
- Suppression de pizzas par ID
- Connexion à une base de données MySQL locale

---

## 📦 Prérequis

- Python 3.x
- MAMP installé et configuré
- Base de données MySQL contenant une table `pizzas`

### Installation des dépendances

```bash
pip install customtkinter mysql-connector-python
```

---

## 🛠️ Configuration de la base de données

### 1. Créer la base de données

Accède à **phpMyAdmin** via MAMP et exécute :

```sql
CREATE DATABASE pizzeria;
```

### 2. Créer la table `pizzas`

```sql
USE pizzeria;

CREATE TABLE pizzas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    prix DECIMAL(5,2) NOT NULL
);
```

---

## 🚀 Lancement de l'application

```bash
python app.py
```

L'application s'ouvrira avec une interface graphique.

---

## 📁 Structure du projet

```
pizzeria-app/
│
├── app.py       # Interface graphique et logique principale
├── api.py       # Accès à la base de données MySQL (CRUD)
└── README.md    # Documentation du projet
```

---

## ⚙️ Configuration de connexion MySQL

Dans `api.py`, vérifiez que les infos de connexion sont correctes :

```python
config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'unix_socket': '/Applications/MAMP/tmp/mysql/mysql.sock',
    'database': 'pizzeria',
}
```

---

## 📌 À venir (suggestions)

- Modification de pizzas existantes
- Filtrage / recherche dans la liste
- Ajout d’images ou descriptions
- Export CSV ou PDF du menu

---

## 👨‍💻 Auteur

Projet développé par Antonin.
