// ── SPA Navigation ──────────────────────────────────────────
  function showPage(id) {
    document.querySelectorAll('.page').forEach(function(p){ p.classList.remove('active'); });
    var page = document.getElementById(id);
    if(page) page.classList.add('active');
    document.querySelectorAll('.nav-link').forEach(function(l){ l.classList.remove('active'); });
    var el = document.getElementById('nav-' + id);
    if(el) el.classList.add('active');
    window.scrollTo(0, 0);
    var nav = document.getElementById('navLinks');
    if(nav) nav.classList.remove('open');
  }

  // Handle deep-link from pro-firmy pages (e.g. ../index.html#o-mne)
  document.addEventListener('DOMContentLoaded', function() {
    var hash = window.location.hash.slice(1);
    if (hash && document.getElementById(hash)) showPage(hash);
  });

  function handleForm(e) {
    e.preventDefault();
    var s = document.getElementById('form-success');
    if(s) s.style.display = 'block';
  }

  function toggleFaq(btn) {
    var item = btn.closest('.faq-item');
    var wasOpen = item.classList.contains('open');
    document.querySelectorAll('.faq-item.open').forEach(function(i) { i.classList.remove('open'); });
    if (!wasOpen) item.classList.add('open');
  }

  function navigateTo(id) {
    // Navigate to page without closing dropdown - dropdown closes naturally when mouse leaves
    showPage(id);
    // Re-open dropdown briefly so transition feels smooth, then let hover handle it
  }

  function toggleDropdown(e) {
    e.stopPropagation();
    var dd = e.target.closest('.dropdown');
    if(dd) dd.classList.toggle('open');
  }

  function toggleMobileMenu() {
    var nav = document.getElementById('navLinks');
    if(nav) nav.classList.toggle('open');
  }

  document.addEventListener('click', function(e) {
    var nav = document.getElementById('navLinks');
    var menu = document.querySelector('.hamburger');
    if(nav && nav.classList.contains('open') && !nav.contains(e.target) && menu && !menu.contains(e.target)) {
      nav.classList.remove('open');
    }
    var dropdowns = document.querySelectorAll('.dropdown.open');
    dropdowns.forEach(function(dd) {
      if(!dd.contains(e.target)) dd.classList.remove('open');
    });
  });

  // Testimonials carousel
  (function() {
    var slides = document.querySelectorAll('#testimonials-carousel .tc-slide');
    var dots   = document.querySelectorAll('#testimonials-carousel .tc-dot');
    if (!slides.length) return;
    var current = 0, timer;
    function tcShow(n) {
      slides[current].classList.remove('tc-active');
      dots[current].classList.remove('tc-dot-active');
      current = (n + slides.length) % slides.length;
      slides[current].classList.add('tc-active');
      dots[current].classList.add('tc-dot-active');
    }
    window.tcMove = function(dir) { clearInterval(timer); tcShow(current + dir); startTimer(); };
    window.tcGoTo = function(n)   { clearInterval(timer); tcShow(n);             startTimer(); };
    function startTimer() { timer = setInterval(function() { tcShow(current + 1); }, 6000); }
    startTimer();
  })();

