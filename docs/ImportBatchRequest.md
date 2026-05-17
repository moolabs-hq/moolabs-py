# ImportBatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_provider** | **str** | &#39;aws&#39;, &#39;gcp&#39;, or &#39;azure&#39; | 
**billing_period_start** | **datetime** |  | 
**billing_period_end** | **datetime** |  | 
**rows** | [**List[CloudCostRowInput]**](CloudCostRowInput.md) |  | 
**reporting_currency** | **str** |  | [optional] [default to 'USD']

## Example

```python
from moolabs.models.import_batch_request import ImportBatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ImportBatchRequest from a JSON string
import_batch_request_instance = ImportBatchRequest.from_json(json)
# print the JSON string representation of the object
print(ImportBatchRequest.to_json())

# convert the object into a dict
import_batch_request_dict = import_batch_request_instance.to_dict()
# create an instance of ImportBatchRequest from a dict
import_batch_request_from_dict = ImportBatchRequest.from_dict(import_batch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


