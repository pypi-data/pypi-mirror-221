from .exception import CamelliaVerilogUnknownParameterError
from .exception import CamelliaVerilogUnknownPortError
from .exception import CamelliaVerilogPortConflictError
from .exception import CamelliaVerilogUndrivenInputError
from .exception import CamelliaVerilogSyntaxError

class Instance:
  def __init__(self, module_name, inst_name):
    self.module_name = module_name
    self.inst_name = inst_name
    self.param_list = []
    self.connect_list = []

  def set_params(self, params_dict, params_str):
    for line in params_str.splitlines():
      spl = line.split()

      if 0 == len(spl):
        continue

      if not (3 == len(spl) and "=" == spl[1]):
        raise CamelliaVerilogSyntaxError()

      name, val = spl[0], spl[2]
      if name in params_dict:
        self.param_list.append((name, val))
      else:
        raise CamelliaVerilogUnknownParameterError(name)

  def set_ports(self, ports_dict, eq_list):
    """Set instance's ports connectivity.

    Parameters
    ----------
    port_dict : {name: BundlePorts}
      The ports dictionary maintained by a Module object. It consists of
      BundlePorts objects that can be accessed by name.
    eq_list : [BundleEquation]
      A list of BundleEquation objects.
    """

    # Merge multiple equations into one. Check for conflicts at the same time.
    connect_dict = {}
    for equation in eq_list:
      for lval, rval in equation.values():
        if lval in connect_dict:
          raise CamelliaVerilogPortConflictError(lval)
        else:
          connect_dict[lval] = rval

    for ports in ports_dict.values():
      for name, width, direct in ports.values():
        if name in connect_dict:
          self.connect_list.append((name, connect_dict[name]))
        elif "out" == direct:
          # Unused output port.
          self.connect_list.append((name, "/* not used */"))
        else:
          raise CamelliaVerilogUndrivenInputError(name)

  def verilog(self, indent, indent_level):
    text = (indent * indent_level) + "{} ".format(self.module_name)

    if 0 != len(self.param_list):
      text += "#(\n"
      for name, val in self.param_list:
        text += (indent * (indent_level + 1)) + ".{}({}),\n".format(name, val)
      text = text[:-2] + "\n" + (indent * indent_level) + ") "

    text += self.inst_name + " (\n"
    for name, val in self.connect_list:
      text += (indent * (indent_level + 1)) + ".{}({}),\n".format(name, val)
    text = text[:-2] + "\n" + (indent * indent_level) + ");\n"

    return text
