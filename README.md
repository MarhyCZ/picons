<a href="#cz---marhyho-picony--ikony">Přeskočte na CZ popis</a>

## Introduction to Marhy's Picons
At home I am using several clients for TV watching (Kodi, Tvheadend clients on iOS, UWP on Windows 10) and most picon packs that are available on the internet are either transparent, which means some of them look fine on dark backgrounds, but are awful on light backgrounds and vice versa. The ones that do have a background look either outdated by my taste (lots of old gradients, unnecessary effects like glass reflections, too much skeuomorphism) or if they have for example a solid color background, some of the picons aren't visible, because their logo has the same primary color.

So I've decided to create my own picon pack, that would look nice in my eyes and on a broad range of end clients. I create every picon manually. Most of them is about applying primary color or gradient of the logo to the background of the picon and making the logo itself white. Achieving modern, sleek look, unique, distinctive backgrounds, but keeping familiar look to the original logos. I am trying to have every picon in vector format for future scaling, I will upload the source files in .ai after a while.


The disadvantage against the most other picon packs is, that I am nowhere near close to the amount of channel logos they provide. So in the meantime you can use in junction with my picons this excellent repository of picons on https://github.com/picons/picons-source

#### TL;DR: " It's modern, flat, rectangular picon pack with colorful backgrounds "

### Small taste

#### TV
![Náhled TV](http://marhycz.github.io/picons/docs/images/nahled-tv.png)

#### Radio
![Náhled Rádio stanice](http://marhycz.github.io/picons/docs/images/nahled-radio.png)

### Usage in Tvheadend

This is an example of how to use Marhy's Picons package in Tvheadend

- Go to Configuration -> General -> Base -> Picon

- Channel icon path defines path to the directory, where picons are located. If they are on your local drive, use following syntax: file:// + path to directory /%C.png (%C is variable which tvheadend replaces with his generated picon names)
  - e.g. file:///home/user/icons/%C.png (3 slashes, the third one is root of filesystem / )

- Set channel icon scheme to "Service name picons" and save changes

- Go to Configuration -> Channel/EPG. List all channels (right corner -> Show All)
- Press CTRL+A to select all channels and press "Reset icon button". Tvheadend will generate new picon paths for every channel by our new settings.

- Save changes and you're done!

<img src="http://marhycz.github.io/picons/docs/images/tvheadendconf.png" width="384"><img src="http://marhycz.github.io/picons/docs/images/tvheadendconf2.png" height="378">

<hr>

### Downloads

You can download Marhy's picons pack in 2 versions. Either 512x512px suitable for 1080p TVs or 1024x1024px for 4K TVs and retina displays. I am also preparing source files in vector format, so you can create your own flavours.
 
[@512px](https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/MarhyCZ/picons/tree/master/512) (.zip)

[@1024px](https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/MarhyCZ/picons/tree/master/1024) (.zip)

You can browse the picons [here](https://github.com/MarhyCZ/picons/tree/master/1024)


#### URL for Tvheadend (Channel icon path):

You don't have to download the picons package! Just point Tvheadend to these URLs and as I'll add more and more picons, your Tvheadend will pick them up!

```markdown

@512px - https://marhycz.github.io/picons/512/%C.png
@1024px - https://marhycz.github.io/picons/1024/%C.png

(např. https://marhycz.github.io/picons/512/ct1.png)
```

<hr>

## CZ - Marhyho Picony & Ikony

Pokud se v multimediálním centru zrovna nesleduje obsah, sledují se ikony, typografie, celý skin. Proto jsem se rozhodl vytvořit vlastní balíček piconů (loga televizních stanic) a ikon doplňků z českého repozitáře "[Kodi CZ&SK Doplňky](https://kodi-czsk.github.io/repository)"


## Picony

Nějakou chvíli jsem si dělal svůj vlastní balíček TV ikon jak do Kodi, tak Tvheadend klientů. Protože polovina klasických ikon není vidět na tmavém skinu a polovina není vidět na světlém skinu. Udělal jsem tedy old school čtvercová loga, jejichž pozadí je dominantní barva loga té televizní stanice a to logo samotné je světlé.
Pro mě to vypadá hezky jak na výchozím novém Kodi skinu, tak třeba i v TvhClientu na iOS.

Stáhnout si můžete jak soubor .ai, kde jsou téměř veškerá loga vektorová, můžete si je upravit dle své libosti a vyexportovat do jakéhokoliv rozlišení chcete. 
Anebo tu mám už hotový balíček s rozlišením 512px, což se mi ukázalo jako ideál pro Kodi do většiny skinů

Pro 4K panely mám vyexportovaný balíček v @2x rozlišení, tedy 1024px. Pro uživatele 4K televizoru s 1080p vstupem (např. malinou) je toto zbytečné.

Balíček si můžete stáhnout v příloze do vašeho vlastního serveru, případně hostuji zde na GitHubu identickou kopii.


### Použití v Tvheadend

Balíček ikon je je připravený pro použití v Tvheadendu a ikony jsou pojmenované podle schéma satelitních kanálů.

- Stačí jít do záložky Configuration -> General -> Base -> Picon

- Channel icon path udává cestu ke složce, ve které se nachází ikony. Pokud se nachází ikony na lokálním disku, je cesta v následujícím formátu: file:// + cesta ke složce /%C.png (za %C se dosadí vygenerovaný název)
  - např. file:///home/user/icons/%C.png (3 lomítka na začátku, protože třetí je root / )

- Channel icon scheme nastavit na Service name picons a uložte změny

- Jděte do Configuration -> Channel/EPG. Zde si zobrazte všechny kanály (vpravo dole Show All)
- Stiskem CTRL+A všechny kanály označte a stiskněte Reset icon. Tím se pro každý kanál nově vygeneruje cesta k piconám podle nového nastavení.
- Změny uložte a hotovo.

<img src="http://marhycz.github.io/picons/docs/images/tvheadendconf.png" width="384"><img src="http://marhycz.github.io/picons/docs/images/tvheadendconf2.png" height="378">

<hr>

### Ke stažení
 
[@512px](https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/MarhyCZ/picons/tree/master/512) (.zip)

[@1024px](https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/MarhyCZ/picons/tree/master/1024) (.zip)

A Složku můžete procházet [zde](https://github.com/MarhyCZ/picons/tree/master/1024)

Vektorový formát - coming soon

#### Link pro Tvheadend (Channel icon path):

```markdown

@512px - https://marhycz.github.io/picons/512/%C.png
@1024px - https://marhycz.github.io/picons/1024/%C.png

(např. https://marhycz.github.io/picons/512/hbohd.png)
```

<hr>

## Kodi CZ&SK Doplňky

Další hojně používanou částí v našem prostředí jsou skvělé doplňky ze společného českého a slovenského repozitáře "[Kodi CZ&SK Doplňky](https://kodi-czsk.github.io/repository)". Napadlo mě redesignovat ikony všech doplňků najednou, aby měli koherentní design a návrhy poslat na jednotlivé github stránky doplňků.

Návrhy můžete prohlížet v [této složce](https://github.com/MarhyCZ/picons/tree/master/kodi-czsk-icons/navrhy)

![Náhled návrhů](http://marhycz.github.io/picons/kodi-czsk-icons/czsknahled.png)
