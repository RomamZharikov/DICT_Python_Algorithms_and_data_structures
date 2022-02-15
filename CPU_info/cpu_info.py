class CPUInfo(object):
    def __init__(self, manufacturer, model, socket, cores, frequency, tdp):
        self.Manufacturer = manufacturer
        self.Model = model
        self.Socket = socket
        self.Cores = cores
        self.Frequency = frequency
        self.TDP = tdp

    def get_info(self):
        pass


if __name__ == "__main__":
    intelI7 = CPUInfo("Intel", "i7-7700K", "1151", "4", "", "4,2 (4,5 Turbo)")
    intelI7.get_info()

