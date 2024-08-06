from typing import Iterable


def product(x: Iterable[float]) -> float:
    """Computes the product of numbers in an iterable object.

    Args:
        x (Iterable[float]): An iterable object containing numbers.

    Returns:
        float: Product of the numbers.

    Raises:
        ValueError: If the iterable is empty.
    """
    # use len(x) == 0 (becos np.array, pd.Series)
    # or check with next(iter(x)) with StopIteration
    if not x:
        raise ValueError("Iterable must not be empty")

    result = 1.0
    for val in x:
        result *= val
    return result


def arithmetic_mean(x: Iterable[float]) -> float:
    """Computes the arithmetic mean of numbers in an iterable object.

    Args:
        x (Iterable[float]): An iterable object containing numbers.

    Returns:
        float: Arithmetic mean of the numbers.

    Raises:
        ValueError: If the iterable is empty.
    """
    if not x:
        raise ValueError("Iterable must not be empty")

    return sum(x) / len(x)


def geometric_mean(x: Iterable[float]) -> float:
    """Computes the geometric mean of numbers in an iterable object.

    Args:
        x (Iterable[float]): An iterable object containing numbers.

    Returns:
        float: Geometric mean of the numbers.

    Raises:
        ValueError: If the iterable is empty or contains non-positive numbers.
    """
    if not x:
        raise ValueError("Iterable must not be empty")

    if any(val <= 0 for val in x):
        raise ValueError(
            "All numbers must be positive for geometric mean calculation")

    return product(x) ** (1 / len(x))


def harmonic_mean(x: Iterable[float]) -> float:
    """Computes the harmonic mean of numbers in an iterable object.

    Args:
        x (Iterable[float]): An iterable object containing numbers.

    Returns:
        float: Harmonic mean of the numbers.

    Raises:
        ValueError: If the iterable is empty or contains non-positive numbers.
    """
    if not x:
        raise ValueError("Iterable must not be empty")

    if any(val <= 0 for val in x):
        raise ValueError(
            "All numbers must be positive for harmonic mean calculation")

    return len(x) / sum(1 / val for val in x)


class Means:
    """Provides common means calculations for numbers in an iterable object."""

    def __init__(self, x: Iterable[float]):
        """Initializes the Means class with an iterable object.

        Args:
            x (Iterable[float]): An iterable object containing numbers.

        Raises:
            ValueError: If the iterable is empty.
        """
        if not x:
            raise ValueError("Iterable must not be empty")
        self.x = x

    def product(self) -> float:
        """Finds the product of items in the iterable.

        Returns:
            float: Product of the items.
        """
        return product(self.x)

    def arithmetic_mean(self) -> float:
        """Finds the arithmetic mean of items in the iterable.

        Returns:
            float: Arithmetic mean of the items.
        """
        return arithmetic_mean(self.x)

    def geometric_mean(self) -> float:
        """Finds the geometric mean of items in the iterable.

        Returns:
            float: Geometric mean of the items.
        """
        return geometric_mean(self.x)

    def harmonic_mean(self) -> float:
        """Finds the harmonic mean of items in the iterable.

        Returns:
            float: Harmonic mean of the items.
        """
        return harmonic_mean(self.x)
