from abc import abstractmethod
from lesson_20_02_20.structure_driver import JSONFileDriver, JSONStringDriver, PickleDriver


class SDBuilder:
    @abstractmethod
    def build(self):
        return None


class JSONFileBuilder(SDBuilder):
    def build(self):
        filename = input('Enter filename (.json)>')
        return JSONFileDriver(filename)


class JSONStrBuilder(SDBuilder):
    def build(self):
        return JSONStringDriver()


class PickleBuilder(SDBuilder):
    def build(self):
        filename = input('Enter filename (.bin)>')
        return PickleDriver(filename)


class SDFabric:
    def get_sd_driver(self, driver_name):
        builders = {'json': JSONFileBuilder,
                    'json_str': JSONStrBuilder,
                    'pickle': PickleBuilder}
        try:
            return builders[driver_name]()
        except:
            return SDBuilder()


if __name__ == "__main__":
    driver_name = input('Please enter driver name >')
    driver_builder = SDFabric().get_sd_driver(driver_name)
    print(driver_builder.build())