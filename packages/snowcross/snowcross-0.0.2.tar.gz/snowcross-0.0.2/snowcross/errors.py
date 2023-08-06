from typing import List


class CompositeError(Exception):
    """Error containing multiple errors."""

    def __init__(self, errors: List[Exception]):
        """Create a new composite error.

        Args:
            errors (List[Exception]): A list of exceptions
        """
        self.message = "CompositeError[\n" + "".join(f"  {e}\n" for e in errors) + "]"
        super().__init__(self.message)

    def __str__(self) -> str:
        return self.message
