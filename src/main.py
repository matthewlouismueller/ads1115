import asyncio
from typing import Any, ClassVar, Final, List, Mapping, Optional, Sequence

from typing_extensions import Self
from viam.components.sensor import Sensor
from viam.module.module import Module
from viam.proto.app.robot import ComponentConfig
from viam.proto.common import ResourceName
from viam.resource.base import ResourceBase
from viam.resource.easy_resource import EasyResource
from viam.resource.types import Model, ModelFamily
from viam.utils import SensorReading, struct_to_dict

import Adafruit_ADS1x15
import time

class adc(Sensor, EasyResource):
    MODEL: ClassVar[Model] = Model(ModelFamily("kodama", "ads1115"), "adc")

    @classmethod
    def new(
        cls, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]
    ) -> Self:
        """This method creates a new instance of this Sensor component.
        The default implementation sets the name from the `config` parameter and then calls `reconfigure`.

        Args:
            config (ComponentConfig): The configuration for this resource
            dependencies (Mapping[ResourceName, ResourceBase]): The dependencies (both implicit and explicit)

        Returns:
            Self: The resource
        """
        return super().new(config, dependencies)

    @classmethod
    def validate_config(cls, config: ComponentConfig) -> Sequence[str]:
        """This method allows you to validate the configuration object received from the machine,
        as well as to return any implicit dependencies based on that `config`.

        Args:
            config (ComponentConfig): The configuration for this resource

        Returns:
            Sequence[str]: A list of implicit dependencies
        """
        fields = config.attributes.fields

        if "i2c_address" in fields:
            if not fields["i2c_address"].HasField("string_value"):
                raise Exception("i2c_address must be a valid string.")
            
        if "i2c_bus" in fields:
            if not fields["i2c_bus"].HasField("number_value"):
                raise Exception("i2c_bus must be a valid integer.")
        
        if "ch0_gain" in fields:
            if not fields["ch0_gain"].HasField("number_value"):
                raise Exception("ch0_gain must be a valid integer.")
        if "ch1_gain" in fields:
            if not fields["ch1_gain"].HasField("number_value"):
                raise Exception("ch1_gain must be a valid integer.")
        if "ch2_gain" in fields:
            if not fields["ch2_gain"].HasField("number_value"):
                raise Exception("ch2_gain must be a valid integer.")
        if "ch3_gain" in fields:
            if not fields["ch3_gain"].HasField("number_value"):
                raise Exception("ch3_gain must be a valid integer.")

        return []

    def reconfigure(
        self, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]
    ):
        """This method allows you to dynamically update your service when it receives a new `config` object.

        Args:
            config (ComponentConfig): The new configuration
            dependencies (Mapping[ResourceName, ResourceBase]): Any dependencies (both implicit and explicit)
        """
        attrs = struct_to_dict(config.attributes)
        self.i2c_address = attrs.get("i2c_address", 0x48)
        if isinstance(self.i2c_address,str):
            address_json = {
                "0x48": 0x48,
                "0x49": 0x49,
                "0x4A": 0x4A,
                "0x4B": 0x4B
            }
            try:
                self.i2c_address = address_json[self.i2c_address]
            except:
                self.i2c_address = 0x48
        self.i2c_bus = attrs.get("i2c_bus", 1)
        self.ch0_gain = attrs.get("ch0_gain", 1)
        self.ch1_gain = attrs.get("ch1_gain", 1)
        self.ch2_gain = attrs.get("ch2_gain", 1)
        self.ch3_gain = attrs.get("ch3_gain", 1)
        return super().reconfigure(config, dependencies)

    async def get_readings(
        self,
        *,
        extra: Optional[Mapping[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs
    ) -> Mapping[str, SensorReading]:
        
        adc = Adafruit_ADS1x15.ADS1015(address=self.i2c_address, busnum=int(self.i2c_bus))

        chan0 = adc.read_adc(0, gain=self.ch0_gain)
        time.sleep(0.1)
        chan1 = adc.read_adc(1, gain=self.ch1_gain)
        time.sleep(0.1)
        chan2 = adc.read_adc(2, gain=self.ch2_gain)
        time.sleep(0.1)
        chan3 = adc.read_adc(3, gain=self.ch3_gain)

        # Return a dictionary of the readings
        return {
            "chan0": chan0,
            "chan1": chan1,
            "chan2": chan2,
            "chan3": chan3
        }

if __name__ == "__main__":
    asyncio.run(Module.run_from_registry())

