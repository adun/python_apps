"""The base file for all converters."""


def bin2dec(self, n):
    """Convert a binary number to decimal.

    Args:
        n (str): The string representation of a binary number to convert.

    Returns:
        int: The result decimal number if n is valid.
    """
    return int(n, 2)
