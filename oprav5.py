with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Zmensit vysku hero sekcie
content = content.replace(
    'padding-top: 72px; min-height: 100vh;',
    'padding-top: 72px; min-height: 75vh;'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Hotovo!')
