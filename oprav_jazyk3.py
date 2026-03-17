#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

INPUT_FILE = "index.html"
OUTPUT_FILE = "index.html"

with open(INPUT_FILE, encoding="utf-8") as f:
    html = f.read()

NEW_SETLANG = """    function setLang(lang) {
        document.getElementById('btn-cz').classList.toggle('active', lang === 'cz');
        document.getElementById('btn-en').classList.toggle('active', lang === 'en');

        var t = {
            'nav-cta':             { cz: 'Chci bezplatnou konzultaci', en: 'Book a free consultation' },
            'q-h2-1':              { cz: 'Otázky, se kterými přicházejí moji klienti', en: 'Questions my clients bring' },
            'q-h2-2':              { cz: 'Pokud vás oslovila alespoň jedna otázka, nejste sami.', en: 'If at least one of these resonates, you are not alone.' },
            'svc-h2':              { cz: 'Vyberte si cestu, která vám sedí', en: 'Choose the path that suits you' },
            'corp-h2':             { cz: 'Investujete do rozvoje svých lidí?', en: 'Investing in your people\\'s development?' },
            'contact-write-h3':    { cz: 'Napište mi', en: 'Write to me' },
            'ref-h2':              { cz: 'Co říkají klienti', en: 'What clients say' },
            'cta-h2':              { cz: 'Jste připraveni na změnu?', en: 'Ready for a change?' },
            'svc-kou-btn':         { cz: 'Začněme společně', en: 'Let\\'s start together' },
            'kou-help-h2':         { cz: 'S čím vám pomůžu', en: 'How I can help you' },
            'kou-how-h2':          { cz: 'Jak to probíhá', en: 'How it works' },
            'contact-reserve-btn': { cz: 'Rezervovat konzultaci', en: 'Book a consultation' },
            'prism-how-h2':        { cz: 'Jak to celé probíhá', en: 'How it all works' },
            'gallup-btn':          { cz: 'Objednat Gallup', en: 'Book Gallup' },
            'gallup-var-h2':       { cz: 'Varianty konzultace', en: 'Consultation options' },
            'rdl-phases-h2':       { cz: '12 měsíců, 4 fáze', en: '12 months, 4 phases' },
            'rdl-btn':             { cz: 'Zjistit více', en: 'Learn more' },
            'about-h2':            { cz: 'Pojďme se poznat', en: 'Let\\'s get to know each other' },
            'contact-free-h3':     { cz: '30 minut zdarma', en: '30 minutes free' },
            'contact-connect-h3':  { cz: 'Spojte se se mnou', en: 'Connect with me' },
            'contact-btn':         { cz: 'Odeslat zprávu', en: 'Send message' },
            'footer-copy':         { cz: '© 2026 Katka Hrouzková · Koučink &amp; Talentové poradenství', en: '© 2026 Katka Hrouzková · Coaching &amp; Talent Advisory' },
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

        var navTexts = {
            cz: { 'nav-home': 'Domů', 'nav-o-mne': 'O mně', 'nav-kontakt': 'Kontakt' },
            en: { 'nav-home': 'Home', 'nav-o-mne': 'About me', 'nav-kontakt': 'Contact' }
        };
        ['nav-home','nav-o-mne','nav-kontakt'].forEach(function(id) {
            var el = document.getElementById(id);
            if (el) el.textContent = navTexts[lang][id];
        });

        var dt = document.querySelector('.dropdown-toggle');
        if (dt) dt.innerHTML = (lang === 'en') ? 'Services ↓' : 'Služby ↓';

        var dmis = document.querySelectorAll('.dmi');
        var dmiTexts = {
            cz: [
                { h: '1:1 Koučování', p: 'Pravidelná podpora při rozhodování a kariérních změnách.' },
                { h: '<em>PRISM</em> Brain Mapping', p: 'Pochopte, jak přirozeně fungujete. Vědecky podložené.' },
                { h: 'Gallup CliftonStrengths', p: 'Odhalte, v čem přirozeně vynikáte – a stavějte na tom.' },
                { h: 'Redesign Your Life', p: 'Roční transformační program. Kompletní kariérní proměna.' }
            ],
            en: [
                { h: '1:1 Coaching', p: 'Regular support for decision-making and career transitions.' },
                { h: '<em>PRISM</em> Brain Mapping', p: 'Understand how you naturally function. Science-backed.' },
                { h: 'Gallup CliftonStrengths', p: 'Discover where you naturally excel – and build on it.' },
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

        var heroH1 = document.querySelector('.hero h1');
        if (heroH1) {
            heroH1.innerHTML = (lang === 'en')
                ? 'KNOW YOURSELF BETTER.<br><em>work and live in a way that suits you</em>'
                : 'POZNEJTE SE LÉPE.<br><em>pracujte a žijte způsobem, který vám sedí</em>';
        }

        var heroSub = document.querySelector('.hero-sub');
        if (heroSub) {
            heroSub.textContent = (lang === 'en')
                ? 'I will help you understand yourself better – whether you are navigating a career change, workplace relationships, your own way of working, or simply looking for what comes next.'
                : 'Pomůžu vám lépe porozumět sobě – ať řešíte kariéru, vztahy v práci, vlastní způsob fungování, nebo prostě hledáte, co dál.';
        }

        var heroEyebrow = document.querySelector('.hero-eyebrow');
        if (heroEyebrow) {
            heroEyebrow.textContent = (lang === 'en') ? 'Coaching & Talent Advisory' : 'Koučink & Talentové poradenství';
        }

        var heroCreds = document.querySelector('.hero-creds');
        if (heroCreds) {
            heroCreds.innerHTML = (lang === 'en')
                ? 'Psychology · 17 years in global HR · <em>PRISM</em> Brain Mapping certified · Inpram certified (Gallup CliftonStrengths) · Erickson coaching'
                : 'Psychologie · 17 let v globálním HR · <em>PRISM</em> Brain Mapping certifikace · Inpram certifikace (Gallup CliftonStrengths) · Erickson koučink';
        }

        var pqs = document.querySelectorAll('.pain-q');
        var pqTexts = {
            cz: [
                'Dělám práci, která dává smysl – ale přesto jsem vyčerpaný/á. Proč?',
                'Mám vzdělání i zkušenosti, ale nevím, kam dál.',
                'Nevím, v čem jsem dobrý/á. Jak zjistím své silné stránky?',
                'Je mi 40+ a ptám se, jestli tohle chci až do důchodu.',
                'Chci se posunout, ale nevím jak. Co je ten správný krok?',
                'Práce mě dřív bavila – teď už ne. Jak najít smysl tam, kde jsem?',
                'Jsem nový manažer a nevím, jak vést tým po svém.',
                'Firma mi dala budget na rozvoj – chci ho využít smysluplně.'
            ],
            en: [
                'I do meaningful work – yet I feel exhausted. Why?',
                'I have the education and experience, but I don\\'t know where to go next.',
                'I don\\'t know what I\\'m good at. How do I find my strengths?',
                'I\\'m 40+ and wondering if this is really what I want until retirement.',
                'I want to move forward, but I don\\'t know how. What\\'s the right step?',
                'Work used to excite me – not anymore. How do I find meaning where I am?',
                'I\\'m a new manager and don\\'t know how to lead a team in my own way.',
                'My company gave me a development budget – I want to use it meaningfully.'
            ]
        };
        pqs.forEach(function(pq, i) {
            if (pqTexts[lang][i]) pq.textContent = pqTexts[lang][i];
        });

        var svcCards = document.querySelectorAll('.services-section .service-card, .services-grid .service-card');
        var svcTexts = {
            cz: [
                { h: '1:1 Koučování', p: 'Pravidelná podpora při rozhodování, kariérních změnách nebo leadership rozvoji.' },
                { h: '<em>PRISM</em> Brain Mapping', p: 'Zjistěte, jak přirozeně fungujete – a proč vám některé věci jdou snadno, jiné stojí zbytečně moc energie.' },
                { h: 'Gallup CliftonStrengths', p: 'Odhalte, v čem přirozeně vynikáte – a stavějte kariéru i život na tom, co vám jde.' },
                { h: 'Redesign Your Life', p: 'Roční program: talentový profil + AI job crafting + koučování. Kompletní proměna.' }
            ],
            en: [
                { h: '1:1 Coaching', p: 'Regular support for decision-making, career transitions or leadership development.' },
                { h: '<em>PRISM</em> Brain Mapping', p: 'Find out how you naturally function – and why some things come easily while others drain your energy.' },
                { h: 'Gallup CliftonStrengths', p: 'Discover where you naturally excel – and build your career and life on what you do best.' },
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

        document.documentElement.lang = (lang === 'en') ? 'en' : 'cs';
        try { localStorage.setItem('kh-lang', lang); } catch(e) {}
    }

    document.addEventListener('DOMContentLoaded', function() {
        var saved = 'cz';
        try { saved = localStorage.getItem('kh-lang') || 'cz'; } catch(e) {}
        setLang(saved);
    });

    window.setLang = setLang;"""

pattern = r'function setLang\(lang\).*?window\.setLang = setLang;'
new_html, count = re.subn(pattern, NEW_SETLANG.strip(), html, flags=re.DOTALL, count=1)

if count == 0:
    print("CHYBA: Nepodarilo sa najst setLang funkciu!")
else:
    print("OK: setLang funkcia nahradena")

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(new_html)

print("Hotovo! Nahraj index.html na GitHub.")
