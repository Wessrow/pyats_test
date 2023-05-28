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

class TestDefaultRoute(aetest.Testcase):

    @aetest.setup
    def setup(self, testbed):
        """asdf"""
        self.routing = {}

        for device_name, device in testbed.devices.items():
            self.routing[device_name] = device.learn("routing").info

    @aetest.test
    def test_default_route(self, steps):
        """asdf"""
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
                                f"VRF: {vrf_name} - No default route present."
                            )

class TestBGP(aetest.Testcase):

    @aetest.setup
    def setup(self, testbed):
        """asdf"""
        self.routing = {}

        for device_name, device in testbed.devices.items():
            self.routing[device_name] = device.learn("bgp").info

    @aetest.test
    def test_bgp_peers(self, steps):
        """asdf"""

        # import json
        # print(json.dumps(self.routing, indent=2))

        for device, vrfs in self.routing.items():
            logger.info(device)
            with steps.start(
                device
            ) as device_step:
                for vrf_name, vrf in vrfs["instance"]["default"]["vrf"].items():
                    if "neighbor" in vrf.keys():
                        with device_step.start(
                            vrf_name, continue_=True
                        ) as vrf_step:
                            for neighbor, data in vrf["neighbor"].items():
                                if data["session_state"].lower() != "established":
                                    vrf_step.failed(
                                        f"Neighbor: {neighbor} - Status: {data['session_state']}"
                                    )



if __name__ == "__main__":

    aetest.main()
