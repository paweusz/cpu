from registers import FourBitRegister
from registers import Register
from registers import REG_WIDTH

def test_register_eval():
    reg = FourBitRegister()

    reg.d[3] = 0
    reg.d[2] = 1
    reg.d[1] = 0
    reg.d[0] = 1

    reg.e = 1

    reg.eval()

    assert reg.q[3] == 0
    assert reg.q[2] == 1
    assert reg.q[1] == 0
    assert reg.q[0] == 1

    for i in range(REG_WIDTH):
        reg.d[i] = 0
    reg.e = 0

    reg.eval()

    assert reg.q[3] == 0
    assert reg.q[2] == 1
    assert reg.q[1] == 0
    assert reg.q[0] == 1

def test_register_str():
    reg = FourBitRegister()

    reg.d[3] = 0
    reg.d[2] = 1
    reg.d[1] = 0
    reg.d[0] = 1

    reg.e = 1

    reg.eval()

    assert reg.__str__() == 'E1\nDDDD\n0101\nQQQQ\n0101'

def test_register_load():
    reg = Register()
    reg.enable = 1

    reg.load = 1
    reg.clk = 1
    reg.d = 1
    reg.eval()
    assert reg.q == 1

    reg.load = 0
    reg.clk = 1
    reg.d = 0
    reg.eval()
    assert reg.q == 1

    reg.load = 1
    reg.clk = 0
    reg.d = 0
    reg.eval()
    assert reg.q == 1

    reg.load = 1
    reg.clk = 1
    reg.d = 0
    reg.eval()
    assert reg.q == 0

def test_register_enable():
    reg = Register()

    reg.load = 1
    reg.clk = 1
    reg.d = 1
    reg.enable = 1
    reg.eval()
    assert reg.q == 1

    reg.enable = 0
    reg.eval()
    assert reg.q == None

