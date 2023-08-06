class Rawcode:
  """Raw Verilog code that's not modified."""

  def __init__(self, text):
    self.line_list = []

    for line in text.splitlines():
      self.line_list.append(line.strip())

  def verilog(self, indent, indent_level):
    text = ""
    for line in self.line_list:
      text += (indent * indent_level) if line else ""
      text += line + "\n"

    return text
