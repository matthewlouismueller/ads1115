# Module ads1115 

This module is for reading an ADS1115 analog to digital converter into Viam as a sensor over 12C.

## Model kodama:ads1115:adc

Currently, the model reads and returns all four analog input channels with a 0.1 second delay between each reading whenever ```get_readings()``` is called. Future work to support other modes of use for the ADS1115.

### Configuration
The following attribute template can be used to configure this model:

```json
{
  "i2c_address":"0x48",
  "i2c_bus":1,
  "ch0_gain":1,
  "ch1_gain":1,
  "ch2_gain":1,
  "ch3_gain":1
}
```

#### Attributes

The following attributes are available for this model:

| Name          | Type   | Inclusion | Description                |
|---------------|--------|-----------|----------------------------|
| `i2c_address` | string  | Optional  | i2c address of ADS1115 sensor (default is 0x48) |
| `i2c_bus` | int | Optional  | i2c bus number (default is 1) |
| `ch0_gain` | int | Optional  | gain for A0 reading (default is 1) |
| `ch1_gain` | int | Optional  | gain for A1 reading (default is 1) |
| `ch2_gain` | int | Optional  | gain for A2 reading (default is 1) |
| `ch3_gain` | int | Optional  | gain for A3 reading (default is 1) |

#### Example Configuration

```json
{
  "i2c_address":"0x48",
  "i2c_bus":1
}
```
