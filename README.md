# collect invoices @ feup

## About

Simple script to extract and save all the invoices files that you have on your FEUP account.

## Requirments

- Python 3.3+
- RoboBrowser


## Installation

```
conda env create -f environment.yml
source activate feup_invoices
```

## Usage

After having performed the steps above, run the following command:

```
python invoices.py
```

The files will be saved on a folder that is created named "invoices".