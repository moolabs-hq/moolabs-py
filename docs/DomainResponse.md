# DomainResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** |  | 
**domain_type** | **str** |  | [optional] 
**verification_status** | **str** |  | 
**last_checked_at** | **str** |  | 
**dns_records** | **Dict[str, object]** |  | [optional] 

## Example

```python
from moolabs.models.domain_response import DomainResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DomainResponse from a JSON string
domain_response_instance = DomainResponse.from_json(json)
# print the JSON string representation of the object
print(DomainResponse.to_json())

# convert the object into a dict
domain_response_dict = domain_response_instance.to_dict()
# create an instance of DomainResponse from a dict
domain_response_from_dict = DomainResponse.from_dict(domain_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


