from PyPDF2 import PdfReader, PdfWriter
from icecream import ic
from math import trunc, ceil

archivo = PdfReader(open('./python/PIII.pdf', 'rb'))
paginas = len(archivo.pages)
cantidad = 3
total_sections = paginas/cantidad
sections = trunc(total_sections)
rest = ceil((total_sections - sections) * cantidad)
lastpage = paginas - rest
lenIndex = len(str(sections))

#ic(paginas, cantidad, total_sections, sections,rest, lastpage)


def createSection(frompage, topage, filename):
    newArchivo = PdfWriter()
    for page in range(frompage, topage):
        newArchivo.add_page(archivo.pages[page])
    with open(f'./python/sections/{filename}.pdf', 'wb') as farchivo:
        newArchivo.write(farchivo)

def generateIndex(num, length):
    num = str(num)
    return '0'*(length-len(num))+num

for section in range(sections):
    newSection = section*cantidad
    createSection(newSection, newSection+cantidad,f'parte_{generateIndex(section+1,lenIndex)}')

if rest!=0:
    createSection(lastpage, lastpage+rest,f'parte_{generateIndex(sections+1,lenIndex)}')