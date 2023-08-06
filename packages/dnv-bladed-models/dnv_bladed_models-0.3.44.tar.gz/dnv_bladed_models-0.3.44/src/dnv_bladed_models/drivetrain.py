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


from dnv_bladed_models.brake import Brake

from dnv_bladed_models.component import Component

from dnv_bladed_models.connectable_node import ConnectableNode

from dnv_bladed_models.drivetrain_output_group import DrivetrainOutputGroup

from dnv_bladed_models.high_speed_shaft_flexibility import HighSpeedShaftFlexibility

from dnv_bladed_models.mechanical_losses import MechanicalLosses

from dnv_bladed_models.pallet_mounting_flexibility import PalletMountingFlexibility

from dnv_bladed_models.slipping_clutch import SlippingClutch


class Drivetrain(Component, ComponentType='Drivetrain'):
    """Drivetrain - A drivetrain component, typically connecting the nacelle (at it&#39;s main bearing) to a generator.
    
    Attributes:
    ----------
    ShaftBrakes : List[Brake], default=list()
        Definitions for the brakes on the various shafts of the drivetrain.
    GearboxRatio : float
        A number representing a fraction, ratio, or other non-dimensionalised property.
    GearboxInertia : float
        A number representing an angular inertia.  The SI units for angular inertia are kilogram radian squareds.
    HighSpeedShaftInertia : float
        A number representing an angular inertia.  The SI units for angular inertia are kilogram radian squareds.
    SlippingClutch : SlippingClutch
    HighSpeedShaftTorsion : HighSpeedShaftFlexibility
    MountingFlexibility : PalletMountingFlexibility
    Losses : MechanicalLosses, abstract
    OutputGroups : Dict[str, DrivetrainOutputGroup], default=dict()
        A library which contains any number of named output groups.  These can be referenced from 'SelectedOutputGroup'
    ConnectableNodes : Dict[str, ConnectableNode], default=dict()
        A declaration of what nodes can be connected to.
    ComponentType : str, readonly, default='Drivetrain'
        Allows the schema to identify the type of the object.  For this type of object, this must always be set to 'Drivetrain'
    
    Notes:
    ---------
    Losses has the following concrete types:
        - PowerScalingLosses
        - TorqueScalingLosses
    
    """

    ShaftBrakes: Optional[List[Brake]] = Field(alias="ShaftBrakes", default=list())
    GearboxRatio: Optional[float] = Field(alias="GearboxRatio", default=None)
    GearboxInertia: Optional[float] = Field(alias="GearboxInertia", default=None)
    HighSpeedShaftInertia: Optional[float] = Field(alias="HighSpeedShaftInertia", default=None)
    SlippingClutch: Optional[SlippingClutch] = Field(alias="SlippingClutch", default=None)
    HighSpeedShaftTorsion: Optional[HighSpeedShaftFlexibility] = Field(alias="HighSpeedShaftTorsion", default=None)
    MountingFlexibility: Optional[PalletMountingFlexibility] = Field(alias="MountingFlexibility", default=None)
    Losses: Optional[MechanicalLosses] = Field(alias="Losses", default=None)
    OutputGroups: Optional[Dict[str, DrivetrainOutputGroup]] = Field(alias="OutputGroups", default=dict())
    ConnectableNodes: Optional[Dict[str, ConnectableNode]] = Field(alias="ConnectableNodes", default=dict())
    ComponentType: Optional[str] = Field(alias="ComponentType", default='Drivetrain', allow_mutation=False)

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
        Drivetrain
            The model object.

        Raises
        ------
        ValueError, ValidationError
            If the JSON document does not correctly describe the model according to the model schema.

        Examples
        --------
        >>> model = Drivetrain.from_file('/path/to/file')
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
        Drivetrain
            The model object.

        Raises
        ------
        ValueError, ValidationError
            If the JSON document does not correctly describe the model according to the model schema.

        Examples
        --------
        >>> model = Drivetrain.from_json('{ ... }')
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
        Drivetrain
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

Drivetrain.update_forward_refs()
