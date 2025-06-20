import os
import re

# Percorso alla cartella root del progetto Obsidian
root_dir = r"myrootpath" # CAMBIARE CON CARTELLA ROOT DEL PROGETTO

# Costruisce una mappa filename -> percorso relativo
file_map = {}

for folder, _, files in os.walk(root_dir):
    for file in files:
        if file.endswith(".md"):
            rel_dir = os.path.relpath(folder, root_dir)
            file_map[file] = rel_dir

# Funzione per aggiornare i link nei file
link_pattern = re.compile(r'\[([^\]]+)\]\(([^/()\s]+\.md)\)')

for folder, _, files in os.walk(root_dir):
    for file in files:
        if file.endswith(".md"):
            file_path = os.path.join(folder, file)
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            def replacer(match):
                label, target_file = match.groups()
                if target_file in file_map:
                    new_path = f"{file_map[target_file]}/{target_file}".replace("\\", "/")
                    return f"[{label}]({new_path})"
                return match.group(0)

            new_content = link_pattern.sub(replacer, content)

            # Sovrascrive il file solo se ci sono cambiamenti
            if new_content != content:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(new_content)
