from generator import Generator
from cpu_info import CPUInfo

if __name__ == "__main__":
    gen = Generator()
    for j in gen.generate_10_000():
        print(j)