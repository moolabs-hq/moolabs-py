# MeterQueryRequest

A meter query request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | Client ID Useful to track progress of a query. | [optional] 
**var_from** | **datetime** | Start date-time in RFC 3339 format.  Inclusive. | [optional] 
**to** | **datetime** | End date-time in RFC 3339 format.  Inclusive. | [optional] 
**window_size** | [**WindowSize**](WindowSize.md) | If not specified, a single usage aggregate will be returned for the entirety of the specified period for each subject and group. | [optional] 
**window_time_zone** | **str** | The value is the name of the time zone as defined in the IANA Time Zone Database (http://www.iana.org/time-zones). If not specified, the UTC timezone will be used. | [optional] [default to 'UTC']
**subject** | **List[str]** | Filtering by multiple subjects. | [optional] 
**filter_customer_id** | **List[str]** | Filtering by multiple customers. | [optional] 
**filter_group_by** | **Dict[str, List[str]]** | Simple filter for group bys with exact match. | [optional] 
**advanced_meter_group_by_filters** | [**Dict[str, FilterString]**](FilterString.md) | Optional advanced meter group by filters. You can use this to filter for values of the meter groupBy fields. | [optional] 
**group_by** | **List[str]** | If not specified a single aggregate will be returned for each subject and time window. &#x60;subject&#x60; is a reserved group by value. | [optional] 

## Example

```python
from moolabs.models.meter_query_request import MeterQueryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MeterQueryRequest from a JSON string
meter_query_request_instance = MeterQueryRequest.from_json(json)
# print the JSON string representation of the object
print(MeterQueryRequest.to_json())

# convert the object into a dict
meter_query_request_dict = meter_query_request_instance.to_dict()
# create an instance of MeterQueryRequest from a dict
meter_query_request_from_dict = MeterQueryRequest.from_dict(meter_query_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


