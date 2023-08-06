from .exception import CamelliaVerilogUnknownVariableError
from .exception import CamelliaVerilogSyntaxError
from .exception import CamelliaVerilogValTypeError
from .exception import CamelliaVerilogInputAsLvalError
from .exception import CamelliaVerilogInvalidObjectError

class Bundle:
  """Define a common interface to interact with a set of items.

  In Verilog Programming, it's frequent that programmers need to use multiple
  items (e.g. registers, wires, ports) as a unified bundle of things. This
  class provides the ability to do so.
  """

  def __init__(self, dictionary):
    self.dictionary = dictionary

  def keys(self):
    return list(self.dictionary.keys())

  def values(self):
    return list(self.dictionary.values())

  def items(self):
    return self.dictionary.items()

  def get(self, key):
    return self.dictionary[key]

  def incl(self, *idents):
    return self.__class__({key: self.dictionary[key]
                           for key in idents if key in self.dictionary.keys()})

  def excl(self, *idents):
    return self.__class__({key: self.dictionary[key]
                           for key in self.dictionary.keys()
                           if not key in idents})


class BundleVar(Bundle):
  def __init__(self, dictionary, comment):
    """Intialization.

    Parameters
    ----------
    dictionary : {name: (verilog_name, verilog_width)}
      Dictionary used to present Verilog variables (ports, regs or wires).
    comment : str
      The comment text to generated above the variables.
    """

    self.comment = comment
    super().__init__(dictionary)

  def helper_comment_(self, indent, indent_level):
    return "{}// {}\n".format(indent * indent_level, self.comment) \
           if self.comment else ""

  def helper_width_(self, width):
    return "[{}-1:0] ".format(width) if not width.isnumeric() else \
           "" if "1" == width else \
           "[{}:0] ".format(int(width) - 1)

  def name(self, name):
    if name in self.dictionary:
      return self.dictionary[name][0]
    else:
      # Raise an exception to alert the programmer that he/she just accessed a
      # nonexisting variable.
      raise CamelliaVerilogUnknownVariableError(name)

  def wires(self, **kwargs):
    """Derive wires from current object."""

    prefix = kwargs["prefix"] if "prefix" in kwargs.keys() else ""
    suffix = kwargs["suffix"] if "suffix" in kwargs.keys() else ""
    comment = kwargs["comment"] if "comment" in kwargs.keys() else ""

    return BundleWires({key: ("{}{}{}".format(prefix, val[0], suffix), val[1]) \
                       for key, val in self.items()}, \
                       comment)

  def regs(self, **kwargs):
    """Derive regs from current object."""

    prefix = kwargs["prefix"] if "prefix" in kwargs.keys() else ""
    suffix = kwargs["suffix"] if "suffix" in kwargs.keys() else ""
    # Use 0 as the default reset value.
    reset = kwargs["reset"] if "reset" in kwargs.keys() else "0"
    comment = kwargs["comment"] if "comment" in kwargs.keys() else ""

    return BundleRegs( \
        {key: ("{}{}{}".format(prefix, val[0], suffix), val[1], reset) \
        for key, val in self.items()}, \
        comment)

  def expr(self):
    """Derive expression from current object."""

    return BundleExpr({key: val[0] for key, val in self.items()})

  def eq(self, expr):
    """Create BundleEquation"""

    if type(expr) is str:
      dictionary = {}
      for line in expr.splitlines():
        spl = line.split()

        if 0 == len(spl):
          continue

        # Assign all lvals to the same value.
        if 1 == len(spl):
          if 0 == len(dictionary):
            return BundleEquation(self, spl[0])
          else:
            raise CamelliaVerilogSyntaxError()

        if not (3 == len(spl) and "=" == spl[1]):
          raise CamelliaVerilogSyntaxError()

        name, val = spl[0], spl[2]
        dictionary[name] = val

      expr = BundleExpr(dictionary)
    elif not (type(expr) is BundleExpr):
      raise CamelliaVerilogInvalidObjectError(expr)

    return BundleEquation(self, expr)


