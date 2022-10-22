# assetScrapper

Only an asset Scrapper based on https://statusinvest.com/fundos-imobiliarios/\<TickerToScrape\> (Ex.: hctr11)

## Pre requisites

- ``` pip install requests bs4```
- know about some assets in the brasilian trade market (Only work with ```fundos imobiliarios```)
  
## An explorer of assets

### Steps

1. Just run main.py with arguments to scrape
   - `python main.py -a ticker1 ticker2 ticker3...`
     - ticker eg.: hctr11 (pattern with 4 letters and 11 suffix)
2. Check the [assets.json](assets.json) file for results

## Next Step

- Create a python wheel to run this program