# Module ads1115 

Provide a description of the purpose of the module and any relevant information.

## Model kodama:ads1115:adc

Provide a description of the model and any relevant information.

### Configuration
The following attribute template can be used to configure this model:

```json
{
  "i2c_address":"0x48",
  "i2c_bus":1
}
```

#### Attributes

The following attributes are available for this model:

| Name          | Type   | Inclusion | Description                |
|---------------|--------|-----------|----------------------------|
| `i2c_address` | string  | Optional  | i2c address of ADS1115 sensor (default is 0x48) |
| `i2c_bus` | int | Optional  | i2c bus number (default is 1) |

#### Example Configuration

```json
{
  "i2c_address":"0x48",
  "i2c_bus":1
}
```
