from oblig3_software.funksjon import isLeapYear
import pytest


def test_if_year_devisible_by_4_but_not_100():
    assert isLeapYear(2020) == True
    assert isLeapYear(2024) == True
    assert isLeapYear(1604) == True
    assert isLeapYear(2028) == True
    assert isLeapYear(1616) == True


def test_if_year_deivisible_by_400():
    assert isLeapYear(2000) == True
    assert isLeapYear(1200) == True
    assert isLeapYear(1600) == True
    assert isLeapYear(2400) == True
    assert isLeapYear(2800) == True


def test_if_year_not_devisible_by_4():
    assert isLeapYear(1700) == False
    assert isLeapYear(1777) == False
    assert isLeapYear(1987) == False
    assert isLeapYear(1999) == False
    assert isLeapYear(1997) == False


def test_if_year_devisible_by_100_but_not_400():
    assert isLeapYear(1900) == False
    assert isLeapYear(1800) == False
    assert isLeapYear(2100) == False
    assert isLeapYear(1500) == False
    assert isLeapYear(2300) == False
