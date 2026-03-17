with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    'min-height: calc(100vh - 72px);',
    'min-height: calc(60vh - 72px);'
)

content = content.replace(
    'min-height: 60vh;',
    'min-height: 60vh; max-height: 600px;'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Hotovo!')
