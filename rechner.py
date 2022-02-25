from enum_tax_rates import Tax_Rates

class Rechner:
    @staticmethod
    def calc_price_with_item_number(preis_einzel: float, anzahl: int):
        return preis_einzel * anzahl

    @staticmethod
    def calc_price_with_state_code(tx: Tax_Rates, price_items: float):
        return (price_items * tx.value) + price_items

    @staticmethod
    def calc_price_with_discount_rate(order_values: float, discount_list: list):
        pass
