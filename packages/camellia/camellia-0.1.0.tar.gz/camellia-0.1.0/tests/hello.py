from camellia import verilog
import unittest

class TestHello(unittest.TestCase):
  def test_hello(self):
    module = verilog.Module("hello")

    module.params("""DATA_WIDTH = 32
                  ADDR_WIDTH = 32""")

    clk_ports = module.ports("clock", """
      in 1 clk
      in 1 rst_n
    """, "Clock and reset.")
    din_ports = module.ports("in_data", """
      in DATA_WIDTH din data
      in ADDR_WIDTH ain addr
    """)
    dout_ports = module.ports("out_data", din_ports.flip())

    d_regs = module.claim(verilog.Regs("""
      DATA_WIDTH r_data data
      ADDR_WIDTH r_addr addr
    """, "Registers to store input data"))

    module.always("posedge clk or negedge rst_n",
      verilog.If("!rst_n",
        d_regs.eq("32'd0")
      ).Elif("0 == {}".format(din_ports.name("addr")),
        d_regs.eq("""
          data = 32'd1
          addr = 32'hffff_ffff
        """)
      ).Else(
        d_regs.eq(din_ports.expr())
      )
    )

    module.claim(dout_ports.eq(d_regs.expr()))

    mod2 = verilog.Module("world")
    mod2.claim(module.inst("module_inst", params="""
      DATA_WIDTH = 32
    """, ports={
      module.get_ports("clock").eq("0"),
      module.get_ports("in_data").eq("0")
    }))

    mod2.initial(module.get_ports("clock").eq("""
      clk = 0'b0
      rst_n = 1'b1
    """))

    print(module)
    print(mod2)
