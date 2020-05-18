
def printer_error (colors):
    invalid_colors = [color for color in colors if color not in 'abcdefghijklm']
    return str(len(invalid_colors))+'/'+str(len(colors))

printer_error('acdfxñ') 
