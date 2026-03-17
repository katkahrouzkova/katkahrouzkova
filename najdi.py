with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Najdi a vypis kontext okolo pain-q::before
idx = content.find('pain-q::before')
if idx >= 0:
    print("NASLO SA:")
    print(repr(content[idx-5:idx+100]))
else:
    print("NENASLO SA pain-q::before")

# Najdi pain-q font size
idx2 = content.find('.pain-q {')
if idx2 >= 0:
    print("PAIN-Q CSS:")
    print(repr(content[idx2:idx2+150]))
