# POST /offers


# GET /offers/{offer_id}
class OfferService:
    def __init__(self):
        pass

    def generate_offer(self):
        """
        This function POSTs to the azure function responsible for getting the price
        the azure function also stores the offer and returns the offerID
        """
        offer_id = "ABCDE"
        price = 500

        return (offer_id, price)

    def get_offer_by_id(self, offer_id):

        offer_id = "ABCDE"
        price = 500
        return price, offer_id
