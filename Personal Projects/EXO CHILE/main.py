import re

descripcion = input("Hola, pon aquí el texto que quieras editar: ")

date_pattern = r'(\d{6})'
final_pattern = r'\[ EXO Chile \]'

emoji = []
if "Video" in descripcion:
    emoji.append("🎥")
if "Imagen" in descripcion:
    emoji.append("📸")
if "Info" in descripcion:
    emoji.append("🌐")
if "Trad" in descripcion:
    emoji.append("📝")
if "◆" in descripcion and emoji:
    descripcion = descripcion.replace("◆", emoji[0])

# Reemplazar las llaves en la descripción
if "{" in descripcion or "}" in descripcion:
    descripcion = descripcion.replace("{", "").replace("}", "")

match = re.search(date_pattern, descripcion)
match_dos = re.search(final_pattern, descripcion)

if match:
    date = match.group(0)
    date_index = descripcion.index(date)
    descripcion = descripcion[date_index:]

    if match_dos:
        final_text = match_dos.group(0)
        final_index = descripcion.index(final_text) + len(final_text)
        descripcion = descripcion[:final_index]
        if "#Chen" in descripcion:
            descripcion = descripcion + "\n @weareoneEXO @CHEN_INB100 #EXO #엑소"
        elif "#Baekhyun" in descripcion:
            descripcion = descripcion + "\n @weareoneEXO @B_hundred_Hyun #EXO #엑소"
        elif "#Xiumin" in descripcion:
            descripcion = descripcion + "\n @weareoneEXO @XIUMIN_INB100 #EXO #엑소"
        elif "#Lay" in descripcion:
            descripcion = descripcion + "\n @weareoneEXO @layzhang #EXO #엑소"
        else:
            descripcion = descripcion + "\n @weareoneEXO #EXO #엑소"

        print(descripcion)
    else:
        print("No se encontró 'EXO Chile' en el texto.")
else:
    print("El formato no es correcto.")
