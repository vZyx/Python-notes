
class ConfigurationManger:
    def __init__(self, configuration_path):
        self.configuration_path = configuration_path
        # Other attributes
        self._load()

    def _load(self):
        # takes 30 minutes to load data
        print('Loading the Configuration')
        self.servers_ips = ["10.20.30.40",
                            "10.20.30.41", "10.20.30.42"]
        self.aws_service_url = "amazon-aws.com"
        # load heavy data
        import time
        time.sleep(1)


def f1():
    mgr = ConfigurationManger('disk/config.json')
    print(mgr.configuration_path)

def f2():
    mgr = ConfigurationManger('disk/config.json')
    print(mgr.configuration_path)

def f3():
    mgr = ConfigurationManger('disk/config.json')
    print(mgr.configuration_path)

if __name__ == '__main__':
    f1()
    f1()
    f1()
    f2()
    f3()