def create_character(name, strength, intelligence, charisma):
    # 1. Name Validation
    if not isinstance(name, str):
        return "The character name should be a string."
    if name == "":
        return "The character should have a name."
    if len(name) > 10:
        return "The character name is too long."
    if " " in name:
        return "The character name should not contain spaces."

    # 2. Type Check on Stats
    if not (isinstance(strength, int) and isinstance(intelligence, int) and isinstance(charisma, int)):
        return "All stats should be integers."

    # 3. Value Constraints on Stats
    if strength < 1 or intelligence < 1 or charisma < 1:
        return "All stats should be no less than 1."
    if strength > 4 or intelligence > 4 or charisma > 4:
        return "All stats should be no more than 4."
    if (strength + intelligence + charisma) != 7:
        return "The character should start with 7 points."

    # 4. Stat Bar Visualization Components
    f_dot = "●"
    e_dot = "○"

    return (
        f"{name}\n"
        f"STR {f_dot * strength}{e_dot * (10 - strength)}\n"
        f"INT {f_dot * intelligence}{e_dot * (10 - intelligence)}\n"
        f"CHA {f_dot * charisma}{e_dot * (10 - charisma)}"
    )

# Demonstration Case Execution
print(create_character('ren', 4, 2, 1))