class BundleWires(BundleVar):
  def __init__(self, wires_desc, comment=""):
    """Initialization. It parses wires_str into a Wires object.

    Parameters
    ----------
    wires_desc : str/dict
      The description of wires. It can be either a string with multiple lines,
      or a dictionary.

      If wires_desc is a string, then the syntax would be like:
        1 clk         // width = 1, verilog_name = tag_name = clk
        1 clk clock   // width = 1, verilog_name = clk, tag_name = clock

      Otherwise it should be a dictionary in certain format like:
        { name : (verilog_name, verilog_width) }

    comment : str
      The comment generated above the variable.
    """

    dictionary = None
    if type(wires_desc) is dict:
      dictionary = wires_desc
    elif type(wires_desc) is str:
      dictionary = {}
      for line in wires_desc.splitlines():
        spl = line.split()
        # Escape empty lines.
        if 0 == len(spl):
          continue
        if 2 != len(spl) and 3 != len(spl):
          raise CamelliaVerilogSyntaxError()

        (width, verilog_name, tag_name) = \
            (spl[0], spl[1], spl[2] if 3 == len(spl) else spl[1])
        dictionary[tag_name] = (verilog_name, width)
    else:
      raise CamelliaVerilogInvalidObjectError(wires_desc)

    super().__init__(dictionary, comment)

  def verilog(self, indent, indent_level):
    ret = self.helper_comment_(indent, indent_level)
    for name, width in self.values():
      ret += (indent * indent_level) + "wire " + \
             self.helper_width_(width) + name + ";\n"
    return ret

class BundleRegs(BundleVar):
  def __init__(self, regs_desc, comment=""):
    """Initialization.

    Parameters
    ----------
      regs_desc : str/dictionary
        regs_desc describle the registers that we are to construct. It can be
        either a string in certain format, which will be parsed into a formatted
        dictionary later, or a dictionary that's parsed already.

        If it's a string, the syntax would be like:
          // width = 1, verilog_name = r_clk, name = clock, reset_val = 0
          1 r_clk clock 0
          // width = 1, verilog_name = r_clk, name = r_clk, reset_val = 0
          1 r_clk
          // width = 1, verilog_name = r_clk, name = r_clk, reset_val = 1
          1 r_clk - 1
          // width = 1, verilog_name = r_clk, name = clock, reset_val = 0
          1 r_clk clock

        Otherwise a dictionary should be provided. It's in a format like:
          { name : (verilog_name, verilog_width, reset_val) }

      comment : str
        The comment generated above the variable.
    """

    dictionary = None

    if type(regs_desc) is dict:
      dictionary = regs_desc
    elif type(regs_desc) is str:
      dictionary = {}
      for line in regs_desc.splitlines():
        spl = line.split()

        # Escape empty lines.
        if 0 == len(spl):
          continue

        if not (len(spl) >= 2 and len(spl) <= 4):
          raise CamelliaVerilogSyntaxError()

        (width, verilog_name, tag_name, reset_val) = \
            (spl[0], spl[1], spl[2], spl[3]) if 4 == len(spl) else \
            (spl[0], spl[1], spl[2], "0") if 3 == len(spl) else \
            (spl[0], spl[1], spl[1], "0")
        if "-" == tag_name:
          tag_name = verilog_name

        dictionary[tag_name] = (verilog_name, width, reset_val)
    else:
       raise CamelliaVerilogInvalidObjectError(regs_desc)

    super().__init__(dictionary, comment)

  def verilog(self, indent, indent_level):
    ret = self.helper_comment_(indent, indent_level)
    for name, width, reset_val in self.values():
      ret += (indent * indent_level) + "reg " + \
             self.helper_width_(width) + name + ";\n"
    return ret

  def reset(self):
    dictionary = {}
    for name, val in self.items():
      dictionary[name] = val[2]

    return BundleEquation(self, BundleExpr(dictionary))

  def set_reset(self, name, reset_val):
    self.dictionary[name][2] = reset_val

