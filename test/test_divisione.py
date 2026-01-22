from operazioni import divisione
import pytest

def test_divisione_positivi():
    assert divisione(6, 3) == 2

def test_divisione_negativi():
    assert divisione(-6, -3) == 2

def test_divisione_misti():
    assert divisione(-6, 3) == -2

def test_divisione_float():
    assert divisione(7.5, 2.5) == 3.0

def test_divisione_float_misti():
    assert divisione(-7.5, 2.5) == -3.0

def test_divisione_zero_numeratore():
    assert divisione(0, 5) == 0

def test_divisione_per_zero():
    assert divisione(5, 0) is None

def test_divisione_con_stringa():
    assert divisione("hello", 3) is None

