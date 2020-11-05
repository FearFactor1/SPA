# Нужен для хранения баркодов по ТЛБ для утилизации
import pytest


@pytest.fixture(params=["71750440000100496"])
def fixture_barcode_bingo75(request):
    return request.param


@pytest.fixture(params=["71750440000100603"])
def fixture_barcode_bingo75_2(request):
    return request.param