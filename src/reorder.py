def calculate_reorder_point(
    average_daily_demand,
    lead_time_days,
    safety_stock
):
    """
    Calculate the inventory level at which
    a replenishment order should be placed.
    """

    lead_time_demand = (
        average_daily_demand
        * lead_time_days
    )

    reorder_point = (
        lead_time_demand
        + safety_stock
    )

    return reorder_point