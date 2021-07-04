import math

from ....source_shared.base import Base
from ....utilities.byte_io_mdl import ByteIO


class StudioBone(Base):
    def __init__(self):
        self.parent = 0
        self.flags = 0
        self.pos = []

    def read(self, reader: ByteIO):
        self.parent = reader.read_int32()
        self.flags = reader.read_int32()
        self.pos = reader.read_fmt('3f')
