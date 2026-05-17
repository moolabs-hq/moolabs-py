# PTPFulfillRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_id** | **str** |  | 
**amount_micros** | **int** |  | 

## Example

```python
from moolabs.models.ptp_fulfill_request import PTPFulfillRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PTPFulfillRequest from a JSON string
ptp_fulfill_request_instance = PTPFulfillRequest.from_json(json)
# print the JSON string representation of the object
print(PTPFulfillRequest.to_json())

# convert the object into a dict
ptp_fulfill_request_dict = ptp_fulfill_request_instance.to_dict()
# create an instance of PTPFulfillRequest from a dict
ptp_fulfill_request_from_dict = PTPFulfillRequest.from_dict(ptp_fulfill_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


