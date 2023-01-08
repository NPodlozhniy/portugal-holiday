# portugal-holiday

[![Python application](https://github.com/NPodlozhniy/portugal-holiday/actions/workflows/python-app.yml/badge.svg?branch=master)](https://github.com/NPodlozhniy/portugal-holiday/actions/workflows/python-app.yml)

The project is dedicated to simplifying vacation planning

## Getting started

Since it's a very simple app, all the packages used are built in, so if Python 3 is already installed, that is enough

### Installation

You can just copy the repo without installing any additional packages

```
$ git clone https://github.com/NPodlozhniy/portugal-holiday.git
```

### Tests

Open the folder where you just copied the app and run tests using pytest

```
$ cd portugal-holiday
$ python -m pytest
```

### Usage

To get the holiday calendar for the current year, just run the following command
```
$ python main.py
```
If you want to get the calendar for a speciefic year just add the `--year` argument, for example
```
$ python main.py --year 2000
```
