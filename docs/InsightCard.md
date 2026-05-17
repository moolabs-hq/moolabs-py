# InsightCard


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | [**CardType**](CardType.md) |  | 
**title** | **str** |  | 
**description** | **str** |  | 
**cta_label** | **str** |  | 
**cta_route** | **str** |  | 
**priority** | [**Priority**](Priority.md) |  | 
**icon** | **str** |  | 
**icon_color** | **str** |  | 
**icon_bg** | **str** |  | 
**persona** | **List[str]** |  | 
**metric_value** | **str** |  | [optional] 

## Example

```python
from moolabs.models.insight_card import InsightCard

# TODO update the JSON string below
json = "{}"
# create an instance of InsightCard from a JSON string
insight_card_instance = InsightCard.from_json(json)
# print the JSON string representation of the object
print(InsightCard.to_json())

# convert the object into a dict
insight_card_dict = insight_card_instance.to_dict()
# create an instance of InsightCard from a dict
insight_card_from_dict = InsightCard.from_dict(insight_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


