#Act_1
# Escriba una función list_of_hexa_colors que devuelva cualquier número de 
# colores hexadecimales en una matriz (seis números hexadecimales escritos 
# después de #. El sistema de numeración hexadecimal está formado por 16 
# símbolos, del 0 al 9 y las primeras 6 letras del alfabeto, de la a a la f. 
# Compruebe la tarea 6 para ver ejemplos de salida).
import random
def list_of_hexa_colors(number_of_colors):
    hexa_colors = []
    for _ in range(number_of_colors):
        color = "#" + ''.join(random.choice('0123456789abcdef') for _ in range(6))
        hexa_colors.append(color)
    return hexa_colors
number = int(input("Introduce el número de colores hexadecimales que deseas generar: "))
colors = list_of_hexa_colors(number)
print("Colores hexadecimales generados:", colors)

#Act_2
#Escriba una función list_of_rgb_colors que devuelva cualquier número de 
# colores RGB en una matriz.
import random
def list_of_rgb_colors(number_of_colors):
    rgb_colors = []
    for _ in range(number_of_colors):
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        rgb_colors.append((red, green, blue))
    return rgb_colors
number = int(input("Introduce el número de colores RGB que deseas generar: "))
colors = list_of_rgb_colors(number)
print("Colores RGB generados:", colors)

#Act_3
# Escriba una función generate_colors que pueda generar cualquier número de 
# colores hexadecimales o rgb.
import random
def generate_colors(format_type, number_of_colors):
    colors = []
    if format_type.lower() == "hexa":
        for _ in range(number_of_colors):
            color = "#" + ''.join(random.choice('0123456789abcdef') for _ in range(6))
            colors.append(color)
    elif format_type.lower() == "rgb":
        for _ in range(number_of_colors):
            red = random.randint(0, 255)
            green = random.randint(0, 255)
            blue = random.randint(0, 255)
            colors.append(f"rgb({red}, {green}, {blue})")
    else:
        return "Formato no válido. Usa 'hexa' o 'rgb'."
    return colors


















