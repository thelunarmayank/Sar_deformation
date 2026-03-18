def apply_thresholds(snow_depth, density):
    """
    Apply thresholds to snow depth and density data.
    Handle ZeroDivisionError gracefully.
    """
    try:
        if density == 0:
            raise ZeroDivisionError("Density cannot be zero.")
        # Threshold application logic here
        adjusted_depth = snow_depth / density
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        adjusted_depth = 0  # or some default value
    return adjusted_depth

# Complete SAR snow depth and density analysis code focused on Beas Watershed in Himachal Pradesh
# Implementation details here
