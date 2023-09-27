# Minimalbeispiel

Hier findet Ihr ein kleines Beispiel, wie der Code einer einfachen Beispielabgabe aussehen könnte.

Natürlich ist es nur eine sehr kurze und rudimäntere Implementierung, aber Ihr könnt gerne auf diesem Code aufbauen und ihn verbessern oder auch eine völlig andere Programmiersprache und Codebase verwenden.

Es ist Euer Projekt!

## Benutzung

Das Programm kann mit Python ausgeführt werden. Hierzu benötigt Ihr zunächst eine Python-Umgebung mit `skimage`, `pathlib` und `numpy`.

Beispiel für die Augmentierung einer Bilddatei:

```bash
python main.py ai_gen_images/clownfish.png output/clownfish_augmented.png
```

Beispiel für die Augmentierung einer Textdatei:

```bash
python main.py ai_gen_text/alpen.txt output/alpen_augmented.txt
```

## Daten

In den beiden Ordnern `ai_gen_images` und `ai_gen_text` findet Ihr Beispieleingaben für Text und Bilder, die von einer KI erstellt worden ist.

Wir werden weitere Testdaten im Laufe des Wettbewerbs veröffentlichen, aber ihr könnt auch gerne selbst neue Texte und Bilder für eure Testzwecke generieren.
