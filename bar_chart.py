
"""

bar_chart.py

Author: Mohan Chinnappan
-------------------------------------------------------------
This script creates a character-based bar chart in the terminal based on the provided categories and values.
The chart can be displayed as either a horizontal or vertical bar chart.

Usage:
    python bar_chart.py --categories 'Category1,Category2,Category3' --values 'Value1,Value2,Value3'
    
Options:
    --categories : Comma-separated list of categories or labels for the bars.
    --values : Comma-separated list of values corresponding to each category.
    --bar_type : Type of bar chart to display, either 'horizontal' (default) or 'vertical'.
    
Examples:
    To create a horizontal bar chart:
    python bar_chart.py --categories 'Total,Available,Reserved' --values '5,3,7'
    
    To create a vertical bar chart:
    python bar_chart.py --categories 'Total,Available,Reserved' --values '5,3,7' --bar_type vertical
"""

import argparse

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

    def create_chart(self):
        if self.bar_type == 'horizontal':
            self.horizontal_chart()
        elif self.bar_type == 'vertical':
            self.vertical_chart()
        else:
            raise ValueError("Invalid bar type. Use 'horizontal' or 'vertical'.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create a character-based bar chart.')
    parser.add_argument('--categories', type=str, help='Comma-separated list of categories')
    parser.add_argument('--values', type=str, help='Comma-separated list of values')
    parser.add_argument('--bar_type', type=str, default='horizontal', help='Type of bar chart (horizontal or vertical)')

    args = parser.parse_args()

    categories = args.categories.split(',')
    values = [int(val) for val in args.values.split(',')]
    bar_type = args.bar_type.lower()

    chart = BarChart(categories, values, bar_type)
    chart.create_chart()
