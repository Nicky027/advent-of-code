import pandas as pd
from expenses import multiply_add_up_entries


def main():
    input_df = pd.read_csv("input.csv")
    expense_report = input_df["expenses"].to_list()
    print(multiply_add_up_entries(expense_report, 2020, 2))
    print(multiply_add_up_entries(expense_report, 2020, 3))


if __name__ == '__main__':
    main()
