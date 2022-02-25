class Rechner:
    @staticmethod
    def calc_price_with_item_number(preis_einzel: float, anzahl: int):
        return preis_einzel * anzahl

    @staticmethod
    def calc_price_with_state_code(tx: TAX, price_items: float):
        return (price_items * TAX.value) + price_items
