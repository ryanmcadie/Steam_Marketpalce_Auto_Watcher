import requests
import time
import json

# API endpoint to retrieve information about the item
API_ENDPOINT = "https://steamcommunity.com/market/priceoverview/?currency=20&appid=730&market_hash_name={}"

def get_price(item_name):
    # Use the API endpoint to retrieve information about the item
    response = requests.get(API_ENDPOINT.format(item_name))
    
    # Check if the request was successful
    if response.status_code != 200:
        raise Exception("Failed to retrieve information from the API")
    
    # Parse the response and retrieve the current price of the item
    data = json.loads(response.text)
    price = data["lowest_price"]
    
    return price

item_thresholds = {
    "AK-47 | Slate (Factory New)" : 20,
    "USP-S | Ticket to Hell (Factory New)" : 10,
    "M4A1-S | Printstream (Factory New)" : 550,
    "Desert Eagle | Night Heist (Factory New)" : 15,
    "Desert Eagle | Trigger Discipline (Factory New)" : 10,
    "SSG 08 | Fever Dream (Factory New)" : 10
}

while True:
    for item_name, threshold_price in item_thresholds.items():
        try:
            price_string = get_price(item_name)
            price_parts = price_string.split(" ")
            if len(price_parts) != 2:
                raise Exception("Unexpected format of price string: {}".format(price_string))
            current_price = int(float(price_parts[1]))
        except Exception as e:
            print("An error occurred while trying to retrieve the price of the item '{}': {}".format(item_name, e))
            continue
        if current_price < threshold_price:
            print("Item {} is now below the threshold price, take action!".format(item_name), f"{price_string}")
        else :
            print("NO ITEM PRICE CHANGE")
    print("-----------------------------------------------------------------------------------------------------")
    time.sleep(30) # Wait for 30 seconds before checking again
