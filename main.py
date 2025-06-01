from database import lire_tickets, ajouter_ticket, modifier_ticket, supprimer_ticket

def afficher_menu():
    print("\n🎟️ Gestion des Tickets")
    print("1️⃣ Ajouter un ticket")
    print("2️⃣ Voir tous les tickets")
    print("3️⃣ Modifier un ticket")
    print("4️⃣ Supprimer un ticket")
    print("5️⃣ Quitter")

def main():
    while True:
        afficher_menu()
        choix = input("➡️ Choisissez une option : ")

        if choix == "1":
            ajouter_ticket()
        elif choix == "2":
            lire_tickets()
        elif choix == "3":
            modifier_ticket()
        elif choix == "4":
            supprimer_ticket()
        elif choix == "5":
            print("👋 Au revoir !")
            break
        else:
            print("❌ Option invalide, veuillez réessayer.")

if __name__ == "__main__":
    main()