// ── CZ/EN Translation ──────────────────────────────────────
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
        'hero-sub':         { cz: 'Pomůžu vám lépe porozumět vlastnímu potenciálu. Nespoléhám jen na teorii – propojuji psychologii, poznatky z neurověd a práci s talenty s více než 17 lety praxe v globálním HR a certifikovaným koučinkem.', en: 'I will help you understand yourself better – whether you are navigating a career change, workplace relationships, your own way of working, or simply looking for what comes next.' },
        'hero-cred':        { cz: 'Psychologie · 17 let v globálním HR · PRISM Brain Mapping certifikace · Inpram certifikace (Gallup CliftonStrengths) · Erickson koučink', en: 'Psychology · 17 years in global HR · PRISM Brain Mapping certified · Inpram certified (Gallup CliftonStrengths) · Erickson coaching' },
        'hero-btn':         { cz: 'Chci bezplatnou konzultaci', en: 'Book a free consultation' },

        /* === SEKCIA – otázky klientov === */
        'q-intro':          { cz: '', en: 'These are the questions that open every conversation I have.' },
        'q-h2-1':           { cz: 'Otázky, se kterými přicházejí moji klienti', en: 'Questions my clients bring' },
        'q-h2-2':           { cz: 'Co se stane, když se ozvete', en: 'If at least one of these resonates, you are not alone.' },
        'q-q1':             { cz: '„Dělám správnou práci? Nebo jen tu, co se ode mě čeká?"', en: '"Am I doing the right work? Or just what is expected of me?"' },
        'q-q2':             { cz: '„Chtěl/a bych změnu – ale nevím, co vlastně chci."', en: '"I want a change – but I don\'t know what I actually want."' },
        'q-q3':             { cz: '„Navenek mám vše – ale uvnitř se neptám, jestli mě to naplňuje."', en: '"On the surface I have it all – but inside I wonder if it fulfils me."' },
        'q-q4':             { cz: '„Mám pocit, že dávám do práce víc, než dostávám zpátky."', en: '"I feel like I give more to work than I get back."' },
        'q-q5':             { cz: '„Je mi 40+ a ptám se, jestli tohle opravdu chci až do důchodu."', en: '"I am 40+ and wondering if this is really what I want until retirement."' },
        'q-q6':             { cz: '"AI mění moje odvětví. Co teď se sebou?"', en: '"AI is changing my industry. What do I do now?"' },

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
        'svc-rdl-p':        { cz: 'Dlouhodobý program. Kompletní kariérní proměna.', en: 'Annual transformation programme. Complete career reinvention.' },
        'svc-rdl-btn':      { cz: 'Zjistit více', en: 'Learn more' },

        /* === SEKCIA – firmy === */
        'corp-h2':          { cz: 'Investujete do rozvoje svých lidí?', en: 'Investing in your people\'s development?' },
        'corp-btn':         { cz: 'Napište mi', en: 'Write to me' },

        /* === SEKCIA – klienti === */
        'ref-h2':           { cz: 'Co říkají klienti', en: 'What clients say' },

        /* === SEKCIA – CTA === */
        'cta-h2':           { cz: 'Jste připraveni na změnu?', en: 'Ready for a change?' },
        'cta-p':            { cz: 'Napište mi a probereme, jak vám můžu pomoct', en: 'Write to me and we will discuss how I can help you' },
        'cta-btn':          { cz: 'Rezervovat konzultaci', en: 'Book a consultation' },

        /* === STRÁNKA PRO JEDNOTLIVCE === */
        'pg-svc-h1':        { cz: 'Služby', en: 'Services' },
        'pg-svc-prolog':    { cz: 'Promluvíme si – a společně přijdeme na to, co dává smysl.', en: 'We will talk – and together figure out what makes sense.' },

        /* === KOUČOVANIE === */
        'kou-h1':           { cz: '1:1 Individuální koučování', en: '1:1 Individual coaching' },
        'kou-for-h3':       { cz: 'Pro koho je koučování?', en: 'Who is coaching for?' },
        'kou-help-h2':      { cz: 'S čím vám pomůžu', en: 'How I can help you' },
        'kou-a1-h4':        { cz: 'Kariérní rozhodování', en: 'Career decisions' },
        'kou-a1-p':         { cz: 'Pomůžu vám projít rozhodnutím strukturovaně – zjistíme, co je pro vás důležité, jaká jsou rizika a co vám sedí dlouhodobě.', en: 'I will guide you through decisions in a structured way – what matters to you, what the risks are, and what suits you long-term.' },
        'kou-a2-h4':        { cz: 'Leadership & vedení lidí', en: 'Leadership & people management' },
        'kou-a2-p':         { cz: 'Zvládnete přechod do role lídra, obtížné konverzace, delegování i každodenní práci s týmem.', en: 'Transitioning into a leadership role, difficult conversations, delegation and teamwork.' },
        'kou-a3-h4':        { cz: 'Work-life balance', en: 'Work-life balance' },
        'kou-a3-p':         { cz: 'Nastavíme zdravé hranice a priority. Naučíte se lépe zvládat stres, předcházet vyhoření a najít ztracenou rovnováhu.', en: 'Setting boundaries, priorities, managing stress, preventing burnout and finding balance.' },
        'kou-a4-h4':        { cz: 'Midlife & nový směr', en: 'Midlife & new direction' },
        'kou-a4-p':         { cz: 'Pomůžu vám najít nový směr – bez zbytečné paniky, s jasnou hlavou a konkrétním plánem.', en: 'I will help you find a new direction – without unnecessary panic, with a clear head and a concrete plan.' },
        'kou-a5-h4':        { cz: 'Kariéra v éře AI', en: 'Career in the AI era' },
        'kou-a5-p':         { cz: 'Zmapujeme vaše unikátní silné stránky, které AI nahradit nemůže. Zjistíme, jak zůstat na trhu relevantní.', en: 'We will map your unique strengths that AI cannot replace. We will find where you will stay relevant.' },
        'kou-a6-h4':        { cz: 'Sebedůvěra & rozvoj', en: 'Self-confidence & development' },
        'kou-a6-p':         { cz: 'Popracujeme na vnitřních blocích, přesvědčeními a strachu. Získáte koučink, který vás skutečně posune vpřed.', en: 'Working with inner blocks, beliefs and fears. Coaching that moves you forward.' },
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
        'gallup-btn':       { cz: 'Zjistěte více', en: 'Learn more about Gallup' },

        /* === REDESIGN YOUR LIFE === */
        'rdl-h1':           { cz: 'Redesign Your Life', en: 'Redesign Your Life' },
        'rdl-h3':           { cz: 'Pro koho je tento program?', en: 'Who is this programme for?' },
        'rdl-intro':        { cz: 'Komplexní kariérní proměna ve vašem tempu – podložená ověřenými nástroji, AI job craftingem a osobním koučováním.', en: 'Complete career reinvention in 12 months – with assessment, AI job crafting and personal coaching.' },
        'rdl-phases-h2':    { cz: '4 fáze programu', en: '12 months, 4 phases' },
        'rdl-p1-h4':        { cz: 'Diagnostika', en: 'Assessment (months 1–2)' },
        'rdl-p1-p':         { cz: 'PRISM Brain Mapping + Gallup CliftonStrengths. Hluboké pochopení toho, kdo jste, jak fungujete a kde budete nejúspěšnější.', en: 'PRISM Brain Mapping + Gallup CliftonStrengths. Deep understanding of who you are, how you work and where you will be most successful.' },
        'rdl-p2-h4':        { cz: 'Kariérní strategie', en: 'Career strategy (months 3–5)' },
        'rdl-p2-p':         { cz: 'Mapování kariérních možností, AI job crafting, identifikace rolí, které vám sedí. Vytvoříme váš kariérní kompas.', en: 'Mapping career options, AI job crafting, identifying roles and environments where you will shine. We will create your career compass.' },
        'rdl-p3-h4':        { cz: 'Akční fáze', en: 'Action phase (months 6–10)' },
        'rdl-p3-p':         { cz: 'Implementace plánu. Pravidelné koučovací sezení, podpora při konkrétních krocích, networking, příprava CV a pohovorů.', en: 'Plan implementation. Regular coaching sessions, support with concrete steps, networking, CV and interview preparation.' },
        'rdl-p4-h4':        { cz: 'Konsolidace', en: 'Consolidation (months 11–12)' },
        'rdl-p4-p':         { cz: 'Usazení v nové kariéře, integrace nových zvyklostí, příprava na dlouhodobý rozvoj a plán dalšího růstu.', en: 'Settling into your new career, integrating new habits, preparing for long-term development and a plan for further growth.' },
        'rdl-btn':          { cz: 'Zjistit více', en: 'Learn more' },

        /* === O MNE === */
        'about-h1':         { cz: 'Katka Hrouzková', en: 'Katka Hrouzková' },
        'about-h2':         { cz: 'Pojďme se poznat', en: 'Let\'s get to know each other' },
        'about-cta-p':      { cz: 'Pokud vás můj příběh oslovil – pojďme si popovídat. První hovor je zdarma a nezávazný.', en: 'If my story resonated with you – let\'s have a chat. The first call is free and non-binding.' },
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
        'contact-reserve-btn': { cz: 'Rezervovat úvodní setkání zdarma', en: 'Book a free intro session' },

        /* === FOOTER === */
        'footer-copy':      { cz: '© 2026 Katka Hrouzková · KOUČINK & TALENTOVÉ PORADENSTVÍ', en: '© 2026 Katka Hrouzková · Coaching & Talent Advisory' },
    };

        function setLang(lang) {
        document.getElementById('btn-cz').classList.toggle('active', lang === 'cz');
        document.getElementById('btn-en').classList.toggle('active', lang === 'en');
        var t=translations;
        document.querySelectorAll('[data-lang-key]').forEach(function(el){var k=el.getAttribute('data-lang-key');if(t[k]&&t[k][lang])el.innerHTML=t[k][lang];});
        var n={cz:{'nav-home':'Domů','nav-o-mne':'O mně','nav-faq':'FAQ<span style="text-transform:none">s</span>','nav-kontakt':'Kontakt'},en:{'nav-home':'Home','nav-o-mne':'About me','nav-faq':'FAQ<span style="text-transform:none">s</span>','nav-kontakt':'Contact'}};
        ['nav-home','nav-o-mne','nav-faq','nav-kontakt'].forEach(function(id){var el=document.getElementById(id);if(el)el.innerHTML=n[lang][id];});
        var dt=document.querySelector('.dropdown-toggle');if(dt)dt.innerHTML=(lang==='en')?'Services':'Služby';
        var h1=document.querySelector('.hero h1');if(h1)h1.innerHTML=(lang==='en')?'KNOW YOURSELF BETTER.<br><em>work and live in a way that suits you</em>':'POZNEJTE SE LÉPE.<br><em>pracujte a žijte způsobem, který vám sedí</em>';
        var hs=document.querySelector('.hero-sub');if(hs)hs.textContent=(lang==='en')?'I will help you understand yourself better – whether you are navigating a career change, workplace relationships, or simply looking for what comes next.':'Pomůžu vám lépe porozumět vlastnímu potenciálu. Nespoléhám jen na teorii – propojuji psychologii, poznatky z neurověd a práci s talenty s více než 17 lety praxe v globálním HR a certifikovaným koučinkem.';
        document.documentElement.lang=(lang==='en')?'en':'cs';
        try{localStorage.setItem('kh-lang',lang);}catch(e){}
    }
    window.setLang=setLang;
    document.addEventListener('DOMContentLoaded',function(){var s='cz';try{s=localStorage.getItem('kh-lang')||'cz';}catch(e){}setLang(s);});
})();

