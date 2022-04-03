from cpu_info import CPUInfo
from generator import Generator


def test_cpu_info():
    t = CPUInfo("AMD", "7 4700G", "AM4", [8, 8], [2.6, 3.64], 22)
    assert t.manufacturer == "AMD"
    assert t.model == "7 4700G"
    assert t.socket == "AM4"
    assert t.cores == [8, 8]
    assert t.frequency == [2.6, 3.64]
    assert t.tdp == 22


def test_gen_single_types():
    g = Generator()
    g_one = g.generator()
    assert isinstance(g_one, CPUInfo)
    assert isinstance(g_one.manufacturer, str)
    assert isinstance(g_one.model, str)
    assert isinstance(g_one.socket, str)
    assert isinstance(g_one.cores, list)
    assert isinstance(g_one.frequency, list)
    assert isinstance(g_one.tdp, int)


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
