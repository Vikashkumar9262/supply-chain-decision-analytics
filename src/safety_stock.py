import pandas as pd
import numpy as np


def calculate_safety_stock(
    demand_std,
    lead_time_days,
    service_level_z=1.65
):
    """
    Calculate safety stock based on demand variability
    and supplier lead time.
    """

    safety_stock = (
        service_level_z
        * demand_std
        * np.sqrt(lead_time_days)
    )

    return safety_stock