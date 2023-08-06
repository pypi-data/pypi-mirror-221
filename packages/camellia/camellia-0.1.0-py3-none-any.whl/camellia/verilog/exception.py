# Common exceptions defined in camellia.verilog.

class CamelliaVerilogAssignError(Exception):
  def __init__(self, name):
    self.message = "Fail to assign '{}'".format(name)
    super().__init__(self.message)

class CamelliaVerilogUnknownVariableError(Exception):
  def __init__(self, name):
    self.message = "Unknown variable name '{}'".format(name)
    super().__init__(self.message)

class CamelliaVerilogSyntaxError(Exception):
  def __init__(self):
    self.message = "Camellia syntax error"
    super().__init__(self.message)

class CamelliaVerilogValTypeError(Exception):
  def __init__(self, val):
    self.message = "Invalid val {} {}".format(val.__name__, val.__class__)
    super().__init__(self.message)

class CamelliaVerilogInputAsLvalError(Exception):
  def __init__(self, name):
    self.message = "Input {} can't be lval".format(name)
    super().__init__(self.message)

class CamelliaVerilogInvalidObjectError(Exception):
  def __init__(self, obj):
    self.message = "Invalid object type '{}'".format(type(obj))
    super().__init__(self.message)

class CamelliaVerilogUnknownParameterError(Exception):
  def __init__(self, param_name):
    self.message = "Unknown parameter '{}'".format(param_name)
    super().__init__(self.message)

class CamelliaVerilogUnknownPortError(Exception):
  def __init__(self, port_name):
    self.message = "Unknown port '{}'".format(port_name)
    super().__init__(self.message)

class CamelliaVerilogUndrivenInputError(Exception):
  def __init__(self, port_name):
    self.message = "Undriven input port '{}'".format(port_name)
    super().__init__(self.message)

class CamelliaVerilogPortConflictError(Exception):
  def __init__(self, port_name):
    self.message = "Port conflict with '{}'".format(port_name)
    super().__init__(self.message)
