"""
This is the demo code that uses hydra to access the parameters in under the directory config.

Author: Khuyen Tran
"""

import hydra
import pandas as pd
from omegaconf import DictConfig


@hydra.main(config_path="../config", config_name="main", version_base=None)
def process_data(config: DictConfig):
    """Function to process the data"""

    print(f"Process data using {config.data.raw}")

    data = pd.read_csv(config.data.raw)

    print(f"Columns used: {config.process.use_columns}")
    processed_data = data[config.process.use_columns]

    print(f"Target column: {config.process.target}")
    target = data[config.process.target]

    processed_data.to_csv(config.data.processed, index=False)
    target.to_csv(config.data.final, index=False)


if __name__ == "__main__":
    process_data()
