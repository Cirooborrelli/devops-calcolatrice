# Calcolatrice semplice

Questo repository contiene una semplice funzione di somma e dei test che ne verificano il comportamento.

**Scopo:** mostrare un esempio minimale di funzione, gestione di tipi e test con `pytest`.

**Struttura del progetto**
- [operazioni.py](operazioni.py): implementa la funzione `somma(a, b)`.
- [test.py](test.py): test unitari per la funzione `somma` (usa `pytest`).
- [pyproject.toml](pyproject.toml): metadati del progetto (se presenti).

Funzionalità principali
- `somma(a, b)` accetta numeri interi o float e restituisce la loro somma.
- Se uno degli argomenti non è né `int` né `float`, la funzione restituisce `None`.
- Nota: in Python i valori booleani sono sottoclassi di `int` (es. `True == 1`), quindi `somma(True, False)` ritorna `1`.

- `sottrazione(a, b)` effettua la stessa cosa ma facendo la sottrazione.

Esempio d'uso
```
from operazioni import somma

print(somma(2, 3))       # 5
print(somma(2.5, 3.5))   # 6.0
print(somma("a", 3))    # None
```

Eseguire i test
- Installa `pytest` se non è già presente:

```
pip install pytest
```

- Lancia i test con:

```
pytest -v
```

**Requisiti e avvio**

- Requisiti minimi:
	- Python 3.8+ installato.
	- `pip` per installare le dipendenze.
	- (Opzionale ma raccomandato) un ambiente virtuale (`venv`).

- Installazione rapida (PowerShell):

```powershell
# crea e attiva un virtualenv (opzionale ma consigliato)
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# installa dipendenze di sviluppo e utilità
pip install --upgrade pip
pip install pytest uv
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
##Github upload

git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Cirooborrelli/devops-calcolatrice.git
git push -u origin main
