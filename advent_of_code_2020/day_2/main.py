import pandas as pd
from validators import validator_1, validator_2, input_validator


def main():
    input_df = pd.read_csv("input.csv")
    print(input_validator(input_df, validator_1))
    print(input_validator(input_df, validator_2))


if __name__ == '__main__':
    main()
