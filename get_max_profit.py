

class GetMaxProfit():

    def get_max_difference(self, values):
        max_diff = 0
        min_price = values[0]
        for value in values:
            if value - min_price > max_diff:
                max_diff = value - min_price
            if min_price > value:
                min_price = value
        return max_diff

    def check_values_length(self, values):
        if len(values) >= 2:
            return True
        return False

    def calculate_max_profit(self, values):
        if self.check_values_length(values):
            return self.get_max_difference(values)
        return 'Error: not enough values'
