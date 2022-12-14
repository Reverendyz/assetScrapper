# assetScrapper

Only an asset Scrapper based on `https://statusinvest.com/fundos-imobiliarios/<TickerToScrape>` (Ex.: hctr11)

## Usage

### Raw usage

- `python scrapper/main.py -a <hctr11 recr11 ...> -p <10 32 ...> [-o filename without extension]`
  
### From installed wheel

- `scrapper-a <hctr11 recr11 ...> -p <10 32 ...> [-o filename without extension]`
  
## Prerequisites

- [Python](https://www.python.org/downloads/)

## Installing

### Pipenv

- run `pipenv install` then `pipenv shell`

### Wheel Install

- you can install this `.whl` by runnning: `pip wheel -w dist .` then  `pip install dist/scrapper`
  - If you're in pipenv, please use `pipenv run` before these commands
  
## Getting next payment amount

- run `jq '[.Assets[] | .Position * .Next.Value] | add' myfile.json` or `scrapper -a hctr11 -p 18 | jq '[.Assets[] | .Position * .Next.Value] | add'`