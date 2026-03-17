with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Odstran pomlcky - presny text z kodu
content = content.replace('.pain-q::before { content: "-";', '.pain-q::before { content: "";')

# Zvacsi text otazok
content = content.replace('.pain-q {\n            padding: 1.1rem 1rem;', '.pain-q {\n            font-size: 1.15rem;\n            padding: 1.1rem 1rem;')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Hotovo!')
