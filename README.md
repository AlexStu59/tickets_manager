# 🎟️ Gestionnaire de Tickets - Python & MySQL  

Un **système de gestion de tickets** codé en Python avec MySQL, permettant l'ajout, la lecture, la modification et la suppression de tickets via une interface CLI.  

## 📌 Fonctionnalités  
✅ **Créer un ticket** avec un titre, une description et une priorité.  
✅ **Lire tous les tickets** et les afficher sous forme de tableau.  
✅ **Modifier un ticket** (statut ou priorité).  
✅ **Supprimer un ticket** définitivement par son ID.  
✅ **Menu interactif** pour naviguer entre les options facilement.  

## 🛠️ Installation  

### 1️⃣ **Cloner le dépôt**  
```bash
git clone https://github.com/AlexStu59/tickets_manager.git
cd tickets_manager
```

### 2️⃣ **Créer un environnement virtuel** _(recommandé)_  
```bash
python -m venv monenv
source monenv/bin/activate  # Sur Mac/Linux
monenv\Scripts\activate  # Sur Windows
```

### 3️⃣ **Installer les dépendances**  
```bash
pip install -r requirements.txt
```

### 4️⃣ **Configurer la base de données**  
1️⃣ Assure-toi que **MySQL est installé et accessible**.  
2️⃣ Crée la base de données et la table `tickets` :  
```sql
CREATE DATABASE gestion_tickets;
USE gestion_tickets;

CREATE TABLE tickets (
    id INT PRIMARY KEY AUTO_INCREMENT,
    titre VARCHAR(255) NOT NULL,
    description TEXT,
    priorite ENUM('faible', 'moyenne', 'haute') NOT NULL,
    statut ENUM('ouvert', 'en cours', 'fermé') DEFAULT 'ouvert',
    date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
3️⃣ **Créer un fichier `.env`** pour stocker les infos de connexion :  
```
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=ton_mot_de_passe
DB_NAME=gestion_tickets
DB_PORT=3306
```

## 🚀 Lancement du programme  

Exécute simplement :  
```bash
python main.py
```
Un **menu interactif** te permettra de gérer les tickets directement.  

## 📜 Exemple de fonctionnement  

```
🎟️ Gestion des Tickets
1️⃣ Ajouter un ticket
2️⃣ Voir tous les tickets
3️⃣ Modifier un ticket
4️⃣ Supprimer un ticket
5️⃣ Quitter
➡️ Choisissez une option : _
```

## 🤝 Contribution  
Si tu veux améliorer ce projet :
1. **Fork** le dépôt.  
2. **Crée une branche** (`git checkout -b feature-nouvelle-fonction`).  
3. **Fais tes modifications** et **commit** (`git commit -m "Ajout d'une nouvelle fonctionnalité"`).  
4. **Push** et **ouvre une Pull Request**.  

## 📄 Licence  
Ce projet est sous licence **MIT**, tu peux le modifier et le réutiliser librement.
