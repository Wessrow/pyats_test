"""

"""

import logging
from pyats import aetest

logger =logging.getLogger(__name__)

class common(aetest.CommonSetup):
    """
    """

    @aetest.subsection
    def connect(self, testbed):
        """asdf"""
        testbed.connect(log_stdout=False)

class IsDefaultRoute(aetest.Testcase):

    @aetest.setup
    def setup(self, testbed):
        """asdf"""
        self.routing = {}

        for device_name, device in testbed.devices.items():
            self.routing[device_name] = device.learn("routing").info

    @aetest.test
    def test_default_route(self, steps):
        for device, vrfs in self.routing.items():
            logger.info(device)
            with steps.start(
                device
            ) as device_step:
                for vrf_name, vrf in vrfs["vrf"].items():
                    with device_step.start(
                        vrf_name, continue_=True
                    ) as vrf_step:
                        if "0.0.0.0/0" not in vrf["address_family"]["ipv4"]["routes"].keys():
                            vrf_step.failed(
                                f"{vrf_name} has no default-route ):"
                            )

if __name__ == "__main__":

    aetest.main()
