import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old = re.search(r'<section class="pain-section".*?</section>', content, re.DOTALL).group()

new = '''<section class="pain-section" style="background:var(--beige-warm);">
            <div class="wrap">
                <span class="section-label">Poznáváte se?</span>
                <h2 class="section-title">Otázky, se kterými přicházejí moji klienti</h2>
                <div class="pain-questions" style="margin-top:2.5rem;">
                    <div class="pain-q">Dělám práci, která dává smysl – ale přesto jsem vyčerpaný/á. Proč?</div>
                    <div class="pain-q">Mám vzdělání i zkušenosti, ale nevím, kam dál.</div>
                    <div class="pain-q">Nevím, v čem jsem dobrý/á. Jak zjistím své silné stránky?</div>
                    <div class="pain-q">Je mi 40+ a ptám se, jestli tohle chci až do důchodu.</div>
                    <div class="pain-q">Chci se posunout, ale nevím jak. Co je ten správný krok?</div>
                    <div class="pain-q">Práce mě dřív bavila – teď už ne. Jak najít smysl tam, kde jsem?</div>
                    <div class="pain-q">Jsem nový manažer a nevím, jak vést tým po svém.</div>
                    <div class="pain-q">Firma mi dala budget na rozvoj – chci ho využít smysluplně.</div>
                </div>
            </div>
        </section>

        <section style="background:var(--petrol);padding:5rem 0;">
            <div class="wrap">
                <p style="font-size:1rem;color:rgba(255,255,255,0.75);line-height:1.7;max-width:600px;margin:0 auto 3rem;text-align:center;">Pokud vás oslovila alespoň jedna otázka, nejste sami. Jsou na začátku každého rozhovoru, který vedu.</p>
                <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:1.5rem;max-width:900px;margin:0 auto;">
                    <div style="background:rgba(255,255,255,0.08);border-radius:12px;padding:1.8rem;border:1px solid rgba(255,255,255,0.15);">
                        <div style="width:2.2rem;height:2.2rem;border-radius:50%;background:rgba(255,255,255,0.2);color:white;display:flex;align-items:center;justify-content:center;font-size:0.85rem;font-weight:600;margin-bottom:1rem;">1</div>
                        <h4 style="margin:0 0 0.5rem;font-size:1rem;color:white;font-weight:600;">Pochopíte sami sebe</h4>
                        <p style="margin:0;font-size:0.88rem;color:rgba(255,255,255,0.75);line-height:1.6;">Zjistíte své talenty a jak přirozeně fungujete.</p>
                    </div>
                    <div style="background:rgba(255,255,255,0.08);border-radius:12px;padding:1.8rem;border:1px solid rgba(255,255,255,0.15);">
                        <div style="width:2.2rem;height:2.2rem;border-radius:50%;background:rgba(255,255,255,0.2);color:white;display:flex;align-items:center;justify-content:center;font-size:0.85rem;font-weight:600;margin-bottom:1rem;">2</div>
                        <h4 style="margin:0 0 0.5rem;font-size:1rem;color:white;font-weight:600;">Najdeme váš směr</h4>
                        <p style="margin:0;font-size:0.88rem;color:rgba(255,255,255,0.75);line-height:1.6;">Kariérní možnosti odpovídající vašim talentům a hodnotám.</p>
                    </div>
                    <div style="background:rgba(255,255,255,0.08);border-radius:12px;padding:1.8rem;border:1px solid rgba(255,255,255,0.15);">
                        <div style="width:2.2rem;height:2.2rem;border-radius:50%;background:rgba(255,255,255,0.2);color:white;display:flex;align-items:center;justify-content:center;font-size:0.85rem;font-weight:600;margin-bottom:1rem;">3</div>
                        <h4 style="margin:0 0 0.5rem;font-size:1rem;color:white;font-weight:600;">Vytvoříte konkrétní plán</h4>
                        <p style="margin:0;font-size:0.88rem;color:rgba(255,255,255,0.75);line-height:1.6;">Konkrétní kroky, timeline a podpora po celé cestě.</p>
                    </div>
                </div>
            </div>
        </section>'''

content = content.replace(old, new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Hotovo!')
