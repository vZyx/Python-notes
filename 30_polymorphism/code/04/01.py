
from abc import ABC, abstractmethod

class ICameraDevice(ABC):
    @abstractmethod
    def get_version(self):
        pass

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class UbuntuDriverOpenSource(ICameraDevice):
    pass  # Override methods

class UbuntuDriver3rdPart(ICameraDevice):
    pass  # Override methods

class Windows10Driver(ICameraDevice):
    pass  # Override methods


class UbuntuOS:
    def get_app(self, app_name):
        return UbuntuDriverOpenSource()

if __name__ == '__main__':
    os = UbuntuOS()
    device = os.get_app('camera cheese')
    device.start()
    device.stop()