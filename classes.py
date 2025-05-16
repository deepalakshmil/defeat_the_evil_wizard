import random

#============== BASE CHARACTER CLASS ============================
class Character:
    def __init__(self,name,health,attack_power):
        self.name=name
        self.health=health
        self.attack_power=attack_power
        self.max_health = health   # Store the original health for maximum limit
        self.high_speed_attack=110
    
    def attack(self,opponent):
        damage=self.attack_power
        opponent.health -=damage
        print(f"\n{self.name} attacks {opponent.name} for {damage} damage!!")      
        print(f"{opponent.name} has {opponent.health} remaining")  
    
    def heal(self):
        self.health += random.randrange(10,70,10)
        if self.health > self.max_health:
            self.health=self.max_health
        print(f"\n{self.name} regenerates successfully!!! The current Health : {self.health}/{self.max_health}")
    
    def display_stats(self):
        print(f"\n{self.name}'s Stats - Health : {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

# ====================== SUBCLASSES ============================        
# Warrior class (inherits from Character)

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=random.randint(10,30))

    def special_ability(self,opponent):
        print("\nSpecial Abilities")
        print("1. Deadly Strike")
        print("2. Vampiric Strike")
        action=input("\nWhich ability do you want to use?: ") 

        if action == "1":
             
             '''
            Ability: Deadly Strike
            Description: The fighter performs a deadly strike which does significant damage to the opponent.
            '''
             damage=self.attack_power * 3
             opponent.health -=damage
             print(f"\n{self.name} strikes {opponent.name} and does {damage} damage!!!")
        elif action == "2":
             '''
            Ability: Vampiric Strike
            Description: The fighter strikes his opponent and heals for the damage done.
            '''
             damage=self.attack_power
             opponent.health -= damage
             self.health += damage
              # Check if our current health exceeds our maximum health
             if self.health > self.max_health:
                self.health = self.max_health
             print(f"{self.name} attacks {opponent.name} and does {damage} damage and heals for the same amount")
             print(f"{self.name} now has current helath {self.health}.")
        else:
            print(f"Invalid selection. Defaulting to Deadly Strike")
            # Default to Choice 1
            damage=self.attack_power * 3
            opponent.health -=damage
            print(f"\n{self.name} strikes {opponent.name} and does {damage} damage!!!")

# ====================== SUBCLASSES ============================        
# EvilWizard class (inherits from Character)

class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=random.randint(10,30))
    
    def regenerate(self):
        self.health += 7
        print(f"\n{self.name} Regenerates 7 Health!!! Now the Current Health: {self.health}")


# ====================== SUBCLASSES ============================        
# Mage class (inherits from Character)

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=random.randint(10,30))
    
    def special_ability(self,opponent):
        print("\nSpecial Abilities")
        print("1. Spellweave Echo")
        print("2. Arcane Mirage")
        action=input("\nWhich ability do you want to use?: ") 

        if action == "1":
            """
            Effect: The last spell she casts automatically triggers a second time after a few seconds at 75% strength. Can affect damage, healing, or status spells.
            """
            damage=self.attack_power *2
            opponent.health -=damage
            self.health += 55
            if self.health > self.max_health:
                self.health = self.max_health
            print(f"{self.name} spells the {opponent.name} and does {damage} damage!!! and the {self.name} increasing health {self.health}")

        elif action == "2":
            """
            Effect: Temporary clones draw enemy attention and deal area magic damage on destruction.
            """
            self.attack_power +=30
            print(f"{self.name} just got a whole lot stronger!! Attack power is now set to {self.attack_power} ")

        else:
             print(f"Invalid selection. Defaulting to Spellweave Echo")
             # Default to Choice 1
             damage=self.attack_power *2
             opponent.health -=damage
             self.health += 55
             if self.health > self.max_health:
                self.health = self.max_health
             print(f"{self.name} spells the {opponent.name} and does {damage} damage!!! and the {self.name} increasing health {self.health}")

# ====================== SUBCLASSES ============================        
# Rogue class (inherits from Character)

