from dataclasses import dataclass


@dataclass
class Dividend:
    amount: int
    days: int


class FuturePricingEngine:
    def __init__(self, stock_price: int, dividends: list[Dividend]):
        self.stock_price = stock_price
        self.current_day = 0
        self.dividends = dividends
        self.pass_dividends = 0

    def update_dividend(self, dividend_id: int, updated_dividend: Dividend):
        self.dividends[dividend_id - 1 - self.pass_dividends] = updated_dividend

    def calculate_future_price(self, days_to_future: int) -> int:
        if self.current_day >= days_to_future:
            return self.stock_price

        i = 0
        while i < len(self.dividends) and self.dividends[i].days <= days_to_future:
            self.stock_price -= self.dividends[i].amount
            self.current_day = self.dividends[i].days
            i += 1
        self.pass_dividends = i
        self.dividends = self.dividends[i:]
        return self.stock_price


engine = FuturePricingEngine(1000, [Dividend(100, 10), Dividend(50, 100)])
print(engine.calculate_future_price(15))
engine.update_dividend(2, Dividend(40, 20))
print(engine.calculate_future_price(15))
print(engine.calculate_future_price(25))

print("--------")
engine2 = FuturePricingEngine(100, [Dividend(1, 1), Dividend(2, 2), Dividend(3, 3), Dividend(4, 4), Dividend(5, 5)])
print(engine2.calculate_future_price(1))
print(engine2.calculate_future_price(2))
print(engine2.calculate_future_price(3))
print(engine2.calculate_future_price(4))
print(engine2.calculate_future_price(5))
