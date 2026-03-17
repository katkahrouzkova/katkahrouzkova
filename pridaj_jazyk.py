#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Skript: pridaj_jazyk.py
Pridá CZ/EN prepínač do index.html webu Katka Hrouzková
Spusti v priečinku kde je index.html:
  python3 pridaj_jazyk.py
"""

import re

INPUT_FILE = "index.html"
OUTPUT_FILE = "index.html"

with open(INPUT_FILE, encoding="utf-8") as f:
    html = f.read()

# ─────────────────────────────────────────────
# 1. CSS pre prepínač
# ─────────────────────────────────────────────
LANG_CSS = """
        /* ── Jazykový prepínač ── */
        .lang-switcher {
            display: flex;
            align-items: center;
            gap: 0;
            border: 1px solid var(--sage-light);
            border-radius: 20px;
            overflow: hidden;
            margin-left: 1.5rem;
            flex-shrink: 0;
        }
        .lang-switcher button {
            background: transparent;
            border: none;
            padding: 0.28rem 0.75rem;
            font-size: 0.78rem;
            font-weight: 500;
            letter-spacing: 0.04em;
            cursor: pointer;
            color: var(--text-light);
            transition: background 0.2s, color 0.2s;
            font-family: inherit;
        }
        .lang-switcher button.active {
            background: var(--sage);
            color: var(--white);
        }
        .lang-switcher button:hover:not(.active) {
            background: var(--sage-pale);
        }
        /* Skryje/zobrazí texty podľa jazyka */
        [data-en] { }
        .lang-en [data-cz]:not([data-en]) { }
