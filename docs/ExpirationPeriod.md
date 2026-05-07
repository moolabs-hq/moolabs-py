# ExpirationPeriod

The grant expiration definition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration** | [**ExpirationDuration**](ExpirationDuration.md) | The unit of time for the expiration period. | 
**count** | **int** | The number of time units in the expiration period. | 

## Example

```python
from moolabs.models.expiration_period import ExpirationPeriod

# TODO update the JSON string below
json = "{}"
# create an instance of ExpirationPeriod from a JSON string
expiration_period_instance = ExpirationPeriod.from_json(json)
# print the JSON string representation of the object
print(ExpirationPeriod.to_json())

# convert the object into a dict
expiration_period_dict = expiration_period_instance.to_dict()
# create an instance of ExpirationPeriod from a dict
expiration_period_from_dict = ExpirationPeriod.from_dict(expiration_period_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


