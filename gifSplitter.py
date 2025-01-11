big_list = ['Articuno', 'Blaziken', 'Charizard', 'Dragonite', 'Gardevoir',
            'Gengar', 'Groudon', 'Gyarados', 'Kyogre', 'Lapras', 'Lucario',
            'Lugia', 'Machamp', 'Mew', 'Mewtwo', 'Moltres', 'Pikachu',
            'Rayquaza', 'Sceptile', 'Swampert', 'Zapdos']

from PIL import Image
import os
for i in big_list:
    for j in range(2):
        os.remove(f'static/images/{i}/{['front', 'back'][j]}_animation.gif')
