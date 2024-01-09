import pytest
from string_utils import StringUtils

# Создаем экземпляр класса StringUtils для тестирования
string_utils = StringUtils()

# Тесты для функции capitilize
def test_capitilize_positive():
    assert string_utils.capitilize("skypro") == "Skypro"

def test_capitilize_empty_string():
    assert string_utils.capitilize("") == ""

# Тесты для функции trim
def test_trim_positive():
    assert string_utils.trim("   skypro") == "skypro"

def test_trim_empty_string():
    assert string_utils.trim("") == ""

# Тесты для функции to_list
def test_to_list_default_delimiter():
    assert string_utils.to_list("a,b,c,d") == ["a", "b", "c", "d"]

def test_to_list_custom_delimiter():
    assert string_utils.to_list("1:2:3", ":") == ["1", "2", "3"]

# Тесты для функции contains
def test_contains_positive():
    assert string_utils.contains("SkyPro", "S") == True

def test_contains_negative():
    assert string_utils.contains("SkyPro", "U") == False

# Тесты для функции delete_symbol
def test_delete_symbol_present():
    assert string_utils.delete_symbol("SkyPro", "k") == "SyPro"

def test_delete_symbol_not_present():
    assert string_utils.delete_symbol("SkyPro", "X") == "SkyPro"

# Тесты для функции starts_with
def test_starts_with_true():
    assert string_utils.starts_with("SkyPro", "S") == True

def test_starts_with_false():
    assert string_utils.starts_with("SkyPro", "P") == False

# Тесты для функции end_with
def test_end_with_true():
    assert string_utils.end_with("SkyPro", "o") == True

def test_end_with_false():
    assert string_utils.end_with("SkyPro", "y") == False

# Тесты для функции is_empty
def test_is_empty_empty_string():
    assert string_utils.is_empty("") == True

def test_is_empty_whitespace():
    assert string_utils.is_empty(" ") == True

def test_is_empty_non_empty_string():
    assert string_utils.is_empty("SkyPro") == False

# Тесты для функции list_to_string
def test_list_to_string_default_joiner():
    assert string_utils.list_to_string([1, 2, 3, 4]) == "1, 2, 3, 4"

def test_list_to_string_custom_joiner():
    assert string_utils.list_to_string(["Sky", "Pro"], "-") == "Sky-Pro"
