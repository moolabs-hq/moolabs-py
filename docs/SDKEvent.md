# SDKEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**usage_event_id** | **str** |  | 
**request_id** | **str** |  | 
**tenant_id** | **str** |  | [optional] 
**customer_id** | **str** |  | [optional] 
**feature_key** | **str** |  | [optional] 
**spans** | [**List[SDKSpan]**](SDKSpan.md) |  | 
**expected_span_count** | **int** | Informational only — the server does NOT reject the event when len(spans) !&#x3D; expectedSpanCount. Provided by the SDK for client-side reconciliation / observability; the contract is documented in the rev 3 sdk-cost-capability-acute-backing contracts doc §4.4 / CONTRACT-Q6 RESOLVED. | [optional] 
**timestamp** | **datetime** |  | 

## Example

```python
from moolabs.models.sdk_event import SDKEvent

# TODO update the JSON string below
json = "{}"
# create an instance of SDKEvent from a JSON string
sdk_event_instance = SDKEvent.from_json(json)
# print the JSON string representation of the object
print(SDKEvent.to_json())

# convert the object into a dict
sdk_event_dict = sdk_event_instance.to_dict()
# create an instance of SDKEvent from a dict
sdk_event_from_dict = SDKEvent.from_dict(sdk_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


