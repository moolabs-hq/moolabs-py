# AgingBucketDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket** | **str** |  | 
**case_count** | **int** |  | 
**total_outstanding_micros** | **int** |  | 
**percentage** | **float** |  | 

## Example

```python
from moolabs.models.aging_bucket_detail import AgingBucketDetail

# TODO update the JSON string below
json = "{}"
# create an instance of AgingBucketDetail from a JSON string
aging_bucket_detail_instance = AgingBucketDetail.from_json(json)
# print the JSON string representation of the object
print(AgingBucketDetail.to_json())

# convert the object into a dict
aging_bucket_detail_dict = aging_bucket_detail_instance.to_dict()
# create an instance of AgingBucketDetail from a dict
aging_bucket_detail_from_dict = AgingBucketDetail.from_dict(aging_bucket_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


