"""
Aniket Tayade
Contact Details
aniket@theanikettayade.tech  || theanikettayade.tech || 7057530791

"""
import easyocr

reader = easyocr.Reader(['en'])
result = reader.readtext('text.jpg')

with open('output.txt', 'w') as file:
    for item in result:
        file.write(str(item) + '\n')
