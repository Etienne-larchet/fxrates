# fxrates

fxrates provide historical exchange rates. For now, only daily rates are available, using the Frankfurter project's REST API on ECB data. (see: https://github.com/hakanensari/frankfurter).
The data refreshes around 16:00 CET every working day. and only business days are retrieved.


## Getting Started

Reference documentation for Frankfurter REST API can be found here:

https://www.frankfurter.app/docs/


### Installing

pip install fxrates

### Exemple

```
from fxrates import ExchangeRate


# Retrieve most recent exchange rate for JPY/USD
params = {
    'targets_codes': 'USD',
    'base_code': 'JPY',
    'date_from': None,
    'date_to': None,
    'amount': 1
}
data = ExchangeRate.convert(**params)


# Get exchange rates of EUR/USD and EUR/CAD for all business days from a date to most recent data
params = {
    'targets_codes': ['USD', 'CAD'],
    'base_code': 'EUR',
    'date_from': '2023-01-01',
    'date_to': None,
    'amount': 1
}
data = ExchangeRate.convert(**params)


# Get amount of USD and CAD corresponding to 100.5 EUR for a specific date
params = {
    'targets_codes': ['USD', 'CAD'],
    'base_code': 'EUR',
    'date_from': None,
    'date_to': '2024-01-01',
    'amount': 100.5
}
data = ExchangeRate.convert(**params)


# Get amount of USD and CAD corresponding to 100 EUR for all business days between 2 dates
params = {
    'targets_codes': ['USD', 'CAD'],
    'base_code': 'EUR',
    'date_from': '2022-01-01',
    'date_to': '2024-05-30',
    'amount': 100
}
data = ExchangeRate.convert(**params)
```


## Version History

* 0.1.0
    * Initial release

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

