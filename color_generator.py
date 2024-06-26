from PIL import Image
import random
import webcolors
import os

path_name = "images"
if not os.path.exists(path_name):
    os.makedirs(path_name)

R = random.randrange(16, 256)
G = random.randrange(16, 256)
B = random.randrange(16, 256)

hex_name_lower = webcolors.rgb_to_hex((R, G, B))
hex_name = hex_name_lower.upper()

css3_hex_to_names = {'#F0F8FF': 'Aliceblue', '#FAEBD7': 'Antiquewhite', '#00FFFF': 'Cyan', '#7FFFD4': 'Aquamarine', '#F0FFFF': 'Azure', '#F5F5DC': 'Beige', '#FFE4C4': 'Bisque', '#000000': 'Black', '#FFEBCD': 'Blanchedalmond', '#0000FF': 'Blue', '#8A2BE2': 'Blueviolet', '#A52A2A': 'Brown', '#DEB887': 'Burlywood', '#5F9EA0': 'Cadetblue', '#7FFF00': 'Chartreuse', '#D2691E': 'Chocolate', '#FF7F50': 'Coral', '#6495ED': 'Cornflowerblue', '#FFF8DC': 'Cornsilk', '#DC143C': 'Crimson', '#00008B': 'Darkblue', '#008B8B': 'Darkcyan', '#B8860B': 'Darkgoldenrod', '#A9A9A9': 'Darkgray', '#006400': 'Darkgreen', '#BDB76B': 'Darkkhaki', '#8B008B': 'Darkmagenta', '#556B2F': 'Darkolivegreen', '#FF8C00': 'Darkorange', '#9932CC': 'Darkorchid', '#8B0000': 'Darkred', '#E9967A': 'Darksalmon', '#8FBC8F': 'Darkseagreen', '#483D8B': 'Darkslateblue', '#2F4F4F': 'Darkslategray', '#00CED1': 'Darkturquoise', '#9400D3': 'Darkviolet', '#FF1493': 'Deeppink', '#00BFFF': 'Deepskyblue', '#696969': 'Dimgray', '#1E90FF': 'Dodgerblue', '#B22222': 'Firebrick', '#FFFAF0': 'Floralwhite', '#228B22': 'Forestgreen', '#FF00FF': 'Magenta', '#DCDCDC': 'Gainsboro', '#F8F8FF': 'Ghostwhite', '#FFD700': 'Gold', '#DAA520': 'Goldenrod', '#808080': 'Gray', '#008000': 'Green', '#ADFF2F': 'Greenyellow', '#F0FFF0': 'Honeydew', '#FF69B4': 'Hotpink', '#CD5C5C': 'Indianred', '#4B0082': 'Indigo', '#FFFFF0': 'Ivory', '#F0E68C': 'Khaki', '#E6E6FA': 'Lavender', '#FFF0F5': 'Lavenderblush', '#7CFC00': 'Lawngreen', '#FFFACD': 'Lemonchiffon', '#ADD8E6': 'Lightblue', '#F08080': 'Lightcoral', '#E0FFFF': 'Lightcyan', '#FAFAD2': 'Lightgoldenrodyellow', '#D3D3D3': 'Lightgray', '#90EE90': 'Lightgreen', '#FFB6C1': 'Lightpink', '#FFA07A': 'Lightsalmon', '#20B2AA': 'Lightseagreen', '#87CEFA': 'Lightskyblue', '#778899': 'Lightslategray', '#B0C4DE': 'Lightsteelblue', '#FFFFE0': 'Lightyellow', '#00FF00': 'Lime', '#32CD32': 'Limegreen', '#FAF0E6': 'Linen', '#800000': 'Maroon', '#66CDAA': 'Mediumaquamarine', '#0000CD': 'Mediumblue', '#BA55D3': 'Mediumorchid', '#9370DB': 'Mediumpurple', '#3CB371': 'Mediumseagreen', '#7B68EE': 'Mediumslateblue', '#00FA9A': 'Mediumspringgreen', '#48D1CC': 'Mediumturquoise', '#C71585': 'Mediumvioletred', '#191970': 'Midnightblue', '#F5FFFA': 'Mintcream', '#FFE4E1': 'Mistyrose', '#FFE4B5': 'Moccasin', '#FFDEAD': 'Navajowhite', '#000080': 'Navy', '#FDF5E6': 'Oldlace', '#808000': 'Olive', '#6B8E23': 'Olivedrab', '#FFA500': 'Orange', '#FF4500': 'Orangered', '#DA70D6': 'Orchid', '#EEE8AA': 'Palegoldenrod', '#98FB98': 'Palegreen', '#AFEEEE': 'Paleturquoise', '#DB7093': 'Palevioletred', '#FFEFD5': 'Papayawhip', '#FFDAB9': 'Peachpuff', '#CD853F': 'Peru', '#FFC0CB': 'Pink', '#DDA0DD': 'Plum', '#B0E0E6': 'Powderblue', '#800080': 'Purple', '#FF0000': 'Red', '#BC8F8F': 'Rosybrown', '#4169E1': 'Royalblue', '#8B4513': 'Saddlebrown', '#FA8072': 'Salmon', '#F4A460': 'Sandybrown', '#2E8B57': 'Seagreen', '#FFF5EE': 'Seashell', '#A0522D': 'Sienna', '#C0C0C0': 'Silver', '#87CEEB': 'Skyblue', '#6A5ACD': 'Slateblue', '#708090': 'Slategray', '#FFFAFA': 'Snow', '#00FF7F': 'Springgreen', '#4682B4': 'Steelblue', '#D2B48C': 'Tan', '#008080': 'Teal', '#D8BFD8': 'Thistle', '#FF6347': 'Tomato', '#40E0D0': 'Turquoise', '#EE82EE': 'Violet', '#F5DEB3': 'Wheat', '#FFFFFF': 'White', '#F5F5F5': 'Whitesmoke', '#FFFF00': 'Yellow', '#9ACD32': 'Yellowgreen'}
# capitalized_css3_hex_to_names = {k: v.capitalize() for k, v in css3_hex_to_names.items()}

def closest_colour(requested_colour):
    min_colours = {}
    for key, name in css3_hex_to_names.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def get_colour_name(requested_colour):
    try:
        closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
    except ValueError:
        closest_name = closest_colour(requested_colour)
        actual_name = None
    return actual_name, closest_name

requested_colour = (R, G, B)
actual_name, closest_name = get_colour_name(requested_colour)






im = Image.new(mode="RGB", size=(200, 200), color=(R, G, B))
# im.show()
# path_name = "/Users/user/Desktop/combibot/images"
im.save(f"{path_name}/{closest_name}.png")



print(hex_name, R, G, B)
print("color name: ", closest_name)


# img = Image.open(r"image.jpg")
# # img.show()
# print(img.mode)
# print(img.size)
# img.resize(size=(100, 100))