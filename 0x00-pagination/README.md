# 0x00-pagination
This readme coveres pagination

## Pagination
Paging requires an implied ordering. By default this may be the item’s unique identifier, but can be other ordered fields such as a created date.

## types of pagination
* Offset Pagination - This is the simplest form of paging. Limit/Offset became popular with apps using SQL databases which already have LIMIT and OFFSET as part of the SQL SELECT Syntax. Very little business logic is required to implement Limit/Offset paging.
`` GET /items?limit=20&offset=100.``

* Keyset Pagination - Keyset pagination uses the filter values of the last page to fetch the next set of items. Those columns would be indexed.
`` GET /items?limit=20&created:lte:2021-01-19T00:00:00 ``

* Seek Pagination - eek Paging is an extension of Keyset paging. By adding an after_id or start_id URL parameter, we can remove the tight coupling of paging to filters and sorting. Since unique identifiers are naturally high cardinality, we won’t run into issues unlike if sorting by a low cardinality field like state enums or category name.
``GET /items?limit=20&after_id=20``


