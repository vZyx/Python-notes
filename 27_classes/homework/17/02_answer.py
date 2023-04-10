"""
Our goal is the load happens only once: All objects see the same loaded data?
This should trigger static variables.

Let's formulate the problem in another way
Can we have only a single instance loading the data, and every new object is just using the old instance?
This is solved using the singleton design pattern! It is a very common problem.

It is hard to provide both simple and elegant solutions.

Below is one ok way to do that(mainly easy to understand)

We rename our old class and make it an inner class inside another one
The outer class will have a static instance from the inner class
With every request to init, we create only the inner object in the first call
I used @property to delegate calls for attributes
If there are methods, we can call the corresponding ones in the inner class

This should trigger questions about why this way and not this way?
    Please play with the code.
    Feel free to think in different ways

Future readings:
    https://stackoverflow.com/questions/31875/is-there-a-simple-elegant-way-to-define-singletons
    https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Singleton.html
    https://refactoring.guru/design-patterns/singleton/python/example

"""


class ConfigurationManger:
    __instance = None

    # Push the whole old class as inner one
    class ConfigurationMangerInner:
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
            time.sleep(2)

    def __init__(self, configuration_path):
        # If no instances created before, create one. This way we make it one for callers
        if not ConfigurationManger.__instance:
            ConfigurationManger.__instance = ConfigurationManger.ConfigurationMangerInner(configuration_path)

    # Delegate methods/attributes calls
    @property
    def configuration_path(self):
        return ConfigurationManger.__instance.configuration_path

    @configuration_path.setter
    def configuration_path(self, value):
        ConfigurationManger.__instance.configuration_path = value


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