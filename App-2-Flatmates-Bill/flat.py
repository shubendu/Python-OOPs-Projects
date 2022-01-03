class Bill:
    """
    Object that contain data about bill
    """
    def __init__(self, amount, period):
        self.period = period
        self.amount = amount


class Flatmate:
    """
    Creates a name for flatmates and pay share of bill
    """

    def __init__(self, names, days_in_house):
        self.days_in_house = days_in_house
        self.names = names

    def pays(self, bill, flatemate2):
        weight = self.days_in_house/(self.days_in_house + flatemate2.days_in_house)
        to_pay = weight * bill.amount
        return to_pay