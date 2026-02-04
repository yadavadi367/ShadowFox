total_jumps = 0
target = 100
set_size = 10

while total_jumps < target:
    # Perform 10 jumping jacks
    total_jumps += set_size
    print(f"\nYou did {set_size} jumping jacks.")
    
    # Check if workout is complete
    if total_jumps >= target:
        print("Congratulations! You completed the workout 🎉")
        break

    # Ask if tired
    tired = input("Are you tired? (yes/y or no/n): ").lower()

    if tired == "yes" or tired == "y":
        skip = input("Do you want to skip the remaining sets? (yes/y or no/n): ").lower()
        if skip == "yes" or skip == "y":
            print(f"You completed a total of {total_jumps} jumping jacks.")
            break
    else:
        remaining = target - total_jumps
        print(f"{remaining} jumping jacks remaining.")
