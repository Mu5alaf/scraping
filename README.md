# Twitter Stock Mentions Scraper

## Introduction
This script automates the process of scraping Twitter accounts for mentions of stock symbols. It uses Selenium WebDriver to navigate Twitter pages and extract tweet content, and regular expressions to search for mentions of specific stock symbols.

## Dependencies
- Python 3
- Selenium WebDriver
- Chrome WebDriver
- Regular Expressions

## Code Explanation

### Importing Libraries
The script imports necessary libraries for browser automation and regular expressions.

### Function Definition
The `scrape_twitter_accounts` function is defined to perform the scraping task. It takes three arguments:
- `twitter_account_urls`: a list of Twitter account URLs to scrape.
- `ticker`: the stock symbol to search for.
- `interval`: the time interval between scraping attempts.

### Setting up Chrome WebDriver
The Chrome WebDriver is configured with custom options to run in headless mode (without UI) and handle various settings like SSL errors and log levels.

### Main Scraping Logic
The script enters an indefinite loop to continuously scrape Twitter accounts.
- For each Twitter account URL provided, it navigates to the page.
- It waits for the presence of tweets using WebDriverWait.
- It then extracts tweet content and searches for mentions of the specified stock symbol using regular expressions.
- The count of mentions is printed for each account.
- Errors, if any, are caught and printed.

### Define Inputs and Call the Function
The script defines inputs including Twitter account URLs, stock symbol, and scraping interval.
Finally, it calls the `scrape_twitter_accounts` function with the provided inputs to initiate the scraping process.

## Conclusion
This script provides a convenient way to monitor Twitter for mentions of specific stock symbols across various accounts.


Uploading git.mp4…


