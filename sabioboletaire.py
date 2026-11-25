#!/usr/bin/env python3

from datetime import date
from pathlib import Path
from calendar import isleap
import argparse
import textwrap

# Directorio donde se encuentra el programa
BASE_DIR = Path(__file__).parent

QUOTES_FILE = BASE_DIR / "quotes.txt"
SABIO_FILE = BASE_DIR / "sabio.txt"


def get_quote(current_date):
    """Obtiene la frase correspondiente al día del año."""

    quotes = QUOTES_FILE.read_text(encoding="utf-8").splitlines()

    if len(quotes) != 365:
        raise ValueError(
            f"Se necesitan 365 frases. Actualmente hay {len(quotes)}."
        )

    if any(not quote.strip() for quote in quotes):
        raise ValueError("Hay líneas vacías en quotes.txt.")

    day_number = current_date.timetuple().tm_yday

    # Ajustar los años bisiestos
    if current_date.month == 2 and current_date.day == 29:
        day_number = 59
    elif isleap(current_date.year) and current_date.month > 2:
        day_number -= 1

    return quotes[day_number - 1], day_number


def print_quote(quote):
    """Dibuja el bocadillo de la frase."""

    lines = textwrap.wrap(
        quote,
        width=42,
        break_long_words=False
    )

    width = max(len(line) for line in lines)

    print("  " + "_" * (width + 2))

    for line in lines:
        print(" / " + line.ljust(width) + " \\")

    print(" \\" + "_" * (width + 2) + "/")


def main():
    parser = argparse.ArgumentParser(
        description="Una frase sabia cada día."
    )

    parser.add_argument(
        "--date",
        help="Consultar una fecha concreta (YYYY-MM-DD)."
    )

    args = parser.parse_args()

    current_date = (
        date.fromisoformat(args.date)
        if args.date
        else date.today()
    )

    quote, day_number = get_quote(current_date)

    print()
    print_quote(quote)

    sabio = SABIO_FILE.read_text(encoding="utf-8")
    print(sabio.rstrip())

    print()

if __name__ == "__main__":
    main()
