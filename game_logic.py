# This imports all the classes we created from a file called 'classes.py'
from classes import *

# ======================= CREATE CHARACTER FUNCTION =========================
def create_character():
    print("\nWelcome to our Gaming program")
    print("******************************")
    print("******************************\n")
    print("Choose Your Character Class")
    print("1. Warrior")
    print("2. Mage")
    print("3. Rogue")
    print("4. Kael")
    print("5. Ninja")

    class_choice= input("\nEnter the Number of Your Class Choice: ")
    name=input("\nEnter Your Character's Name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Rogue(name)
    elif class_choice =='4':
        return Kael(name)
    elif class_choice=='5':
        return Ninja(name)
    else:
        print("Invalid Choice. Defaulting to Warrior.")
        return Warrior(name)
# ========================== BATTLE FUNCTION =============================
def battle(player,wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n**** Your Turn ****")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")

        choice=input("\nChoose an action: ")


        if choice == '1':
            player.attack(wizard)
        elif choice =='2':
            player.special_ability(wizard)
        elif choice == '3':
            player.heal()
        elif choice == '4':
            player.display_stats()
        else:
            print("Invalid choice. Try Again..")
         # Evil Wizard's turn to attack and regenerate
        if wizard.health>0:
            wizard.regenerate()
            wizard.attack(player)
        
        if player.health <= 0:
            print(f"{player.name} has been defeated!!")
    
    if wizard.health <= 0:
        print(f"The Wizard {wizard.name} has been defeated by {player.name}!!!!")

    print("!!!****Game over****!!")


def main():
    # Character creation phase    
    player= create_character()
     # Evil Wizard is created
    wizard= EvilWizard("The Dark Wizard")
     # Start the battle
    battle(player,wizard)

if __name__=="__main__":
    main()
        

