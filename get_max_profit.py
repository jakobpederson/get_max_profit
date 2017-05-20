

class GetMaxProfit():

    def get_max_difference(self, values):
        max_diff = values[1] - values[0]
        min_price = values[0]
        print(max_diff)
        for index, value in enumerate(values):
            if index > 0:
                if value - min_price > max_diff:
                    max_diff = value - min_price
                if min_price > value:
                    min_price = value
            print(max_diff)
        return max_diff

    def check_values_length(self, values):
        if len(values) >= 2:
            return True
        return False

    def calculate_max_profit(self, values):
        if self.check_values_length(values):
            return self.get_max_difference(values)
        return 'Error: not enough values'
