#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
oprav_jazyk2.py
Opraví CZ/EN prepínač - nahradí setLang funkciu verziou ktorá priamo mení texty
"""

import re

INPUT_FILE = "index.html"
OUTPUT_FILE = "index.html"

with open(INPUT_FILE, encoding="utf-8") as f:
    html = f.read()

# ─────────────────────────────────────────────
# Nová setLang funkcia - priama náhrada textov
# ─────────────────────────────────────────────
NEW_SETLANG = '''    function setLang(lang) {
        document.getElementById('btn-cz').classList.toggle('active', lang === 'cz');
        document.getElementById('btn-en').classList.toggle('active', lang === 'en');

        // Texty podla data-lang-key
        var t = {
            'nav-cta':           { cz: 'Chci bezplatnou konzultaci',    en: 'Book a free consultation' },
            'q-h2-1':            { cz: 'Otázky, se kterými přicházejí moji klienti', en: 'Questions my clients bring' },
            'q-h2-2':            { cz: 'Pokud vás oslovila alespoň jedna otázka, nejste sami.', en: 'If at least one of these resonates, you are not alone.' },
            'svc-h2':            { cz: 'Vyberte si cestu, která vám sedí', en: 'Choose the path that suits you' },
            'corp-h2':           { cz: 'Investujete do rozvoje svých lidí?', en: 'Investing in your people\'s development?' },
            'contact-write-h3':  { cz: 'Napište mi', en: 'Write to me' },
            'ref-h2':            { cz: 'Co říkají klienti', en: 'What clients say' },
            'cta-h2':            { cz: 'Jste připraveni na změnu?', en: 'Ready for a change?' },
            'svc-kou-btn':       { cz: 'Začněme společně', en: 'Let\'s start together' },
            'kou-help-h2':       { cz: 'S čím vám pomůžu', en: 'How I can help you' },
            'kou-how-h2':        { cz: 'Jak to probíhá', en: 'How it works' },
            'contact-reserve-btn': { cz: 'Rezervovat konzultaci', en: 'Book a consultation' },
            'prism-how-h2':      { cz: 'Jak to celé probíhá', en: 'How it all works' },
            'gallup-btn':        { cz: 'Objednat Gallup', en: 'Book Gallup' },
            'gallup-var-h2':     { cz: 'Varianty konzultace', en: 'Consultation options' },
            'rdl-phases-h2':     { cz: '12 měsíců, 4 fáze', en: '12 months, 4 phases' },
            'rdl-btn':           { cz: 'Zjistit více', en: 'Learn more' },
            'about-h2':          { cz: 'Pojďme se poznat', en: 'Let\'s get to know each other' },
            'contact-free-h3':   { cz: '30 minut zdarma', en: '30 minutes free' },
            'contact-connect-h3':{ cz: 'Spojte se se mnou', en: 'Connect with me' },
            'contact-btn':       { cz: 'Odeslat zprávu', en: 'Send message' },
            'footer-copy':       { cz: '\\u00a9 2026 Katka Hrouzkov\\u00e1 \\u00b7 Kou\\u010dink & Talentov\\u00e9 poradenstv\\u00ed', en: '\\u00a9 2026 Katka Hrouzkov\\u00e1 \\u00b7 Coaching & Talent Advisory' },
        };

        document.querySelectorAll('[data-lang-key]').forEach(function(el) {
            var key = el.getAttribute('data-lang-key');
            if (t[key] && t[key][lang]) {
                if (el.tagName === 'INPUT' || el.tagName === 'TEXTAREA') {
                    el.placeholder = t[key][lang];
                } else {
                    el.innerHTML = t[key][lang];
                }
            }
        });

        // Nav polozky podla ID
        var navTexts = {
            cz: { 'nav-home': 'Dom\\u016f', 'nav-o-mne': 'O mn\\u011b', 'nav-kontakt': 'Kontakt' },
            en: { 'nav-home': 'Home', 'nav-o-mne': 'About me', 'nav-kontakt': 'Contact' }
        };
        ['nav-home','nav-o-mne','nav-kontakt'].forEach(function(id) {
            var el = document.getElementById(id);
            if (el) el.textContent = navTexts[lang][id];
        });

        // Dropdown Sluzby/Services
        var dt = document.querySelector('.dropdown-toggle');
        if (dt) dt.innerHTML = (lang === 'en') ? 'Services \\u2193' : 'Slu\\u017eby \\u2193';

        // Dropdown menu polozky
        var dmis = document.querySelectorAll('.dmi');
        var dmiTexts = {
            cz: [
                { h: '1:1 Kou\\u010dov\\u00e1n\\u00ed', p: 'Pravideln\\u00e1 podpora p\\u0159i rozhodov\\u00e1n\\u00ed a kari\\u00e9rn\\u00edch zm\\u011bn\\u00e1ch.' },
                { h: '<em>PRISM</em> Brain Mapping', p: 'Pochopte, jak p\\u0159irozen\\u011b fungujete. V\\u011bdeck\\u00fd podlo\\u017een\\u00e9.' },
                { h: 'Gallup CliftonStrengths', p: 'Odhalte, v \\u010dem p\\u0159irozen\\u011b vy\\u010dn\\u00edv\\u00e1te \\u2013 a stav\\u011bjte na tom.' },
                { h: 'Redesign Your Life', p: 'Ro\\u010dn\\u00ed transforma\\u010dn\\u00ed program. Kompletn\\u00ed kari\\u00e9rn\\u00ed prom\\u011bna.' }
            ],
            en: [
                { h: '1:1 Coaching', p: 'Regular support for decision-making and career transitions.' },
                { h: '<em>PRISM</em> Brain Mapping', p: 'Understand how you naturally function. Science-backed.' },
                { h: 'Gallup CliftonStrengths', p: 'Discover where you naturally excel \\u2013 and build on it.' },
                { h: 'Redesign Your Life', p: 'Annual transformation programme. Complete career reinvention.' }
            ]
        };
        dmis.forEach(function(dmi, i) {
            if (dmiTexts[lang][i]) {
                var h4 = dmi.querySelector('h4');
                var p = dmi.querySelector('p');
                if (h4) h4.innerHTML = dmiTexts[lang][i].h;
                if (p) p.textContent = dmiTexts[lang][i].p;
            }
        });

        // Hero sekcia
        var heroH1 = document.querySelector('.hero h1');
        if (heroH1) {
            heroH1.innerHTML = (lang === 'en')
                ? 'KNOW YOURSELF BETTER.<br><em>work and live in a way that suits you</em>'
                : 'POZNEJTE SE L\\u00c9PE.<br><em>pracujte a \\u017eijte zp\\u016fsobem, kter\\u00fd v\\u00e1m sed\\u00ed</em>';
        }

        var heroSub = document.querySelector('.hero-sub');
        if (heroSub) {
            heroSub.textContent = (lang === 'en')
                ? 'I will help you understand yourself better \\u2013 whether you are navigating a career change, workplace relationships, your own way of working, or simply looking for what comes next.'
                : 'Pom\\u016f\\u017eu v\\u00e1m l\\u00e9pe porozum\\u011bt sob\\u011b \\u2013 a\\u0165 \\u0159e\\u0161\\u00edte kari\\u00e9ru, vztahy v pr\\u00e1ci, vlastn\\u00ed zp\\u016fsob fungov\\u00e1n\\u00ed, nebo prost\\u011b hled\\u00e1te, co d\\u00e1l.';
        }

        var heroEyebrow = document.querySelector('.hero-eyebrow');
        if (heroEyebrow) {
            heroEyebrow.textContent = (lang === 'en')
                ? 'Coaching & Talent Advisory'
                : 'Kou\\u010dink & Talentov\\u00e9 poradenstv\\u00ed';
        }

        var heroCreds = document.querySelector('.hero-creds');
        if (heroCreds) {
            heroCreds.innerHTML = (lang === 'en')
                ? 'Psychology \\u00b7 17 years in global HR \\u00b7 <em>PRISM</em> Brain Mapping certified \\u00b7 Inpram certified (Gallup CliftonStrengths) \\u00b7 Erickson coaching'
                : 'Psychologie \\u00b7 17 let v glob\\u00e1ln\\u00edm HR \\u00b7 <em>PRISM</em> Brain Mapping certifikace \\u00b7 Inpram certifikace (Gallup CliftonStrengths) \\u00b7 Erickson kou\\u010dink';
        }

        // Sekcia otazok (pain-q)
        var pqs = document.querySelectorAll('.pain-q');
        var pqTexts = {
            cz: [
                'D\\u011bl\\u00e1m pr\\u00e1ci, kter\\u00e1 d\\u00e1v\\u00e1 smysl \\u2013 ale p\\u0159esto jsem vy\\u010derpan\\u00fd/\\u00e1. Pro\\u010d?',
                'M\\u00e1m vzd\\u011bl\\u00e1n\\u00ed i zku\\u0161enosti, ale nev\\u00edm, kam d\\u00e1l.',
                'Nev\\u00edm, v \\u010dem jsem dobr\\u00fd/\\u00e1. Jak zji\\u0161t\\u00edm sv\\u00e9 siln\\u00e9 str\\u00e1nky?',
                'Je mi 40+ a pt\\u00e1m se, jestli tohle chci a\\u017e do d\\u016fchodu.',
                'Chci se posunout, ale nev\\u00edm jak. Co je ten spr\\u00e1vn\\u00fd krok?',
                'Pr\\u00e1ce m\\u011b d\\u0159\\u00edv bavila \\u2013 te\\u010f u\\u017e ne. Jak naj\\u00edt smysl tam, kde jsem?',
                'Jsem nov\\u00fd mana\\u017eer a nev\\u00edm, jak v\\u00e9st t\\u00fdm po sv\\u00e9m.',
                'Firma mi dala budget na rozvoj \\u2013 chci ho vyu\\u017e\\u00edt smyslupln\\u011b.'
            ],
            en: [
                'I do meaningful work \\u2013 yet I feel exhausted. Why?',
                'I have the education and experience, but I don\\u2019t know where to go next.',
                'I don\\u2019t know what I\\u2019m good at. How do I find my strengths?',
                'I\\u2019m 40+ and wondering if this is really what I want until retirement.',
                'I want to move forward, but I don\\u2019t know how. What\\u2019s the right step?',
                'Work used to excite me \\u2013 not anymore. How do I find meaning where I am?',
                'I\\u2019m a new manager and don\\u2019t know how to lead a team in my own way.',
                'My company gave me a development budget \\u2013 I want to use it meaningfully.'
            ]
        };
        pqs.forEach(function(pq, i) {
            if (pqTexts[lang][i]) pq.textContent = pqTexts[lang][i];
        });

        // Gain boxy (1,2,3)
        var gainBoxes = document.querySelectorAll('.pain-section ~ section h4, [style*="petrol"] h4');
        var gainTexts = {
            cz: ['Pochop\\u00edte sami sebe', 'Najdeme v\\u00e1\\u0161 sm\\u011br', 'Vytvo\\u0159\\u00edte konkr\\u00e9tn\\u00ed pl\\u00e1n'],
            en: ['You will understand yourself', 'We will find your direction', 'You will create a concrete plan']
        };

        // Service cards na hlavnej stranke
        var svcCards = document.querySelectorAll('.services-section .service-card, .services-grid .service-card');
        var svcTexts = {
            cz: [
                { h: '1:1 Kou\\u010dov\\u00e1n\\u00ed', p: 'Pravideln\\u00e1 podpora p\\u0159i rozhodov\\u00e1n\\u00ed, kari\\u00e9rn\\u00edch zm\\u011bn\\u00e1ch nebo leadership rozvoji.' },
                { h: '<em>PRISM</em> Brain Mapping', p: 'Zji\\u0161t\\u011bte, jak p\\u0159irozen\\u011b fungujete \\u2013 a pro\\u010d v\\u00e1m n\\u011bkter\\u00e9 v\\u011bci jdou snadno, jin\\u00e9 stoj\\u00ed zbyte\\u010dn\\u011b moc energie.' },
                { h: 'Gallup CliftonStrengths', p: 'Odhalte, v \\u010dem p\\u0159irozen\\u011b vy\\u010dn\\u00edv\\u00e1te \\u2013 a stav\\u011bjte kari\\u00e9ru i \\u017eivot na tom, co v\\u00e1m jde.' },
                { h: 'Redesign Your Life', p: 'Ro\\u010dn\\u00ed program: talentov\\u00fd profil + AI job crafting + kou\\u010dov\\u00e1n\\u00ed. Kompletn\\u00ed prom\\u011bna.' }
            ],
            en: [
                { h: '1:1 Coaching', p: 'Regular support for decision-making, career transitions or leadership development.' },
                { h: '<em>PRISM</em> Brain Mapping', p: 'Find out how you naturally function \\u2013 and why some things come easily while others drain your energy.' },
                { h: 'Gallup CliftonStrengths', p: 'Discover where you naturally excel \\u2013 and build your career and life on what you do best.' },
                { h: 'Redesign Your Life', p: 'Annual programme: talent profile + AI job crafting + coaching. Complete transformation.' }
            ]
        };
        svcCards.forEach(function(card, i) {
            if (svcTexts[lang][i]) {
                var h3 = card.querySelector('h3');
                var p = card.querySelector('p');
                if (h3) h3.innerHTML = svcTexts[lang][i].h;
                if (p) p.textContent = svcTexts[lang][i].p;
            }
        });

        // Sluzby stranka - section label
        var svcLabel = document.querySelector('#sluzby-prehled .section-label');
        if (svcLabel) svcLabel.textContent = (lang === 'en') ? 'Services' : 'Nab\\u00eddka';

        var svcH1 = document.querySelector('#sluzby-prehled h1');
        if (svcH1) svcH1.textContent = (lang === 'en') ? 'Services' : 'Slu\\u017eby';

        var svcIntro = document.querySelector('#sluzby-prehled p');
        if (svcIntro) svcIntro.textContent = (lang === 'en')
            ? 'Every person is different \\u2013 that\\u2019s why I offer different paths. From a one-off session to a year-long programme with full support.'
            : 'Ka\\u017ed\\u00fd \\u010dlov\\u011bk je jin\\u00fd \\u2013 proto nab\\u00edzim r\\u016fzn\\u00e9 cesty. Od jednorazov\\u00e9ho setk\\u00e1n\\u00ed a\\u017e po ro\\u010dn\\u00ed program s plnou podporou.';

        // html lang atribut
        document.documentElement.lang = (lang === 'en') ? 'en' : 'cs';

        try { localStorage.setItem('kh-lang', lang); } catch(e) {}
    }

    document.addEventListener('DOMContentLoaded', function() {
        var saved = 'cz';
        try { saved = localStorage.getItem('kh-lang') || 'cz'; } catch(e) {}
        setLang(saved);
    });

    window.setLang = setLang;'''

# Nahradíme starú setLang funkciu
pattern = r'function setLang\(lang\).*?window\.setLang = setLang;'
new_html, count = re.subn(pattern, NEW_SETLANG.strip(), html, flags=re.DOTALL, count=1)

if count == 0:
    print("CHYBA: Nepodarilo sa najst setLang funkciu!")
else:
    print(f"OK: setLang funkcia nahradena ({count}x)")

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(new_html)

print("Hotovo! Nahraj index.html na GitHub.")
print("Prepinac CZ/EN bude prekladat:")
print("  - Navigaciu (Home/Domů, About me/O mně, Contact/Kontakt)")
print("  - Hero sekciu (nadpis, podnadpis, credencials)")
print("  - Otazky klientov")
print("  - Karty sluzieb")
print("  - Vsetky nadpisy sekcii")
print("  - Tlacidla")
