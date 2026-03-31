def estimate_cost_inr(damage_type, severity):

    # Base costs in INR (realistic Indian market estimates)
    base_cost = {
        "Scratch": (1500, 4000),
        "Dent": (3000, 8000),
        "Crack": (6000, 15000),
        "Broken": (10000, 30000),
        "No Damage": (0, 0)
    }

    severity_multiplier = {
        "Minor": 1.0,
        "Moderate": 1.5,
        "Severe": 2.2
    }

    low, high = base_cost.get(damage_type, (2000, 6000))
    multiplier = severity_multiplier.get(severity, 1.2)

    low_final = int(low * multiplier)
    high_final = int(high * multiplier)

    return f"₹{low_final:,} - ₹{high_final:,}"