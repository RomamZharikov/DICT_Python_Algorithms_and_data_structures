from random import choice
from cpu_specifications import cpu_dict_intel, cpu_dict_amd


class CPU:
    manufacturer: str
    model: str
    socket: str
    cores: list
    frequency: list
    tdp: int

    def __init__(self, manufacturer: str, model: str, socket: str, cores: list, frequency: list, tdp: int):
        self.Manufacturer = manufacturer
        self.Model = model
        self.Socket = socket
        self.Cores = cores
        self.Frequency = frequency
        self.TDP = tdp

    def get_info(self) -> str:
        return f"{self.Manufacturer}, {self.Model}, {self.Socket}, {self.Cores[0]} cores ({self.Cores[1]} threads), {self.Frequency[0]} frequency ({self.Frequency[1]} boost), {self.TDP} TDP"

    def __repr__(self):
        return f"CPU {self.Manufacturer}, {self.Model}, {self.Socket}, {self.Cores}, {self.Frequency}, {self.TDP}"


class Generator:
    def __create_manufacturer(self) -> str:
        self.manufacturers = choice(["Intel", "AMD"])
        return self.manufacturers

    def __create_model(self) -> str:
        if self.manufacturers == "Intel":
            self.model1 = choice([*cpu_dict_intel.keys()])
            self.model_num = cpu_dict_intel[self.model1]
        else:
            self.model1 = choice([*cpu_dict_amd.keys()])
            self.model_num = cpu_dict_amd[self.model1]
        self.model = choice(self.model1)
        return f"{self.model_num} {self.model}"

    def __create_socket(self) -> str:
        if self.manufacturers == "Intel":
            if self.model_num[-1] == "3":
                if len(self.model[0]) == 3 or self.model[0] == "L":
                    self.socket = "LGA 1156"
                elif int(self.model[0]) in [2, 3]:
                    self.socket = "LGA 1155"
                elif int(self.model[0]) == 4:
                    self.socket = "LGA 1155"
                elif int(self.model[0]) == 5:
                    self.socket = "BGA 1168"
                elif int(self.model[0]) in [6, 7, 8, 9]:
                    self.socket = "LGA 1151"
                elif int(self.model[0: 2]) == 10:
                    self.socket = "BGA 1528"
                elif int(self.model[0: 2]) == 11:
                    self.socket = "BGA 1449"
            elif self.model_num[-1] == "5":
                if len(self.model[0]) == 3 or self.model[0] == "L":
                    self.socket = "LGA 1156"
                elif int(self.model[0]) in [2, 3]:
                    self.socket = "LGA 1155"
                elif int(self.model[0]) in [4, 5]:
                    self.socket = "LGA 1150"
                elif int(self.model[0]) in [6, 7, 8, 9]:
                    self.socket = "LGA 1151"
                elif int(self.model[0: 2]) == 10:
                    self.socket = "BGA 1528"
                elif int(self.model[0: 2]) == 11:
                    self.socket = "BGA 1449"
                elif int(self.model[0: 2]) == 12:
                    self.socket = "LGA 1700"
            elif self.model_num[-1] == "7":
                if len(self.model[0]) == 3:
                    self.socket = "LGA 1156"
                elif int(self.model[0]) in [2, 3]:
                    self.socket = "LGA 1155"
                elif int(self.model[0]) in [4, 5]:
                    self.socket = "LGA 1150"
                elif int(self.model[0]) in [6, 7, 8, 9]:
                    self.socket = "LGA 1151"
                elif int(self.model[0: 2]) in [10, 11]:
                    self.socket = "BGA 1526"
            elif self.model_num[-1] == "9":
                if int(self.model[0]) == 7:
                    self.socket = "LGA 2066"
                elif self.model[0] in ["8", "9"]:
                    self.socket = "BGA 1440"
                elif int(self.model[0: 2]) in [10, 11, 12]:
                    self.socket = "LGA 1200"
        elif self.manufacturers == "AMD":
            self.socket = "AM4"
        return self.socket

    def __create_cores_threads(self) -> list:
        if self.model_num[-1] == "3":
            cores = choice([2, 4])
            threads = choice([cores * 2, cores])
        elif self.model_num[-1] == "5":
            cores = choice([4, 6, 8])
            threads = choice([cores * 2, cores])
        elif self.model_num[-1] == "7":
            cores = choice([6, 8, 10])
            threads = choice([cores * 2, cores])
        else:
            cores = choice([8, 10, 12])
            threads = choice([cores * 2, cores])
        return [cores, threads]

    def __create_frequency(self) -> list:
        frequency = round(int(self.model_num[-1]) / 5 + choice([1.1, 1.2, 1.3, 1.4, 1.5]), 2)
        frequency_boost = round(frequency * choice([1.1, 1.2, 1.3, 1.4, 1.5]), 2)
        return [frequency, frequency_boost]

    def __create_tdp(self) -> int:
        return int((int(self.model_num[-1]) + 2) * choice([10, 9.5, 6.5, 3.5, 2.5, 1.7]))

    def generator(self) -> CPU:
        return CPU(self.__create_manufacturer(), self.__create_model(), self.__create_socket(),
                   self.__create_cores_threads(), self.__create_frequency(), self.__create_tdp())

    def generate_1000(self) -> list:
        return [self.generator().get_info() for i in range(1000)]

    def generate_10_000(self) -> list:
        return [self.generator().get_info() for i in range(10_000)]


if __name__ == "__main__":
    cpu = Generator()
    for i in cpu.generate_10_000():
        print(i)
