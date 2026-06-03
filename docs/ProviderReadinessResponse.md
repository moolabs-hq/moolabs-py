# ProviderReadinessResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ready** | **bool** |  | 
**from_address** | **str** |  | [optional] 
**verification_status** | **str** |  | [optional] 
**payment_instructions_ready** | **bool** |  | 
**blocking_reasons** | **List[str]** |  | 
**readiness_hash** | **str** |  | 

## Example

```python
from moolabs.models.provider_readiness_response import ProviderReadinessResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderReadinessResponse from a JSON string
provider_readiness_response_instance = ProviderReadinessResponse.from_json(json)
# print the JSON string representation of the object
print(ProviderReadinessResponse.to_json())

# convert the object into a dict
provider_readiness_response_dict = provider_readiness_response_instance.to_dict()
# create an instance of ProviderReadinessResponse from a dict
provider_readiness_response_from_dict = ProviderReadinessResponse.from_dict(provider_readiness_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


