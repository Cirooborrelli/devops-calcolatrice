# Calcolatrice semplice

Questo repository contiene una piccola libreria di operazioni aritmetiche e una semplice interfaccia a riga di comando per provarle, insieme a una suite di test `pytest`.

## Descrizione

Le operazioni principali sono implementate in `operazioni.py` e includono: `somma`, `sottrazione`, `moltiplicazione`, `divisione`.

- Ogni funzione accetta `int` o `float` e, se riceve tipi non supportati, restituisce `None`.
- La funzione `divisione(a, b)` restituisce `None` anche quando `b == 0` (evita divisione per zero).

Il file `calcolatrice.py` fornisce una semplice funzione `calcolatrice(operazione, a, b)` che delega alle funzioni di `operazioni.py`.

## Aggiunte effettuate

- Aggiunto `operazioni.py` con le funzioni: `somma`, `sottrazione`, `moltiplicazione`, `divisione`.
- Aggiunto `calcolatrice.py` con l'helper `calcolatrice(...)` e esempi d'uso sotto `if __name__ == "__main__"`.
- Aggiunta la suite di test sotto la cartella `test/`:
  - `test_somma.py`
  - `test_sottrazione.py`
  - `test_moltiplicazione.py`
  - `test_divisione.py`
- Presenza di `pyproject.toml` per metadati e gestione del progetto (separazione delle configurazioni).

Queste aggiunte forniscono copertura delle funzionalità base e casi limite (tipi non validi, divisione per zero, numeri floating point, booleani come input).

## Struttura del progetto

- operazioni.py — implementa le funzioni aritmetiche.
- calcolatrice.py — piccolo wrapper che usa le funzioni di `operazioni.py`.
- test/ — test unitari per ciascuna operazione (`pytest`).
- pyproject.toml — metadati/config del progetto.

## Esempi d'uso

Esempio minimo dall'interprete o eseguendo `calcolatrice.py`:

```python
from operazioni import somma, divisione

print(somma(2, 3))          # 5
print(divisione(7.5, 2.5))  # 3.0
print(divisione(5, 0))      # None (divisione per zero gestita)
```

Oppure usare il wrapper:

```python
from calcolatrice import calcolatrice

print(calcolatrice("somma", 5, 3))        # 8
print(calcolatrice("sottrazione", 5, 3))  # 2
```

## Eseguire i test

- Installa le dipendenze di sviluppo (es. `pytest`) in un virtualenv:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install pytest
```

- Utilizzo di `uv`:

	- Per usare uv è neccessario effettuare i seguenti passaggi:
        - installare uv (pip install uv).
        - creare l'ambiente (uv venv).
        - sincronizzare l'ambiente (uv sync).
        - lanciare il file (uv run ...)
            - Comando di esempio (esegue `pytest` tramite `uv`):

```powershell
uv run pytest test_somma.py
```
 NOTA BENE: necessario avere un file `pyproject.toml` con i requisiti per l'avvio del progetto .

**requirements.in e requirements.txt**

- Scopo:
    - `requirements.in` è un file di input che elenca le dipendenze principali. Si scrivono i pacchetti che il progetto richiede, senza le versioni esatte.

    - `requirements.txt` è il file usato da `pip install -r requirements.txt` e solitamente contiene dipendenze risolte e vincolate (pinned).

- Flusso tipico con `pip-tools`:
    1. Crei `requirements.in` con le dipendenze top-level, ad esempio:

```text
pytest
uv
```

    2. Installa `pip-tools` e genera `requirements.txt` con il comando:

```powershell
pip install pip-tools
pip-compile requirements.in --output-file requirements.txt
```

    3. Installa le dipendenze bloccate:

```powershell
pip install -r requirements.txt
```

- Alternative e note:
    - Puoi anche generare `requirements-dev.txt` includendo dipendenze di sviluppo (es. `-r requirements.in` e poi aggiungendo `pytest`), oppure usare i gruppi nel `pyproject.toml`.
    - Se vuoi un semplice freeze dello stato attuale dell'ambiente, usa `pip freeze > requirements.txt` (ma questo include tutte le dipendenze installate, utili per ambienti di deploy ma meno leggibili per sviluppo).
    - Mantieni `requirements.in` nel controllo versione e rigenera `requirements.txt` quando aggiorni le dipendenze.

Esempio rapido (PowerShell):
```powershell
# crea virtualenv e attivalo
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# installa pip-tools, genera e installa
pip install pip-tools
echo pytest > requirements.in
echo uv >> requirements.in
pip-compile requirements.in --output-file requirements.txt
pip install -r requirements.txt
```
## Github upload

- git init
- git add README.md
- git commit -m "first commit"
- git branch -M main
- git remote add origin https://github.com/Cirooborrelli/devops-calcolatrice.git
- git push -u origin main
