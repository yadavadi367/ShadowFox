# Initial Justice League list
justice_league = [
    "Superman",
    "Batman",
    "Wonder Woman",
    "Flash",
    "Aquaman",
    "Green Lantern"
]

print("Initial Justice League:", justice_league)

# 1. Number of members
print("\n1. Number of members:", len(justice_league))

# 2. Add Batgirl and Nightwing
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("\n2. After adding Batgirl and Nightwing:", justice_league)

# 3. Move Wonder Woman to the beginning
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("\n3. Wonder Woman as leader:", justice_league)

# 4. Separate Aquaman and Flash
# Move Superman between Aquaman and Flash
justice_league.remove("Superman")
aquaman_index = justice_league.index("Aquaman")
flash_index = justice_league.index("Flash")
justice_league.insert(aquaman_index, "Superman")
print("\n4. After separating Aquaman and Flash:", justice_league)

# 5. Replace with new team
justice_league = [
    "Cyborg",
    "Shazam",
    "Hawkgirl",
    "Martian Manhunter",
    "Green Arrow"
]
print("\n5. New Justice League team:", justice_league)

# 6. Sort alphabetically
justice_league.sort()
print("\n6. Sorted Justice League:", justice_league)

# New leader
print("\nNew Leader:", justice_league[0])