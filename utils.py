import pandas as pd
import numpy as np


def format_large_value(value):
    """
    Format numerical values with appropriate suffixes (K for thousands, M for millions, B for billions).

    Parameters:
    - value (float or int): The numerical value to be formatted.

    Returns:
    - str: A string representing the formatted value with suffixes. 
           If the value is less than 1,000, it returns the number without a suffix.
           For values in the thousands, it appends 'K' (e.g., 1,500 becomes '1.5K').
           For values in the millions, it appends 'M' (e.g., 1,200,000 becomes '1.2M').
           For values in the billions, it appends 'B' (e.g., 1,500,000,000 becomes '1.5B').
           If the value is None, it returns 'N/A'.
    """
    if value is None:
        return "N/A"
    elif value < 1_000:
        return f"{value:.0f}"  # No suffix for values below 1K
    elif value < 1_000_000:
        return f"{value / 1_000:.1f}K"  # Thousands
    elif value < 1_000_000_000:
        return f"{value / 1_000_000:.1f}M"  # Millions
    else:
        return f"{value / 1_000_000_000:.1f}B"  # Billions