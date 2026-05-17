# ImportPromiseItem

One promise-to-pay row for bulk import.  ``external_ptp_id`` is the upstream identifier (e.g. Growfin PTP number) and the upsert key.  ``case_id`` must point at a non-terminal case.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_ptp_id** | **str** |  | 
**case_id** | **str** |  | 
**contact_id** | **str** |  | [optional] 
**invoice_id** | **str** |  | [optional] 
**promised_amount_micros** | **int** |  | 
**fulfilled_amount_micros** | **int** |  | [optional] [default to 0]
**currency_code** | **str** |  | [optional] [default to 'USD']
**promised_date** | **date** |  | 
**status** | **str** |  | [optional] [default to 'open']
**captured_from_channel** | **str** |  | [optional] [default to 'email']
**captured_by** | **str** |  | [optional] [default to 'human']
**confidence** | **float** |  | [optional] 
**ptp_no** | **str** |  | [optional] 
**balance_amount_micros** | **int** |  | [optional] 
**amount_base_currency_micros** | **int** |  | [optional] 
**balance_amount_base_currency_micros** | **int** |  | [optional] 
**slippage_count** | **int** |  | [optional] [default to 0]
**source_app** | **str** |  | [optional] 
**ptp_type** | **str** |  | [optional] 

## Example

```python
from moolabs.models.import_promise_item import ImportPromiseItem

# TODO update the JSON string below
json = "{}"
# create an instance of ImportPromiseItem from a JSON string
import_promise_item_instance = ImportPromiseItem.from_json(json)
# print the JSON string representation of the object
print(ImportPromiseItem.to_json())

# convert the object into a dict
import_promise_item_dict = import_promise_item_instance.to_dict()
# create an instance of ImportPromiseItem from a dict
import_promise_item_from_dict = ImportPromiseItem.from_dict(import_promise_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


