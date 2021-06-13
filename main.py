from firebase import firebase
from utils.scraper import get_price
import time


def post_to_database(c):
    db = firebase.FirebaseApplication("https://twitter-scraper-d589a-default-rtdb.firebaseio.com/", None)
    db.put(f'/crypto/coins/btc/{c.updated}', name="updated", data=c.updated)
    db.put(f'/crypto/coins/btc/{c.updated}', name="price", data=c.price)


if __name__ == "__main__":
    price = ""
    updated = ""

    while True:
        coin = get_price()
        if coin.price != price:
            price = coin.price
            updated = coin.updated
            post_to_database(coin)
        time.sleep(60)
