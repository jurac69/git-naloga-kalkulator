# Kalkulator

[![CI](https://github.com/jurac69/git-naloga-kalkulator/actions/workflows/ci.yml/badge.svg)](https://github.com/jurac69/git-naloga-kalkulator/actions/workflows/ci.yml)

Preprost kalkulator za ukazno vrstico, napisan v Pythonu. Projekt je nastal kot testni
projekt pri nalogi iz nadzora verzij z Gitom.

## Zahteve

- Python 3.11 ali novejši

## Namestitev

```bash
git clone https://github.com/jurac69/git-naloga-kalkulator.git
cd git-naloga-kalkulator
```

## Uporaba

```bash
python3 kalkulator.py 7 + 5
python3 kalkulator.py 9 r 2
```

Podprte operacije: `+`, `-`, `*`, `/`, `^` (potenca), `%` (ostanek), `r` (koren).

## Testiranje

```bash
python3 -m unittest -v
```

## Potek dela

1. Odpri issue z opisom naloge.
2. Ustvari vejo iz `main` (`feature/...`, `fix/...`, `docs/...`).
3. Odpri pull request in počakaj, da CI uspešno konča.
4. Po pregledu združi v `main`. Neposredni push na `main` je onemogočen.

Sporočila commitov pišemo po pravilih Conventional Commits (`feat:`, `fix:`, `docs:`, ...).

## Različice

Uporabljamo semantično verzioniranje. Seznam izdaj je pod zavihkom Releases.

## Licenca

MIT, glej datoteko [LICENSE](LICENSE).
