import re

#lista_nombres = ["ana","pedro","maría","rosa","sandra","celia"]
lst = [
    'Ma1',
    'Ma2',
    'Ma:3',
    'Ma4',
    'Ma5',
    'Se.1',
    'Ba1',
    'Va1',
    'Va2',
    'Ma.A',
    'MaB',
    'MaC'
]

"""for elem in lista_nombres:
    if re.findall('[o-t]$',elem):
        print(elem)"""

for elem in lst:
    if re.findall('Ma[.:]',elem):
        print(elem)