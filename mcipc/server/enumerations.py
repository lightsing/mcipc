"""Common enumerations."""

from enum import Enum

from mcipc.server.datatypes import VarInt


__all__ = ['State']


class State(Enum):
    """Protocol state."""

    HANDSHAKE = VarInt(0)
    STATUS = VarInt(1)
    LOGIN = VarInt(2)

    @classmethod
    def read(cls, readfunc):
        """Reads the state from the respective connection."""
        return cls(VarInt.read(readfunc))
