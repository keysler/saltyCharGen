import random

combatSkills = ["Alteration", "Archery", "Block", "Conjuration", "Destruction", "Illusion", "One Handed", "Restoration", "Sneak", "Two Handed"]
nonCombatSkills = ["Alchemy", "Enchanting", "Lockpicking", "Pickpocket", "Smithing", "Speech"]
races = ["Altmer", "Argonian", "Bosmer", "Breton", "Dunmer", "Imperial", "Khajiit", "Nord", "Orc", "Redguard"]
armour = ["Evasion", "Heavy Armour"]
standingStonesGroups = ["Warrior", "Mage", "Thief", "Serpent"]
majorSkills = []
minorSkills = []
weakSkills = []
race = []
armourSelected = []
stone = []

def generateSetForSelection( source, quantity ):
    selected = []
    while (len(selected) < quantity):
        skill = random.randint(0, (len(source) - 1))
        selected.append(source[skill])
        source.pop(skill)
    return selected;

def promptUserForSelection( source, word ):
    for i in range(len(selected)):
        print(str(i + 1) + ". " + selected[i])
    answer = int(input("Pick " + word + ": ")) - 1
    source.append(selected[answer])
    selected.pop(answer)

print("Step 1: Combat Skills")
print("You will now pick two major skills. Other two will be weak skills.")
selected = generateSetForSelection( combatSkills, 4 )
for i in range(2):
    promptUserForSelection( majorSkills, "major skill" )
weakSkills.extend(selected)

print("Step 2: Non-Combat Skills")
for i in range(2):
    print("You will now pick 1 major and 1 weak skill.")
    selected = generateSetForSelection( nonCombatSkills, 3 )
    promptUserForSelection( majorSkills, "major skill" )
    promptUserForSelection( weakSkills, "weak skill" )
    nonCombatSkills.extend(selected)

print("Step 3: Remaining Skills")
remainingSkills = combatSkills + nonCombatSkills
print("You will now pick one major skill. Other two will be weak skills.")
selected = generateSetForSelection( remainingSkills, 3 )
promptUserForSelection( majorSkills, "major skill" )
weakSkills.extend(selected)

selected = remainingSkills
print("You will now pick one weak skill. The rest will be minor skills.")
promptUserForSelection( weakSkills, "weak skill" )
minorSkills.extend(selected)

selected = generateSetForSelection( races, 2 )
print("You will now pick race.")
promptUserForSelection( race, "race" )

selected = armour
print("You will now select armour type.")
promptUserForSelection( armourSelected, "armour type" )
minorSkills.extend(armourSelected)

selected = minorSkills
print("You will pick one minor skill to be promoted to major")
promptUserForSelection( majorSkills, "skill to promote to major" )
minorSkills.extend(selected)

selected = standingStonesGroups
print("You will now select your stone group")
print(selected)
answer = int(input("Pick standing stones group: ")) - 1
if (selected[answer] == "Serpent"):
    stone.extend(selected[answer])
elif (selected[answer] == "Warrior"):
    print("You will now select your stone")
    selected = generateSetForSelection( ["The Lady", "The Lord", "The Steed", "The Warrior"], 3 )
    promptUserForSelection( stone, "stone" )
elif (selected[answer] == "Mage"):
    print("You will now select your stone")
    selected = generateSetForSelection( ["The Apprentice", "The Atronach", "The Mage", "The Ritual"], 3 )
    promptUserForSelection( stone, "stone" )
elif (selected[answer] == "Thief"):
    print("You will now select your stone")
    selected = generateSetForSelection( ["The Lover", "The Shadow", "The Thief", "The Tower"], 3 )
    promptUserForSelection( stone, "stone" )
    

print("Your major skills are: " + ', '.join(majorSkills))
print("Your minor skills are: " + ', '.join(minorSkills))
print("Your weak skills are: " + ', '.join(weakSkills))
print("Your race is: " + ', '.join(race))
print("Your armour type is: " + ', '.join(armourSelected))
print("Your stone is: " + ', '.join(stone))