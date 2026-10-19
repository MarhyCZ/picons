# Contributing to Marhy's Picons

Děkujeme za zájem o rozšíření a vylepšení balíčku piconů! Aby si celá sada udržela vysokou vizuální úroveň a 100% kompatibilitu s klientskými přehrávači (Tvheadend, Kodi, Apple TV TvhClient, Enigma2), dodržujte prosím následující pravidla.

---

## 🎨 Pravidla Designu

1. **Čtvercový formát (1:1):**
   * Každý picon musí být dodán ve dvou přesných rozlišeních:
     * `640/` ➔ **640×640 px** (pro standardní 1080p obrazovky a Kodi)
     * `1024/` ➔ **1024×1024 px** (pro 4K obrazovky a Apple Retina)
   * Formát: **8-bit RGBA PNG** bez průhledného pozadí (pozadí dlaždice je plně neprůhledné).

2. **Barevná paleta a kontrast:**
   * Pozadí dlaždice tvoří primární, sytá barva značky televizní/rozhlasové stanice (případně její oficiální barevný gradient).
   * Logo je čistě bílé (`#ffffff`), vycentrované vodorovně i svisle.
   * Maximální šířka loga je cílena na **65 % až 70 %** šířky canvasu (cca 448 px u 640px verze).

3. **Pojmenování souborů:**
   * Používá se standard **Service Name Picons (SNP)**.
   * Název souboru je malými písmeny bez mezer a diakritiky: např. `ct1hdt2.png`, `warnertv.png`, `seznamcztv.png`.
   * Všechny varianty a aliasy názvů (např. `test4.png` ➔ `warnertv.png`) definujte v souboru [`source/hardlinks.sh`](source/hardlinks.sh).

---

## 🚀 Jak přidat novou stanici

1. Forkněte si tento repozitář a naklonujte jej lokálně:
   ```bash
   git clone https://github.com/onhala/picons.git
   cd picons
   ```

2. Připravte transparentní podklad (SVG nebo PNG s vysokým rozlišením).
3. Do souboru `generate_missing_picons.py` nebo vlastního exportního skriptu doplňte generování stanice.
4. Spusťte automatizovanou kontrolu kvality:
   ```bash
   python3 tools/validate_picons.py --gallery
   ```
5. Otevřete vygenerovanou galerii `build/gallery.html` v prohlížeči a vizuálně zkontrolujte logo v tmavém i světlém režimu.
6. Commitněte změny a pošlete **Pull Request**. CI pipeline automaticky zkontroluje geometrii, paritu a nepřítomnost chyb maskování.
