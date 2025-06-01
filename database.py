import mysql.connector
from dotenv import load_dotenv
import os
from tabulate import tabulate

# Charger les variables d'environnement
load_dotenv()

def connexion_mysql():
    """Établit une connexion à MySQL et retourne l'objet connexion"""
    try:
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            port=int(os.getenv("DB_PORT", 3306))
        )
        return conn
    except mysql.connector.Error as err:
        print(f"❌ Erreur de connexion : {err}")
        return None

def lire_tickets():
    """Lire tous les tickets de la base de données"""
    conn = connexion_mysql()
    if conn is None:
        return
    
    cursor = conn.cursor()
    query = "SELECT id, titre, priorite, statut, date_creation FROM tickets"
    cursor.execute(query)
    tickets = cursor.fetchall()
    cursor.close()
    conn.close()

    if tickets:
        headers = ["ID", "Titre", "Priorité", "Statut", "Date de Création"]
        print(tabulate(tickets, headers, tablefmt="grid"))
    else:
        print("🚫 Aucun ticket trouvé.")

def ajouter_ticket():
    """Ajoute un ticket dans la base de données"""
    conn = connexion_mysql()
    if conn is None:
        return

    cursor = conn.cursor()

    titre = input("Titre du ticket : ")
    description = input("Description : ")
    priorite = input("Priorité (faible/moyenne/haute) : ")

    if priorite not in ["faible", "moyenne", "haute"]:
        print("❌ Erreur : Priorité invalide.")
        return

    query = "INSERT INTO tickets (titre, description, priorite, statut, date_creation) VALUES (%s, %s, %s, %s, NOW())"
    cursor.execute(query, (titre, description, priorite, "ouvert"))
    conn.commit()

    print("✅ Ticket créé avec succès !")

    cursor.close()
    conn.close()

def modifier_ticket():
    """Modifie le statut ou la priorité d'un ticket"""
    conn = connexion_mysql()
    if conn is None:
        return

    cursor = conn.cursor()

    ticket_id = input("ID du ticket à modifier : ")
    champ = input("Modifier (statut/priorite) : ").lower()

    if champ not in ["statut", "priorite"]:
        print("❌ Erreur : Champ invalide.")
        return

    nouvelle_valeur = input(f"Nouveau {champ} : ")

    query = f"UPDATE tickets SET {champ} = %s WHERE id = %s"
    cursor.execute(query, (nouvelle_valeur, ticket_id))
    conn.commit()

    print(f"✅ Ticket {ticket_id} mis à jour avec {champ} : {nouvelle_valeur}")

    cursor.close()
    conn.close()

def supprimer_ticket():
    """Supprime un ticket par son ID"""
    conn = connexion_mysql()
    if conn is None:
        return

    cursor = conn.cursor()

    ticket_id = input("ID du ticket à supprimer : ")
    query = "DELETE FROM tickets WHERE id = %s"
    cursor.execute(query, (ticket_id,))
    conn.commit()

    print(f"🗑️ Ticket {ticket_id} supprimé définitivement.")

    cursor.close()
    conn.close()
