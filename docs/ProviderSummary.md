# ProviderSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** |  | 
**model_count** | **int** |  | 

## Example

```python
from moolabs.models.provider_summary import ProviderSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderSummary from a JSON string
provider_summary_instance = ProviderSummary.from_json(json)
# print the JSON string representation of the object
print(ProviderSummary.to_json())

# convert the object into a dict
provider_summary_dict = provider_summary_instance.to_dict()
# create an instance of ProviderSummary from a dict
provider_summary_from_dict = ProviderSummary.from_dict(provider_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


