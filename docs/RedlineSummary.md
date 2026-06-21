# RedlineSummary

Verdict breakdown summary for a quick-redline response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**by_verdict** | **Dict[str, int]** |  | 
**total** | **int** |  | 

## Example

```python
from moolabs.models.redline_summary import RedlineSummary

# TODO update the JSON string below
json = "{}"
# create an instance of RedlineSummary from a JSON string
redline_summary_instance = RedlineSummary.from_json(json)
# print the JSON string representation of the object
print(RedlineSummary.to_json())

# convert the object into a dict
redline_summary_dict = redline_summary_instance.to_dict()
# create an instance of RedlineSummary from a dict
redline_summary_from_dict = RedlineSummary.from_dict(redline_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


