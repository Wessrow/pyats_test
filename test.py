"""

"""

from pyats import aetest

class common(aetest.CommonSetup):
    """
    """

    @aetest.subsection
    def connect(self, testbed):
        """asdf"""
        testbed.connect(log_stdout=False)

class TEST(aetest.Testcase):

    @aetest.setup
    def setup(self, testbed):
        """asdf"""
        self.routing = {}

        for device_name, device in testbed.devices.items():
            self.routing[device_name] = device.learn("routing").info

    @aetest.test
    def test(self):
        import json
        print(json.dumps(self.routing, indent=2))

if __name__ == "__main__":

    aetest.main()
