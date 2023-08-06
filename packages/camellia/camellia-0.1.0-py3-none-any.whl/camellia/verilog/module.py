from .block import BlockAlways, BlockInitial
from .bundle import BundlePorts, BundleRegs, BundleWires
from .bundle import BundleEquation
from .rawcode import Rawcode
from .exception import CamelliaVerilogInvalidObjectError
from .instance import Instance

class Module:
  """The Verilog module class"""

  def __init__(self, name, **kwargs):
    self.name = name
    self.params_dict = {}
    self.ports_dict = {}
    self.elem_list = []

    self.indent = kwargs["indent"] if "indent" in kwargs else "  "
    self.indent_level = kwargs["indent_level"] \
                        if "indent_level" in kwargs else 0

  def __str__(self):
    """Convert to Verilog module strings."""

    ret = "module {}".format(self.name)
    # Parameters.
    if 0 != len(self.params_dict):
      ret += " #(\n"
      for name, val in self.params_dict.items():
        ret += "{}parameter {} = {},\n".format(self.indent, name, val)
      ret = ret[:-2] + "\n)"
    # Ports.
    ret += " ("
    if 0 != len(self.ports_dict):
      ret += "\n"
      for ports_obj in self.ports_dict.values():
        ret += ports_obj.verilog(self.indent, self.indent_level + 1)
      ret = ret[:-2] + "\n);\n\n"
    else:
      # Speical case when there's no port to generate.
      ret += ");\n\n"

    # Elements (Regs, Wires, Always-blocks, etc.).
    for elem in self.elem_list:
      ret += elem.verilog(self.indent, self.indent_level) + "\n"

    ret += "endmodule\n"
    return ret

  def params(self, params_str):
    """Convert the pass-in parameters into Python3 dictionary structure."""

    for line in params_str.splitlines():
      spl = line.split()
      if 0 == len(spl):
        continue
      if not (1 == len(spl) or (3 == len(spl) and "=" == spl[1])):
        raise CamelliaSyntaxError()
      (name, val) = (spl[0], spl[2] if len(spl) == 3 else None)

      self.params_dict[name] = val

  def ports(self, ports_name, ports_desc, comment=""):
    """Create Ports object."""

    if type(ports_desc) is str:
      ret = BundlePorts(ports_desc, comment)
    elif type(ports_desc) is BundlePorts:
      ret = ports_desc
    else:
      raise CamelliaVerilogInvalidObjectError(ports_desc)
    self.ports_dict[ports_name] = ret
    return ret

  def get_ports(self, ports_name):
    return self.ports_dict[ports_name]

  def claim(self, obj):
    if type(obj) is BundlePorts:
      self.ports_list.append(obj)
    else:
      if type(obj) is str:
        obj = Rawcode(obj)
      elif type(obj) is BundleEquation:
        text = ""
        for lval, rval in obj.values():
          text += "assign {} = {};\n".format(lval, rval)
        obj = Rawcode(text)
      elif not (type(obj) is BundleRegs or \
                type(obj) is BundleWires or \
                type(obj) is Instance):
        raise CamelliaVerilogInvalidObjectError(obj)

      self.elem_list.append(obj)

    return obj

  def always(self, trigger, *elem_list):
    ret = BlockAlways(trigger, elem_list)
    self.elem_list.append(ret)

    return ret

  def initial(self, *elem_list):
    ret = BlockInitial(elem_list)
    self.elem_list.append(ret)

    return ret

  def inst(self, inst_name, **kwargs):
    ret = Instance(self.name, inst_name)
    if "params" in kwargs:
      ret.set_params(self.params_dict, kwargs["params"])
    ret.set_ports(self.ports_dict, kwargs["ports"])

    return ret
