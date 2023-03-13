# What's new on Bethnal Green?

This is a Python script that scrapes property rental data from the [Rightmove](https://www.rightmove.co.uk/) website using the Beautiful Soup library,
and saves it to a CSV file using the Pandas library.

## Requirements

To run this script, you will need:

* Python 3.6 or higher
* The Beautiful Soup library (version 4.9.3 or higher)
* The Pandas library (version 1.2.4 or higher)
* The requests library (version 2.25.1 or higher)

You can install these libraries using pip, with the following command:

```
pip install beautifulsoup4 pandas requests
```


## Usage

To use this script, simply run the `web_scraping.py` file in your Python environment. The script will scrape the latest property rental data from Rightmove, 
and save it to a CSV file named `data.csv` in the same directory as the script.

## Data

The data saved to the `data.csv` file will include the following fields:

* Address - the address of the rental property
* Price - the rental price per month
* Contact - the phone number of the property agent
* Description - a brief description of the rental property

## Credits

This script was created by lucafungo for an academy exercise using the Beautiful Soup and Pandas libraries. The code is released under the MIT license. 

If you have any questions or feedback, please feel free to contact me at luca.alfieri@xandertalent.com
