# TopConsumer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** |  | 
**total_cost** | **float** |  | 
**request_count** | **int** |  | 
**rank** | **int** |  | 

## Example

```python
from moolabs.models.top_consumer import TopConsumer

# TODO update the JSON string below
json = "{}"
# create an instance of TopConsumer from a JSON string
top_consumer_instance = TopConsumer.from_json(json)
# print the JSON string representation of the object
print(TopConsumer.to_json())

# convert the object into a dict
top_consumer_dict = top_consumer_instance.to_dict()
# create an instance of TopConsumer from a dict
top_consumer_from_dict = TopConsumer.from_dict(top_consumer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


