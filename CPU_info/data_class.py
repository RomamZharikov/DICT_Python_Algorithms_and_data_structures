class CPU:
    manufacturer: str
    model: str
    socket: str
    cores: str
    frequency: str
    tdp: str

    def __init__(self, manufacturer: str, model: str, socket: str, cores: str, frequency: str, tdp: str):
        self.Manufacturer = manufacturer
        self.Model = model
        self.Socket = socket
        self.Cores = cores
        self.Frequency = frequency
        self.TDP = tdp

    def get_info(self) -> str:
        return f"{self.Manufacturer}, {self.Model}, {self.Socket}, {self.Cores}, {self.Frequency}, {self.TDP}"

    def __repr__(self):
        return f"CPU {self.Manufacturer}, {self.Model}, {self.Socket}, {self.Cores}, {self.Frequency}, {self.TDP}"


if __name__ == "__main__":
    cpu = CPU("", "", "", "", "", "")
    print(cpu.get_info())
    cpu2 = CPU(1, 1, 1, 1, 1, 1)
    print(cpu2.get_info())
