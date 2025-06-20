import os
import re

# Percorso alla root del tuo vault
root_dir = r"myrootpath" # CAMBIARE CON CARTELLA ROOT DEL PROGETTO

# Regex: trova tutti i link Markdown che NON iniziano con "/"
link_pattern = re.compile(r'\[([^\]]+)\]\(((?!http)(?!/)[^)\s]+\.md)\)')

for folder, _, files in os.walk(root_dir):
    for file in files:
        if file.endswith(".md"):
            file_path = os.path.join(folder, file)
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Aggiunge "/" all'inizio del path se manca
            def replacer(match):
                label, path = match.groups()
                return f"[{label}](/" + path + ")"

            new_content = link_pattern.sub(replacer, content)

            if new_content != content:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(f"Aggiornato: {file_path}")
