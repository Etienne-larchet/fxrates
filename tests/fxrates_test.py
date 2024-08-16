import pandas as pd
import pytest

from fxrates import ExchangeRate


@pytest.mark.parametrize(
    ("targets_codes", "base_code", "date_from", "date_to", "amount"),
    (
        ("USD", "JPY", None, None, 1),
        (["USD", "CAD"], "EUR", "2023-01-01", None, 100.5),
        (["USD", "CAD"], "EUR", None, "2024-01-01", 100),
        (["USD", "CAD"], "EUR", "2022-01-01", "2024-05-30", 100),
    ),
)
def test_convert(targets_codes, base_code, date_from, date_to, amount):
    data = ExchangeRate.convert(targets_codes, base_code, date_from, date_to, amount)
    assert isinstance(data, pd.DataFrame)
