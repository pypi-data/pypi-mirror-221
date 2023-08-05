from __future__ import annotations
from dataclasses import dataclass
from ..validation import check
from ..decorator import enforce
from .base_int_value import BaseIntValue


# Note that from __future__ import annotations converts annotations to string.
# this means that @enforce.enforce_types will see string as type. This is fine in
# most cases. Especially for built in types.
@enforce.enforce_types
@dataclass(unsafe_hash=True)
class ByteSigned(BaseIntValue):
    """Represents a intensity value from ``0`` to ``100``."""

    def __post_init__(self) -> None:
        check(
            self.value >= -128 and self.value <= 127,
            f"{self}",
            f"Value of {self.value} is out of range. Value must be from -128 to 127.",
        )

    def _from_int(self, value: int) -> ByteSigned:
        return ByteSigned(value)

    def __eq__(self, other: object) -> bool:
        # for some reason BaseIntValue __eq__ is not picked up.
        # I suspect this is due to this class being a dataclass.
        try:
            i = int(other)  # type: ignore
            return i == self.value
        except Exception as e:
            return False
