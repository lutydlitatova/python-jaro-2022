# Instalace
V kurzu budeme pracovat s programovacím jazykem [Python](https://www.python.org/) v prostředí [Visual Studio Code](https://code.visualstudio.com/). Pokud tyto nástroje ještě nemáš nainstalované, níže najdeš instrukce k instalaci.

> V této sekci z velké části využíváme existujících instalačních návodů ze stránky https://kodim.cz/czechitas/uvod-do-progr/priprava/jazyky-nastroje , s mírnými úpravami.

## Obsah
1. [Python](#python)
  - [Windows](#windows)
  - [Mac OS](#mac-os)
  - [Linux](#linux)

2. [Visual Studio Code](#visual-studio-code)
  - [Windows](#windows)
  - [Mac OS](#mac-os)
  - [Linux](#linux)

3. [Nastavení VS Code](#nastaven%C3%AD-vs-code)

## Python
### Windows
Pokud máš počítač s Windows, následuj tyto kroky:
    1. Ujisti se, že máš aktualizovaný systém. To zajistíš nejjednodušeji tak, že svůj počítač restartuješ.

    2. Stáhni si instalaci jazyka Python z [tohoto odkazu](https://www.python.org/ftp/python/3.9.10/python-3.9.10-amd64.exe). Stažený soubor spusť. Rozběhne se průvodce instalací.
    
    3. Na úvodní obrazovce je **velmi důležité** zaškrtnout volbu *Add Python 3.9 to PATH* (viz obrázek)
    ![Instalace](img/python-instalace-win.jpeg)
    
    4. Klikněte na *Install Now*, odsouhlaste případné otázky ohledně změn na vašem počítači a vyčkejte dokončení instalace. Jakmile instalace skončí, zavřete okno tlačítkem *Close*.
    
    5. Pro jistotu restartuj počítač, aby se provedené změny správně usadily.

### Mac OS
Pokud máš počítač s Mac OS, je velmi pravděpodobné, že už máš Python nainstalovaný. Ověř si instalaci.
    1. Pokud ti Python chybí, stáhní si instalaci jazyka Python z [tohoto odkazu](https://www.python.org/ftp/python/3.9.10/python-3.9.10-macos11.pkg).

    2. Stažený soubor spusť a pokračuj dle pokynů instalace až do jejího konce.

### Linux
Pokud používáš některou z populárních distribucí Linuxu jako Ubuntu, Linux Mint apod., je velmi pravděpodobné, že už máš Python nainstalovaný. Ověř si instalaci.

## Visual Studio Code
### Windows
Pokud máš počítač s Windows, následuj tyto kroky:
    1. Z [tohoto odkazu](https://aka.ms/win32-x64-user-stable) si stáhni Visual Studio Code.
    
    2. Stažený soubor spusť. Rozběhne se průvodce instalací, ve kterém stačí klikat na *Next* tak dlouho, dokud se nespustí instalace. Ve druhém kroku je pouze potřeba souhlasit s licencí.
    
    3. Jakmile instalace doběhne, zavřete okno tlačítkem Finish. Visual Studio Code by se mělo samo spustit ihned po instalaci.

### Mac OS
Pokud máš počítač s Mac OS, následuj tyto kroky:
    1. Na [oficiální stránce](https://code.visualstudio.com/) si stáhni Visual Studio Code (modré tlačítko *Download Mac ...*).
    
    2. Spusť instalaci a následuj ji až do zdařilého konce.

### Linux
Pokud máš počítač s Linuxem, následuj tyto kroky:
    1. Na [oficiální stránce](https://code.visualstudio.com/) si stáhni Visual Studio Code (modré tlačítko *.deb* pro Debian/Ubuntu, nebo *.rpm* pro Red Hat/Fedora).
    
    2. Spusť instalaci a následuj ji až do zdařilého konce.

## Nastavení VS Code
Aby se nám ve VS Code dobře programovalo, uložíme si některá užitečná nastavení. Spusťte VS Code a z horního menu vyberte **View → Command Palette...**. Do textového políčka zkopírujte tento text:

```
Open Settings (JSON)
```
a stiskněte enter.
Otevře se okno s editorem. Do jeho pravé časti vložte tento text (přepište cokoliv, co v editoru bylo dosud):

```json
{
  "editor.tabSize": 4,
  "editor.detectIndentation": false,
  "editor.renderWhitespace": "boundary",
  "editor.insertSpaces": true,
  "editor.wordWrap": "on",
  "files.eol": "\n",
  "editor.minimap.enabled": false,
  "editor.fontSize": 16
}
```

a uložte stiskem Ctrl+S nebo z menu vyberte **File → Save**.

## Ověření instalace Pythonu
Ať už jste na jakémkoliv operačním systému, spusťte svoje nově nainstalované Visual Studio Code a z horní lišty vyberte **Terminal → New Terminal**. 
Pokud jste na Windows, napište do okna, které se objeví, toto:
```
python
```
a stiskněte enter. Pokud jste na Macu nebo Linuxu, může být třeba napsat
```
python3
```
Pokud je vše v pořádku, měly by se po pár krypticky vypadajících výpisech ukázat tři zobáčky `>>>` a kurzor. To znamená, že Python je na vás připraven.

## Rozšíření VS Code pro Python
TODO

