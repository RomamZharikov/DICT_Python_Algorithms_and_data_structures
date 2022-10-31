from cpu_specifications import cpu_dict_amd, cpu_dict_intel


class CPUInfo:
    __manufacturer: str
    __model: str
    __socket: str
    __cores: list
    __frequency: list
    __tdp: int

    def __init__(self, manufacturer: str, model: str, socket: str, cores: list, frequency: list, tdp: int):
        self._Manufacturer = manufacturer
        self._Model = model
        self._Socket = socket
        self._Cores = cores
        self._Frequency = frequency
        self._TDP = tdp

    def __repr__(self) -> str:
        return f"{self._Manufacturer}, {self._Model}, {self._Socket}, {self._Cores}, {self._Frequency}, {self._TDP}"

    def __print_unknown(self) -> str:
        return f"""Процессор {self._Manufacturer} {self._Model} с характеристиками:
            *сокет: {self._Socket}
            *количество ядер: {self._Cores} 
            *частота: {self._Frequency}
            *тепловыделение: {self._TDP} 
относится к бюджетной или серверной линейке процессоров"""

    def __print_known(self, line, segment) -> str:
        return f"""Процессор {self._Manufacturer} {line} {self._Model} относится к {segment} серии с характеристиками: 
            *сокет: {self._Socket}
            *количество ядер: {self._Cores[0]}
            *количество потоков: {self._Cores[1]}
            *частота: {self._Frequency[0]}
            *частота (Turbo boost): {self._Frequency[1]}
            *тепловыделение: {self._TDP} """

    def get_info(self) -> str:
        line = None
        segment = None
        if len(str(self._Model).split()) == 1:
            if self._Manufacturer == "Intel":
                for i in cpu_dict_intel.keys():
                    if str(self._Model).upper() in i:
                        line = cpu_dict_intel[i]
                        print(type(cpu_dict_intel[i]))
                        break
            elif self._Manufacturer == "AMD":
                for i in cpu_dict_amd.keys():
                    if str(self._Model).upper() in i:
                        line = cpu_dict_amd.get(i)
        elif len(str(self._Model).split()) == 2:
            line, self._Model = str(self._Model).split()
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
            return self.__print_unknown()
        else:
            return self.__print_known(line, segment)
