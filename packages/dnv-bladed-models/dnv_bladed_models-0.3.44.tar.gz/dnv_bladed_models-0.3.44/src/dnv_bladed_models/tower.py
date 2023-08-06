# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401
from enum import Enum, IntEnum

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Type, Union, Callable  # noqa: F401
from pathlib import Path
from typing import TypeVar
Model = TypeVar('Model', bound='BaseModel')
StrBytes = Union[str, bytes]

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator, root_validator, Extra  # noqa: F401


from dnv_bladed_models.added_inertia import AddedInertia

from dnv_bladed_models.structure import Structure

from dnv_bladed_models.tower_aerodynamic_properties import TowerAerodynamicProperties

from dnv_bladed_models.tower_can import TowerCan

from dnv_bladed_models.tower_connectable_node import TowerConnectableNode

from dnv_bladed_models.tower_hydrodynamic_properties import TowerHydrodynamicProperties

from dnv_bladed_models.tower_material import TowerMaterial

from dnv_bladed_models.tower_output_group import TowerOutputGroup

from dnv_bladed_models.tower_sensor import TowerSensor


class Tower(Structure, ComponentType='Tower'):
    """Tower - An axisymmetric tower, made from a series of tower cans.
    
    Attributes:
    ----------
    MaterialsLibrary : Dict[str, TowerMaterial], default=dict()
        A library of material definitions.  These can be referenced by the tower cans.
    Cans : List[TowerCan], default=list()
        A list of cans, each one sitting on the top of the previous one.  These cans can be constant-section or tapered.
    AerodynamicProperties : TowerAerodynamicProperties
    HydrodynamicProperties : TowerHydrodynamicProperties
    PointInertias : List[AddedInertia], default=list()
        A list of additional inertias to add to the tower.
    OutputGroups : Dict[str, TowerOutputGroup], default=dict()
        A library which contains any number of named output groups.  These can be referenced from 'SelectedOutputGroup'.
    ConnectableNodes : Dict[str, TowerConnectableNode], default=dict()
        A declaration of what nodes can be connected to.
    Sensors : Dict[str, TowerSensor], default=dict()
        A library of sensor objects, each specified with a unique keyword.  This keyword is used for referencing the item elsewhere in the model.
    ComponentType : str, readonly, default='Tower'
        Allows the schema to identify the type of the object.  For this type of object, this must always be set to 'Tower'
    
    """

    MaterialsLibrary: Optional[Dict[str, TowerMaterial]] = Field(alias="MaterialsLibrary", default=dict())
    Cans: Optional[List[TowerCan]] = Field(alias="Cans", default=list())
    AerodynamicProperties: Optional[TowerAerodynamicProperties] = Field(alias="AerodynamicProperties", default=None)
    HydrodynamicProperties: Optional[TowerHydrodynamicProperties] = Field(alias="HydrodynamicProperties", default=None)
    PointInertias: Optional[List[AddedInertia]] = Field(alias="PointInertias", default=list())
    OutputGroups: Optional[Dict[str, TowerOutputGroup]] = Field(alias="OutputGroups", default=dict())
    ConnectableNodes: Optional[Dict[str, TowerConnectableNode]] = Field(alias="ConnectableNodes", default=dict())
    Sensors: Optional[Dict[str, TowerSensor]] = Field(alias="Sensors", default=dict())
    ComponentType: Optional[str] = Field(alias="ComponentType", default='Tower', allow_mutation=False)

    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    @root_validator(pre=True)
    def _parsing_ignores_underscore_properties(cls, values: dict[str, any]):
        allowed_vals = {}
        for key, val in values.items():
            if not key.startswith('_'):
                if isinstance(val, dict):
                    allowed_child_vals = {}
                    for child_key, child_val in val.items():
                        if not child_key.startswith('_'):
                            allowed_child_vals[child_key] = child_val
                    allowed_vals[key] = allowed_child_vals
                else:
                    allowed_vals[key] = val
        return allowed_vals

    def to_json(
        self,
        *, 
        include: Optional[Union['AbstractSetIntStr', 'MappingIntStrAny']] = None, 
        exclude: Optional[Union['AbstractSetIntStr', 'MappingIntStrAny']] = None, 
        by_alias: bool = True, 
        skip_defaults: Optional[bool] = None, 
        exclude_unset: bool = False, 
        exclude_defaults: bool = False, 
        exclude_none: bool = True, 
        encoder: Optional[Callable[[Any], Any]] = None, 
        models_as_dict: bool = True, 
        **dumps_kwargs: Any) -> str:

        r"""
        Generates a JSON string representation of the model.
        
        Notes
        -----
        `include` and `exclude` arguments as per `dict()`.

        `encoder` is an optional function to supply as `default` to json.dumps(), other arguments as per `json.dumps()`.

        Examples
        --------
        >>> model.to_json()

        Renders the full JSON representation of the model object.
        """

        if dumps_kwargs.get('indent') is None:
            dumps_kwargs.update(indent=2)

        return super().json(
                include=include, 
                exclude=exclude, 
                by_alias=by_alias, 
                skip_defaults=skip_defaults, 
                exclude_unset=exclude_unset, 
                exclude_defaults=exclude_defaults, 
                exclude_none=exclude_none, 
                encoder=encoder, 
                models_as_dict=models_as_dict, 
                **dumps_kwargs)
    
    @classmethod
    def from_file(
        cls: Type['Model'],
        path: Union[str, Path]) -> 'Model':
        
        r"""
        Loads a model from a given file path.

        Parameters
        ----------
        path : string
            The file path to the model.

        Returns
        -------
        Tower
            The model object.

        Raises
        ------
        ValueError, ValidationError
            If the JSON document does not correctly describe the model according to the model schema.

        Examples
        --------
        >>> model = Tower.from_file('/path/to/file')
        """
        
        return super().parse_file(path=path)
    
    @classmethod
    def from_json(
        cls: Type['Model'],
        b: StrBytes) -> 'Model':

        r"""
        Creates a model object from a JSON string.

        Parameters
        ----------
        b: StrBytes
            The JSON string describing the model.

        Returns
        -------
        Tower
            The model object.

        Raises
        ------
        ValueError, ValidationError
            If the JSON document does not correctly describe the model according to the model schema.

        Examples
        --------
        >>> model = Tower.from_json('{ ... }')
        """

        return super().parse_raw(
            b=b,
            content_type='application/json')
    
    @classmethod
    def from_dict(
        cls: Type['Model'],
         obj: Any) -> 'Model':

        r"""
        Creates a model object from a dict.

        Parameters
        ----------
        obj : Any
            The dictionary object describing the model.

        Returns
        -------
        Tower
            The model object.

        Raises
        ------
        ValueError, ValidationError
            If the JSON document does not correctly describe the model according to the model schema.
        """
        
        return super().parse_obj(obj=obj)
    
    def to_file(
        self,
        path: Union[str, Path]):

        r"""
        Writes the model as a JSON document to a file with UTF8 encoding.        

        Parameters
        ----------                
        path : string
            The file path to which the model will be written.

        Examples
        --------
        >>> model.to_file('/path/to/file')

        """

        with open(file=path, mode='w', encoding="utf8") as output_file:
            output_file.write(self.to_json())

Tower.update_forward_refs()
