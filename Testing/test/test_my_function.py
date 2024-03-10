import pytest  # importujeme pytest, který jsme nainstalovali "pip install pytest"
import source.main as main  # importujeme testovaný soubor


# vytvoříme funkci pro testování
def test_add():
    result = main.add(1, 2)  # vytvoříme proměnnou result p
    assert result == 3  # zadáme očekávaný výstup


def test_divide():
    result = main.divide(9, 3)
    assert result == 3


def test_divide_by_zero1():
    result = main.divide(10,0)
    assert result == AssertionError("division by zero") # Assertion Error nám vrátí popis chyby; pokud dáme True, tak získáme ZeroDivisionError, protože jsme zadali dělení 0


def test_divide_by_zero2():
    with pytest.raises(ZeroDivisionError): # funkce with pracuje s následným kódem jen v jednom bloku, ale nedá nic na výstup
        main.divide(10, 0) # vytvoření výjimky pro dělení 0
