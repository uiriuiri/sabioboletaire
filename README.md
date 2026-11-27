# sabioboletaire

**un sabio boletaire dijo una vez...**

`sabioboletaire` es un pequeño programa escrito en Python que muestra una frase sabia, diferente cada día del año, acompañada de la ilustración ASCII del sabio boletaire.

Una pequeña dosis diaria de sabiduría, surrealismo y otras formas de conocimiento dadaísta.

## Funcionamiento

El programa selecciona automáticamente una frase de `quotes.txt` según el día del año y la muestra dentro de un bocadillo ASCII, junto al sabio boletaire.

También permite consultar la frase correspondiente a cualquier fecha concreta.

## Ejemplo

```text
  __________________________________
 / Una frase sabia cada día...      \
 \__________________________________/

        \
         \
        >\\\|/<
        |_"""_|                   _---_
        (O) (o)                  (_____)
+----OOO--(_)--OOOo----------------( )-------------+
```

## Instalación

Clona el repositorio:

```bash
git clone https://github.com/YOUR_USERNAME/sabioboletaire.git
cd sabioboletaire
```

No es necesario instalar dependencias externas. Solo necesitas Python 3.

## Instalación como comando

Si quieres ejecutar `sabioboletaire` desde cualquier directorio, puedes añadirlo a tu `PATH`.

Desde la carpeta del repositorio, ejecuta:

```bash
chmod +x sabioboletaire.py
mkdir -p ~/.local/bin
ln -sf "$(realpath sabioboletaire.py)" ~/.local/bin/sabioboletaire
```

Asegúrate de que `~/.local/bin` está incluido en tu `PATH`.

**Si utilizas Bash:**

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

**Si utilizas Zsh:**

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

**Si utilizas Fish:**

```fish
fish_add_path ~/.local/bin
```

Una vez configurado, podrás ejecutar el programa desde cualquier directorio:

```bash
sabioboletaire
```

**Nota:** El enlace simbólico apunta al script original del repositorio. No muevas ni elimines la carpeta del proyecto después de instalarlo.


## Uso

Ejecutar el programa:

```bash
python3 sabioboletaire.py
```

Consultar una fecha concreta:

```bash
python3 sabioboletaire.py --date 2026-01-01
```

El parámetro `--date` acepta fechas en formato `YYYY-MM-DD`.

## Estructura del proyecto

```text
sabioboletaire/
├── sabioboletaire.py   # Programa principal
├── quotes.txt          # Colección de frases
├── sabio.txt           # Ilustración ASCII del sabio
├── README.md           # Documentación
├── LICENSE             # Licencia
└── .gitignore          # Archivos ignorados por Git
```

## Las frases

Las frases se almacenan en `quotes.txt`, con una frase por línea.

El programa utiliza el número de día del año para seleccionar la frase correspondiente:

- 1 de enero: primera frase.
- 2 de enero: segunda frase.
- 31 de diciembre: última frase.

Actualmente, el programa requiere exactamente 365 frases y comprueba que no haya líneas vacías.

### Años bisiestos

Los años bisiestos tienen un tratamiento especial:

- El 29 de febrero utiliza la frase correspondiente al día 59.
- A partir del 1 de marzo, el programa ajusta el número de día para mantener la correspondencia con las 365 frases.
- El 1 de marzo siempre corresponde a la frase número 60.

## Personalización

Puedes modificar el contenido del proyecto fácilmente:

- `quotes.txt`: añade o modifica las frases.
- `sabio.txt`: modifica la ilustración ASCII.
- `sabioboletaire.py`: modifica el funcionamiento del programa.

**Nota:** La colección de frases todavía está en construcción y no contiene necesariamente las 365 frases definitivas.

## Requisitos

- Python 3
- Linux o cualquier sistema compatible con Python 3

No requiere paquetes externos.

## Licencia

Este proyecto está publicado bajo la licencia MIT.
Consulta el archivo [LICENSE](LICENSE) para más información.