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


from dnv_bladed_models.dnv import Dnv


class BladeLoadOutputs(Dnv):
    """BladeLoadOutputs - Loads selected
    
    Attributes:
    ----------
    FlapwiseBendingLoads : bool, default=False
         Output blade bending moments for the flapwise direction (0=no, 1=yes).
    EdgewiseBendingLoads : bool, default=False
         Output blade bending moments for the edgewise direction (0=no, 1=yes).
    FlapwiseShearLoads : bool, default=False
         Output blade shear forces for the flapwise direction (0=no, 1=yes).
    EdgewiseShearLoads : bool, default=False
         Output blade shear forces for the edgewise direction (0=no, 1=yes).
    OutOfPlaneBendingLoads : bool, default=False
         Output blade bending moments for out of plane direction (0=no, 1=yes).
    InPlaneBendingLoads : bool, default=False
         Output blade bending moments for in plane direction (0=no, 1=yes).
    OutOfPlaneShearLoads : bool, default=False
         Output blade shear forces for out of plane direction (0=no, 1=yes).
    InPlaneShearLoads : bool, default=False
         Output blade shear forces for in plane direction (0=no, 1=yes).
    RadialForces : bool, default=False
         Output blade radial forces (0=no, 1=yes).
    LoadsInRootAxisSystem : bool, default=False
         Output blade loads about the root axes system (0=no, 1=yes).
    LoadsInAeroAxisSystem : bool, default=False
         Output blade loads about the aero axes system (0=no, 1=yes).
    LoadsInUserAxisSystem : bool, default=False
         Output blade loads about the user defined axes system (0=no, 1=yes).
    
    """

    FlapwiseBendingLoads: Optional[bool] = Field(alias="FlapwiseBendingLoads", default=False)
    EdgewiseBendingLoads: Optional[bool] = Field(alias="EdgewiseBendingLoads", default=False)
    FlapwiseShearLoads: Optional[bool] = Field(alias="FlapwiseShearLoads", default=False)
    EdgewiseShearLoads: Optional[bool] = Field(alias="EdgewiseShearLoads", default=False)
    OutOfPlaneBendingLoads: Optional[bool] = Field(alias="OutOfPlaneBendingLoads", default=False)
    InPlaneBendingLoads: Optional[bool] = Field(alias="InPlaneBendingLoads", default=False)
    OutOfPlaneShearLoads: Optional[bool] = Field(alias="OutOfPlaneShearLoads", default=False)
    InPlaneShearLoads: Optional[bool] = Field(alias="InPlaneShearLoads", default=False)
    RadialForces: Optional[bool] = Field(alias="RadialForces", default=False)
    LoadsInRootAxisSystem: Optional[bool] = Field(alias="LoadsInRootAxisSystem", default=False)
    LoadsInAeroAxisSystem: Optional[bool] = Field(alias="LoadsInAeroAxisSystem", default=False)
    LoadsInUserAxisSystem: Optional[bool] = Field(alias="LoadsInUserAxisSystem", default=False)

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
        BladeLoadOutputs
            The model object.

        Raises
        ------
        ValueError, ValidationError
            If the JSON document does not correctly describe the model according to the model schema.

        Examples
        --------
        >>> model = BladeLoadOutputs.from_file('/path/to/file')
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
        BladeLoadOutputs
            The model object.

        Raises
        ------
        ValueError, ValidationError
            If the JSON document does not correctly describe the model according to the model schema.

        Examples
        --------
        >>> model = BladeLoadOutputs.from_json('{ ... }')
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
        BladeLoadOutputs
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

BladeLoadOutputs.update_forward_refs()