// ── Scroll Animations ──────────────────────────────────────
document.addEventListener('DOMContentLoaded', function() {
    var io = new IntersectionObserver(function(entries) {
        entries.forEach(function(e) {
            if (e.isIntersecting) { e.target.classList.add('anim-in'); io.unobserve(e.target); }
        });
    }, { threshold: 0.2 });
    var ioQuote = new IntersectionObserver(function(entries) {
        entries.forEach(function(e) {
            if (e.isIntersecting) { e.target.classList.add('anim-in'); ioQuote.unobserve(e.target); }
        });
    }, { threshold: 0.5 });

    function animatePage(page) {
        if (!page) return;
        page.querySelectorAll('.anim-top,.anim-left,.anim-right,.anim-top-scroll,.pa-from-left,.pa-from-right,.pa-from-top,.pa-from-bottom,.pa-visible').forEach(function(el) {
            el.classList.remove('anim-top','anim-left','anim-right','anim-top-scroll','anim-in','pa-from-left','pa-from-right','pa-from-top','pa-from-bottom','pa-visible');
            el.style.transitionDelay = '';
            el.style.animationDelay = '';
        });
        var h1 = page.querySelector('.hero h1, .svc-hero-content h1, .page-header h1');
        if (h1) { void h1.offsetWidth; h1.classList.add('anim-top'); }
        var h2s = Array.from(page.querySelectorAll('.section-title'));
        if (h2s[0]) { h2s[0].classList.add('anim-left');  io.observe(h2s[0]); }
        if (h2s[1]) { h2s[1].classList.add('anim-right'); io.observe(h2s[1]); }
        var quote = page.querySelector('#kh-quote');
        if (quote && !quote.classList.contains('anim-quote')) { quote.classList.add('anim-quote'); ioQuote.observe(quote); }
        // Helper: reset + animate a list of {el, cls, delay} on page switch
        function pageAnim(items) {
            var PA = ['pa-from-left','pa-from-right','pa-from-top','pa-from-bottom','pa-visible'];
            items.forEach(function(t) {
                if (!t.el) return;
                t.el.classList.remove.apply(t.el.classList, PA);
                void t.el.offsetWidth;          // force reflow so transition triggers
                t.el.classList.add(t.cls);
                setTimeout(function() { t.el.classList.add('pa-visible'); }, 60 + (t.delay || 0));
            });
        }
        // FAQ – fadeInDown for page header, IO stagger for accordion items
        if (page.id === 'faq') {
            // h1 animates via general anim-top rule; section-label and perex are static
            var ioFaq = new IntersectionObserver(function(entries) {
                entries.forEach(function(e) {
                    if (e.isIntersecting) { e.target.classList.add('faq-visible'); ioFaq.unobserve(e.target); }
                });
            }, { threshold: 0.08 });
            page.querySelectorAll('.faq-item').forEach(function(el, i) {
                el.classList.remove('faq-visible', 'faq-anim');
                el.style.transitionDelay = '';
                void el.offsetWidth;
                el.classList.add('faq-anim');
                el.style.transitionDelay = (i * 0.1) + 's';
                ioFaq.observe(el);
            });
        }
    }

    animatePage(document.querySelector('.page.active'));
    document.querySelectorAll('.page').forEach(function(page) {
        new MutationObserver(function(muts) {
            muts.forEach(function(m) {
                if (m.attributeName === 'class' && page.classList.contains('active')) animatePage(page);
            });
        }).observe(page, { attributes: true });
    });
});
