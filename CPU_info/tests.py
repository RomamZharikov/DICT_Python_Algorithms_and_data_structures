from cpu_info import CPUInfo
from generator import Generator


def test_cpu_info():
    t = CPUInfo("AMD", "7 4700G", "AM4", [8, 8], [2.6, 3.64], 22)
    assert t.Manufacturer == "AMD"
    assert t.Model == "7 4700G"
    assert t.Socket == "AM4"
    assert t.Cores == [8, 8]
    assert t.Frequency == [2.6, 3.64]
    assert t.TDP == 22


def test_person_getinfo():
    t = CPUInfo("AMD", "7 4700G", "AM4", [8, 8], [2.6, 3.64], 22)
    assert isinstance(t.get_info(), str)


def test_gen_single_types():
    g = Generator()
    g_one = g.generator()
    assert isinstance(g_one, CPUInfo)
    assert isinstance(g_one.Manufacturer, str)
    assert isinstance(g_one.Model, str)
    assert isinstance(g_one.Socket, str)
    assert isinstance(g_one.Cores, list)
    assert isinstance(g_one.Frequency, list)
    assert isinstance(g_one.TDP, int)


def test_gen_1000_type():
    g = Generator()
    g_1000 = g.generate_1000()
    assert isinstance(g_1000, list)
    assert isinstance(g_1000[0], CPUInfo)
    assert len(g_1000) == 1000


def test_gen_10_000_type():
    g = Generator()
    g_10_000 = g.generate_10_000()
    assert isinstance(g_10_000, list)
    assert isinstance(g_10_000[0], CPUInfo)
    assert len(g_10_000) == 10000
