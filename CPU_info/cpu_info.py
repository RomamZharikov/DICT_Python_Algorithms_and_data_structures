from cpu_specifications import cpu_dict_amd, cpu_dict_intel


class CPUInfo:
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

    def __repr__(self) -> str:
        return f"{self.Manufacturer}, {self.Model}, {self.Socket}, {self.Cores}, {self.Frequency}, {self.TDP}"

    def print_unknown(self) -> str:
        return f"""Процессор {self.Manufacturer} {self.Model} с характеристиками:
            *сокет: {self.Socket}
            *количество ядер: {self.Cores} 
            *частота: {self.Frequency}
            *тепловыделение: {self.TDP} 
относится к бюджетной или серверной линейке процессоров"""

    def print_known(self, line, segment) -> str:
        return f"""Процессор {self.Manufacturer} {line} {self.Model} относится к {segment} серии с характеристиками: 
            *сокет: {self.Socket}
            *количество ядер: {self.Cores[0]}
            *количество потоков: {self.Cores[1]}
            *частота: {self.Frequency[0]}
            *частота (Turbo boost): {self.Frequency[1]}
            *тепловыделение: {self.TDP} """

    def get_info(self) -> str:
        line = None
        segment = None
        if len(str(self.Model).split()) == 1:
            if self.Manufacturer == "Intel":
                for i in cpu_dict_intel.keys():
                    if str(self.Model).upper() in i:
                        line = cpu_dict_intel[i]
                        print(type(cpu_dict_intel[i]))
                        break
            elif self.Manufacturer == "AMD":
                for i in cpu_dict_amd.keys():
                    if str(self.Model).upper() in i:
                        line = cpu_dict_amd.get(i)
        elif len(str(self.Model).split()) == 2:
            line, self.Model = str(self.Model).split()
        else:
            line = None
        if line is not None:
            line.split()
            if line[-1] == "9":
                segment = "топовой"
            elif line[-1] == "7":
                segment = "производительной"
            elif line[-1] == "5":
                segment = "средней"
            else:
                segment = "бюджетной"
        if line is None:
            return self.print_unknown()
        else:
            return self.print_known(line, segment)


def test_cpu_info():
    t = CPUInfo("AMD", "7 4700G", "AM4", [8, 8], [2.6, 3.64], 22)
