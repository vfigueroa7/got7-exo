from bs4 import BeautifulSoup

# Cargar los archivos HTML
with open('followers_1.html', 'r', encoding='utf-8') as f:
    followers_html = f.read()

with open('following.html', 'r', encoding='utf-8') as f:
    following_html = f.read()

# Parsear el contenido HTML
followers_soup = BeautifulSoup(followers_html, 'html.parser')
following_soup = BeautifulSoup(following_html, 'html.parser')

# Extraer cualquier texto dentro de las etiquetas <span> y <a>
followers = [item.text.strip() for item in followers_soup.find_all(['span', 'a'])]
following = [item.text.strip() for item in following_soup.find_all(['span', 'a'])]

# Filtrar listas para eliminar entradas vacías
followers = [name for name in followers if name]
following = [name for name in following if name]

# Imprimir las listas para verificar los datos (opcional)
print("Seguidores (followers):")
print(followers)

print("\nSeguidos (following):")
print(following)

# Encontrar a las personas que te siguen pero que tú no sigues de vuelta
not_followed_back = [user for user in followers if user not in following]

# Mostrar los resultados
if not_followed_back:
    print("\nPersonas que te siguen pero tú no sigues de vuelta:")
    for user in not_followed_back:
        print(user)
else:
    print("\nSigues a todos los que te siguen de vuelta.")
