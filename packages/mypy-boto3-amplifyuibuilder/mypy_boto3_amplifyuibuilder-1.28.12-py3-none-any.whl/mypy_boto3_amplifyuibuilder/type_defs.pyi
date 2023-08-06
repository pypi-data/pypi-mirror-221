"""
Type annotations for amplifyuibuilder service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amplifyuibuilder/type_defs/)

Usage::

    ```python
    from mypy_boto3_amplifyuibuilder.type_defs import ActionParametersOutputTypeDef

    data: ActionParametersOutputTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Mapping, Sequence

from .literals import (
    CodegenGenericDataFieldDataTypeType,
    CodegenJobStatusType,
    FormActionTypeType,
    FormButtonsPositionType,
    FormDataSourceTypeType,
    GenericDataRelationshipTypeType,
    JSModuleType,
    JSScriptType,
    JSTargetType,
    LabelDecoratorType,
    SortDirectionType,
    StorageAccessLevelType,
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
    "ActionParametersOutputTypeDef",
    "ActionParametersTypeDef",
    "CodegenFeatureFlagsOutputTypeDef",
    "CodegenFeatureFlagsTypeDef",
    "CodegenGenericDataEnumOutputTypeDef",
    "CodegenGenericDataEnumTypeDef",
    "CodegenGenericDataFieldOutputTypeDef",
    "CodegenGenericDataFieldTypeDef",
    "CodegenGenericDataModelOutputTypeDef",
    "CodegenGenericDataModelTypeDef",
    "CodegenGenericDataNonModelOutputTypeDef",
    "CodegenGenericDataNonModelTypeDef",
    "CodegenGenericDataRelationshipTypeOutputTypeDef",
    "CodegenGenericDataRelationshipTypeTypeDef",
    "CodegenJobAssetTypeDef",
    "CodegenJobGenericDataSchemaOutputTypeDef",
    "CodegenJobGenericDataSchemaTypeDef",
    "CodegenJobRenderConfigOutputTypeDef",
    "CodegenJobRenderConfigTypeDef",
    "CodegenJobSummaryTypeDef",
    "CodegenJobTypeDef",
    "ComponentBindingPropertiesValueOutputTypeDef",
    "ComponentBindingPropertiesValuePropertiesOutputTypeDef",
    "ComponentBindingPropertiesValuePropertiesTypeDef",
    "ComponentBindingPropertiesValueTypeDef",
    "ComponentChildOutputTypeDef",
    "ComponentChildTypeDef",
    "ComponentConditionPropertyOutputTypeDef",
    "ComponentConditionPropertyTypeDef",
    "ComponentDataConfigurationOutputTypeDef",
    "ComponentDataConfigurationTypeDef",
    "ComponentEventOutputTypeDef",
    "ComponentEventTypeDef",
    "ComponentPropertyBindingPropertiesOutputTypeDef",
    "ComponentPropertyBindingPropertiesTypeDef",
    "ComponentPropertyOutputTypeDef",
    "ComponentPropertyTypeDef",
    "ComponentSummaryTypeDef",
    "ComponentTypeDef",
    "ComponentVariantOutputTypeDef",
    "ComponentVariantTypeDef",
    "CreateComponentDataTypeDef",
    "CreateComponentRequestRequestTypeDef",
    "CreateComponentResponseTypeDef",
    "CreateFormDataTypeDef",
    "CreateFormRequestRequestTypeDef",
    "CreateFormResponseTypeDef",
    "CreateThemeDataTypeDef",
    "CreateThemeRequestRequestTypeDef",
    "CreateThemeResponseTypeDef",
    "DeleteComponentRequestRequestTypeDef",
    "DeleteFormRequestRequestTypeDef",
    "DeleteThemeRequestRequestTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ExchangeCodeForTokenRequestBodyTypeDef",
    "ExchangeCodeForTokenRequestRequestTypeDef",
    "ExchangeCodeForTokenResponseTypeDef",
    "ExportComponentsRequestExportComponentsPaginateTypeDef",
    "ExportComponentsRequestRequestTypeDef",
    "ExportComponentsResponseTypeDef",
    "ExportFormsRequestExportFormsPaginateTypeDef",
    "ExportFormsRequestRequestTypeDef",
    "ExportFormsResponseTypeDef",
    "ExportThemesRequestExportThemesPaginateTypeDef",
    "ExportThemesRequestRequestTypeDef",
    "ExportThemesResponseTypeDef",
    "FieldConfigOutputTypeDef",
    "FieldConfigTypeDef",
    "FieldInputConfigOutputTypeDef",
    "FieldInputConfigTypeDef",
    "FieldPositionOutputTypeDef",
    "FieldPositionTypeDef",
    "FieldValidationConfigurationOutputTypeDef",
    "FieldValidationConfigurationTypeDef",
    "FileUploaderFieldConfigOutputTypeDef",
    "FileUploaderFieldConfigTypeDef",
    "FormBindingElementOutputTypeDef",
    "FormBindingElementTypeDef",
    "FormButtonOutputTypeDef",
    "FormButtonTypeDef",
    "FormCTAOutputTypeDef",
    "FormCTATypeDef",
    "FormDataTypeConfigOutputTypeDef",
    "FormDataTypeConfigTypeDef",
    "FormInputBindingPropertiesValueOutputTypeDef",
    "FormInputBindingPropertiesValuePropertiesOutputTypeDef",
    "FormInputBindingPropertiesValuePropertiesTypeDef",
    "FormInputBindingPropertiesValueTypeDef",
    "FormInputValuePropertyBindingPropertiesOutputTypeDef",
    "FormInputValuePropertyBindingPropertiesTypeDef",
    "FormInputValuePropertyOutputTypeDef",
    "FormInputValuePropertyTypeDef",
    "FormStyleConfigOutputTypeDef",
    "FormStyleConfigTypeDef",
    "FormStyleOutputTypeDef",
    "FormStyleTypeDef",
    "FormSummaryTypeDef",
    "FormTypeDef",
    "GetCodegenJobRequestRequestTypeDef",
    "GetCodegenJobResponseTypeDef",
    "GetComponentRequestRequestTypeDef",
    "GetComponentResponseTypeDef",
    "GetFormRequestRequestTypeDef",
    "GetFormResponseTypeDef",
    "GetMetadataRequestRequestTypeDef",
    "GetMetadataResponseTypeDef",
    "GetThemeRequestRequestTypeDef",
    "GetThemeResponseTypeDef",
    "ListCodegenJobsRequestListCodegenJobsPaginateTypeDef",
    "ListCodegenJobsRequestRequestTypeDef",
    "ListCodegenJobsResponseTypeDef",
    "ListComponentsRequestListComponentsPaginateTypeDef",
    "ListComponentsRequestRequestTypeDef",
    "ListComponentsResponseTypeDef",
    "ListFormsRequestListFormsPaginateTypeDef",
    "ListFormsRequestRequestTypeDef",
    "ListFormsResponseTypeDef",
    "ListThemesRequestListThemesPaginateTypeDef",
    "ListThemesRequestRequestTypeDef",
    "ListThemesResponseTypeDef",
    "MutationActionSetStateParameterOutputTypeDef",
    "MutationActionSetStateParameterTypeDef",
    "PaginatorConfigTypeDef",
    "PredicateOutputTypeDef",
    "PredicateTypeDef",
    "PutMetadataFlagBodyTypeDef",
    "PutMetadataFlagRequestRequestTypeDef",
    "ReactStartCodegenJobDataOutputTypeDef",
    "ReactStartCodegenJobDataTypeDef",
    "RefreshTokenRequestBodyTypeDef",
    "RefreshTokenRequestRequestTypeDef",
    "RefreshTokenResponseTypeDef",
    "ResponseMetadataTypeDef",
    "SectionalElementOutputTypeDef",
    "SectionalElementTypeDef",
    "SortPropertyOutputTypeDef",
    "SortPropertyTypeDef",
    "StartCodegenJobDataTypeDef",
    "StartCodegenJobRequestRequestTypeDef",
    "StartCodegenJobResponseTypeDef",
    "ThemeSummaryTypeDef",
    "ThemeTypeDef",
    "ThemeValueOutputTypeDef",
    "ThemeValueTypeDef",
    "ThemeValuesOutputTypeDef",
    "ThemeValuesTypeDef",
    "UpdateComponentDataTypeDef",
    "UpdateComponentRequestRequestTypeDef",
    "UpdateComponentResponseTypeDef",
    "UpdateFormDataTypeDef",
    "UpdateFormRequestRequestTypeDef",
    "UpdateFormResponseTypeDef",
    "UpdateThemeDataTypeDef",
    "UpdateThemeRequestRequestTypeDef",
    "UpdateThemeResponseTypeDef",
    "ValueMappingOutputTypeDef",
    "ValueMappingTypeDef",
    "ValueMappingsOutputTypeDef",
    "ValueMappingsTypeDef",
)

ActionParametersOutputTypeDef = TypedDict(
    "ActionParametersOutputTypeDef",
    {
        "type": "ComponentPropertyOutputTypeDef",
        "url": "ComponentPropertyOutputTypeDef",
        "anchor": "ComponentPropertyOutputTypeDef",
        "target": "ComponentPropertyOutputTypeDef",
        "global": "ComponentPropertyOutputTypeDef",
        "model": str,
        "id": "ComponentPropertyOutputTypeDef",
        "fields": Dict[str, "ComponentPropertyOutputTypeDef"],
        "state": "MutationActionSetStateParameterOutputTypeDef",
    },
    total=False,
)

ActionParametersTypeDef = TypedDict(
    "ActionParametersTypeDef",
    {
        "type": "ComponentPropertyTypeDef",
        "url": "ComponentPropertyTypeDef",
        "anchor": "ComponentPropertyTypeDef",
        "target": "ComponentPropertyTypeDef",
        "global": "ComponentPropertyTypeDef",
        "model": str,
        "id": "ComponentPropertyTypeDef",
        "fields": Mapping[str, "ComponentPropertyTypeDef"],
        "state": "MutationActionSetStateParameterTypeDef",
    },
    total=False,
)

CodegenFeatureFlagsOutputTypeDef = TypedDict(
    "CodegenFeatureFlagsOutputTypeDef",
    {
        "isRelationshipSupported": bool,
        "isNonModelSupported": bool,
    },
    total=False,
)

CodegenFeatureFlagsTypeDef = TypedDict(
    "CodegenFeatureFlagsTypeDef",
    {
        "isRelationshipSupported": bool,
        "isNonModelSupported": bool,
    },
    total=False,
)

CodegenGenericDataEnumOutputTypeDef = TypedDict(
    "CodegenGenericDataEnumOutputTypeDef",
    {
        "values": List[str],
    },
)

CodegenGenericDataEnumTypeDef = TypedDict(
    "CodegenGenericDataEnumTypeDef",
    {
        "values": Sequence[str],
    },
)

_RequiredCodegenGenericDataFieldOutputTypeDef = TypedDict(
    "_RequiredCodegenGenericDataFieldOutputTypeDef",
    {
        "dataType": CodegenGenericDataFieldDataTypeType,
        "dataTypeValue": str,
        "required": bool,
        "readOnly": bool,
        "isArray": bool,
    },
)
_OptionalCodegenGenericDataFieldOutputTypeDef = TypedDict(
    "_OptionalCodegenGenericDataFieldOutputTypeDef",
    {
        "relationship": "CodegenGenericDataRelationshipTypeOutputTypeDef",
    },
    total=False,
)

class CodegenGenericDataFieldOutputTypeDef(
    _RequiredCodegenGenericDataFieldOutputTypeDef, _OptionalCodegenGenericDataFieldOutputTypeDef
):
    pass

_RequiredCodegenGenericDataFieldTypeDef = TypedDict(
    "_RequiredCodegenGenericDataFieldTypeDef",
    {
        "dataType": CodegenGenericDataFieldDataTypeType,
        "dataTypeValue": str,
        "required": bool,
        "readOnly": bool,
        "isArray": bool,
    },
)
_OptionalCodegenGenericDataFieldTypeDef = TypedDict(
    "_OptionalCodegenGenericDataFieldTypeDef",
    {
        "relationship": "CodegenGenericDataRelationshipTypeTypeDef",
    },
    total=False,
)

class CodegenGenericDataFieldTypeDef(
    _RequiredCodegenGenericDataFieldTypeDef, _OptionalCodegenGenericDataFieldTypeDef
):
    pass

_RequiredCodegenGenericDataModelOutputTypeDef = TypedDict(
    "_RequiredCodegenGenericDataModelOutputTypeDef",
    {
        "fields": Dict[str, "CodegenGenericDataFieldOutputTypeDef"],
        "primaryKeys": List[str],
    },
)
_OptionalCodegenGenericDataModelOutputTypeDef = TypedDict(
    "_OptionalCodegenGenericDataModelOutputTypeDef",
    {
        "isJoinTable": bool,
    },
    total=False,
)

class CodegenGenericDataModelOutputTypeDef(
    _RequiredCodegenGenericDataModelOutputTypeDef, _OptionalCodegenGenericDataModelOutputTypeDef
):
    pass

_RequiredCodegenGenericDataModelTypeDef = TypedDict(
    "_RequiredCodegenGenericDataModelTypeDef",
    {
        "fields": Mapping[str, "CodegenGenericDataFieldTypeDef"],
        "primaryKeys": Sequence[str],
    },
)
_OptionalCodegenGenericDataModelTypeDef = TypedDict(
    "_OptionalCodegenGenericDataModelTypeDef",
    {
        "isJoinTable": bool,
    },
    total=False,
)

class CodegenGenericDataModelTypeDef(
    _RequiredCodegenGenericDataModelTypeDef, _OptionalCodegenGenericDataModelTypeDef
):
    pass

CodegenGenericDataNonModelOutputTypeDef = TypedDict(
    "CodegenGenericDataNonModelOutputTypeDef",
    {
        "fields": Dict[str, "CodegenGenericDataFieldOutputTypeDef"],
    },
)

CodegenGenericDataNonModelTypeDef = TypedDict(
    "CodegenGenericDataNonModelTypeDef",
    {
        "fields": Mapping[str, "CodegenGenericDataFieldTypeDef"],
    },
)

_RequiredCodegenGenericDataRelationshipTypeOutputTypeDef = TypedDict(
    "_RequiredCodegenGenericDataRelationshipTypeOutputTypeDef",
    {
        "type": GenericDataRelationshipTypeType,
        "relatedModelName": str,
    },
)
_OptionalCodegenGenericDataRelationshipTypeOutputTypeDef = TypedDict(
    "_OptionalCodegenGenericDataRelationshipTypeOutputTypeDef",
    {
        "relatedModelFields": List[str],
        "canUnlinkAssociatedModel": bool,
        "relatedJoinFieldName": str,
        "relatedJoinTableName": str,
        "belongsToFieldOnRelatedModel": str,
        "associatedFields": List[str],
        "isHasManyIndex": bool,
    },
    total=False,
)

class CodegenGenericDataRelationshipTypeOutputTypeDef(
    _RequiredCodegenGenericDataRelationshipTypeOutputTypeDef,
    _OptionalCodegenGenericDataRelationshipTypeOutputTypeDef,
):
    pass

_RequiredCodegenGenericDataRelationshipTypeTypeDef = TypedDict(
    "_RequiredCodegenGenericDataRelationshipTypeTypeDef",
    {
        "type": GenericDataRelationshipTypeType,
        "relatedModelName": str,
    },
)
_OptionalCodegenGenericDataRelationshipTypeTypeDef = TypedDict(
    "_OptionalCodegenGenericDataRelationshipTypeTypeDef",
    {
        "relatedModelFields": Sequence[str],
        "canUnlinkAssociatedModel": bool,
        "relatedJoinFieldName": str,
        "relatedJoinTableName": str,
        "belongsToFieldOnRelatedModel": str,
        "associatedFields": Sequence[str],
        "isHasManyIndex": bool,
    },
    total=False,
)

class CodegenGenericDataRelationshipTypeTypeDef(
    _RequiredCodegenGenericDataRelationshipTypeTypeDef,
    _OptionalCodegenGenericDataRelationshipTypeTypeDef,
):
    pass

CodegenJobAssetTypeDef = TypedDict(
    "CodegenJobAssetTypeDef",
    {
        "downloadUrl": str,
    },
    total=False,
)

CodegenJobGenericDataSchemaOutputTypeDef = TypedDict(
    "CodegenJobGenericDataSchemaOutputTypeDef",
    {
        "dataSourceType": Literal["DataStore"],
        "models": Dict[str, "CodegenGenericDataModelOutputTypeDef"],
        "enums": Dict[str, "CodegenGenericDataEnumOutputTypeDef"],
        "nonModels": Dict[str, "CodegenGenericDataNonModelOutputTypeDef"],
    },
)

CodegenJobGenericDataSchemaTypeDef = TypedDict(
    "CodegenJobGenericDataSchemaTypeDef",
    {
        "dataSourceType": Literal["DataStore"],
        "models": Mapping[str, "CodegenGenericDataModelTypeDef"],
        "enums": Mapping[str, "CodegenGenericDataEnumTypeDef"],
        "nonModels": Mapping[str, "CodegenGenericDataNonModelTypeDef"],
    },
)

CodegenJobRenderConfigOutputTypeDef = TypedDict(
    "CodegenJobRenderConfigOutputTypeDef",
    {
        "react": "ReactStartCodegenJobDataOutputTypeDef",
    },
    total=False,
)

CodegenJobRenderConfigTypeDef = TypedDict(
    "CodegenJobRenderConfigTypeDef",
    {
        "react": "ReactStartCodegenJobDataTypeDef",
    },
    total=False,
)

_RequiredCodegenJobSummaryTypeDef = TypedDict(
    "_RequiredCodegenJobSummaryTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
    },
)
_OptionalCodegenJobSummaryTypeDef = TypedDict(
    "_OptionalCodegenJobSummaryTypeDef",
    {
        "createdAt": datetime,
        "modifiedAt": datetime,
    },
    total=False,
)

class CodegenJobSummaryTypeDef(
    _RequiredCodegenJobSummaryTypeDef, _OptionalCodegenJobSummaryTypeDef
):
    pass

_RequiredCodegenJobTypeDef = TypedDict(
    "_RequiredCodegenJobTypeDef",
    {
        "id": str,
        "appId": str,
        "environmentName": str,
    },
)
_OptionalCodegenJobTypeDef = TypedDict(
    "_OptionalCodegenJobTypeDef",
    {
        "renderConfig": "CodegenJobRenderConfigOutputTypeDef",
        "genericDataSchema": "CodegenJobGenericDataSchemaOutputTypeDef",
        "autoGenerateForms": bool,
        "features": "CodegenFeatureFlagsOutputTypeDef",
        "status": CodegenJobStatusType,
        "statusMessage": str,
        "asset": "CodegenJobAssetTypeDef",
        "tags": Dict[str, str],
        "createdAt": datetime,
        "modifiedAt": datetime,
    },
    total=False,
)

class CodegenJobTypeDef(_RequiredCodegenJobTypeDef, _OptionalCodegenJobTypeDef):
    pass

ComponentBindingPropertiesValueOutputTypeDef = TypedDict(
    "ComponentBindingPropertiesValueOutputTypeDef",
    {
        "type": str,
        "bindingProperties": "ComponentBindingPropertiesValuePropertiesOutputTypeDef",
        "defaultValue": str,
    },
    total=False,
)

ComponentBindingPropertiesValuePropertiesOutputTypeDef = TypedDict(
    "ComponentBindingPropertiesValuePropertiesOutputTypeDef",
    {
        "model": str,
        "field": str,
        "predicates": List["PredicateOutputTypeDef"],
        "userAttribute": str,
        "bucket": str,
        "key": str,
        "defaultValue": str,
        "slotName": str,
    },
    total=False,
)

ComponentBindingPropertiesValuePropertiesTypeDef = TypedDict(
    "ComponentBindingPropertiesValuePropertiesTypeDef",
    {
        "model": str,
        "field": str,
        "predicates": Sequence["PredicateTypeDef"],
        "userAttribute": str,
        "bucket": str,
        "key": str,
        "defaultValue": str,
        "slotName": str,
    },
    total=False,
)

ComponentBindingPropertiesValueTypeDef = TypedDict(
    "ComponentBindingPropertiesValueTypeDef",
    {
        "type": str,
        "bindingProperties": "ComponentBindingPropertiesValuePropertiesTypeDef",
        "defaultValue": str,
    },
    total=False,
)

_RequiredComponentChildOutputTypeDef = TypedDict(
    "_RequiredComponentChildOutputTypeDef",
    {
        "componentType": str,
        "name": str,
        "properties": Dict[str, "ComponentPropertyOutputTypeDef"],
    },
)
_OptionalComponentChildOutputTypeDef = TypedDict(
    "_OptionalComponentChildOutputTypeDef",
    {
        "children": List[Dict[str, Any]],
        "events": Dict[str, "ComponentEventOutputTypeDef"],
        "sourceId": str,
    },
    total=False,
)

class ComponentChildOutputTypeDef(
    _RequiredComponentChildOutputTypeDef, _OptionalComponentChildOutputTypeDef
):
    pass

_RequiredComponentChildTypeDef = TypedDict(
    "_RequiredComponentChildTypeDef",
    {
        "componentType": str,
        "name": str,
        "properties": Mapping[str, "ComponentPropertyTypeDef"],
    },
)
_OptionalComponentChildTypeDef = TypedDict(
    "_OptionalComponentChildTypeDef",
    {
        "children": Sequence[Dict[str, Any]],
        "events": Mapping[str, "ComponentEventTypeDef"],
        "sourceId": str,
    },
    total=False,
)

class ComponentChildTypeDef(_RequiredComponentChildTypeDef, _OptionalComponentChildTypeDef):
    pass

ComponentConditionPropertyOutputTypeDef = TypedDict(
    "ComponentConditionPropertyOutputTypeDef",
    {
        "property": str,
        "field": str,
        "operator": str,
        "operand": str,
        "then": Dict[str, Any],
        "else": Dict[str, Any],
        "operandType": str,
    },
    total=False,
)

ComponentConditionPropertyTypeDef = TypedDict(
    "ComponentConditionPropertyTypeDef",
    {
        "property": str,
        "field": str,
        "operator": str,
        "operand": str,
        "then": Dict[str, Any],
        "else": Dict[str, Any],
        "operandType": str,
    },
    total=False,
)

_RequiredComponentDataConfigurationOutputTypeDef = TypedDict(
    "_RequiredComponentDataConfigurationOutputTypeDef",
    {
        "model": str,
    },
)
_OptionalComponentDataConfigurationOutputTypeDef = TypedDict(
    "_OptionalComponentDataConfigurationOutputTypeDef",
    {
        "sort": List["SortPropertyOutputTypeDef"],
        "predicate": "PredicateOutputTypeDef",
        "identifiers": List[str],
    },
    total=False,
)

class ComponentDataConfigurationOutputTypeDef(
    _RequiredComponentDataConfigurationOutputTypeDef,
    _OptionalComponentDataConfigurationOutputTypeDef,
):
    pass

_RequiredComponentDataConfigurationTypeDef = TypedDict(
    "_RequiredComponentDataConfigurationTypeDef",
    {
        "model": str,
    },
)
_OptionalComponentDataConfigurationTypeDef = TypedDict(
    "_OptionalComponentDataConfigurationTypeDef",
    {
        "sort": Sequence["SortPropertyTypeDef"],
        "predicate": "PredicateTypeDef",
        "identifiers": Sequence[str],
    },
    total=False,
)

class ComponentDataConfigurationTypeDef(
    _RequiredComponentDataConfigurationTypeDef, _OptionalComponentDataConfigurationTypeDef
):
    pass

ComponentEventOutputTypeDef = TypedDict(
    "ComponentEventOutputTypeDef",
    {
        "action": str,
        "parameters": "ActionParametersOutputTypeDef",
        "bindingEvent": str,
    },
    total=False,
)

ComponentEventTypeDef = TypedDict(
    "ComponentEventTypeDef",
    {
        "action": str,
        "parameters": "ActionParametersTypeDef",
        "bindingEvent": str,
    },
    total=False,
)

_RequiredComponentPropertyBindingPropertiesOutputTypeDef = TypedDict(
    "_RequiredComponentPropertyBindingPropertiesOutputTypeDef",
    {
        "property": str,
    },
)
_OptionalComponentPropertyBindingPropertiesOutputTypeDef = TypedDict(
    "_OptionalComponentPropertyBindingPropertiesOutputTypeDef",
    {
        "field": str,
    },
    total=False,
)

class ComponentPropertyBindingPropertiesOutputTypeDef(
    _RequiredComponentPropertyBindingPropertiesOutputTypeDef,
    _OptionalComponentPropertyBindingPropertiesOutputTypeDef,
):
    pass

_RequiredComponentPropertyBindingPropertiesTypeDef = TypedDict(
    "_RequiredComponentPropertyBindingPropertiesTypeDef",
    {
        "property": str,
    },
)
_OptionalComponentPropertyBindingPropertiesTypeDef = TypedDict(
    "_OptionalComponentPropertyBindingPropertiesTypeDef",
    {
        "field": str,
    },
    total=False,
)

class ComponentPropertyBindingPropertiesTypeDef(
    _RequiredComponentPropertyBindingPropertiesTypeDef,
    _OptionalComponentPropertyBindingPropertiesTypeDef,
):
    pass

ComponentPropertyOutputTypeDef = TypedDict(
    "ComponentPropertyOutputTypeDef",
    {
        "value": str,
        "bindingProperties": "ComponentPropertyBindingPropertiesOutputTypeDef",
        "collectionBindingProperties": "ComponentPropertyBindingPropertiesOutputTypeDef",
        "defaultValue": str,
        "model": str,
        "bindings": Dict[str, "FormBindingElementOutputTypeDef"],
        "event": str,
        "userAttribute": str,
        "concat": List[Dict[str, Any]],
        "condition": Dict[str, Any],
        "configured": bool,
        "type": str,
        "importedValue": str,
        "componentName": str,
        "property": str,
    },
    total=False,
)

ComponentPropertyTypeDef = TypedDict(
    "ComponentPropertyTypeDef",
    {
        "value": str,
        "bindingProperties": "ComponentPropertyBindingPropertiesTypeDef",
        "collectionBindingProperties": "ComponentPropertyBindingPropertiesTypeDef",
        "defaultValue": str,
        "model": str,
        "bindings": Mapping[str, "FormBindingElementTypeDef"],
        "event": str,
        "userAttribute": str,
        "concat": Sequence[Dict[str, Any]],
        "condition": Dict[str, Any],
        "configured": bool,
        "type": str,
        "importedValue": str,
        "componentName": str,
        "property": str,
    },
    total=False,
)

ComponentSummaryTypeDef = TypedDict(
    "ComponentSummaryTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
        "name": str,
        "componentType": str,
    },
)

_RequiredComponentTypeDef = TypedDict(
    "_RequiredComponentTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
        "name": str,
        "componentType": str,
        "properties": Dict[str, "ComponentPropertyOutputTypeDef"],
        "variants": List["ComponentVariantOutputTypeDef"],
        "overrides": Dict[str, Dict[str, str]],
        "bindingProperties": Dict[str, "ComponentBindingPropertiesValueOutputTypeDef"],
        "createdAt": datetime,
    },
)
_OptionalComponentTypeDef = TypedDict(
    "_OptionalComponentTypeDef",
    {
        "sourceId": str,
        "children": List["ComponentChildOutputTypeDef"],
        "collectionProperties": Dict[str, "ComponentDataConfigurationOutputTypeDef"],
        "modifiedAt": datetime,
        "tags": Dict[str, str],
        "events": Dict[str, "ComponentEventOutputTypeDef"],
        "schemaVersion": str,
    },
    total=False,
)

class ComponentTypeDef(_RequiredComponentTypeDef, _OptionalComponentTypeDef):
    pass

ComponentVariantOutputTypeDef = TypedDict(
    "ComponentVariantOutputTypeDef",
    {
        "variantValues": Dict[str, str],
        "overrides": Dict[str, Dict[str, str]],
    },
    total=False,
)

ComponentVariantTypeDef = TypedDict(
    "ComponentVariantTypeDef",
    {
        "variantValues": Mapping[str, str],
        "overrides": Mapping[str, Mapping[str, str]],
    },
    total=False,
)

_RequiredCreateComponentDataTypeDef = TypedDict(
    "_RequiredCreateComponentDataTypeDef",
    {
        "name": str,
        "componentType": str,
        "properties": Mapping[str, "ComponentPropertyTypeDef"],
        "variants": Sequence["ComponentVariantTypeDef"],
        "overrides": Mapping[str, Mapping[str, str]],
        "bindingProperties": Mapping[str, "ComponentBindingPropertiesValueTypeDef"],
    },
)
_OptionalCreateComponentDataTypeDef = TypedDict(
    "_OptionalCreateComponentDataTypeDef",
    {
        "sourceId": str,
        "children": Sequence["ComponentChildTypeDef"],
        "collectionProperties": Mapping[str, "ComponentDataConfigurationTypeDef"],
        "tags": Mapping[str, str],
        "events": Mapping[str, "ComponentEventTypeDef"],
        "schemaVersion": str,
    },
    total=False,
)

class CreateComponentDataTypeDef(
    _RequiredCreateComponentDataTypeDef, _OptionalCreateComponentDataTypeDef
):
    pass

_RequiredCreateComponentRequestRequestTypeDef = TypedDict(
    "_RequiredCreateComponentRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "componentToCreate": "CreateComponentDataTypeDef",
    },
)
_OptionalCreateComponentRequestRequestTypeDef = TypedDict(
    "_OptionalCreateComponentRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class CreateComponentRequestRequestTypeDef(
    _RequiredCreateComponentRequestRequestTypeDef, _OptionalCreateComponentRequestRequestTypeDef
):
    pass

CreateComponentResponseTypeDef = TypedDict(
    "CreateComponentResponseTypeDef",
    {
        "entity": "ComponentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateFormDataTypeDef = TypedDict(
    "_RequiredCreateFormDataTypeDef",
    {
        "name": str,
        "dataType": "FormDataTypeConfigTypeDef",
        "formActionType": FormActionTypeType,
        "fields": Mapping[str, "FieldConfigTypeDef"],
        "style": "FormStyleTypeDef",
        "sectionalElements": Mapping[str, "SectionalElementTypeDef"],
        "schemaVersion": str,
    },
)
_OptionalCreateFormDataTypeDef = TypedDict(
    "_OptionalCreateFormDataTypeDef",
    {
        "cta": "FormCTATypeDef",
        "tags": Mapping[str, str],
        "labelDecorator": LabelDecoratorType,
    },
    total=False,
)

class CreateFormDataTypeDef(_RequiredCreateFormDataTypeDef, _OptionalCreateFormDataTypeDef):
    pass

_RequiredCreateFormRequestRequestTypeDef = TypedDict(
    "_RequiredCreateFormRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "formToCreate": "CreateFormDataTypeDef",
    },
)
_OptionalCreateFormRequestRequestTypeDef = TypedDict(
    "_OptionalCreateFormRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class CreateFormRequestRequestTypeDef(
    _RequiredCreateFormRequestRequestTypeDef, _OptionalCreateFormRequestRequestTypeDef
):
    pass

CreateFormResponseTypeDef = TypedDict(
    "CreateFormResponseTypeDef",
    {
        "entity": "FormTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateThemeDataTypeDef = TypedDict(
    "_RequiredCreateThemeDataTypeDef",
    {
        "name": str,
        "values": Sequence["ThemeValuesTypeDef"],
    },
)
_OptionalCreateThemeDataTypeDef = TypedDict(
    "_OptionalCreateThemeDataTypeDef",
    {
        "overrides": Sequence["ThemeValuesTypeDef"],
        "tags": Mapping[str, str],
    },
    total=False,
)

class CreateThemeDataTypeDef(_RequiredCreateThemeDataTypeDef, _OptionalCreateThemeDataTypeDef):
    pass

_RequiredCreateThemeRequestRequestTypeDef = TypedDict(
    "_RequiredCreateThemeRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "themeToCreate": "CreateThemeDataTypeDef",
    },
)
_OptionalCreateThemeRequestRequestTypeDef = TypedDict(
    "_OptionalCreateThemeRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class CreateThemeRequestRequestTypeDef(
    _RequiredCreateThemeRequestRequestTypeDef, _OptionalCreateThemeRequestRequestTypeDef
):
    pass

CreateThemeResponseTypeDef = TypedDict(
    "CreateThemeResponseTypeDef",
    {
        "entity": "ThemeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteComponentRequestRequestTypeDef = TypedDict(
    "DeleteComponentRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
    },
)

DeleteFormRequestRequestTypeDef = TypedDict(
    "DeleteFormRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
    },
)

DeleteThemeRequestRequestTypeDef = TypedDict(
    "DeleteThemeRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
    },
)

EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredExchangeCodeForTokenRequestBodyTypeDef = TypedDict(
    "_RequiredExchangeCodeForTokenRequestBodyTypeDef",
    {
        "code": str,
        "redirectUri": str,
    },
)
_OptionalExchangeCodeForTokenRequestBodyTypeDef = TypedDict(
    "_OptionalExchangeCodeForTokenRequestBodyTypeDef",
    {
        "clientId": str,
    },
    total=False,
)

class ExchangeCodeForTokenRequestBodyTypeDef(
    _RequiredExchangeCodeForTokenRequestBodyTypeDef, _OptionalExchangeCodeForTokenRequestBodyTypeDef
):
    pass

ExchangeCodeForTokenRequestRequestTypeDef = TypedDict(
    "ExchangeCodeForTokenRequestRequestTypeDef",
    {
        "provider": Literal["figma"],
        "request": "ExchangeCodeForTokenRequestBodyTypeDef",
    },
)

ExchangeCodeForTokenResponseTypeDef = TypedDict(
    "ExchangeCodeForTokenResponseTypeDef",
    {
        "accessToken": str,
        "expiresIn": int,
        "refreshToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredExportComponentsRequestExportComponentsPaginateTypeDef = TypedDict(
    "_RequiredExportComponentsRequestExportComponentsPaginateTypeDef",
    {
        "appId": str,
        "environmentName": str,
    },
)
_OptionalExportComponentsRequestExportComponentsPaginateTypeDef = TypedDict(
    "_OptionalExportComponentsRequestExportComponentsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

class ExportComponentsRequestExportComponentsPaginateTypeDef(
    _RequiredExportComponentsRequestExportComponentsPaginateTypeDef,
    _OptionalExportComponentsRequestExportComponentsPaginateTypeDef,
):
    pass

_RequiredExportComponentsRequestRequestTypeDef = TypedDict(
    "_RequiredExportComponentsRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
    },
)
_OptionalExportComponentsRequestRequestTypeDef = TypedDict(
    "_OptionalExportComponentsRequestRequestTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)

class ExportComponentsRequestRequestTypeDef(
    _RequiredExportComponentsRequestRequestTypeDef, _OptionalExportComponentsRequestRequestTypeDef
):
    pass

ExportComponentsResponseTypeDef = TypedDict(
    "ExportComponentsResponseTypeDef",
    {
        "entities": List["ComponentTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredExportFormsRequestExportFormsPaginateTypeDef = TypedDict(
    "_RequiredExportFormsRequestExportFormsPaginateTypeDef",
    {
        "appId": str,
        "environmentName": str,
    },
)
_OptionalExportFormsRequestExportFormsPaginateTypeDef = TypedDict(
    "_OptionalExportFormsRequestExportFormsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

class ExportFormsRequestExportFormsPaginateTypeDef(
    _RequiredExportFormsRequestExportFormsPaginateTypeDef,
    _OptionalExportFormsRequestExportFormsPaginateTypeDef,
):
    pass

_RequiredExportFormsRequestRequestTypeDef = TypedDict(
    "_RequiredExportFormsRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
    },
)
_OptionalExportFormsRequestRequestTypeDef = TypedDict(
    "_OptionalExportFormsRequestRequestTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)

class ExportFormsRequestRequestTypeDef(
    _RequiredExportFormsRequestRequestTypeDef, _OptionalExportFormsRequestRequestTypeDef
):
    pass

ExportFormsResponseTypeDef = TypedDict(
    "ExportFormsResponseTypeDef",
    {
        "entities": List["FormTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredExportThemesRequestExportThemesPaginateTypeDef = TypedDict(
    "_RequiredExportThemesRequestExportThemesPaginateTypeDef",
    {
        "appId": str,
        "environmentName": str,
    },
)
_OptionalExportThemesRequestExportThemesPaginateTypeDef = TypedDict(
    "_OptionalExportThemesRequestExportThemesPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

class ExportThemesRequestExportThemesPaginateTypeDef(
    _RequiredExportThemesRequestExportThemesPaginateTypeDef,
    _OptionalExportThemesRequestExportThemesPaginateTypeDef,
):
    pass

_RequiredExportThemesRequestRequestTypeDef = TypedDict(
    "_RequiredExportThemesRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
    },
)
_OptionalExportThemesRequestRequestTypeDef = TypedDict(
    "_OptionalExportThemesRequestRequestTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)

class ExportThemesRequestRequestTypeDef(
    _RequiredExportThemesRequestRequestTypeDef, _OptionalExportThemesRequestRequestTypeDef
):
    pass

ExportThemesResponseTypeDef = TypedDict(
    "ExportThemesResponseTypeDef",
    {
        "entities": List["ThemeTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FieldConfigOutputTypeDef = TypedDict(
    "FieldConfigOutputTypeDef",
    {
        "label": str,
        "position": "FieldPositionOutputTypeDef",
        "excluded": bool,
        "inputType": "FieldInputConfigOutputTypeDef",
        "validations": List["FieldValidationConfigurationOutputTypeDef"],
    },
    total=False,
)

FieldConfigTypeDef = TypedDict(
    "FieldConfigTypeDef",
    {
        "label": str,
        "position": "FieldPositionTypeDef",
        "excluded": bool,
        "inputType": "FieldInputConfigTypeDef",
        "validations": Sequence["FieldValidationConfigurationTypeDef"],
    },
    total=False,
)

_RequiredFieldInputConfigOutputTypeDef = TypedDict(
    "_RequiredFieldInputConfigOutputTypeDef",
    {
        "type": str,
    },
)
_OptionalFieldInputConfigOutputTypeDef = TypedDict(
    "_OptionalFieldInputConfigOutputTypeDef",
    {
        "required": bool,
        "readOnly": bool,
        "placeholder": str,
        "defaultValue": str,
        "descriptiveText": str,
        "defaultChecked": bool,
        "defaultCountryCode": str,
        "valueMappings": "ValueMappingsOutputTypeDef",
        "name": str,
        "minValue": float,
        "maxValue": float,
        "step": float,
        "value": str,
        "isArray": bool,
        "fileUploaderConfig": "FileUploaderFieldConfigOutputTypeDef",
    },
    total=False,
)

class FieldInputConfigOutputTypeDef(
    _RequiredFieldInputConfigOutputTypeDef, _OptionalFieldInputConfigOutputTypeDef
):
    pass

_RequiredFieldInputConfigTypeDef = TypedDict(
    "_RequiredFieldInputConfigTypeDef",
    {
        "type": str,
    },
)
_OptionalFieldInputConfigTypeDef = TypedDict(
    "_OptionalFieldInputConfigTypeDef",
    {
        "required": bool,
        "readOnly": bool,
        "placeholder": str,
        "defaultValue": str,
        "descriptiveText": str,
        "defaultChecked": bool,
        "defaultCountryCode": str,
        "valueMappings": "ValueMappingsTypeDef",
        "name": str,
        "minValue": float,
        "maxValue": float,
        "step": float,
        "value": str,
        "isArray": bool,
        "fileUploaderConfig": "FileUploaderFieldConfigTypeDef",
    },
    total=False,
)

class FieldInputConfigTypeDef(_RequiredFieldInputConfigTypeDef, _OptionalFieldInputConfigTypeDef):
    pass

FieldPositionOutputTypeDef = TypedDict(
    "FieldPositionOutputTypeDef",
    {
        "fixed": Literal["first"],
        "rightOf": str,
        "below": str,
    },
    total=False,
)

FieldPositionTypeDef = TypedDict(
    "FieldPositionTypeDef",
    {
        "fixed": Literal["first"],
        "rightOf": str,
        "below": str,
    },
    total=False,
)

_RequiredFieldValidationConfigurationOutputTypeDef = TypedDict(
    "_RequiredFieldValidationConfigurationOutputTypeDef",
    {
        "type": str,
    },
)
_OptionalFieldValidationConfigurationOutputTypeDef = TypedDict(
    "_OptionalFieldValidationConfigurationOutputTypeDef",
    {
        "strValues": List[str],
        "numValues": List[int],
        "validationMessage": str,
    },
    total=False,
)

class FieldValidationConfigurationOutputTypeDef(
    _RequiredFieldValidationConfigurationOutputTypeDef,
    _OptionalFieldValidationConfigurationOutputTypeDef,
):
    pass

_RequiredFieldValidationConfigurationTypeDef = TypedDict(
    "_RequiredFieldValidationConfigurationTypeDef",
    {
        "type": str,
    },
)
_OptionalFieldValidationConfigurationTypeDef = TypedDict(
    "_OptionalFieldValidationConfigurationTypeDef",
    {
        "strValues": Sequence[str],
        "numValues": Sequence[int],
        "validationMessage": str,
    },
    total=False,
)

class FieldValidationConfigurationTypeDef(
    _RequiredFieldValidationConfigurationTypeDef, _OptionalFieldValidationConfigurationTypeDef
):
    pass

_RequiredFileUploaderFieldConfigOutputTypeDef = TypedDict(
    "_RequiredFileUploaderFieldConfigOutputTypeDef",
    {
        "accessLevel": StorageAccessLevelType,
        "acceptedFileTypes": List[str],
    },
)
_OptionalFileUploaderFieldConfigOutputTypeDef = TypedDict(
    "_OptionalFileUploaderFieldConfigOutputTypeDef",
    {
        "showThumbnails": bool,
        "isResumable": bool,
        "maxFileCount": int,
        "maxSize": int,
    },
    total=False,
)

class FileUploaderFieldConfigOutputTypeDef(
    _RequiredFileUploaderFieldConfigOutputTypeDef, _OptionalFileUploaderFieldConfigOutputTypeDef
):
    pass

_RequiredFileUploaderFieldConfigTypeDef = TypedDict(
    "_RequiredFileUploaderFieldConfigTypeDef",
    {
        "accessLevel": StorageAccessLevelType,
        "acceptedFileTypes": Sequence[str],
    },
)
_OptionalFileUploaderFieldConfigTypeDef = TypedDict(
    "_OptionalFileUploaderFieldConfigTypeDef",
    {
        "showThumbnails": bool,
        "isResumable": bool,
        "maxFileCount": int,
        "maxSize": int,
    },
    total=False,
)

class FileUploaderFieldConfigTypeDef(
    _RequiredFileUploaderFieldConfigTypeDef, _OptionalFileUploaderFieldConfigTypeDef
):
    pass

FormBindingElementOutputTypeDef = TypedDict(
    "FormBindingElementOutputTypeDef",
    {
        "element": str,
        "property": str,
    },
)

FormBindingElementTypeDef = TypedDict(
    "FormBindingElementTypeDef",
    {
        "element": str,
        "property": str,
    },
)

FormButtonOutputTypeDef = TypedDict(
    "FormButtonOutputTypeDef",
    {
        "excluded": bool,
        "children": str,
        "position": "FieldPositionOutputTypeDef",
    },
    total=False,
)

FormButtonTypeDef = TypedDict(
    "FormButtonTypeDef",
    {
        "excluded": bool,
        "children": str,
        "position": "FieldPositionTypeDef",
    },
    total=False,
)

FormCTAOutputTypeDef = TypedDict(
    "FormCTAOutputTypeDef",
    {
        "position": FormButtonsPositionType,
        "clear": "FormButtonOutputTypeDef",
        "cancel": "FormButtonOutputTypeDef",
        "submit": "FormButtonOutputTypeDef",
    },
    total=False,
)

FormCTATypeDef = TypedDict(
    "FormCTATypeDef",
    {
        "position": FormButtonsPositionType,
        "clear": "FormButtonTypeDef",
        "cancel": "FormButtonTypeDef",
        "submit": "FormButtonTypeDef",
    },
    total=False,
)

FormDataTypeConfigOutputTypeDef = TypedDict(
    "FormDataTypeConfigOutputTypeDef",
    {
        "dataSourceType": FormDataSourceTypeType,
        "dataTypeName": str,
    },
)

FormDataTypeConfigTypeDef = TypedDict(
    "FormDataTypeConfigTypeDef",
    {
        "dataSourceType": FormDataSourceTypeType,
        "dataTypeName": str,
    },
)

FormInputBindingPropertiesValueOutputTypeDef = TypedDict(
    "FormInputBindingPropertiesValueOutputTypeDef",
    {
        "type": str,
        "bindingProperties": "FormInputBindingPropertiesValuePropertiesOutputTypeDef",
    },
    total=False,
)

FormInputBindingPropertiesValuePropertiesOutputTypeDef = TypedDict(
    "FormInputBindingPropertiesValuePropertiesOutputTypeDef",
    {
        "model": str,
    },
    total=False,
)

FormInputBindingPropertiesValuePropertiesTypeDef = TypedDict(
    "FormInputBindingPropertiesValuePropertiesTypeDef",
    {
        "model": str,
    },
    total=False,
)

FormInputBindingPropertiesValueTypeDef = TypedDict(
    "FormInputBindingPropertiesValueTypeDef",
    {
        "type": str,
        "bindingProperties": "FormInputBindingPropertiesValuePropertiesTypeDef",
    },
    total=False,
)

_RequiredFormInputValuePropertyBindingPropertiesOutputTypeDef = TypedDict(
    "_RequiredFormInputValuePropertyBindingPropertiesOutputTypeDef",
    {
        "property": str,
    },
)
_OptionalFormInputValuePropertyBindingPropertiesOutputTypeDef = TypedDict(
    "_OptionalFormInputValuePropertyBindingPropertiesOutputTypeDef",
    {
        "field": str,
    },
    total=False,
)

class FormInputValuePropertyBindingPropertiesOutputTypeDef(
    _RequiredFormInputValuePropertyBindingPropertiesOutputTypeDef,
    _OptionalFormInputValuePropertyBindingPropertiesOutputTypeDef,
):
    pass

_RequiredFormInputValuePropertyBindingPropertiesTypeDef = TypedDict(
    "_RequiredFormInputValuePropertyBindingPropertiesTypeDef",
    {
        "property": str,
    },
)
_OptionalFormInputValuePropertyBindingPropertiesTypeDef = TypedDict(
    "_OptionalFormInputValuePropertyBindingPropertiesTypeDef",
    {
        "field": str,
    },
    total=False,
)

class FormInputValuePropertyBindingPropertiesTypeDef(
    _RequiredFormInputValuePropertyBindingPropertiesTypeDef,
    _OptionalFormInputValuePropertyBindingPropertiesTypeDef,
):
    pass

FormInputValuePropertyOutputTypeDef = TypedDict(
    "FormInputValuePropertyOutputTypeDef",
    {
        "value": str,
        "bindingProperties": "FormInputValuePropertyBindingPropertiesOutputTypeDef",
        "concat": List[Dict[str, Any]],
    },
    total=False,
)

FormInputValuePropertyTypeDef = TypedDict(
    "FormInputValuePropertyTypeDef",
    {
        "value": str,
        "bindingProperties": "FormInputValuePropertyBindingPropertiesTypeDef",
        "concat": Sequence[Dict[str, Any]],
    },
    total=False,
)

FormStyleConfigOutputTypeDef = TypedDict(
    "FormStyleConfigOutputTypeDef",
    {
        "tokenReference": str,
        "value": str,
    },
    total=False,
)

FormStyleConfigTypeDef = TypedDict(
    "FormStyleConfigTypeDef",
    {
        "tokenReference": str,
        "value": str,
    },
    total=False,
)

FormStyleOutputTypeDef = TypedDict(
    "FormStyleOutputTypeDef",
    {
        "horizontalGap": "FormStyleConfigOutputTypeDef",
        "verticalGap": "FormStyleConfigOutputTypeDef",
        "outerPadding": "FormStyleConfigOutputTypeDef",
    },
    total=False,
)

FormStyleTypeDef = TypedDict(
    "FormStyleTypeDef",
    {
        "horizontalGap": "FormStyleConfigTypeDef",
        "verticalGap": "FormStyleConfigTypeDef",
        "outerPadding": "FormStyleConfigTypeDef",
    },
    total=False,
)

FormSummaryTypeDef = TypedDict(
    "FormSummaryTypeDef",
    {
        "appId": str,
        "dataType": "FormDataTypeConfigOutputTypeDef",
        "environmentName": str,
        "formActionType": FormActionTypeType,
        "id": str,
        "name": str,
    },
)

_RequiredFormTypeDef = TypedDict(
    "_RequiredFormTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
        "name": str,
        "formActionType": FormActionTypeType,
        "style": "FormStyleOutputTypeDef",
        "dataType": "FormDataTypeConfigOutputTypeDef",
        "fields": Dict[str, "FieldConfigOutputTypeDef"],
        "sectionalElements": Dict[str, "SectionalElementOutputTypeDef"],
        "schemaVersion": str,
    },
)
_OptionalFormTypeDef = TypedDict(
    "_OptionalFormTypeDef",
    {
        "tags": Dict[str, str],
        "cta": "FormCTAOutputTypeDef",
        "labelDecorator": LabelDecoratorType,
    },
    total=False,
)

class FormTypeDef(_RequiredFormTypeDef, _OptionalFormTypeDef):
    pass

GetCodegenJobRequestRequestTypeDef = TypedDict(
    "GetCodegenJobRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
    },
)

GetCodegenJobResponseTypeDef = TypedDict(
    "GetCodegenJobResponseTypeDef",
    {
        "job": "CodegenJobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetComponentRequestRequestTypeDef = TypedDict(
    "GetComponentRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
    },
)

GetComponentResponseTypeDef = TypedDict(
    "GetComponentResponseTypeDef",
    {
        "component": "ComponentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFormRequestRequestTypeDef = TypedDict(
    "GetFormRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
    },
)

GetFormResponseTypeDef = TypedDict(
    "GetFormResponseTypeDef",
    {
        "form": "FormTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMetadataRequestRequestTypeDef = TypedDict(
    "GetMetadataRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
    },
)

GetMetadataResponseTypeDef = TypedDict(
    "GetMetadataResponseTypeDef",
    {
        "features": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetThemeRequestRequestTypeDef = TypedDict(
    "GetThemeRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
    },
)

GetThemeResponseTypeDef = TypedDict(
    "GetThemeResponseTypeDef",
    {
        "theme": "ThemeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListCodegenJobsRequestListCodegenJobsPaginateTypeDef = TypedDict(
    "_RequiredListCodegenJobsRequestListCodegenJobsPaginateTypeDef",
    {
        "appId": str,
        "environmentName": str,
    },
)
_OptionalListCodegenJobsRequestListCodegenJobsPaginateTypeDef = TypedDict(
    "_OptionalListCodegenJobsRequestListCodegenJobsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

class ListCodegenJobsRequestListCodegenJobsPaginateTypeDef(
    _RequiredListCodegenJobsRequestListCodegenJobsPaginateTypeDef,
    _OptionalListCodegenJobsRequestListCodegenJobsPaginateTypeDef,
):
    pass

_RequiredListCodegenJobsRequestRequestTypeDef = TypedDict(
    "_RequiredListCodegenJobsRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
    },
)
_OptionalListCodegenJobsRequestRequestTypeDef = TypedDict(
    "_OptionalListCodegenJobsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListCodegenJobsRequestRequestTypeDef(
    _RequiredListCodegenJobsRequestRequestTypeDef, _OptionalListCodegenJobsRequestRequestTypeDef
):
    pass

ListCodegenJobsResponseTypeDef = TypedDict(
    "ListCodegenJobsResponseTypeDef",
    {
        "entities": List["CodegenJobSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListComponentsRequestListComponentsPaginateTypeDef = TypedDict(
    "_RequiredListComponentsRequestListComponentsPaginateTypeDef",
    {
        "appId": str,
        "environmentName": str,
    },
)
_OptionalListComponentsRequestListComponentsPaginateTypeDef = TypedDict(
    "_OptionalListComponentsRequestListComponentsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

class ListComponentsRequestListComponentsPaginateTypeDef(
    _RequiredListComponentsRequestListComponentsPaginateTypeDef,
    _OptionalListComponentsRequestListComponentsPaginateTypeDef,
):
    pass

_RequiredListComponentsRequestRequestTypeDef = TypedDict(
    "_RequiredListComponentsRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
    },
)
_OptionalListComponentsRequestRequestTypeDef = TypedDict(
    "_OptionalListComponentsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListComponentsRequestRequestTypeDef(
    _RequiredListComponentsRequestRequestTypeDef, _OptionalListComponentsRequestRequestTypeDef
):
    pass

ListComponentsResponseTypeDef = TypedDict(
    "ListComponentsResponseTypeDef",
    {
        "entities": List["ComponentSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListFormsRequestListFormsPaginateTypeDef = TypedDict(
    "_RequiredListFormsRequestListFormsPaginateTypeDef",
    {
        "appId": str,
        "environmentName": str,
    },
)
_OptionalListFormsRequestListFormsPaginateTypeDef = TypedDict(
    "_OptionalListFormsRequestListFormsPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

class ListFormsRequestListFormsPaginateTypeDef(
    _RequiredListFormsRequestListFormsPaginateTypeDef,
    _OptionalListFormsRequestListFormsPaginateTypeDef,
):
    pass

_RequiredListFormsRequestRequestTypeDef = TypedDict(
    "_RequiredListFormsRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
    },
)
_OptionalListFormsRequestRequestTypeDef = TypedDict(
    "_OptionalListFormsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListFormsRequestRequestTypeDef(
    _RequiredListFormsRequestRequestTypeDef, _OptionalListFormsRequestRequestTypeDef
):
    pass

ListFormsResponseTypeDef = TypedDict(
    "ListFormsResponseTypeDef",
    {
        "entities": List["FormSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListThemesRequestListThemesPaginateTypeDef = TypedDict(
    "_RequiredListThemesRequestListThemesPaginateTypeDef",
    {
        "appId": str,
        "environmentName": str,
    },
)
_OptionalListThemesRequestListThemesPaginateTypeDef = TypedDict(
    "_OptionalListThemesRequestListThemesPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)

class ListThemesRequestListThemesPaginateTypeDef(
    _RequiredListThemesRequestListThemesPaginateTypeDef,
    _OptionalListThemesRequestListThemesPaginateTypeDef,
):
    pass

_RequiredListThemesRequestRequestTypeDef = TypedDict(
    "_RequiredListThemesRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
    },
)
_OptionalListThemesRequestRequestTypeDef = TypedDict(
    "_OptionalListThemesRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListThemesRequestRequestTypeDef(
    _RequiredListThemesRequestRequestTypeDef, _OptionalListThemesRequestRequestTypeDef
):
    pass

ListThemesResponseTypeDef = TypedDict(
    "ListThemesResponseTypeDef",
    {
        "entities": List["ThemeSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MutationActionSetStateParameterOutputTypeDef = TypedDict(
    "MutationActionSetStateParameterOutputTypeDef",
    {
        "componentName": str,
        "property": str,
        "set": "ComponentPropertyOutputTypeDef",
    },
)

MutationActionSetStateParameterTypeDef = TypedDict(
    "MutationActionSetStateParameterTypeDef",
    {
        "componentName": str,
        "property": str,
        "set": "ComponentPropertyTypeDef",
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

PredicateOutputTypeDef = TypedDict(
    "PredicateOutputTypeDef",
    {
        "or": List[Dict[str, Any]],
        "and": List[Dict[str, Any]],
        "field": str,
        "operator": str,
        "operand": str,
        "operandType": str,
    },
    total=False,
)

PredicateTypeDef = TypedDict(
    "PredicateTypeDef",
    {
        "or": Sequence[Dict[str, Any]],
        "and": Sequence[Dict[str, Any]],
        "field": str,
        "operator": str,
        "operand": str,
        "operandType": str,
    },
    total=False,
)

PutMetadataFlagBodyTypeDef = TypedDict(
    "PutMetadataFlagBodyTypeDef",
    {
        "newValue": str,
    },
)

PutMetadataFlagRequestRequestTypeDef = TypedDict(
    "PutMetadataFlagRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "featureName": str,
        "body": "PutMetadataFlagBodyTypeDef",
    },
)

ReactStartCodegenJobDataOutputTypeDef = TypedDict(
    "ReactStartCodegenJobDataOutputTypeDef",
    {
        "module": JSModuleType,
        "target": JSTargetType,
        "script": JSScriptType,
        "renderTypeDeclarations": bool,
        "inlineSourceMap": bool,
    },
    total=False,
)

ReactStartCodegenJobDataTypeDef = TypedDict(
    "ReactStartCodegenJobDataTypeDef",
    {
        "module": JSModuleType,
        "target": JSTargetType,
        "script": JSScriptType,
        "renderTypeDeclarations": bool,
        "inlineSourceMap": bool,
    },
    total=False,
)

_RequiredRefreshTokenRequestBodyTypeDef = TypedDict(
    "_RequiredRefreshTokenRequestBodyTypeDef",
    {
        "token": str,
    },
)
_OptionalRefreshTokenRequestBodyTypeDef = TypedDict(
    "_OptionalRefreshTokenRequestBodyTypeDef",
    {
        "clientId": str,
    },
    total=False,
)

class RefreshTokenRequestBodyTypeDef(
    _RequiredRefreshTokenRequestBodyTypeDef, _OptionalRefreshTokenRequestBodyTypeDef
):
    pass

RefreshTokenRequestRequestTypeDef = TypedDict(
    "RefreshTokenRequestRequestTypeDef",
    {
        "provider": Literal["figma"],
        "refreshTokenBody": "RefreshTokenRequestBodyTypeDef",
    },
)

RefreshTokenResponseTypeDef = TypedDict(
    "RefreshTokenResponseTypeDef",
    {
        "accessToken": str,
        "expiresIn": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

_RequiredSectionalElementOutputTypeDef = TypedDict(
    "_RequiredSectionalElementOutputTypeDef",
    {
        "type": str,
    },
)
_OptionalSectionalElementOutputTypeDef = TypedDict(
    "_OptionalSectionalElementOutputTypeDef",
    {
        "position": "FieldPositionOutputTypeDef",
        "text": str,
        "level": int,
        "orientation": str,
        "excluded": bool,
    },
    total=False,
)

class SectionalElementOutputTypeDef(
    _RequiredSectionalElementOutputTypeDef, _OptionalSectionalElementOutputTypeDef
):
    pass

_RequiredSectionalElementTypeDef = TypedDict(
    "_RequiredSectionalElementTypeDef",
    {
        "type": str,
    },
)
_OptionalSectionalElementTypeDef = TypedDict(
    "_OptionalSectionalElementTypeDef",
    {
        "position": "FieldPositionTypeDef",
        "text": str,
        "level": int,
        "orientation": str,
        "excluded": bool,
    },
    total=False,
)

class SectionalElementTypeDef(_RequiredSectionalElementTypeDef, _OptionalSectionalElementTypeDef):
    pass

SortPropertyOutputTypeDef = TypedDict(
    "SortPropertyOutputTypeDef",
    {
        "field": str,
        "direction": SortDirectionType,
    },
)

SortPropertyTypeDef = TypedDict(
    "SortPropertyTypeDef",
    {
        "field": str,
        "direction": SortDirectionType,
    },
)

_RequiredStartCodegenJobDataTypeDef = TypedDict(
    "_RequiredStartCodegenJobDataTypeDef",
    {
        "renderConfig": "CodegenJobRenderConfigTypeDef",
    },
)
_OptionalStartCodegenJobDataTypeDef = TypedDict(
    "_OptionalStartCodegenJobDataTypeDef",
    {
        "genericDataSchema": "CodegenJobGenericDataSchemaTypeDef",
        "autoGenerateForms": bool,
        "features": "CodegenFeatureFlagsTypeDef",
        "tags": Mapping[str, str],
    },
    total=False,
)

class StartCodegenJobDataTypeDef(
    _RequiredStartCodegenJobDataTypeDef, _OptionalStartCodegenJobDataTypeDef
):
    pass

_RequiredStartCodegenJobRequestRequestTypeDef = TypedDict(
    "_RequiredStartCodegenJobRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "codegenJobToCreate": "StartCodegenJobDataTypeDef",
    },
)
_OptionalStartCodegenJobRequestRequestTypeDef = TypedDict(
    "_OptionalStartCodegenJobRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class StartCodegenJobRequestRequestTypeDef(
    _RequiredStartCodegenJobRequestRequestTypeDef, _OptionalStartCodegenJobRequestRequestTypeDef
):
    pass

StartCodegenJobResponseTypeDef = TypedDict(
    "StartCodegenJobResponseTypeDef",
    {
        "entity": "CodegenJobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ThemeSummaryTypeDef = TypedDict(
    "ThemeSummaryTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
        "name": str,
    },
)

_RequiredThemeTypeDef = TypedDict(
    "_RequiredThemeTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
        "name": str,
        "createdAt": datetime,
        "values": List["ThemeValuesOutputTypeDef"],
    },
)
_OptionalThemeTypeDef = TypedDict(
    "_OptionalThemeTypeDef",
    {
        "modifiedAt": datetime,
        "overrides": List["ThemeValuesOutputTypeDef"],
        "tags": Dict[str, str],
    },
    total=False,
)

class ThemeTypeDef(_RequiredThemeTypeDef, _OptionalThemeTypeDef):
    pass

ThemeValueOutputTypeDef = TypedDict(
    "ThemeValueOutputTypeDef",
    {
        "value": str,
        "children": List[Dict[str, Any]],
    },
    total=False,
)

ThemeValueTypeDef = TypedDict(
    "ThemeValueTypeDef",
    {
        "value": str,
        "children": Sequence[Dict[str, Any]],
    },
    total=False,
)

ThemeValuesOutputTypeDef = TypedDict(
    "ThemeValuesOutputTypeDef",
    {
        "key": str,
        "value": Dict[str, Any],
    },
    total=False,
)

ThemeValuesTypeDef = TypedDict(
    "ThemeValuesTypeDef",
    {
        "key": str,
        "value": Dict[str, Any],
    },
    total=False,
)

UpdateComponentDataTypeDef = TypedDict(
    "UpdateComponentDataTypeDef",
    {
        "id": str,
        "name": str,
        "sourceId": str,
        "componentType": str,
        "properties": Mapping[str, "ComponentPropertyTypeDef"],
        "children": Sequence["ComponentChildTypeDef"],
        "variants": Sequence["ComponentVariantTypeDef"],
        "overrides": Mapping[str, Mapping[str, str]],
        "bindingProperties": Mapping[str, "ComponentBindingPropertiesValueTypeDef"],
        "collectionProperties": Mapping[str, "ComponentDataConfigurationTypeDef"],
        "events": Mapping[str, "ComponentEventTypeDef"],
        "schemaVersion": str,
    },
    total=False,
)

_RequiredUpdateComponentRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateComponentRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
        "updatedComponent": "UpdateComponentDataTypeDef",
    },
)
_OptionalUpdateComponentRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateComponentRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class UpdateComponentRequestRequestTypeDef(
    _RequiredUpdateComponentRequestRequestTypeDef, _OptionalUpdateComponentRequestRequestTypeDef
):
    pass

UpdateComponentResponseTypeDef = TypedDict(
    "UpdateComponentResponseTypeDef",
    {
        "entity": "ComponentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateFormDataTypeDef = TypedDict(
    "UpdateFormDataTypeDef",
    {
        "name": str,
        "dataType": "FormDataTypeConfigTypeDef",
        "formActionType": FormActionTypeType,
        "fields": Mapping[str, "FieldConfigTypeDef"],
        "style": "FormStyleTypeDef",
        "sectionalElements": Mapping[str, "SectionalElementTypeDef"],
        "schemaVersion": str,
        "cta": "FormCTATypeDef",
        "labelDecorator": LabelDecoratorType,
    },
    total=False,
)

_RequiredUpdateFormRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateFormRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
        "updatedForm": "UpdateFormDataTypeDef",
    },
)
_OptionalUpdateFormRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateFormRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class UpdateFormRequestRequestTypeDef(
    _RequiredUpdateFormRequestRequestTypeDef, _OptionalUpdateFormRequestRequestTypeDef
):
    pass

UpdateFormResponseTypeDef = TypedDict(
    "UpdateFormResponseTypeDef",
    {
        "entity": "FormTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateThemeDataTypeDef = TypedDict(
    "_RequiredUpdateThemeDataTypeDef",
    {
        "values": Sequence["ThemeValuesTypeDef"],
    },
)
_OptionalUpdateThemeDataTypeDef = TypedDict(
    "_OptionalUpdateThemeDataTypeDef",
    {
        "id": str,
        "name": str,
        "overrides": Sequence["ThemeValuesTypeDef"],
    },
    total=False,
)

class UpdateThemeDataTypeDef(_RequiredUpdateThemeDataTypeDef, _OptionalUpdateThemeDataTypeDef):
    pass

_RequiredUpdateThemeRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateThemeRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
        "updatedTheme": "UpdateThemeDataTypeDef",
    },
)
_OptionalUpdateThemeRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateThemeRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class UpdateThemeRequestRequestTypeDef(
    _RequiredUpdateThemeRequestRequestTypeDef, _OptionalUpdateThemeRequestRequestTypeDef
):
    pass

UpdateThemeResponseTypeDef = TypedDict(
    "UpdateThemeResponseTypeDef",
    {
        "entity": "ThemeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredValueMappingOutputTypeDef = TypedDict(
    "_RequiredValueMappingOutputTypeDef",
    {
        "value": "FormInputValuePropertyOutputTypeDef",
    },
)
_OptionalValueMappingOutputTypeDef = TypedDict(
    "_OptionalValueMappingOutputTypeDef",
    {
        "displayValue": "FormInputValuePropertyOutputTypeDef",
    },
    total=False,
)

class ValueMappingOutputTypeDef(
    _RequiredValueMappingOutputTypeDef, _OptionalValueMappingOutputTypeDef
):
    pass

_RequiredValueMappingTypeDef = TypedDict(
    "_RequiredValueMappingTypeDef",
    {
        "value": "FormInputValuePropertyTypeDef",
    },
)
_OptionalValueMappingTypeDef = TypedDict(
    "_OptionalValueMappingTypeDef",
    {
        "displayValue": "FormInputValuePropertyTypeDef",
    },
    total=False,
)

class ValueMappingTypeDef(_RequiredValueMappingTypeDef, _OptionalValueMappingTypeDef):
    pass

_RequiredValueMappingsOutputTypeDef = TypedDict(
    "_RequiredValueMappingsOutputTypeDef",
    {
        "values": List["ValueMappingOutputTypeDef"],
    },
)
_OptionalValueMappingsOutputTypeDef = TypedDict(
    "_OptionalValueMappingsOutputTypeDef",
    {
        "bindingProperties": Dict[str, "FormInputBindingPropertiesValueOutputTypeDef"],
    },
    total=False,
)

class ValueMappingsOutputTypeDef(
    _RequiredValueMappingsOutputTypeDef, _OptionalValueMappingsOutputTypeDef
):
    pass

_RequiredValueMappingsTypeDef = TypedDict(
    "_RequiredValueMappingsTypeDef",
    {
        "values": Sequence["ValueMappingTypeDef"],
    },
)
_OptionalValueMappingsTypeDef = TypedDict(
    "_OptionalValueMappingsTypeDef",
    {
        "bindingProperties": Mapping[str, "FormInputBindingPropertiesValueTypeDef"],
    },
    total=False,
)

class ValueMappingsTypeDef(_RequiredValueMappingsTypeDef, _OptionalValueMappingsTypeDef):
    pass
