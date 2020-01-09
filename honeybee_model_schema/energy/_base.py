"""Base class for all objects requiring a valid EnergyPlus name."""
from pydantic import BaseModel, Schema, validator


class NamedEnergyBaseModel(BaseModel):
    """Base class for all objects requiring a valid EnergyPlus name."""

    name: str = Schema(
        ...,
        min_length=1,
        max_length=100,
        description='Name of the object used in EnergyPlus. Must use only ASCII '
            'characters, avoid (, ; ! \\n \\t), and not be more than 100 characters.'
    )

    @validator('name')
    def check_name(cls, v):
        assert all(ord(i) < 128 for i in v), 'Name contains non ASCII characters.'
        assert all(char not in v for char in (',', ';', '!', '\n', '\t')), \
            'Name contains invalid character for EnergyPlus (, ; ! \\n \\t).'
        assert len(v) > 0, 'Name is an empty string.'
        assert len(v) <= 100, 'Number of characters must be less than 100.'
        return v