class BundlePorts(BundleVar):
  """Class to present Verilog modules ports"""

  def __init__(self, ports_desc, comment=""):
    """Initialization.

    Parameters
    ----------
    ports_desc : str/dict
      The description of ports. It can be either a string with multiple lines,
      or a dictionary that for internal direct use.

      If ports_desc is a string, then its syntax would be like:
        // input, width = 1, verilog_name = tag_name = clk
        in 1 clk
        // output, width = 1, verilog_name = rst_n, tag_name = reset
        out 1 rst_n reset

      Otherwise it should be a dictionary in certain format like:
        { name : (verilog_name, verilog_width, direction) }

    comment : str
      The comment text generated above the variable.
    """

    dictionary = None
    if type(ports_desc) is dict:
      dictionary = ports_desc
    elif type(ports_desc) is str:
      dictionary = {}
      # Validate port definition strings.
      for line in ports_desc.splitlines():
        spl = line.split()
        if 0 == len(spl):
          continue
        if 3 != len(spl) and 4 != len(spl):
          raise CamelliaVerilogSyntaxError()

        (direct, width, verilog_name, tag_name) = \
            (spl[0], spl[1], spl[2], spl[3] if 4 == len(spl) else spl[2])
        dictionary[tag_name] = (verilog_name, width, direct)
    else:
      raise CamelliaVerilogInvalidObjectError(ports_desc)

    super().__init__(dictionary, comment)

  def verilog(self, indent, indent_level):
    ret = self.helper_comment_(indent, indent_level)
    for name, width, direct in self.values():
      ret += (indent * indent_level) + "{}put ".format(direct) + \
             self.helper_width_(width) + name + ",\n"
    return ret

  def inputs(self):
    return BundlePorts({key: val
                        for key, val in self.items() if "in" == val[2]})

  def outputs(self):
    return BundlePorts({key: val
                        for key, val in self.items() if "out" == val[2]})

  def flip(self):
    """Flip the directions in current object. Turn input ports as output, and
    vice versa.
    """

    return BundlePorts({key: \
                        (val[0], val[1], "in" if "out" == val[2] else "out") \
                        for key, val in self.items()})


class BundleExpr(Bundle):
  def __init__(self, dictionary):
    """Initialization.

    Parameters
    ----------
    dictionary : {name: expression}
      A list of Verilog expressions which can be accessed with names.
    """

    super().__init__(dictionary)

  def apply(self, func):
    return BundleExpr(
        {key: func(expr) for key, expr in self.items()})


class BundleEquation(Bundle):
  """A special kind of bundle that defines the connectivity between variables
  and expressions.
  """

  def __init__(self, lval, rval):
    """Equation initialization.

    Parameters
    ----------
    lval :
      The left value variable that's assigned.
    rval :
      The right value that provides the expression as the value to assign.
    """

    # Validate lval and rval.
    if not (type(lval) is BundleVar or type(lval) is BundlePorts or \
            type(lval) is BundleRegs or type(lval) is BundleWires):
      raise CamelliaVerilogValTypeError(lval)
    if not (type(rval) is BundleExpr or type(rval) is str):
      raise CamelliaVerilogValTypeError(rval)

    # Fields: (lval, rval)
    dictionary = {}
    if type(rval) is str:
      for name, val in lval.items():
        dictionary[name] = (val[0], rval)
    else:
      for name, val in lval.items():
        if name in rval.keys():
          (rval_expr) = rval.get(name)
          if type(lval) is BundlePorts and "in" == val[2]:
            # Swap lval and rval's position if lval is input.
            dictionary[name] = (rval_expr, val[0])
          else:
            dictionary[name] = (val[0], rval_expr)

    super().__init__(dictionary)
