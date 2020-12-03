import numpy as np
import pandas as pd
from treemap import expand_map, traverse_map


def main():
    input_df = pd.read_csv("input.csv")
    expanded_map = expand_map(input_df)
    print(
        sum(
            traverse_map(expanded_map.copy(), 3, 1)["map"].apply(
                lambda x: "X" in x
            )
        )
    )

    print(
        np.prod(
            [
                sum(
                    traverse_map(expanded_map.copy(), slope[0], slope[1])[
                        "map"
                    ].apply(lambda x: "X" in x)
                )
                for slope in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
            ]
        )
    )


if __name__ == "__main__":
    main()
