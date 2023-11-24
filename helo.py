import re

def tim(file_path):
    with open(file_path, 'r') as file:
        van_ban = file.read()
    
    day_so = '\d+'
    cac_so = re.findall(day_so, van_ban)
    
    return cac_so

ket_qua = tim('helo.txt')

print(ket_qua)

