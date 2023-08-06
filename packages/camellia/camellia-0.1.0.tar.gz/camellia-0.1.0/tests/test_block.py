import unittest
from camellia.verilog.block import *
from camellia.verilog.exception import *
# Import bundle because we use it to generate assignments in blocks. And we
# also generates some
from camellia.verilog import bundle

class TestBlockAlways(unittest.TestCase):
  pass


class TestBlockCond(unittest.TestCase):
  pass


class TestBlockInitial(unittest.TestCase):
  def test_verilog(self):
    pass
