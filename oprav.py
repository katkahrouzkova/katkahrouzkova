import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Odstran pomlcky
content = re.sub(r'content:\s*"-";', 'content: "";', content)

# Oprav farby textu v pain-right
content = content.replace(
    'font-style:italic;font-size:1.15rem;color:var(--petrol)',
    'font-style:italic;font-size:1.15rem;color:rgba(255,255,255,0.9)'
)

# Oprav nadpisy kariet na biele
content = content.replace(
    'font-size:1rem;color:var(--petrol);">Pochopíte',
    'font-size:1rem;color:white;font-weight:600;">Pochopíte'
)
content = content.replace(
    'font-size:1rem;color:var(--petrol);">Najdeme',
    'font-size:1rem;color:white;font-weight:600;">Najdeme'
)
content = content.replace(
    'font-size:1rem;color:var(--petrol);">Vytvoříte',
    'font-size:1rem;color:white;font-weight:600;">Vytvoříte'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Hotovo!')
