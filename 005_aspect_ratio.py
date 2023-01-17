"""
 * Dificultad: DIFÍCIL
 *
 * Enunciado: Crea un programa que se encargue de calcular el aspect ratio de una imagen a partir de una url.
 * - Url de ejemplo: https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png
 * - Por ratio hacemos referencia por ejemplo a los "16:9" de una imagen de 1920*1080px.
 *
"""

from PIL import Image
import requests
from fractions import Fraction

url = "https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png"

im = Image.open(requests.get(url, stream=True).raw)
width = im.width
height = im.height
# width = 100
# height = 5
im.close()
ratio = width/height

# ! Calculo de relacion de aspecto
#           widht       2550
# ratio = --------- =  ------ =
#           height      820

# todo: Falta resolver :C
