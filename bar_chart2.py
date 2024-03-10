import argparse
import matplotlib.pyplot as plt

# python3 bar_chart2.py --categories 'Total,Available,Reserved' --values '5,3,7' --bar_type horizontal
# python3 bar_chart2.py --categories 'Total,Available,Reserved' --values '5,3,7' --bar_type vertical

# python3 bar_chart2.py --categories 'Total,Available,Reserved' --values '5,3,7' --bar_type matplotlib

class BarChart:
    def __init__(self, categories, values, bar_type='horizontal'):
        self.categories = categories
        self.values = values
        self.bar_type = bar_type

    def horizontal_chart(self):
        max_value = max(self.values)
        max_category_length = max(len(cat) for cat in self.categories)

        for category, value in zip(self.categories, self.values):
            bar = '#' * int(value * 50 / max_value)  # Scale the bar length
            print(f'{category.ljust(max_category_length)}: {bar}')

    def vertical_chart(self):
        max_value = max(self.values)
        max_category_length = max(len(cat) for cat in self.categories)

        for i in range(max_value, 0, -1):
            line = ' '.join(['#' if val >= i else ' ' for val in self.values])
            print(line)

        print('-' * (len(self.categories) * 2 - 1))  # Separator line

        for category in self.categories:
            print(category.ljust(max_category_length), end=' ')
        print()

    def matplotlib_chart(self):
        plt.barh(self.categories, self.values, color='skyblue')
        plt.xlabel('Values')
        plt.ylabel('Categories')
        plt.title('Horizontal Bar Chart')
        plt.show()

    def create_chart(self):
        if self.bar_type == 'horizontal':
            self.horizontal_chart()
        elif self.bar_type == 'vertical':
            self.vertical_chart()
        elif self.bar_type == 'matplotlib':
            self.matplotlib_chart()
        else:
            raise ValueError("Invalid bar type. Use 'horizontal', 'vertical', or 'matplotlib'.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create a character-based or matplotlib bar chart.')
    parser.add_argument('--categories', type=str, help='Comma-separated list of categories')
    parser.add_argument('--values', type=str, help='Comma-separated list of values')
    parser.add_argument('--bar_type', type=str, default='horizontal', help='Type of bar chart (horizontal, vertical, or matplotlib)')

    args = parser.parse_args()

    categories = args.categories.split(',')
    values = [int(val) for val in args.values.split(',')]
    bar_type = args.bar_type.lower()

    chart = BarChart(categories, values, bar_type)
    chart.create_chart()
