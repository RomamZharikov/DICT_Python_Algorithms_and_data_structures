from cpu_specifications import cpu_dict_amd, cpu_dict_intel


class CPUInfo(object):
    def __init__(self, manufacturer, model, socket, cores, frequency, tdp):
        self.Manufacturer = manufacturer
        self.Model = model
        self.Socket = socket
        self.Cores = cores
        self.Frequency = frequency
        self.TDP = tdp

    def print_unknown(self):
        print(f"""Процессор {self.Manufacturer} {self.Model} с характеристиками:
            *сокет: {self.Socket}
            *количество ядер: {self.Cores} 
            *частота: {self.Frequency}
            *тепловыделение: {self.TDP} 
относится к бюджетной или серверной линейке процессоров""")

    def print_known(self, line, segment):
        print(f"""Процессор {self.Manufacturer} {line} {self.Model} относится к {segment} серии с характеристиками: 
            *сокет: {self.Socket}
            *количество ядер: {self.Cores}
            *частота: {self.Frequency}
            *тепловыделение: {self.TDP} """)

    def get_info(self):
        line = str
        segment = str
        if len(str(self.Model).split()) == 1:
            if self.Manufacturer == "Intel":
                for i in cpu_dict_intel.keys():
                    if str(self.Model).upper() in i:
                        line = cpu_dict_intel.get(i)
                        break
                if line == str:
                    line = ""
            elif self.Manufacturer == "AMD":
                for i in cpu_dict_amd.keys():
                    if str(self.Model).upper() in i:
                        line = cpu_dict_amd.get(i)
                        break
                    if line == str:
                        line = ""
            else:
                line = ""
        elif len(str(self.Model).split()) == 2:
            line, self.Model = str(self.Model).split()
        else:
            line = ""
        if line != "":
            if line[-1] == "9":
                segment = "топовой"
            elif line[-1] == "7":
                segment = "производительной"
            elif line[-1] == "5":
                segment = "средней"
            else:
                segment = "бюджетной"
        if line == "":
            self.print_unknown()
        else:
            self.print_known(line, segment)


if __name__ == "__main__":
    intelI7 = CPUInfo("Intel", "i9 9900KF", "1151", "8", "3.60 (5.0 Turbo)", "95")
    intelI7.get_info()
