# List of superheroes
justice_league = ["Superman", "Batman", "WonderWoman", "Flash", "Aquaman", "Green Lantern"]

members_in_league = len(justice_league)
print(members_in_league)

justice_league.append("Batgirl")
justice_league.append("Nightwing")
# printing justice league
print(justice_league)

# Moving wonder woman to the beginning of the list
justice_league.remove("WonderWoman")
justice_league.insert(0, "WonderWoman")
# printing justice league
print(justice_league)

# Moving Superman in between Aquaman and Flash
justice_league.remove("Superman")
justice_league.insert(3, "Superman")
# printing justice league
print(justice_league)

# Replacing the justice league with a new list
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
# printing justice league
print(justice_league)

# Sorting the justice league alphabetically
justice_league.sort()
# printing justice league
print(justice_league)

# The new leader of the justice league
print(justice_league[0])
# printing justice league
print(justice_league)
