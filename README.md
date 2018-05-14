# KIWI.KI Client

This is the unofficial KIWI.KI Client Library. Checkout the KIWI.KI API here: https://developer.kiwi.ki/

## Example

```python
import json
from kiwiki import KiwiClient, KiwiException

client = KiwiClient(username='foobar@example.com', password='supersecret')

# Get a list of all my doors
my_doors = client.get_locks()
print(json.dumps(my_doors, indent=2, sort_keys=True))
#[
#  {
#    "address": {
#      "city": "Berlin",
#      "country": "DE",
#      "lat": 52.55657169,
#      "lng": 13.66660845,
#      "postal_code": "10110",
#      "specifier": "SPEC_01",
#      "state": "Berlin",
#      "street": "Foo Street 23"
#    },
#    "can_invite": true,
#    "hardware_type": "DOOR",
#    "highest_permission": "IS_ADMIN",
#    "image": null,
#    "is_owner": true,
#    "sensor_id": 12345,
#    "sensor_name": null,
#    "sensor_uuid": "unavailable"
#  }
#]

# Now, open a door
try:
    client.open_door(12345)
except KiwiException as e:
    print(e)
```

# Installation

`pip install kiwiki-client`
