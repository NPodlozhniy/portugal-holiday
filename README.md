# portugal-holiday

[![Python application](https://img.shields.io/github/actions/workflow/status/NPodlozhniy/portugal-holiday/python-app.yml?branch=master&label=build)](https://github.com/NPodlozhniy/portugal-holiday/actions/workflows/python-app.yml)

Know exactly how many days off you get — and when — for any year between 1900 and 2099.

`portugal-holiday` calculates all Portuguese public holidays, including moveable feasts tied to Easter (Carnival, Holy Friday, Body of Christ), and optionally adds the municipal holiday for your city.

## Getting started

No external dependencies required — Python 3 is all you need.

```
$ git clone https://github.com/NPodlozhniy/portugal-holiday.git
$ cd portugal-holiday
```

## Usage

Get the holiday calendar for the current year:
```
$ python main.py
```

Specify a year:
```
$ python main.py --year 2025
```

Add your city's municipal holiday with `--region`:
```
$ python main.py --year 2025 --region lisbon
$ python main.py --region sintra
```

Supported regions: `almada`, `arouca`, `aveiro`, `braganca`, `braga`, `caldas-da-rainha`,
`cascais`, `coimbra`, `evora`, `faro`, `funchal`, `guimaraes`, `leiria`, `lisbon`,
`obidos`, `portimao`, `porto`, `santarem`, `setubal`, `sintra`, `viana-do-castelo`,
`vila-nova-de-gaia`, `vila-real`, `viseu`.

## Tests

```
$ pip install -r requirements.txt
$ python -m pytest
```