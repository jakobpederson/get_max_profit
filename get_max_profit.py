

class GetMaxProfit():

    def get_max_difference(self, values):
        differences = []
        for value in values:
            differences.append(max([value - x for x in values]))
        return max(differences)

    def check_values_length(self, values):
        if len(values) >= 2:
            return True
        return False

    def calculate_max_profit(self, values):
        if self.check_values_length(values):
            return self.get_max_difference(values)
        return 'Error: not enough values'
