# TopupDefaultsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_mode** | **str** |  | [optional] 
**cooldown_hours** | **float** |  | [optional] 
**daily_cap** | **int** |  | [optional] 
**threshold_template** | **str** |  | [optional] 

## Example

```python
from moolabs.models.topup_defaults_request import TopupDefaultsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TopupDefaultsRequest from a JSON string
topup_defaults_request_instance = TopupDefaultsRequest.from_json(json)
# print the JSON string representation of the object
print(TopupDefaultsRequest.to_json())

# convert the object into a dict
topup_defaults_request_dict = topup_defaults_request_instance.to_dict()
# create an instance of TopupDefaultsRequest from a dict
topup_defaults_request_from_dict = TopupDefaultsRequest.from_dict(topup_defaults_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