"""

# Vložíme CSS pred </style> (prvý výskyt)
html = html.replace("</style>", LANG_CSS + "\n        </style>", 1)

# ─────────────────────────────────────────────
# 2. HTML prepínača do navigácie
# ─────────────────────────────────────────────
LANG_BTN_HTML = """<div class="lang-switcher">
                <button id="btn-cz" class="active" onclick="setLang('cz')">CZ</button>
                <button id="btn-en" onclick="setLang('en')">EN</button>
            </div>"""

# Pridáme prepínač do .wrap v nav — za posledný </a> pred </div>
# Hľadáme </nav> a pred ňou vložíme do .wrap
html = re.sub(
    r'(</div>\s*</nav>)',
    LANG_BTN_HTML + r'\n        \1',
    html,
    count=1
)

# ─────────────────────────────────────────────
# 3. JavaScript prepínača
# ─────────────────────────────────────────────
LANG_JS = """
<script>
/* ── CZ/EN prepínač ── */
(function () {
    var translations = {
        /* === NAVIGÁCIA === */
        'nav-sluzby':       { cz: 'Služby',          en: 'Services' },
        'nav-o-mne':        { cz: 'O mně',            en: 'About me' },
        'nav-kontakt':      { cz: 'Kontakt',          en: 'Contact' },
        'nav-cta':          { cz: 'Chci bezplatnou konzultaci', en: 'Free consultation' },

        /* === HERO === */
        'hero-h1-line1':    { cz: 'POZNEJTE SE LÉPE.', en: 'KNOW YOURSELF BETTER.' },
        'hero-h1-line2':    { cz: 'pracujte a žijte způsobem, který vám sedí', en: 'work and live in a way that suits you' },
        'hero-sub':         { cz: 'Pomůžu vám lépe porozumět sobě – ať řešíte kariéru, vztahy v práci, vlastní způsob fungování, nebo prostě hledáte, co dál.', en: 'I will help you understand yourself better – whether you are navigating a career change, workplace relationships, your own way of working, or simply looking for what comes next.' },
        'hero-cred':        { cz: 'Psychologie · 17 let v globálním HR · PRISM Brain Mapping certifikace · Inpram certifikace (Gallup CliftonStrengths) · Erickson koučink', en: 'Psychology · 17 years in global HR · PRISM Brain Mapping certified · Inpram certified (Gallup CliftonStrengths) · Erickson coaching' },
        'hero-btn':         { cz: 'Chci bezplatnou konzultaci', en: 'Book a free consultation' },

        /* === SEKCIA – otázky klientov === */
        'q-intro':          { cz: 'Jsou na začátku každého rozhovoru, který vedu.', en: 'These are the questions that open every conversation I have.' },
        'q-h2-1':           { cz: 'Otázky, se kterými přicházejí moji klienti', en: 'Questions my clients bring' },
        'q-h2-2':           { cz: 'Pokud vás oslovila alespoň jedna otázka, nejste sami.', en: 'If at least one of these resonates, you are not alone.' },
        'q-q1':             { cz: '„Dělám správnou práci? Nebo jen tu, co se ode mě čeká?"', en: '\"Am I doing the right work? Or just what is expected of me?\"' },
        'q-q2':             { cz: '„Chtěl/a bych změnu – ale nevím, co vlastně chci."', en: '\"I want a change – but I don\'t know what I actually want.\"' },
        'q-q3':             { cz: '„Navenek mám vše – ale uvnitř se neptám, jestli mě to naplňuje."', en: '\"On the surface I have it all – but inside I wonder if it fulfils me.\"' },
        'q-q4':             { cz: '„Mám pocit, že dávám do práce víc, než dostávám zpátky."', en: '\"I feel like I give more to work than I get back.\"' },
        'q-q5':             { cz: '„Je mi 40+ a ptám se, jestli tohle opravdu chci až do důchodu."', en: '\"I am 40+ and wondering if this is really what I want until retirement.\"' },
        'q-q6':             { cz: '\"AI mění moje odvětví. Co teď se sebou?"', en: '\"AI is changing my industry. What do I do now?\"' },

        /* === SEKCIA – čo získate === */
        'gain-h4-1':        { cz: 'Pochopíte sami sebe', en: 'You will understand yourself' },
        'gain-h4-2':        { cz: 'Najdeme váš směr', en: 'We will find your direction' },
        'gain-h4-3':        { cz: 'Vytvoříte konkrétní plán', en: 'You will create a concrete plan' },

        /* === SEKCIA – služby (výber) === */
        'svc-h2':           { cz: 'Vyberte si cestu, která vám sedí', en: 'Choose the path that suits you' },
        'svc-kou-h3':       { cz: '1:1 Koučování', en: '1:1 Coaching' },
        'svc-kou-p':        { cz: 'Pravidelná podpora při rozhodování a kariérních změnách.', en: 'Regular support for decision-making and career transitions.' },
        'svc-kou-btn':      { cz: 'Začněme společně', en: 'Let\'s start together' },
        'svc-prism-p':      { cz: 'Pochopte, jak přirozeně fungujete. Vědecky podložené.', en: 'Understand how you naturally function. Science-backed.' },
        'svc-prism-btn':    { cz: 'ObjednatPRISM', en: 'Book PRISM' },
        'svc-gallup-p':     { cz: 'Odhalte, v čem přirozeně vynikáte – a stavějte na tom.', en: 'Discover where you naturally excel – and build on it.' },
        'svc-gallup-btn':   { cz: 'Objednat Gallup', en: 'Book Gallup' },
        'svc-rdl-p':        { cz: 'Roční transformační program. Kompletní kariérní proměna.', en: 'Annual transformation programme. Complete career reinvention.' },
        'svc-rdl-btn':      { cz: 'Zjistit více', en: 'Learn more' },

        /* === SEKCIA – firmy === */
        'corp-h2':          { cz: 'Investujete do rozvoje svých lidí?', en: 'Investing in your people\'s development?' },
        'corp-btn':         { cz: 'Napište mi', en: 'Write to me' },

        /* === SEKCIA – klienti === */
        'ref-h2':           { cz: 'Co říkají klienti', en: 'What clients say' },

        /* === SEKCIA – CTA === */
        'cta-h2':           { cz: 'Jste připraveni na změnu?', en: 'Ready for a change?' },
        'cta-btn':          { cz: 'Rezervovat konzultaci', en: 'Book a consultation' },

        /* === STRÁNKA SLUŽBY === */
        'pg-svc-h1':        { cz: 'Služby', en: 'Services' },
        'pg-svc-prolog':    { cz: 'Promluvíme si – a společně přijdeme na to, co dává smysl.', en: 'We will talk – and together figure out what makes sense.' },

        /* === KOUČOVANIE === */
        'kou-h1':           { cz: '1:1 Individuální koučování', en: '1:1 Individual coaching' },
        'kou-for-h3':       { cz: 'Pro koho je koučování?', en: 'Who is coaching for?' },
        'kou-help-h2':      { cz: 'S čím vám pomůžu', en: 'How I can help you' },
        'kou-a1-h4':        { cz: 'Kariérní rozhodování', en: 'Career decisions' },
        'kou-a1-p':         { cz: 'Pomůžu vám projít rozhodnutím strukturovaně – co je pro vás důležité, jaká jsou rizika, co vám sedí dlouhodobě.', en: 'I will guide you through decisions in a structured way – what matters to you, what the risks are, and what suits you long-term.' },
        'kou-a2-h4':        { cz: 'Leadership & vedení lidí', en: 'Leadership & people management' },
        'kou-a2-p':         { cz: 'Přechod do leadership role, obtížné konverzace, delegování a práce s týmem.', en: 'Transitioning into a leadership role, difficult conversations, delegation and teamwork.' },
        'kou-a3-h4':        { cz: 'Work-life balance', en: 'Work-life balance' },
        'kou-a3-p':         { cz: 'Nastavení hranic, priority, zvládání stresu, prevence vyhoření a hledání rovnováhy.', en: 'Setting boundaries, priorities, managing stress, preventing burnout and finding balance.' },
        'kou-a4-h4':        { cz: 'Midlife & nový směr', en: 'Midlife & new direction' },
        'kou-a4-p':         { cz: 'Pomůžu vám najít nový směr – bez zbytečné paniky, s jasnou hlavou a konkrétním plánem.', en: 'I will help you find a new direction – without unnecessary panic, with a clear head and a concrete plan.' },
        'kou-a5-h4':        { cz: 'Kariéra v éře AI', en: 'Career in the AI era' },
        'kou-a5-p':         { cz: 'Zmapujeme vaše unikátní silné stránky, které AI nahradit nemůže. Najdeme, kde budete relevantní.', en: 'We will map your unique strengths that AI cannot replace. We will find where you will stay relevant.' },
        'kou-a6-h4':        { cz: 'Sebedůvěra & rozvoj', en: 'Self-confidence & development' },
        'kou-a6-p':         { cz: 'Práce s vnitřními bloky, přesvědčeními a strachem. Koučování, které vás posune vpřed.', en: 'Working with inner blocks, beliefs and fears. Coaching that moves you forward.' },
        'kou-how-h2':       { cz: 'Jak to probíhá', en: 'How it works' },
        'kou-s1-h4':        { cz: 'Úvodní konzultace (zdarma)', en: 'Introductory consultation (free)' },
        'kou-s1-p':         { cz: '30 minut, kde probereme vaši situaci a zjistíme, jestli a jak vám můžu pomoct. Bez závazků.', en: '30 minutes to discuss your situation and find out if and how I can help. No commitment.' },
        'kou-s2-h4':        { cz: 'Pravidelná sezení', en: 'Regular sessions' },
        'kou-s2-p':         { cz: '60minutové sezení přibližně jednou za 3–4 týdny. Online nebo osobně v Brně. Celkem 6–12 sezení.', en: '60-minute session approximately every 3–4 weeks. Online or in person in Brno. 6–12 sessions in total.' },
        'kou-s3-h4':        { cz: 'Podpora mezi sezeními', en: 'Support between sessions' },
        'kou-s3-p':         { cz: 'Zdroje, reflexe a podpora emailem – protože život se neodehrává jen v koučovací místnosti.', en: 'Resources, reflection and email support – because life does not only happen in the coaching room.' },
        'kou-btn':          { cz: 'Chci bezplatnou konzultaci', en: 'Book a free consultation' },

        /* === PRISM === */
        'prism-h1':         { cz: 'PRISMBrain Mapping', en: 'PRISM Brain Mapping' },
        'prism-h3':         { cz: 'Proč děláte to, co děláte?', en: 'Why do you do what you do?' },
        'prism-intro':      { cz: 'Pochopte, jak váš mozek přirozeně funguje – a proč se chováte tak, jak se chováte.', en: 'Understand how your brain naturally works – and why you behave the way you do.' },
        'prism-p1':         { cz: 'Každý z nás má přirozené vzorce chování – způsoby, jak myslíme, komunikujeme, reagujeme na stres. Většinou o nich ani nevíme. A právě tam vznikají třecí plochy – s kolegy, s rolí, se sebou samým.', en: 'Each of us has natural behavioural patterns – the ways we think, communicate and respond to stress. We are mostly unaware of them. And that is exactly where friction arises – with colleagues, with our role, with ourselves.' },
        'prism-what-h2':    { cz: 'Co PRISM měří', en: 'What PRISM measures' },
        'prism-b1-h4':      { cz: 'Produktivita & sebeřízení', en: 'Productivity & self-management' },
        'prism-b2-h4':      { cz: 'Komunikace & vztahy', en: 'Communication & relationships' },
        'prism-b3-h4':      { cz: 'Emoční inteligence', en: 'Emotional intelligence' },
        'prism-b4-h4':      { cz: 'Stres & výkon', en: 'Stress & performance' },
        'prism-b5-h4':      { cz: 'Leadership potenciál', en: 'Leadership potential' },
        'prism-b6-h4':      { cz: 'Kariéra & pracovní prostředí', en: 'Career & work environment' },
        'prism-how-h2':     { cz: 'Jak to celé probíhá', en: 'How it all works' },
        'prism-s1-h4':      { cz: 'Online dotazník', en: 'Online questionnaire' },
        'prism-s1-p':       { cz: 'Vyplníte PRISM dotazník z pohodlí domova. Cca 30–45 minut. Mapuje, jak fungujete přirozeně i pod tlakem.', en: 'You complete the PRISM questionnaire from the comfort of your home. About 30–45 minutes. It maps how you function naturally and under pressure.' },
        'prism-s2-h4':      { cz: 'Rozvojová konzultace', en: 'Development consultation' },
        'prism-s2-p':       { cz: 'Na 90minutové konzultaci prozkoumáme výsledky: komunikaci, spolupráci, výkon, stres a energii.', en: 'In a 90-minute consultation we explore the results: communication, collaboration, performance, stress and energy.' },
        'prism-s3-h4':      { cz: 'Volitelné koučování', en: 'Optional coaching' },
        'prism-s3-p':       { cz: 'Můžeme pokračovat koučovacím programem zaměřeným na oblasti, kde chcete růst.', en: 'We can continue with a coaching programme focused on areas where you want to grow.' },
        'prism-btn':        { cz: 'ObjednatPRISM', en: 'Book PRISM' },

        /* === GALLUP === */
        'gallup-h1':        { cz: 'Gallup CliftonStrengths', en: 'Gallup CliftonStrengths' },
        'gallup-h3':        { cz: 'Proč je lepší rozvíjet silné stránky než opravovat slabiny?', en: 'Why is it better to develop strengths than fix weaknesses?' },
        'gallup-p1':        { cz: 'Po 40 letech výzkumů – nástroj, který odhalí, v čem přirozeně vynikáte a kde máte největší potenciál.', en: 'After 40 years of research – a tool that reveals where you naturally excel and where your greatest potential lies.' },
        'gallup-how-h2':    { cz: 'Jak to probíhá', en: 'How it works' },
        'gallup-s1-h4':     { cz: 'Online test', en: 'Online test' },
        'gallup-s1-p':      { cz: 'Vyplníte Gallup CliftonStrengths test. Cca 30–45 minut. Zcela online z pohodlí domova.', en: 'You complete the Gallup CliftonStrengths test. About 30–45 minutes. Fully online from home.' },
        'gallup-s2-h4':     { cz: 'Konzultace nad výsledky', en: 'Results consultation' },
        'gallup-s2-p':      { cz: 'Společně prozkoumáme, co vaše talenty znamenají v praxi a jak je využít v kariéře.', en: 'Together we explore what your talents mean in practice and how to use them in your career.' },
        'gallup-s3-h4':     { cz: 'Kariérní doporučení', en: 'Career recommendations' },
        'gallup-s3-p':      { cz: 'Dostanete konkrétní tipy, jaké role a prostředí vám sedí a kde budete přirozeně úspěšní.', en: 'You will receive specific tips on which roles and environments suit you and where you will naturally succeed.' },
        'gallup-var-h2':    { cz: 'Varianty konzultace', en: 'Consultation options' },
        'gallup-v1-h4':     { cz: 'Top 5 talentů', en: 'Top 5 talents' },
        'gallup-v1-p':      { cz: 'Základní verze pro ty, kdo chtějí rychlý přehled svých 5 nejsilnějších talentů. 60minutová konzultace.', en: 'Basic version for those who want a quick overview of their 5 strongest talents. 60-minute consultation.' },
        'gallup-v2-h4':     { cz: 'Všech 34 talentů', en: 'All 34 talents' },
        'gallup-v2-p':      { cz: 'Kompletní profil s kariérními doporučeními. 90minutová konzultace, hlubší analýza a akční plán.', en: 'Complete profile with career recommendations. 90-minute consultation, deeper analysis and action plan.' },
        'gallup-v3-h4':     { cz: 'Gallup + koučování', en: 'Gallup + coaching' },
        'gallup-v3-p':      { cz: 'Diagnostika a 3 koučovací sezení pro uvedení talentů do praxe. Pro maximální dopad.', en: 'Assessment and 3 coaching sessions to put your talents into practice. For maximum impact.' },
        'gallup-btn':       { cz: 'Objednat Gallup', en: 'Book Gallup' },

        /* === REDESIGN YOUR LIFE === */
        'rdl-h1':           { cz: 'Redesign Your Life', en: 'Redesign Your Life' },
        'rdl-h3':           { cz: 'Pro koho je tento program?', en: 'Who is this programme for?' },
        'rdl-intro':        { cz: 'Kompletní kariérní proměna za 12 měsíců – s diagnostikou, AI job craftingem a osobním koučováním.', en: 'Complete career reinvention in 12 months – with assessment, AI job crafting and personal coaching.' },
        'rdl-phases-h2':    { cz: '12 měsíců, 4 fáze', en: '12 months, 4 phases' },
        'rdl-p1-h4':        { cz: 'Diagnostika (měsíce 1–2)', en: 'Assessment (months 1–2)' },
        'rdl-p1-p':         { cz: 'PRISM Brain Mapping + Gallup CliftonStrengths. Hluboké pochopení toho, kdo jste, jak fungujete a kde budete nejúspěšnější.', en: 'PRISM Brain Mapping + Gallup CliftonStrengths. Deep understanding of who you are, how you work and where you will be most successful.' },
        'rdl-p2-h4':        { cz: 'Kariérní strategie (měsíce 3–5)', en: 'Career strategy (months 3–5)' },
        'rdl-p2-p':         { cz: 'Mapování kariérních možností, AI job crafting, identifikace rolí a prostředí, kde budete záříte. Vytvoříme váš kariérní kompas.', en: 'Mapping career options, AI job crafting, identifying roles and environments where you will shine. We will create your career compass.' },
        'rdl-p3-h4':        { cz: 'Akční fáze (měsíce 6–10)', en: 'Action phase (months 6–10)' },
        'rdl-p3-p':         { cz: 'Implementace plánu. Pravidelné koučovací sezení, podpora při konkrétních krocích, networking, příprava CV a pohovorů.', en: 'Plan implementation. Regular coaching sessions, support with concrete steps, networking, CV and interview preparation.' },
        'rdl-p4-h4':        { cz: 'Konsolidace (měsíce 11–12)', en: 'Consolidation (months 11–12)' },
        'rdl-p4-p':         { cz: 'Usazení v nové kariéře, integrace nových zvyklostí, příprava na dlouhodobý rozvoj a plán dalšího růstu.', en: 'Settling into your new career, integrating new habits, preparing for long-term development and a plan for further growth.' },
        'rdl-btn':          { cz: 'Zjistit více', en: 'Learn more' },

        /* === O MNE === */
        'about-h1':         { cz: 'Katka Hrouzková', en: 'Katka Hrouzková' },
        'about-h2':         { cz: 'Pojďme se poznat', en: 'Let\'s get to know each other' },
        'about-p1':         { cz: 'Koučka a konzultantka se zázemím v HR. Pracuji s lidmi, kteří hledají větší soulad – se sebou, se svou prací, se svým životem.', en: 'Coach and consultant with a background in HR. I work with people seeking greater alignment – with themselves, their work and their life.' },
        'about-cred':       { cz: 'Psychologie · 17 let v globálním HR · PRISM Brain Mapping certifikace · Inpram certifikace (Gallup CliftonStrengths) · Erickson koučink', en: 'Psychology · 17 years in global HR · PRISM Brain Mapping certified · Inpram certified (Gallup CliftonStrengths) · Erickson coaching' },

        /* === KONTAKT === */
        'contact-h1':       { cz: 'Začněme společně', en: 'Let\'s start together' },
        'contact-free-h3':  { cz: '30 minut zdarma', en: '30 minutes free' },
        'contact-free-p':   { cz: 'Úvodní konzultace je bezplatná. Probereme vaši situaci a zjistíme, jestli a jak vám můžu pomoct. Bez závazků.', en: 'The introductory consultation is free. We will discuss your situation and find out if and how I can help. No commitment.' },
        'contact-connect-h3': { cz: 'Spojte se se mnou', en: 'Connect with me' },
        'contact-loc':      { cz: 'Osobně Brno · Online kdekoli', en: 'In person Brno · Online anywhere' },
        'contact-write-h3': { cz: 'Napište mi', en: 'Write to me' },
        'contact-write-p':  { cz: 'Pár vět mi stačí, abych se mohla připravit.', en: 'A few sentences are enough for me to prepare.' },
        'contact-btn':      { cz: 'Odeslat zprávu', en: 'Send message' },
        'contact-reserve-btn': { cz: 'Rezervovat konzultaci', en: 'Book a consultation' },

        /* === FOOTER === */
        'footer-copy':      { cz: '© 2026 Katka Hrouzková · Koučink & Talentové poradenství', en: '© 2026 Katka Hrouzková · Coaching & Talent Advisory' },
    };

    function setLang(lang) {
        // Prepínač aktívny stav
        document.getElementById('btn-cz').classList.toggle('active', lang === 'cz');
        document.getElementById('btn-en').classList.toggle('active', lang === 'en');

        // Prepneme všetky elementy s data-lang-key
        document.querySelectorAll('[data-lang-key]').forEach(function (el) {
            var key = el.getAttribute('data-lang-key');
            if (translations[key] && translations[key][lang]) {
                // Ak element obsahuje HTML (napr. <strong>), použijeme innerHTML
                var val = translations[key][lang];
                if (el.tagName === 'INPUT' || el.tagName === 'TEXTAREA') {
                    el.placeholder = val;
                } else {
                    el.innerHTML = val;
                }
            }
        });

        // Uložíme výber
        try { localStorage.setItem('kh-lang', lang); } catch(e) {}

        // Nastavíme lang atribút na <html>
        document.documentElement.lang = (lang === 'en') ? 'en' : 'cs';
    }

    // Inicializácia po načítaní stránky
    document.addEventListener('DOMContentLoaded', function () {
        var saved = 'cz';
        try { saved = localStorage.getItem('kh-lang') || 'cz'; } catch(e) {}
        setLang(saved);
    });

    // Globálna funkcia
    window.setLang = setLang;
})();
</script>
"""

# Vložíme JS pred </body>
html = html.replace("</body>", LANG_JS + "\n</body>", 1)

# ─────────────────────────────────────────────
# 4. Pridáme data-lang-key atribúty k elementom
# ─────────────────────────────────────────────

# Mapovanie: hľadaný text → kľúč
# Formát: (hľadaný_text, key, použiť_regex)
text_keys = [
    # NAV
    ('Chci bezplatnou konzultaci', 'nav-cta'),
    # HERO
    ('POZNEJTE SE LÉPE.', 'hero-h1-line1'),
    ('pracujte a žijte způsobem, který vám sedí', 'hero-h1-line2'),
    # Tlačidlá
    ('Rezervovat konzultaci', 'contact-reserve-btn'),
    ('Odeslat zprávu', 'contact-btn'),
    ('Objednat Gallup', 'gallup-btn'),
    ('Zjistit více', 'rdl-btn'),
    ('Začněme společně', 'svc-kou-btn'),
    # Footer
    ('© 2026 Katka Hrouzková · Koučink &amp; Talentové poradenství', 'footer-copy'),
    # Headings
    ('Otázky, se kterými přicházejí moji klienti', 'q-h2-1'),
    ('Pokud vás oslovila alespoň jedna otázka, nejste sami.', 'q-h2-2'),
    ('Vyberte si cestu, která vám sedí', 'svc-h2'),
    ('Investujete do rozvoje svých lidí?', 'corp-h2'),
    ('Co říkají klienti', 'ref-h2'),
    ('Jste připraveni na změnu?', 'cta-h2'),
    ('Pojďme se poznat', 'about-h2'),
    ('S čím vám pomůžu', 'kou-help-h2'),
    ('Jak to probíhá', 'kou-how-h2'),
    ('Co PRISM měří', 'prism-what-h2'),
    ('Jak to celé probíhá', 'prism-how-h2'),
    ('Varianty konzultace', 'gallup-var-h2'),
    ('12 měsíců, 4 fáze', 'rdl-phases-h2'),
    ('30 minut zdarma', 'contact-free-h3'),
    ('Spojte se se mnou', 'contact-connect-h3'),
    ('Napište mi', 'contact-write-h3'),
]

def add_lang_key(html, search_text, key):
    """Pridá data-lang-key k prvému elementu obsahujúcemu daný text."""
    # Hľadáme tag obsahujúci text
    pattern = r'(<(?:h[1-4]|p|button|a|span|div)[^>]*?)>((?:[^<]*?)' + re.escape(search_text) + r'(?:[^<]*?))</'
    def replacer(m):
        tag_open = m.group(1)
        content = m.group(2)
        if 'data-lang-key' in tag_open:
            return m.group(0)  # Už má key
        return tag_open + ' data-lang-key="' + key + '">' + content + '</'
    new_html, count = re.subn(pattern, replacer, html, count=1)
    return new_html

for search_text, key in text_keys:
    html = add_lang_key(html, search_text, key)

# ─────────────────────────────────────────────
# 5. Uložíme výsledok
# ─────────────────────────────────────────────
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(html)

print("✅ Hotovo! index.html bol aktualizovaný.")
print("   - Pridaný CZ/EN prepínač do navigácie")
print("   - Pridaný JavaScript pre prepínanie jazykov")
print("   - Pridané data-lang-key atribúty k hlavným textom")
print()
print("Nahraj index.html na GitHub a za 1-2 minúty uvidíš zmeny.")
