"""
Attributes
----------

Represent Attributes in an RDF Data Cube.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Set, TypeVar

import pandas as pd

from csvcubed.inputs import PandasDataTypes, pandas_input_to_columnar_optional_str
from csvcubed.models.cube.qb.components.constants import ACCEPTED_DATATYPE_MAPPING
from csvcubed.models.uriidentifiable import UriIdentifiable
from csvcubed.models.validatedmodel import ValidationFunction
from csvcubed.models.validationerror import (
    ValidateModelPropertiesError,
    ValidationError,
)
from csvcubed.utils import validations as v
from csvcubed.utils.qb.validation.uri_safe import ensure_no_uri_safe_conflicts
from csvcubed.utils.uri import uri_safe

from .arbitraryrdf import ArbitraryRdf, RdfSerialisationHint, TripleFragmentBase
from .attributevalue import NewQbAttributeValue
from .datastructuredefinition import QbColumnStructuralDefinition
from .validationerrors import UndefinedAttributeValueUrisError


@dataclass
class QbAttribute(QbColumnStructuralDefinition, ArbitraryRdf, ABC):
    @abstractmethod
    def get_is_required(self) -> bool:
        pass

    @abstractmethod
    def get_new_attribute_values(self) -> List[NewQbAttributeValue]:
        pass

    @abstractmethod
    def get_observed_value_col_title(self) -> Optional[str]:
        pass

    def _validate_data_new_attribute_values(
        self, data: pd.Series
    ) -> List[ValidationError]:
        """
        Validate that all of the values in :obj`data` are defined in :attr:`new_attribute_values` if values are defined.
        """
        if len(self.new_attribute_values) > 0:  # type: ignore
            expected_values = {
                av.uri_safe_identifier for av in self.new_attribute_values  # type: ignore
            }
            actual_values = {
                uri_safe(str(v)) for v in set(data.unique()) if not pd.isna(v)
            }
            undefined_values = expected_values - actual_values

            if len(undefined_values) > 0:
                return [UndefinedAttributeValueUrisError(self, undefined_values)]

        return []


@dataclass
class ExistingQbAttribute(QbAttribute):
    attribute_uri: str
    new_attribute_values: List[NewQbAttributeValue] = field(
        default_factory=list, repr=False
    )
    is_required: bool = field(default=False, repr=False)
    arbitrary_rdf: List[TripleFragmentBase] = field(default_factory=list, repr=False)
    observed_value_col_title: Optional[str] = field(default=None, repr=False)

    def get_observed_value_col_title(self) -> Optional[str]:
        return self.observed_value_col_title

    def _get_arbitrary_rdf(self) -> List[TripleFragmentBase]:
        return self.arbitrary_rdf

    def get_is_required(self) -> bool:
        return self.is_required

    def get_new_attribute_values(self) -> List[NewQbAttributeValue]:
        return self.new_attribute_values

    def get_default_node_serialisation_hint(self) -> RdfSerialisationHint:
        return RdfSerialisationHint.Component

    def get_permitted_rdf_fragment_hints(self) -> Set[RdfSerialisationHint]:
        return {RdfSerialisationHint.Component}

    def validate_data(
        self,
        data: pd.Series,
        column_csvw_name: str,
        csv_column_uri_template: str,
        column_csv_title: str,
    ) -> List[ValidationError]:
        return self._validate_data_new_attribute_values(data)

    def _get_validations(self) -> Dict[str, ValidationFunction]:
        return {
            "attribute_uri": v.uri,
            "new_attribute_values": v.all_of(
                v.list(v.validated_model(NewQbAttributeValue)),
                self._validate_attribute_values_non_conflicting,
            ),
            "is_required": v.boolean,
            "arbitrary_rdf": v.list(v.validated_model(TripleFragmentBase)),
            "observed_value_col_title": v.optional(v.string),
        }

    @staticmethod
    def _validate_attribute_values_non_conflicting(
        new_attribute_values: List[NewQbAttributeValue], property_path: List[str]
    ) -> List[ValidateModelPropertiesError]:
        """
        Ensure that there are no collisions where multiple attribute values map to the same URI-safe value.
        """
        return ensure_no_uri_safe_conflicts(
            [(val.label, val.uri_safe_identifier) for val in new_attribute_values],
            ExistingQbAttribute,
            property_path,
            new_attribute_values,
        )


@dataclass
class NewQbAttribute(QbAttribute, UriIdentifiable):
    label: str
    description: Optional[str] = field(default=None, repr=False)
    new_attribute_values: List[NewQbAttributeValue] = field(
        default_factory=list, repr=False
    )
    parent_attribute_uri: Optional[str] = field(default=None, repr=False)
    source_uri: Optional[str] = field(default=None, repr=False)
    is_required: bool = field(default=False, repr=False)
    uri_safe_identifier_override: Optional[str] = field(default=None, repr=False)
    arbitrary_rdf: List[TripleFragmentBase] = field(default_factory=list, repr=False)
    observed_value_col_title: Optional[str] = field(default=None, repr=False)

    def get_observed_value_col_title(self) -> Optional[str]:
        return self.observed_value_col_title

    def _get_arbitrary_rdf(self) -> List[TripleFragmentBase]:
        return self.arbitrary_rdf

    def get_is_required(self) -> bool:
        return self.is_required

    def get_new_attribute_values(self) -> List[NewQbAttributeValue]:
        return self.new_attribute_values

    def get_default_node_serialisation_hint(self) -> RdfSerialisationHint:
        return RdfSerialisationHint.Property

    def get_permitted_rdf_fragment_hints(self) -> Set[RdfSerialisationHint]:
        return {
            RdfSerialisationHint.Property,
            RdfSerialisationHint.Component,
        }

    def get_identifier(self) -> str:
        return self.label

    @staticmethod
    def from_data(
        label: str,
        data: PandasDataTypes,
        description: Optional[str] = None,
        parent_attribute_uri: Optional[str] = None,
        source_uri: Optional[str] = None,
        is_required: bool = False,
        uri_safe_identifier_override: Optional[str] = None,
        arbitrary_rdf: List[TripleFragmentBase] = list(),
        observed_value_col_title: Optional[str] = None,
    ) -> "NewQbAttribute":
        columnar_data = pandas_input_to_columnar_optional_str(data)
        new_attribute_values_from_column = [
            NewQbAttributeValue(v)
            for v in sorted(set([d for d in columnar_data if d is not None]))
        ]

        return NewQbAttribute(
            label=label,
            description=description,
            new_attribute_values=new_attribute_values_from_column,
            parent_attribute_uri=parent_attribute_uri,
            source_uri=source_uri,
            is_required=is_required,
            uri_safe_identifier_override=uri_safe_identifier_override,
            arbitrary_rdf=arbitrary_rdf,
            observed_value_col_title=observed_value_col_title,
        )

    def validate_data(
        self,
        data: pd.Series,
        column_csvw_name: str,
        csv_column_uri_template: str,
        column_csv_title: str,
    ) -> List[ValidationError]:
        return self._validate_data_new_attribute_values(data)

    def _get_validations(self) -> Dict[str, ValidationFunction]:
        return {
            "label": v.string,
            "description": v.optional(v.string),
            "new_attribute_values": v.all_of(
                v.list(v.validated_model(NewQbAttributeValue)),
                self._validate_concepts_non_conflicting,
            ),
            "parent_attribute_uri": v.optional(v.uri),
            "source_uri": v.optional(v.uri),
            "is_required": v.boolean,
            **UriIdentifiable._get_validations(self),
            "arbitrary_rdf": v.list(v.validated_model(TripleFragmentBase)),
            "observed_value_col_title": v.optional(v.string),
        }

    @staticmethod
    def _validate_concepts_non_conflicting(
        new_attribute_values: List[NewQbAttributeValue], property_path: List[str]
    ) -> List[ValidateModelPropertiesError]:
        """
        Ensure that there are no collisions where multiple attribute values map to the same URI-safe value.
        """
        return ensure_no_uri_safe_conflicts(
            [(val.label, val.uri_safe_identifier) for val in new_attribute_values],
            NewQbAttribute,
            property_path,
            new_attribute_values,
        )


@dataclass
class QbAttributeLiteral(QbAttribute, ABC):
    """A literal attribute allows for a non-uri-based resource to be referenced in attributes. Acceptable types
    are numeric, dates, times, and strings.
    """

    data_type: str = field(repr=False)

    def _get_validations(self) -> Dict[str, ValidationFunction]:
        return {"data_type": v.any_of(v.data_type, v.uri)}


@dataclass
class ExistingQbAttributeLiteral(ExistingQbAttribute, QbAttributeLiteral):
    new_attribute_values: List[NewQbAttributeValue] = field(
        default_factory=list, init=False, repr=False
    )
    arbitrary_rdf: List[TripleFragmentBase] = field(default_factory=list, repr=False)
    observed_value_col_title: Optional[str] = field(default=None, repr=False)

    def get_observed_value_col_title(self) -> Optional[str]:
        return self.observed_value_col_title

    def validate_data(
        self,
        data: pd.Series,
        column_csvw_name: str,
        csv_column_uri_template: str,
        column_csv_title: str,
    ) -> List[ValidationError]:
        # csv-validation will check that all literals match the expected data type.
        return []

    def _get_validations(self) -> Dict[str, ValidationFunction]:
        return {
            **QbAttributeLiteral._get_validations(self),
            **ExistingQbAttribute._get_validations(self),
            "new_attribute_values": v.list(v.validated_model(NewQbAttributeValue)),
            "arbitrary_rdf": v.list(v.validated_model(TripleFragmentBase)),
            "observed_value_col_title": v.optional(v.string),
        }


@dataclass
class NewQbAttributeLiteral(NewQbAttribute, QbAttributeLiteral):
    new_attribute_values: List[NewQbAttributeValue] = field(
        default_factory=list, init=False, repr=False
    )
    arbitrary_rdf: List[TripleFragmentBase] = field(default_factory=list, repr=False)
    observed_value_col_title: Optional[str] = field(default=None, repr=False)

    def get_observed_value_col_title(self) -> Optional[str]:
        return self.observed_value_col_title

    def _get_arbitrary_rdf(self) -> List[TripleFragmentBase]:
        return self.arbitrary_rdf

    def validate_data(
        self,
        data: pd.Series,
        column_csvw_name: str,
        csv_column_uri_template: str,
        column_csv_title: str,
    ) -> List[ValidationError]:
        # csv-validation will check that all literals match the expected data type.
        return []

    def _get_validations(self) -> Dict[str, ValidationFunction]:
        return {
            **QbAttributeLiteral._get_validations(self),
            **NewQbAttribute._get_validations(self),
            "new_attribute_values": v.list(v.validated_model(NewQbAttributeValue)),
            "arbitrary_rdf": v.list(v.validated_model(TripleFragmentBase)),
            "observed_value_col_title": v.optional(v.string),
        }
