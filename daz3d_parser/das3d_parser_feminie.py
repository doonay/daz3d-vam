#Characters > Humans > Feminine
import requests
import json

url = 'https://www.daz3d.com/dazstatic/slab/getPrices/id/0'
headers = {
	'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
	'Referer': 'https://www.daz3d.com/catalogsearch/result?pp=40&q=&category[]=Characters+>+Humans+>+Feminine&s=score&p=1&guid=',
	'sec-ch-ua-mobile': '?0',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
	'sec-ch-ua-platform': '"Windows"',
}
session = requests.Session()
r = session.get(url, headers=headers)
json_data = json.loads(r.text.replace('var dazPricingGroup = 0;var dazPricing = ', ''))
keylist = json_data.keys()
with open('keys.txt', 'w', encoding='utf-8') as file:
	for key in keylist:
		file.writelines(f'{key}\n')

"""
%5B = [
%5D = ]
%3E = >
(all URL-codes https://html5css.ru/tags/ref_urlencode.php)

headers for ALL daz3d resources:
All
'Referer': 'https://www.daz3d.com/catalogsearch/result?pp=80&q=&s=score&p=1&guid='
---
Add-Ons only
'Referer: https://www.daz3d.com/catalogsearch/result?pp=80&q=&category[]=Add-Ons&s=score&p=1&guid='
---
Characters
Characters > Animals
Characters > Animals > Air
Characters > Animals > Land
---
Characters > Animals > Land > Bugs and Insects
'Referer: https://www.daz3d.com/catalogsearch/result?pp=40&q=&category[]=Characters+>+Animals+>+Land+>+Bugs+and+Insects&s=score&p=1&guid='
---
Characters > Animals > Sea
Characters > Creatures
Characters > Creatures > Aliens
Characters > Creatures > Beasts
Characters > Creatures > Humanoids
Characters > Humans
---
Characters > Humans > Feminine
'Referer': 'https://www.daz3d.com/catalogsearch/result?pp=40&q=&category[]=Characters+>+Humans+>+Feminine&s=score&p=1&guid='
---
Characters > Humans > Masculine
Characters > Humans > Non-Binary
Characters > Modifiers
Characters > Modifiers > Anatomical elements
Characters > Modifiers > Body
Characters > Modifiers > Eyes
Characters > Modifiers > Geografts
Characters > Modifiers > Head
Characters > Modifiers > Horns
Characters > Modifiers > Morphs and Shapes
Characters > Modifiers > Skin textures
Characters > Modifiers > Wings
Characters > Robots
Clothes and Accessories
Clothes and Accessories > Accessories
Clothes and Accessories > Accessories > Headwear
Clothes and Accessories > Accessories > Headwear > glasses
Clothes and Accessories > Accessories > Jewelry
Clothes and Accessories > Accessories > Other Accessories
Clothes and Accessories > Accessories > Tattoos and Makeup
Clothes and Accessories > Clothing
Clothes and Accessories > Clothing > Bottoms
Clothes and Accessories > Clothing > Clothing Textures
Clothes and Accessories > Clothing > Dresses
Clothes and Accessories > Clothing > Hosiery
Clothes and Accessories > Clothing > Intimates
Clothes and Accessories > Clothing > Outerwear
Clothes and Accessories > Clothing > Outfits
Clothes and Accessories > Clothing > Outfits > Armor
Clothes and Accessories > Clothing > Outfits > Costumes
Clothes and Accessories > Clothing > Outfits > Full body
Clothes and Accessories > Clothing > Shoes
Clothes and Accessories > Clothing > Swimwear
Clothes and Accessories > Clothing > Tops
Clothing and Accessories > Shoes and footwear
Environments
Environments > Exteriors
"""