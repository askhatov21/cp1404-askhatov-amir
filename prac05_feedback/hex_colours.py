COLOUR_TO_HEX = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a", "AliceBlue": "#f0f8ff", "Alizarin crimson": "#e32636",
                "Amaranth": "#e52b50", "Amber": "ffbf00", "Amethyst": "#9966cc", "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#faebd7",
                "AntiqueWhite2": "#eedfcc"}
print(COLOUR_TO_HEX)

color_name = input("Enter the name: ").strip()

while color_name != "":
    try:
        """Convert input to case-intensive lookup(title casing the input"""
        hex_code = COLOUR_TO_HEX[color_name.title()]
        print(f'{color_name} is {hex_code}')
    except KeyError:
        print("Invalid color")
    color_name = input("Enter the name: ").strip()
print("Program excited")