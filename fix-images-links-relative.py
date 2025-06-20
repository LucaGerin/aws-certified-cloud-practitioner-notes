import os
import re

# Percorso al vault
root_dir = r"myrootpath" # CAMBIARE CON CARTELLA ROOT DEL PROGETTO

# Regex: trova ![Alt text](qualcosa.png) dove qualcosa NON contiene già "img/"
img_pattern = re.compile(r'!\[([^\]]*)\]\((?!img/)([^)\s]+\.(?:png|jpg|jpeg|gif|svg))\)', re.IGNORECASE)

# Scansiona tutti i file .md
for folder, _, files in os.walk(root_dir):
    for file in files:
        if file.endswith(".md"):
            file_path = os.path.join(folder, file)
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Aggiunge "img/" davanti al percorso immagine
            def replacer(match):
                alt, img_file = match.groups()
                return f"![{alt}](img/{img_file})"

            new_content = img_pattern.sub(replacer, content)

            if new_content != content:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(f"Aggiornato: {file_path}")
