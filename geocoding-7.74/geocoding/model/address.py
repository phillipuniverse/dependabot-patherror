"""
    Geocoding and Search API v7

    This document describes the Geocoding and Search API.  # noqa: E501

    The version of the OpenAPI document: 7.74
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from geocoding.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)
from ..model_utils import OpenApiModel
from geocoding.exceptions import ApiAttributeError



class Address(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'label': (str,),  # noqa: E501
            'country_code': (str,),  # noqa: E501
            'country_name': (str,),  # noqa: E501
            'state_code': (str,),  # noqa: E501
            'state': (str,),  # noqa: E501
            'county_code': (str,),  # noqa: E501
            'county': (str,),  # noqa: E501
            'city': (str,),  # noqa: E501
            'district': (str,),  # noqa: E501
            'subdistrict': (str,),  # noqa: E501
            'street': (str,),  # noqa: E501
            'block': (str,),  # noqa: E501
            'subblock': (str,),  # noqa: E501
            'postal_code': (str,),  # noqa: E501
            'house_number': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'label': 'label',  # noqa: E501
        'country_code': 'countryCode',  # noqa: E501
        'country_name': 'countryName',  # noqa: E501
        'state_code': 'stateCode',  # noqa: E501
        'state': 'state',  # noqa: E501
        'county_code': 'countyCode',  # noqa: E501
        'county': 'county',  # noqa: E501
        'city': 'city',  # noqa: E501
        'district': 'district',  # noqa: E501
        'subdistrict': 'subdistrict',  # noqa: E501
        'street': 'street',  # noqa: E501
        'block': 'block',  # noqa: E501
        'subblock': 'subblock',  # noqa: E501
        'postal_code': 'postalCode',  # noqa: E501
        'house_number': 'houseNumber',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """Address - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            label (str): Assembled address value built out of the address components according to the regional postal rules. These are the same rules for all endpoints. It may not include all the input terms. For example: \"Schulstraße 4, 32547 Bad Oeynhausen, Germany\". [optional]  # noqa: E501
            country_code (str): A three-letter country code. For example: \"DEU\". [optional]  # noqa: E501
            country_name (str): The localised country name. For example: \"Deutschland\". [optional]  # noqa: E501
            state_code (str): A state code or state name abbreviation – country specific. For example, in the United States it is the two letter state abbreviation: \"CA\" for California.. [optional]  # noqa: E501
            state (str): The state division of a country. For example: \"North Rhine-Westphalia\". [optional]  # noqa: E501
            county_code (str): A county code or county name abbreviation – country specific. For example, for Italy it is the province abbreviation: \"RM\" for Rome.. [optional]  # noqa: E501
            county (str): A division of a state; typically, a secondary-level administrative division of a country or equivalent.. [optional]  # noqa: E501
            city (str): The name of the primary locality of the place. For example: \"Bad Oyenhausen\". [optional]  # noqa: E501
            district (str): A division of city; typically an administrative unit within a larger city or a customary name of a city's neighborhood. For example: \"Bad Oyenhausen\". [optional]  # noqa: E501
            subdistrict (str): A subdivision of a district. For example: \"Minden-Lübbecke\". [optional]  # noqa: E501
            street (str): Name of street. For example: \"Schulstrasse\". [optional]  # noqa: E501
            block (str): Name of block.. [optional]  # noqa: E501
            subblock (str): Name of sub-block.. [optional]  # noqa: E501
            postal_code (str): An alphanumeric string included in a postal address to facilitate mail sorting, such as post code, postcode, or ZIP code. For example: \"32547\". [optional]  # noqa: E501
            house_number (str): House number. For example: \"4\". [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """Address - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            label (str): Assembled address value built out of the address components according to the regional postal rules. These are the same rules for all endpoints. It may not include all the input terms. For example: \"Schulstraße 4, 32547 Bad Oeynhausen, Germany\". [optional]  # noqa: E501
            country_code (str): A three-letter country code. For example: \"DEU\". [optional]  # noqa: E501
            country_name (str): The localised country name. For example: \"Deutschland\". [optional]  # noqa: E501
            state_code (str): A state code or state name abbreviation – country specific. For example, in the United States it is the two letter state abbreviation: \"CA\" for California.. [optional]  # noqa: E501
            state (str): The state division of a country. For example: \"North Rhine-Westphalia\". [optional]  # noqa: E501
            county_code (str): A county code or county name abbreviation – country specific. For example, for Italy it is the province abbreviation: \"RM\" for Rome.. [optional]  # noqa: E501
            county (str): A division of a state; typically, a secondary-level administrative division of a country or equivalent.. [optional]  # noqa: E501
            city (str): The name of the primary locality of the place. For example: \"Bad Oyenhausen\". [optional]  # noqa: E501
            district (str): A division of city; typically an administrative unit within a larger city or a customary name of a city's neighborhood. For example: \"Bad Oyenhausen\". [optional]  # noqa: E501
            subdistrict (str): A subdivision of a district. For example: \"Minden-Lübbecke\". [optional]  # noqa: E501
            street (str): Name of street. For example: \"Schulstrasse\". [optional]  # noqa: E501
            block (str): Name of block.. [optional]  # noqa: E501
            subblock (str): Name of sub-block.. [optional]  # noqa: E501
            postal_code (str): An alphanumeric string included in a postal address to facilitate mail sorting, such as post code, postcode, or ZIP code. For example: \"32547\". [optional]  # noqa: E501
            house_number (str): House number. For example: \"4\". [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