class Rogue(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=random.randint(10,30))
        '''
          evadeNextAttack is going to be used as a flag to determine whether the Rogue is going to evade the next attack.
        '''
        self.evadeNextAttack = False
    def special_ability(self,opponent):
        print("\nSpecial Abilities:")
        print("1. Gathering Shadows")
        print("2. Siphoning Strikes")
        print("3. Preemptive Dodge (Evade)")
        action = input("Which ability do you want to use? ")

        if action == "1":
             """
        Ability: Gathering Shadows
        Increases the Rogue's damage by 30, but does not attack.
            """
             self.attack_power +=36
             print(f"\nShadows gather around {self.name} increasing their damage to {self.attack_power}.")
        elif action == "2":
             """
        Ability: Siphoning Strikes
        Strikes the opponent and heals for half of the damage dealt.  
            """
             opponent.health -= self.attack_power
             self.health += self.attack_power // 2    # Floor division rounds to the nearest integer (whole number)
             if self.health > self.max_health:
                self.health == self.max_health
             print(f"\n{self.name} strikes {opponent.name} with vampiric daggers, dealing {self.attack_power} damage and siphoning the wizard's health to {self.health} health.")
        elif action == "3":
            """
        Ability: Preemptive Dodge
        Dodge the next attack.
            """
            self.evadeNextAttack = True
            print(f"\n{self.name} uses Preemptive Dodge. He will evade the next attack!")
        else:
            print(f"Invalid selection. Defaulting to Gathering Shadows")
            # Default to Choice 1
            self.attack_power +=36
            print(f"\nShadows gather around {self.name} increasing their damage to {self.attack_power}.")


# ====================== SUBCLASSES ============================        
# Kael class (inherits from Character)

class Kael(Character):
    def __init__(self, name):
        super().__init__(name, health=180, attack_power=random.randint(10,30))

    def special_ability(self,opponent):
        print("\nSpecial Abilities")
        print("1. Flamecut Arc Fire")
        print("2. Ember Rebirth")
        action=input("\nWhich ability do you want to use?: ") 

        if action == "1":
            """
        Role: Spellsword (Hybrid Fighter + Fire Mage)
        Kael swings his blade in a wide arc, releasing a wave of searing flame that burns enemies in a cone.
        Effect: Deals fire + slashing damage; can ignite enemies or flammable surroundings.
            """
            opponent.health -=35
            opponent.attack_power -=6
            if opponent.attack_power <= 0:
                opponent.attack_power =10
            print(f"The {self.name} was used Flamecut Arc Fire on {opponent.name}. Their health was reduced to {opponent.health} and attack power to {opponent.attack_power}")
        
        elif action == "2":
            """
        When Kael is knocked to the brink of death, he can ignite himself into a flaming aura, burning nearby enemies and restoring a portion of his health.
        Effect: Once per day; self-heal + area burn + temporary boost to fire damage.    
            """
            opponent.health -= self.attack_power
            self.health += self.attack_power //2
            if self.health > self.max_health:
                self.health = self.max_health
            print(f"{self.name} uses Life self-healing now health is {self.health}, and takes away {self.attack_power} health from {opponent.name} and regenerated some health.")

        else:
            print(f"Invalid selection. Defaulting to Flamecut Arc Fire")
             # Default to Choice 1
            opponent.health -=35
            opponent.attack_power -=6
            if opponent.attack_power <= 0:
                opponent.attack_power =10
            print(f"The {self.name} was used Flamecut Arc Fire on {opponent.name}. Their health was reduced to {opponent.health} and attack power to {opponent.attack_power}")
        
 # ====================== SUBCLASSES ============================        
# Ninja class (inherits from Character)

class Ninja(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=random.randint(10,30))

    def special_ability(self,opponent):
        print("\nSpecial Abilities")
        print("1. Shadow Ripple")
        print("2. Death Lotus")
        action=input("\nWhich ability do you want to use?: ") 

        if action == "1":
            """
        Role: Ninja (Stealth + Speed Assassin)
        Kiro hurls a smoke-dagger into the ground, instantly creating a field of thick shadow mist. He can dash between any shadows within this mist, 
        making it nearly impossible to predict or target him.

        Effect: Grants short-range teleportation between shadows + invisibility while in mist.
           """
            print(f"{self.name} shadow a ripple, the kiro shadow's charges {opponent.name}")
            opponent.health -=30
            print(f"The kiro does 30 damage to {opponent.name}. Health now at {opponent.health}")        
        elif action == "2":
            """
        Kiro unleashes a flurry of spinning shuriken and slashes in a 360° radius while rapidly moving between enemies, appearing as a blur of steel and blood.
        Effect: Multi-target high-speed attack; each hit reduces enemy defense temporarily.
            """
            high_speed_attack=50
            opponent.health -=high_speed_attack
            self.high_speed_attack +=high_speed_attack
            print(f"Kiro was added. {self.name} has gained high speed attack of {self.high_speed_attack} and {opponent.name} health was reduced to {opponent.health}")
        else:
            print(f"Invalid selection. Defaulting to Shadow Ripple")   
              # Default to Choice 1
            print(f"{self.name} shadow a ripple, the kiro shadow's charges {opponent.name}")
            opponent.health -=30
            print(f"The kiro does 30 damage to {opponent.name}. Health now at {opponent.health}")    




    

