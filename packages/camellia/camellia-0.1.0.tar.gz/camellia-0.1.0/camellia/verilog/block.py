from .bundle import BundleEquation
from .rawcode import Rawcode
from .exception import CamelliaVerilogAssignError

class BlockAlways:
  """Verilog always statements block."""

  def __init__(self, trigger, elem_list):
    self.trigger = trigger
    self.elem_list = []
    # Is the always block combinational logic or not.
    self.is_comb = not "posedge" in trigger and not "negedage" in trigger

    for elem in elem_list:
      if type(elem) is str:
        elem = Rawcode(elem)
      elif type(elem) is BundleEquation:
        text = ""
        for lval, rval in elem.values():
          text += lval + (" = " if self.is_comb else " <= ") + rval + ";\n"
        elem = Rawcode(text)
      elif type(elem) is BlockCond:
        elem.convert(self.is_comb)

      self.elem_list.append(elem)

  def verilog(self, indent, indent_level):
    text = (indent * indent_level) + "always @({}) begin\n".format(self.trigger)
    for elem in self.elem_list:
      text += elem.verilog(indent, indent_level + 1) + "\n"
    return text[:-1] + (indent * indent_level) + "end\n"

class BlockCond:
  """Verilog conditional block."""

  def __init__(self, cond, elem_list):
    self.cond = cond
    self.blk_if = None
    self.elem_list = list(elem_list)

  def convert(self, is_comb):
    """Convert BundleEquation into Rawcode, according to is_comb."""

    for i in range(len(self.elem_list)):
      if type(self.elem_list[i]) is str:
        self.elem_list[i] = Rawcode(self.elem_list[i])
      elif type(self.elem_list[i]) is BundleEquation:
        text = ""
        for lval, rval in self.elem_list[i].values():
          text += lval + (" = " if is_comb else " <= ") + rval + ";\n"
        self.elem_list[i] = Rawcode(text)
      elif type(self.elem_list[i]) is BlockCond:
        self.elem_list[i].convert(is_comb)

    if None != self.blk_if:
      self.blk_if.convert(is_comb)

  def verilog(self, indent, indent_level):
    text = self.blk_if.verilog(indent, indent_level) if None != self.blk_if \
           else ""

    text += (indent * indent_level) + self.cond + " begin\n"
    for elem in self.elem_list:
      text += elem.verilog(indent, indent_level + 1) + "\n"
    text = text[:-1] + (indent * indent_level) + "end\n"

    return text

  def Else(self, *elem_list):
    blk = BlockCond("else", elem_list)
    blk.blk_if = self

    return blk

  def Elif(self, cond, *elem_list):
    blk = BlockCond("else if ({})".format(cond), elem_list)
    blk.blk_if = self

    return blk

def If(cond, *elem_list):
  return BlockCond("if ({})".format(cond), elem_list)


class BlockInitial:
  """Verilog initial statements block."""

  def __init__(self, elem_list):
    self.elem_list = []

    for elem in elem_list:
      if type(elem) is str:
        elem = Rawcode(elem)
      elif type(elem) is BundleEquation:
        text = ""
        for lval, rval in elem.values():
          text += lval + " <= " + rval + ";\n"
        elem = Rawcode(text)
      elif type(elem) is BlockCond:
        elem.convert(False)

      self.elem_list.append(elem)

  def verilog(self, indent, indent_level):
    text = (indent * indent_level) + "initial begin\n"
    for elem in self.elem_list:
      text += elem.verilog(indent, indent_level + 1) + "\n"
    return text[:-1] + (indent * indent_level) + "end\n"
