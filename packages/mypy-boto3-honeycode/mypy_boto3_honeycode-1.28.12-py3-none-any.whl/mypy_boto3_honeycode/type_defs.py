"""
Type annotations for honeycode service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_honeycode/type_defs/)

Usage::

    ```python
    from mypy_boto3_honeycode.type_defs import FailedBatchItemTypeDef

    data: FailedBatchItemTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from .literals import (
    ErrorCodeType,
    FormatType,
    ImportDataCharacterEncodingType,
    TableDataImportJobStatusType,
    UpsertActionType,
)

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "FailedBatchItemTypeDef",
    "BatchDeleteTableRowsRequestRequestTypeDef",
    "UpsertRowsResultTypeDef",
    "CellInputTypeDef",
    "CellTypeDef",
    "ColumnMetadataTypeDef",
    "DataItemTypeDef",
    "DelimitedTextImportOptionsOutputTypeDef",
    "DelimitedTextImportOptionsTypeDef",
    "DescribeTableDataImportJobRequestRequestTypeDef",
    "SourceDataColumnPropertiesOutputTypeDef",
    "SourceDataColumnPropertiesTypeDef",
    "FilterTypeDef",
    "VariableValueTypeDef",
    "ImportDataSourceConfigOutputTypeDef",
    "ImportDataSourceConfigTypeDef",
    "ImportJobSubmitterTypeDef",
    "InvokeScreenAutomationResultTypeDef",
    "ListTableColumnsRequestListTableColumnsPaginateTypeDef",
    "ListTableColumnsRequestRequestTypeDef",
    "TableColumnTypeDef",
    "ListTableRowsRequestListTableRowsPaginateTypeDef",
    "ListTableRowsRequestRequestTypeDef",
    "ListTablesRequestListTablesPaginateTypeDef",
    "ListTablesRequestRequestTypeDef",
    "TableTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResultTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "StartTableDataImportJobResultTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "BatchCreateTableRowsResultTypeDef",
    "BatchDeleteTableRowsResultTypeDef",
    "BatchUpdateTableRowsResultTypeDef",
    "BatchUpsertTableRowsResultTypeDef",
    "CreateRowDataTypeDef",
    "UpdateRowDataTypeDef",
    "TableRowTypeDef",
    "ResultRowTypeDef",
    "DestinationOptionsOutputTypeDef",
    "DestinationOptionsTypeDef",
    "QueryTableRowsRequestQueryTableRowsPaginateTypeDef",
    "QueryTableRowsRequestRequestTypeDef",
    "UpsertRowDataTypeDef",
    "GetScreenDataRequestRequestTypeDef",
    "InvokeScreenAutomationRequestRequestTypeDef",
    "ImportDataSourceOutputTypeDef",
    "ImportDataSourceTypeDef",
    "ListTableColumnsResultTypeDef",
    "ListTablesResultTypeDef",
    "BatchCreateTableRowsRequestRequestTypeDef",
    "BatchUpdateTableRowsRequestRequestTypeDef",
    "ListTableRowsResultTypeDef",
    "QueryTableRowsResultTypeDef",
    "ResultSetTypeDef",
    "ImportOptionsOutputTypeDef",
    "ImportOptionsTypeDef",
    "BatchUpsertTableRowsRequestRequestTypeDef",
    "GetScreenDataResultTypeDef",
    "TableDataImportJobMetadataTypeDef",
    "StartTableDataImportJobRequestRequestTypeDef",
    "DescribeTableDataImportJobResultTypeDef",
)

FailedBatchItemTypeDef = TypedDict(
    "FailedBatchItemTypeDef",
    {
        "id": str,
        "errorMessage": str,
    },
)

_RequiredBatchDeleteTableRowsRequestRequestTypeDef = TypedDict(
    "_RequiredBatchDeleteTableRowsRequestRequestTypeDef",
    {
        "workbookId": str,
        "tableId": str,
        "rowIds": Sequence[str],
    },
)
_OptionalBatchDeleteTableRowsRequestRequestTypeDef = TypedDict(
    "_OptionalBatchDeleteTableRowsRequestRequestTypeDef",
    {
        "clientRequestToken": str,
    },
    total=False,
)


class BatchDeleteTableRowsRequestRequestTypeDef(
    _RequiredBatchDeleteTableRowsRequestRequestTypeDef,
    _OptionalBatchDeleteTableRowsRequestRequestTypeDef,
):
    pass


UpsertRowsResultTypeDef = TypedDict(
    "UpsertRowsResultTypeDef",
    {
        "rowIds": List[str],
        "upsertAction": UpsertActionType,
    },
)

CellInputTypeDef = TypedDict(
    "CellInputTypeDef",
    {
        "fact": str,
        "facts": Sequence[str],
    },
    total=False,
)

CellTypeDef = TypedDict(
    "CellTypeDef",
    {
        "formula": str,
        "format": FormatType,
        "rawValue": str,
        "formattedValue": str,
        "formattedValues": List[str],
    },
    total=False,
)

ColumnMetadataTypeDef = TypedDict(
    "ColumnMetadataTypeDef",
    {
        "name": str,
        "format": FormatType,
    },
)

DataItemTypeDef = TypedDict(
    "DataItemTypeDef",
    {
        "overrideFormat": FormatType,
        "rawValue": str,
        "formattedValue": str,
    },
    total=False,
)

_RequiredDelimitedTextImportOptionsOutputTypeDef = TypedDict(
    "_RequiredDelimitedTextImportOptionsOutputTypeDef",
    {
        "delimiter": str,
    },
)
_OptionalDelimitedTextImportOptionsOutputTypeDef = TypedDict(
    "_OptionalDelimitedTextImportOptionsOutputTypeDef",
    {
        "hasHeaderRow": bool,
        "ignoreEmptyRows": bool,
        "dataCharacterEncoding": ImportDataCharacterEncodingType,
    },
    total=False,
)


class DelimitedTextImportOptionsOutputTypeDef(
    _RequiredDelimitedTextImportOptionsOutputTypeDef,
    _OptionalDelimitedTextImportOptionsOutputTypeDef,
):
    pass


_RequiredDelimitedTextImportOptionsTypeDef = TypedDict(
    "_RequiredDelimitedTextImportOptionsTypeDef",
    {
        "delimiter": str,
    },
)
_OptionalDelimitedTextImportOptionsTypeDef = TypedDict(
    "_OptionalDelimitedTextImportOptionsTypeDef",
    {
        "hasHeaderRow": bool,
        "ignoreEmptyRows": bool,
        "dataCharacterEncoding": ImportDataCharacterEncodingType,
    },
    total=False,
)


class DelimitedTextImportOptionsTypeDef(
    _RequiredDelimitedTextImportOptionsTypeDef, _OptionalDelimitedTextImportOptionsTypeDef
):
    pass


DescribeTableDataImportJobRequestRequestTypeDef = TypedDict(
    "DescribeTableDataImportJobRequestRequestTypeDef",
    {
        "workbookId": str,
        "tableId": str,
        "jobId": str,
    },
)

SourceDataColumnPropertiesOutputTypeDef = TypedDict(
    "SourceDataColumnPropertiesOutputTypeDef",
    {
        "columnIndex": int,
    },
    total=False,
)

SourceDataColumnPropertiesTypeDef = TypedDict(
    "SourceDataColumnPropertiesTypeDef",
    {
        "columnIndex": int,
    },
    total=False,
)

_RequiredFilterTypeDef = TypedDict(
    "_RequiredFilterTypeDef",
    {
        "formula": str,
    },
)
_OptionalFilterTypeDef = TypedDict(
    "_OptionalFilterTypeDef",
    {
        "contextRowId": str,
    },
    total=False,
)


class FilterTypeDef(_RequiredFilterTypeDef, _OptionalFilterTypeDef):
    pass


VariableValueTypeDef = TypedDict(
    "VariableValueTypeDef",
    {
        "rawValue": str,
    },
)

ImportDataSourceConfigOutputTypeDef = TypedDict(
    "ImportDataSourceConfigOutputTypeDef",
    {
        "dataSourceUrl": str,
    },
    total=False,
)

ImportDataSourceConfigTypeDef = TypedDict(
    "ImportDataSourceConfigTypeDef",
    {
        "dataSourceUrl": str,
    },
    total=False,
)

ImportJobSubmitterTypeDef = TypedDict(
    "ImportJobSubmitterTypeDef",
    {
        "email": str,
        "userArn": str,
    },
    total=False,
)

InvokeScreenAutomationResultTypeDef = TypedDict(
    "InvokeScreenAutomationResultTypeDef",
    {
        "workbookCursor": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTableColumnsRequestListTableColumnsPaginateTypeDef = TypedDict(
    "_RequiredListTableColumnsRequestListTableColumnsPaginateTypeDef",
    {
        "workbookId": str,
        "tableId": str,
    },
)
_OptionalListTableColumnsRequestListTableColumnsPaginateTypeDef = TypedDict(
    "_OptionalListTableColumnsRequestListTableColumnsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListTableColumnsRequestListTableColumnsPaginateTypeDef(
    _RequiredListTableColumnsRequestListTableColumnsPaginateTypeDef,
    _OptionalListTableColumnsRequestListTableColumnsPaginateTypeDef,
):
    pass


_RequiredListTableColumnsRequestRequestTypeDef = TypedDict(
    "_RequiredListTableColumnsRequestRequestTypeDef",
    {
        "workbookId": str,
        "tableId": str,
    },
)
_OptionalListTableColumnsRequestRequestTypeDef = TypedDict(
    "_OptionalListTableColumnsRequestRequestTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)


class ListTableColumnsRequestRequestTypeDef(
    _RequiredListTableColumnsRequestRequestTypeDef, _OptionalListTableColumnsRequestRequestTypeDef
):
    pass


TableColumnTypeDef = TypedDict(
    "TableColumnTypeDef",
    {
        "tableColumnId": str,
        "tableColumnName": str,
        "format": FormatType,
    },
    total=False,
)

_RequiredListTableRowsRequestListTableRowsPaginateTypeDef = TypedDict(
    "_RequiredListTableRowsRequestListTableRowsPaginateTypeDef",
    {
        "workbookId": str,
        "tableId": str,
    },
)
_OptionalListTableRowsRequestListTableRowsPaginateTypeDef = TypedDict(
    "_OptionalListTableRowsRequestListTableRowsPaginateTypeDef",
    {
        "rowIds": Sequence[str],
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListTableRowsRequestListTableRowsPaginateTypeDef(
    _RequiredListTableRowsRequestListTableRowsPaginateTypeDef,
    _OptionalListTableRowsRequestListTableRowsPaginateTypeDef,
):
    pass


_RequiredListTableRowsRequestRequestTypeDef = TypedDict(
    "_RequiredListTableRowsRequestRequestTypeDef",
    {
        "workbookId": str,
        "tableId": str,
    },
)
_OptionalListTableRowsRequestRequestTypeDef = TypedDict(
    "_OptionalListTableRowsRequestRequestTypeDef",
    {
        "rowIds": Sequence[str],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListTableRowsRequestRequestTypeDef(
    _RequiredListTableRowsRequestRequestTypeDef, _OptionalListTableRowsRequestRequestTypeDef
):
    pass


_RequiredListTablesRequestListTablesPaginateTypeDef = TypedDict(
    "_RequiredListTablesRequestListTablesPaginateTypeDef",
    {
        "workbookId": str,
    },
)
_OptionalListTablesRequestListTablesPaginateTypeDef = TypedDict(
    "_OptionalListTablesRequestListTablesPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class ListTablesRequestListTablesPaginateTypeDef(
    _RequiredListTablesRequestListTablesPaginateTypeDef,
    _OptionalListTablesRequestListTablesPaginateTypeDef,
):
    pass


_RequiredListTablesRequestRequestTypeDef = TypedDict(
    "_RequiredListTablesRequestRequestTypeDef",
    {
        "workbookId": str,
    },
)
_OptionalListTablesRequestRequestTypeDef = TypedDict(
    "_OptionalListTablesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class ListTablesRequestRequestTypeDef(
    _RequiredListTablesRequestRequestTypeDef, _OptionalListTablesRequestRequestTypeDef
):
    pass


TableTypeDef = TypedDict(
    "TableTypeDef",
    {
        "tableId": str,
        "tableName": str,
    },
    total=False,
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResultTypeDef = TypedDict(
    "ListTagsForResourceResultTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, str],
        "RetryAttempts": int,
    },
)

StartTableDataImportJobResultTypeDef = TypedDict(
    "StartTableDataImportJobResultTypeDef",
    {
        "jobId": str,
        "jobStatus": TableDataImportJobStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Mapping[str, str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)

BatchCreateTableRowsResultTypeDef = TypedDict(
    "BatchCreateTableRowsResultTypeDef",
    {
        "workbookCursor": int,
        "createdRows": Dict[str, str],
        "failedBatchItems": List[FailedBatchItemTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchDeleteTableRowsResultTypeDef = TypedDict(
    "BatchDeleteTableRowsResultTypeDef",
    {
        "workbookCursor": int,
        "failedBatchItems": List[FailedBatchItemTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchUpdateTableRowsResultTypeDef = TypedDict(
    "BatchUpdateTableRowsResultTypeDef",
    {
        "workbookCursor": int,
        "failedBatchItems": List[FailedBatchItemTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchUpsertTableRowsResultTypeDef = TypedDict(
    "BatchUpsertTableRowsResultTypeDef",
    {
        "rows": Dict[str, UpsertRowsResultTypeDef],
        "workbookCursor": int,
        "failedBatchItems": List[FailedBatchItemTypeDef],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRowDataTypeDef = TypedDict(
    "CreateRowDataTypeDef",
    {
        "batchItemId": str,
        "cellsToCreate": Mapping[str, CellInputTypeDef],
    },
)

UpdateRowDataTypeDef = TypedDict(
    "UpdateRowDataTypeDef",
    {
        "rowId": str,
        "cellsToUpdate": Mapping[str, CellInputTypeDef],
    },
)

TableRowTypeDef = TypedDict(
    "TableRowTypeDef",
    {
        "rowId": str,
        "cells": List[CellTypeDef],
    },
)

_RequiredResultRowTypeDef = TypedDict(
    "_RequiredResultRowTypeDef",
    {
        "dataItems": List[DataItemTypeDef],
    },
)
_OptionalResultRowTypeDef = TypedDict(
    "_OptionalResultRowTypeDef",
    {
        "rowId": str,
    },
    total=False,
)


class ResultRowTypeDef(_RequiredResultRowTypeDef, _OptionalResultRowTypeDef):
    pass


DestinationOptionsOutputTypeDef = TypedDict(
    "DestinationOptionsOutputTypeDef",
    {
        "columnMap": Dict[str, SourceDataColumnPropertiesOutputTypeDef],
    },
    total=False,
)

DestinationOptionsTypeDef = TypedDict(
    "DestinationOptionsTypeDef",
    {
        "columnMap": Mapping[str, SourceDataColumnPropertiesTypeDef],
    },
    total=False,
)

_RequiredQueryTableRowsRequestQueryTableRowsPaginateTypeDef = TypedDict(
    "_RequiredQueryTableRowsRequestQueryTableRowsPaginateTypeDef",
    {
        "workbookId": str,
        "tableId": str,
        "filterFormula": FilterTypeDef,
    },
)
_OptionalQueryTableRowsRequestQueryTableRowsPaginateTypeDef = TypedDict(
    "_OptionalQueryTableRowsRequestQueryTableRowsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class QueryTableRowsRequestQueryTableRowsPaginateTypeDef(
    _RequiredQueryTableRowsRequestQueryTableRowsPaginateTypeDef,
    _OptionalQueryTableRowsRequestQueryTableRowsPaginateTypeDef,
):
    pass


_RequiredQueryTableRowsRequestRequestTypeDef = TypedDict(
    "_RequiredQueryTableRowsRequestRequestTypeDef",
    {
        "workbookId": str,
        "tableId": str,
        "filterFormula": FilterTypeDef,
    },
)
_OptionalQueryTableRowsRequestRequestTypeDef = TypedDict(
    "_OptionalQueryTableRowsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class QueryTableRowsRequestRequestTypeDef(
    _RequiredQueryTableRowsRequestRequestTypeDef, _OptionalQueryTableRowsRequestRequestTypeDef
):
    pass


UpsertRowDataTypeDef = TypedDict(
    "UpsertRowDataTypeDef",
    {
        "batchItemId": str,
        "filter": FilterTypeDef,
        "cellsToUpdate": Mapping[str, CellInputTypeDef],
    },
)

_RequiredGetScreenDataRequestRequestTypeDef = TypedDict(
    "_RequiredGetScreenDataRequestRequestTypeDef",
    {
        "workbookId": str,
        "appId": str,
        "screenId": str,
    },
)
_OptionalGetScreenDataRequestRequestTypeDef = TypedDict(
    "_OptionalGetScreenDataRequestRequestTypeDef",
    {
        "variables": Mapping[str, VariableValueTypeDef],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class GetScreenDataRequestRequestTypeDef(
    _RequiredGetScreenDataRequestRequestTypeDef, _OptionalGetScreenDataRequestRequestTypeDef
):
    pass


_RequiredInvokeScreenAutomationRequestRequestTypeDef = TypedDict(
    "_RequiredInvokeScreenAutomationRequestRequestTypeDef",
    {
        "workbookId": str,
        "appId": str,
        "screenId": str,
        "screenAutomationId": str,
    },
)
_OptionalInvokeScreenAutomationRequestRequestTypeDef = TypedDict(
    "_OptionalInvokeScreenAutomationRequestRequestTypeDef",
    {
        "variables": Mapping[str, VariableValueTypeDef],
        "rowId": str,
        "clientRequestToken": str,
    },
    total=False,
)


class InvokeScreenAutomationRequestRequestTypeDef(
    _RequiredInvokeScreenAutomationRequestRequestTypeDef,
    _OptionalInvokeScreenAutomationRequestRequestTypeDef,
):
    pass


ImportDataSourceOutputTypeDef = TypedDict(
    "ImportDataSourceOutputTypeDef",
    {
        "dataSourceConfig": ImportDataSourceConfigOutputTypeDef,
    },
)

ImportDataSourceTypeDef = TypedDict(
    "ImportDataSourceTypeDef",
    {
        "dataSourceConfig": ImportDataSourceConfigTypeDef,
    },
)

ListTableColumnsResultTypeDef = TypedDict(
    "ListTableColumnsResultTypeDef",
    {
        "tableColumns": List[TableColumnTypeDef],
        "nextToken": str,
        "workbookCursor": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTablesResultTypeDef = TypedDict(
    "ListTablesResultTypeDef",
    {
        "tables": List[TableTypeDef],
        "nextToken": str,
        "workbookCursor": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredBatchCreateTableRowsRequestRequestTypeDef = TypedDict(
    "_RequiredBatchCreateTableRowsRequestRequestTypeDef",
    {
        "workbookId": str,
        "tableId": str,
        "rowsToCreate": Sequence[CreateRowDataTypeDef],
    },
)
_OptionalBatchCreateTableRowsRequestRequestTypeDef = TypedDict(
    "_OptionalBatchCreateTableRowsRequestRequestTypeDef",
    {
        "clientRequestToken": str,
    },
    total=False,
)


class BatchCreateTableRowsRequestRequestTypeDef(
    _RequiredBatchCreateTableRowsRequestRequestTypeDef,
    _OptionalBatchCreateTableRowsRequestRequestTypeDef,
):
    pass


_RequiredBatchUpdateTableRowsRequestRequestTypeDef = TypedDict(
    "_RequiredBatchUpdateTableRowsRequestRequestTypeDef",
    {
        "workbookId": str,
        "tableId": str,
        "rowsToUpdate": Sequence[UpdateRowDataTypeDef],
    },
)
_OptionalBatchUpdateTableRowsRequestRequestTypeDef = TypedDict(
    "_OptionalBatchUpdateTableRowsRequestRequestTypeDef",
    {
        "clientRequestToken": str,
    },
    total=False,
)


class BatchUpdateTableRowsRequestRequestTypeDef(
    _RequiredBatchUpdateTableRowsRequestRequestTypeDef,
    _OptionalBatchUpdateTableRowsRequestRequestTypeDef,
):
    pass


ListTableRowsResultTypeDef = TypedDict(
    "ListTableRowsResultTypeDef",
    {
        "columnIds": List[str],
        "rows": List[TableRowTypeDef],
        "rowIdsNotFound": List[str],
        "nextToken": str,
        "workbookCursor": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

QueryTableRowsResultTypeDef = TypedDict(
    "QueryTableRowsResultTypeDef",
    {
        "columnIds": List[str],
        "rows": List[TableRowTypeDef],
        "nextToken": str,
        "workbookCursor": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResultSetTypeDef = TypedDict(
    "ResultSetTypeDef",
    {
        "headers": List[ColumnMetadataTypeDef],
        "rows": List[ResultRowTypeDef],
    },
)

ImportOptionsOutputTypeDef = TypedDict(
    "ImportOptionsOutputTypeDef",
    {
        "destinationOptions": DestinationOptionsOutputTypeDef,
        "delimitedTextOptions": DelimitedTextImportOptionsOutputTypeDef,
    },
    total=False,
)

ImportOptionsTypeDef = TypedDict(
    "ImportOptionsTypeDef",
    {
        "destinationOptions": DestinationOptionsTypeDef,
        "delimitedTextOptions": DelimitedTextImportOptionsTypeDef,
    },
    total=False,
)

_RequiredBatchUpsertTableRowsRequestRequestTypeDef = TypedDict(
    "_RequiredBatchUpsertTableRowsRequestRequestTypeDef",
    {
        "workbookId": str,
        "tableId": str,
        "rowsToUpsert": Sequence[UpsertRowDataTypeDef],
    },
)
_OptionalBatchUpsertTableRowsRequestRequestTypeDef = TypedDict(
    "_OptionalBatchUpsertTableRowsRequestRequestTypeDef",
    {
        "clientRequestToken": str,
    },
    total=False,
)


class BatchUpsertTableRowsRequestRequestTypeDef(
    _RequiredBatchUpsertTableRowsRequestRequestTypeDef,
    _OptionalBatchUpsertTableRowsRequestRequestTypeDef,
):
    pass


GetScreenDataResultTypeDef = TypedDict(
    "GetScreenDataResultTypeDef",
    {
        "results": Dict[str, ResultSetTypeDef],
        "workbookCursor": int,
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TableDataImportJobMetadataTypeDef = TypedDict(
    "TableDataImportJobMetadataTypeDef",
    {
        "submitter": ImportJobSubmitterTypeDef,
        "submitTime": datetime,
        "importOptions": ImportOptionsOutputTypeDef,
        "dataSource": ImportDataSourceOutputTypeDef,
    },
)

StartTableDataImportJobRequestRequestTypeDef = TypedDict(
    "StartTableDataImportJobRequestRequestTypeDef",
    {
        "workbookId": str,
        "dataSource": ImportDataSourceTypeDef,
        "dataFormat": Literal["DELIMITED_TEXT"],
        "destinationTableId": str,
        "importOptions": ImportOptionsTypeDef,
        "clientRequestToken": str,
    },
)

DescribeTableDataImportJobResultTypeDef = TypedDict(
    "DescribeTableDataImportJobResultTypeDef",
    {
        "jobStatus": TableDataImportJobStatusType,
        "message": str,
        "jobMetadata": TableDataImportJobMetadataTypeDef,
        "errorCode": ErrorCodeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
