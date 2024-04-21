import time
import re   # Regular expression operations for string matching
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define function to scrape Twitter accounts for mentions of stock symbols
def scrape_twitter_accounts(twitter_account_urls, ticker, interval):
    # Set up the Chrome WebDriver with custom options
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Work without UI
    chrome_options.add_argument('--disable-dev-shm-usage') 
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--disable-infobars')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--ignore-ssl-errors')
    chrome_options.add_argument('--lang=en-US')
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_argument('--log-level=3')  # Suppress log messages which works on Linux and Windows.
    
    # Set up the Chrome WebDriver
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Loop indefinitely
        while True:
            # Loop through the Twitter accounts
            for account in twitter_account_urls:
                try:
                    # Navigate to the Twitter account page
                    driver.get(account)
                    # Wait for the page to load and presence of first tweet
                    if WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, '//article[@data-testid="tweet"]'))):
                        # Locate all tweets within article elements
                        tweets = driver.find_elements(By.XPATH, '//a[starts-with(text(), "$")]')
                        if not tweets:
                            print("No tweets found on the page")
                        else:
                            # Extract text from each tweet
                            content = [tweet.text.strip() for tweet in tweets if tweet.text.strip()]
                            print(content)
                            # Concatenate tweet content into a single string
                            content = ' '.join(content)
                            # Use regular expressions to find all occurrences of the ticker symbol
                            matches = re.findall(r'\b{}\W*'.format(re.escape(ticker)), content, flags=re.IGNORECASE)
                            count = len(matches)
                            # Print the result
                            print(f"'{ticker}' was mentioned '{count}' times on {account} in the last '{interval}' minutes.")
                except Exception as e:
                    print(f"An error occurred while processing {account}: {e}")
            # Wait for the specified interval before scraping again
            time.sleep(interval * 60)
    finally:
        # Close the WebDriver when done
        driver.quit()

# Define inputs
twitter_account_urls = [
    'https://twitter.com/Mr_Derivatives',
    'https://twitter.com/warrior_0719',
    'https://twitter.com/ChartingProdigy',
    'https://twitter.com/allstarcharts',
    'https://twitter.com/yuriymatso',
    'https://twitter.com/TriggerTrades',
    'https://twitter.com/AdamMancini4',
    'https://twitter.com/CordovaTrades',
    'https://twitter.com/Barchart',
    'https://twitter.com/RoyLMattox',
]
ticker = 'SPY'  # Change the ticker symbol here
interval = 15 # in minutes

# Scrape Twitter accounts for mentions of stock symbols
scrape_twitter_accounts(twitter_account_urls, ticker, interval)
