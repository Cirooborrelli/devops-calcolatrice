from operazioni import moltiplicazione
import pytest

def test_moltiplicazione_positivi():
    assert moltiplicazione(2, 3) == 6

def test_moltiplicazione_negativi():
    assert moltiplicazione(-2, -3) == 6

def test_moltiplicazione_misti():
    assert moltiplicazione(-2, 3) == -6

def test_moltiplicazione_float():
    assert moltiplicazione(2.5, 4.0) == 10.0

def test_moltiplicazione_float_misti():
    assert moltiplicazione(-2.5, 4.0) == -10.0

def test_moltiplicazione_zero():
    assert moltiplicazione(0, 5) == 0

def test_moltiplicazione_con_stringa():
    assert moltiplicazione("hello", 3) is None

