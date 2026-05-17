# AlgorithmInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | 
**grade** | **str** |  | 
**confidence** | **float** |  | 

## Example

```python
from moolabs.models.algorithm_info import AlgorithmInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AlgorithmInfo from a JSON string
algorithm_info_instance = AlgorithmInfo.from_json(json)
# print the JSON string representation of the object
print(AlgorithmInfo.to_json())

# convert the object into a dict
algorithm_info_dict = algorithm_info_instance.to_dict()
# create an instance of AlgorithmInfo from a dict
algorithm_info_from_dict = AlgorithmInfo.from_dict(algorithm_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


