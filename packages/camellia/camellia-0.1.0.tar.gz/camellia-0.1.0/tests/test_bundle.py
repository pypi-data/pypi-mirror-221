import unittest
from camellia.verilog.bundle import *
from camellia.verilog import exception

class TestBundle(unittest.TestCase):
  """Tests for class Bundle."""

  def test_dictionary(self):
    """Bundle works as a Dictionary object."""

    bd = Bundle({
      "key1": "val1",
      "key2": "val2",
      "key3": "val3"
    })

    self.assertListEqual(["key1", "key2", "key3"], bd.keys())
    self.assertListEqual(["val1", "val2", "val3"], bd.values())

    self.assertEqual("val2", bd.get("key2"))
    # An error is raised when getting an unknown key.
    with self.assertRaises(KeyError):
      bd.get("key4")

  def test_include_exclude(self):
    """Test incl()."""

    bd = Bundle({
      "key1": "val1",
      "key2": "val2",
      "key3": "val3"
    })

    self.assertListEqual(["val1", "val2"], bd.incl("key1", "key2").values())
    # incl() also re-arranges the order by given parameters'.
    self.assertListEqual(["val2", "val1", "val3"],
                         bd.incl("key2", "key1", "key3").values())
    # incl() does not raise exception when trying to include an unknown key.
    self.assertListEqual(["val3"], bd.incl("key3", "key4").values())

    self.assertListEqual(["key1"], bd.excl("key2", "key3").keys())
    # Elements in Bundle after excl() keep their order in the original Bundle.
    self.assertListEqual(["key1", "key3"], bd.excl("key2").keys())
    # Trying to exclude unknown keys won't take effects.
    self.assertListEqual(["key1", "key2"], bd.excl("key3", "key4").keys())

class TestBundleVar(unittest.TestCase):
  """Tests for BundleVar."""

  def test_name(self):
    """Test if name() works properly."""

    bdvar = BundleVar({
      "key1": ("name1", "width1"),
      "key2": ("name2", "width2"),
      "key3": ("name3", "width3")
    }, "This is a comment.")

    self.assertEqual("name1", bdvar.name("key1"))
    with self.assertRaises(exception.CamelliaVerilogUnknownVariableError):
      bdvar.name("unknown_key")

  def test_wires_regs(self):
    """Test if wires() and regs() works properly."""

    bdvar = BundleVar({
      "key1": ("name1", "width1"),
      "key2": ("name2", "width2"),
      "key3": ("name3", "width3")
    }, "This is a comment.")

    wire_obj = bdvar.wires(prefix="wires_", comment="Wires derived.")
    self.assertEqual(
        "// Wires derived.\n" +
        "wire [width1-1:0] wires_name1;\n" +
        "wire [width2-1:0] wires_name2;\n" +
        "wire [width3-1:0] wires_name3;\n",
        wire_obj.verilog("", 0))

    regs_obj = bdvar.regs(prefix="regs_", suffix="_derived")
    self.assertEqual(
        "reg [width1-1:0] regs_name1_derived;\n" +
        "reg [width2-1:0] regs_name2_derived;\n" +
        "reg [width3-1:0] regs_name3_derived;\n",
        regs_obj.verilog("", 0))

  def test_expr(self):
    """Test if expr() works properly."""

    bdvar = BundleVar({
      "key1": ("name1", "width1"),
      "key2": ("name2", "width2"),
      "key3": ("name3", "width3")
    }, "This is a comment.")

    bd_expr = bdvar.expr()

    self.assertListEqual(["key1", "key2", "key3"], bd_expr.keys())
    self.assertListEqual(["name1", "name2", "name3"], bd_expr.values())

  def test_eq(self):
    """Test if eq() works properly."""

    bdvar1 = BundleVar({
      "key1": ("name11", "width1"),
      "key2": ("name12", "width2"),
      "key3": ("name13", "width3")
    }, "This is a comment.")

    bdvar2 = BundleVar({
      "key1": ("name21", "width1"),
      "key2": ("name22", "width2"),
      "key3": ("name23", "width3")
    }, "This is a comment.")

    bd_expr = bdvar1.eq(bdvar2.expr())
    self.assertListEqual([("name11", "name21"),
                          ("name12", "name22"),
                          ("name13", "name23")], bd_expr.values())

    bdvar3 = BundleVar({
      "key2": ("name32", "width2"),
      "key4": ("name34", "width4")
    }, "This is a comment.")

    bd_expr = bdvar1.eq(bdvar3.expr())
    self.assertListEqual([("name12", "name32")], bd_expr.values())

    bdvar4 = BundleVar({}, "This is a comment.")
    bd_expr = bdvar1.eq(bdvar4.expr())
    self.assertListEqual([], bd_expr.values())


class TestBundleWires(unittest.TestCase):
  """Tests for BundleWires."""

  def test_verilog(self):
    """Test if BundleWires transfer into Verilog string successfully."""

    # Creating BundleWires with string.
    bd_wires1 = BundleWires("""
      1       clk
      1       rst_n
      32      din1            workload1
      WIDTH   din2            workload2
      1       bd_wires_vld    valid
      1       bd_wires_rdy    ready
    """, "")

    # Creating BundleWires with dictionary.
    bd_wires2 = BundleWires({
      "clk": ("clk", "1"),
      "rst_n": ("rst_n", "1"),
      "workload1": ("din1", "32"),
      "workload2": ("din2", "WIDTH"),
      "valid": ("bd_wires_vld", "1"),
      "ready": ("bd_wires_rdy", "1")
    })

    self.assertEqual(
      "wire clk;\n" +
      "wire rst_n;\n" +
      "wire [31:0] din1;\n" +
      "wire [WIDTH-1:0] din2;\n" +
      "wire bd_wires_vld;\n" +
      "wire bd_wires_rdy;\n",
      bd_wires1.verilog("  ", 0)
    )

    self.assertEqual(bd_wires1.verilog("  ", 0), bd_wires2.verilog("  ", 0))

    # Trigger an exception with invalid object, trying to create a BundleWires.
    with self.assertRaises(exception.CamelliaVerilogInvalidObjectError):
      BundleWires(None)

class TestBundleRegs(unittest.TestCase):
  def test_verilog(self):
    """Test if BundleRegs transfers into Verilog code successfully."""

    bd_regs1 = BundleRegs("""
      32          r_clk   clock   32'd0
      1           r_reset
      DATA_WIDTH  r_din   - 1
      DATA_WIDTH  r_data  data
    """)

    bd_regs2 = BundleRegs({
      "clock": ("r_clk", "32", "32'd0"),
      "r_reset": ("r_reset", "1", "0"),
      "r_din": ("r_din", "DATA_WIDTH", "1"),
      "data": ("r_data", "DATA_WIDTH", "0")
    })

    bd_regs_verilog = \
      "reg [31:0] r_clk;\n" + \
      "reg r_reset;\n" + \
      "reg [DATA_WIDTH-1:0] r_din;\n" + \
      "reg [DATA_WIDTH-1:0] r_data;\n"

    self.assertEqual(bd_reg_verilog, bd_regs1.verilog("  ", 0))
    self.assertEqual(bd_regs1.verilog("  ", 0), bd_regs2.verilog("  ", 0))
