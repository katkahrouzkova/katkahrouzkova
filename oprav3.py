import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Odstran pomlcky z CSS
content = re.sub(r'content:\s*["\u201e]-["\u201c];', 'content: "";', content)
content = re.sub(r"content:\s*'-';", "content: '';", content)

# Zleps nadpis v tmavej sekcii - vacsi font a lepsie formatovanie
content = content.replace(
    '<p style="font-size:1rem;color:rgba(255,255,255,0.75);line-height:1.7;max-width:600px;margin:0 auto 3rem;text-align:center;">Pokud vás oslovila alespoň jedna otázka, nejste sami. Jsou na začátku každého rozhovoru, který vedu.</p>',
    '<h2 style="font-family:Georgia,serif;font-size:2rem;color:white;line-height:1.4;max-width:700px;margin:0 auto 1rem;text-align:center;">Pokud vás oslovila alespoň jedna otázka, nejste sami.</h2><p style="font-size:1rem;color:rgba(255,255,255,0.7);line-height:1.7;max-width:500px;margin:0 auto 3rem;text-align:center;">Jsou na začátku každého rozhovoru, který vedu.</p>'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Hotovo!')
