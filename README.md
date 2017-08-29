---
title: Marhy's Picons
layout: post
---

## Kodi Picons & Icons

Pokud se v multimediálním centru zrovna nesleduje obsah, sledují se ikony, typografie, celý skin. Proto jsem se rozhodl vytvořit vlastní balíček piconů (loga televizních stanic) a ikon doplňků z českého repozitáře "[Kodi CZ&SK Doplňky](https://kodi-czsk.github.io/repository)"


## Kodi CZ Picons

Nějakou chvíli jsem si dělal svůj vlastní balíček TV ikon jak do Kodi, tak Tvheadend klientů. Protože polovina klasických ikon není vidět na tmavém skinu a polovina není vidět na světlém skinu. Udělal jsem tedy old school čtvercová loga, jejichž pozadí je dominantní barva loga té televizní stanice a to logo samotné je světlé.
Pro mě to vypadá hezky jak na výchozím novém Kodi skinu, tak třeba i v TvhClientu na iOS.

Stáhnout si můžete jak soubor .ai, kde jsou téměř veškerá loga vektorová, můžete si je upravit dle své libosti a vyexportovat do jakéhokoliv rozlišení chcete. 
Anebo tu mám už hotový balíček s rozlišením 360px, což se mi ukázalo jako ideál pro Kodi 
(Ve výchozím skinu Estuary se logo na 1080p televizi/monitoru nikde nevyskytuje větší než 360px. Aspoň podle mého zjištění).

Pro 4K panely mám vyexportovaný balíček v @2x rozlišení, tedy 720px. Pro uživatele 4K televizoru s 1080p vstupem (např. malinou) je toto zbytečné.

Balíček si můžete stáhnout v příloze do vašeho vlastního serveru, případně hostuji zde na GitHubu identickou kopii.


### Použití v Tvheadend

Balíček ikon je je připravený pro použití v Tvheadendu a ikony jsou pojmenované podle schéma satelitních kanálů.

- Stačí jít do záložky Configuration -> Base -> Picon

- Channel icon path udává cestu ke složce, ve které se nachází ikony. Pokud se nachází ikony na lokálním disku, je cesta v následujícím formátu: file:// + cesta ke složce /%C.png (za %C se dosadí vygenerovaný název)
  - např. file:///home/user/icons/%C.png (3 lomítka na začátku, protože třetí je root / )

- Channel icon scheme nastavit na Service name picons a uložte změny

- Jděte do Configuration -> Channel/EPG. Zde si zobrazte všechny kanály (vpravo dole Show All)
- Stiskem CTRL+A všechny kanály označte a stiskněte Reset icon. Tím se pro každý kanál nově vygeneruje cesta k piconám podle nového nastavení.
- Změny uložte a hotovo.

<img src="http://marhycz.github.io/picons/images/tvheadendconf.png" width="384"><img src="http://marhycz.github.io/picons/images/tvheadendconf.png" width="384">


### Náhledy

#### Náhled TV
![Náhled TV](http://marhycz.github.io/picons/images/nahled-tv.png)

#### Náhled TV Regionální
![Náhled TV Regionální](http://marhycz.github.io/picons/images/nahled-tvregion.png)

#### Náhled Rádio stanice
![Náhled Rádio stanice](http://marhycz.github.io/picons/images/nahled-radio.png)

<hr>

### Ke stažení
 
[@360px](https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/MarhyCZ/marhycz.github.io/tree/master/picons/360) (.zip)

[@720px](https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/MarhyCZ/marhycz.github.io/tree/master/picons/720) (.zip)

A Složku můžete procházet [zde](https://github.com/MarhyCZ/marhycz.github.io/tree/master/picons/720)

Vektorový formát - coming soon

#### Link pro Tvheadend (Channel icon path):
```markdown

@360px - https://marhycz.github.io/picons/360/%C.png
@720px - https://marhycz.github.io/picons/720/%C.png

(např. https://marhycz.github.io/picons/360/ct1.png)
```

<hr>

## Kodi CZ&SK Doplňky

Další hojně používanou částí v našem prostředí jsou skvělé doplňky ze společného českého a slovenského repozitáře "[Kodi CZ&SK Doplňky](https://kodi-czsk.github.io/repository)". Napadlo mě redesignovat ikony všech doplňků najednou, aby měli koherentní design a návrhy poslat na jednotlivé github stránky doplňků.

Návrhy můžete prohlížet v [této složce](https://github.com/MarhyCZ/marhycz.github.io/tree/master/kodi-czsk-icons/navrhy)

![Náhled návrhů](http://marhycz.github.io/kodi-czsk-icons/czsknahled.png)
