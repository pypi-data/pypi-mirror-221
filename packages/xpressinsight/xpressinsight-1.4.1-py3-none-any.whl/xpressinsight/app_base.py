"""
    Xpress Insight Python package
    =============================

    This is an internal file of the 'xpressinsight' package. Do not import it directly.

    This material is the confidential, proprietary, unpublished property
    of Fair Isaac Corporation.  Receipt or possession of this material
    does not convey rights to divulge, reproduce, use, or allow others
    to use it without the specific written authorization of Fair Isaac
    Corporation and use must conform strictly to the license agreement.

    Copyright (c) 2020-2022 Fair Isaac Corporation. All rights reserved.
"""

import os
import sys
import types
from typing import ValuesView
import inspect

if sys.version_info < (3, 9):
    from typing_extensions import get_args, get_type_hints, get_origin, Annotated
else:
    from typing import get_args, get_type_hints, get_origin, Annotated

from .entities import *
from .exec_mode import ExecMode, ExecModeLoad, ExecModeRun
from .interface import AppInterface
from .interface_test import AppTestInterface
from .interface_rest import AppRestInterface
from .parquet_connector import ParquetConnector
from .table_connector import DataConnector


class AppVersion:
    #
    """
        Class to represent the version number of an Insight Python app, according to semver
        (Semantic Versioning) conventions.

        Examples
        --------
        Example of specifying version "1.2.3"

        >>> @xi.AppConfig(name="My App", version=xi.AppVersion(1, 2, 3))
        ... class InsightApp(xi.AppBase):
        ...     pass

        See Also
        --------
        AppConfig
        AppVersion.__init__
        """

    def __init__(self, major: int = 0, minor: int = 0, patch: int = 0):
        """
        Initializes `AppVersion` with major, minor, and patch version information.

        Parameters
        ----------
        major : int
            The major version between 0 and 999.
        minor : int
            The minor version between 0 and 999.
        patch : int
            The patch version between 0 and 999.

        See Also
        --------
        AppConfig
        AppVersion
        """

        for i in [major, minor, patch]:
            if not isinstance(i, int):
                raise TypeError('The parameters of AppVersion must be integers, '
                                f'but one parameter is a {type(i).__name__} and has value {i}.')
            if i < 0 or 999 < i:
                raise ValueError("The parameters of AppVersion must be integers between 0 and 999, "
                                 "but one parameter value is {}.".format(i))

        self.__major: int = major
        self.__minor: int = minor
        self.__patch: int = patch

    @property
    def major(self) -> int:
        return self.__major

    @property
    def minor(self) -> int:
        return self.__minor

    @property
    def patch(self) -> int:
        return self.__patch

    def __str__(self):
        return "{}.{}.{}".format(self.__major, self.__minor, self.__patch)

    def __repr__(self):
        return "AppVersion({}, {}, {})".format(self.__major, self.__minor, self.__patch)


class AppConfig:
    #
    """
    Insight application configuration decorator. An Insight application class must be decorated with this decorator.

    Examples
    --------
    Example of a minimal Insight app that uses the application configuration:

    >>> import xpressinsight as xi
    ... import sys
    ...
    ... @xi.AppConfig(name="AppConfig Example",
    ...               version=xi.AppVersion(1, 0, 0))
    ... class InsightApp(xi.AppBase):
    ...     @xi.ExecModeLoad()
    ...     def load(self):
    ...         print(f"Current app name: {self.insight.app_name}")
    ...         print(f"Default app name: {self.app_cfg.name}")
    ...         print(f"App version:      {self.app_cfg.version}")
    ...
    ...     @xi.ExecModeRun()
    ...     def run(self):
    ...         pass
    ...
    ... if __name__ == "__main__":
    ...     app = xi.create_app(InsightApp)
    ...     app.insight.app_name = "My " + app.app_cfg.name
    ...     sys.exit(app.call_exec_mode("LOAD"))
    ...
    Current app name: My AppConfig Example
    Default app name: AppConfig Example
    App version:      1.0.0

    See Also
    --------
    AppConfig.__init__
    AppBase.app_cfg
    """
    __name: str
    __version: AppVersion
    __result_data: ResultData

    def __init__(self,
                 name: str,
                 version: AppVersion = AppVersion(0, 0, 0),
                 result_data: ResultData = ResultData(),
                 scen_types: List[str] = None):
        """
        Insight AppConfig constructor. Use this decorator to decorate the Insight application class.

        Parameters
        ----------
        name : str
            Name of the Insight application.
        version : AppVersion = AppVersion(0, 0, 0)
            Version of the Insight application.
        result_data : ResultData = ResultData()):
            Configuration for result data handling.
        scen_types : List[str] = None
            List of scenario type identifiers. It is not necessary to declare the standard
            `"SCENARIO"` type as all apps have this type.

        See Also
        --------
        AppConfig
        AppBase.app_cfg
        """
        self.__entities: Dict[str, EntityBase] = {}
        self.__exec_modes: Dict[str, ExecMode] = {}

        self.__name = name
        self.__version = version
        self.__result_data = result_data
        self.__scen_types: Tuple[str] = self.__validate_scen_types(scen_types)
        self.__data_connector_cls: Type[DataConnector] = ParquetConnector
        check_instance_attribute_types(self)

    def __validate_scen_types(self, scen_types: Optional[List[str]]) -> Tuple[str]:
        default_scen_type = 'SCENARIO'

        if scen_types is None:
            return default_scen_type,

        scen_types = validate_list(self, 'scen_types', str, 'string', scen_types)
        scen_types_set = set(scen_types)

        if len(scen_types_set) < len(scen_types):
            raise ValueError("All scenario type identifiers must be unique.")

        for scen_type in scen_types:
            validate_raw_ident(scen_type, 'scenario type identifier')

        reserved = {'FOLDER', 'VIRTUAL'}.intersection(scen_types_set)
        if len(reserved) > 0:
            raise ValueError(
                f'"{reserved.pop()}" is not a valid scenario type identifier, because it is a reserved keyword.')

        if default_scen_type in scen_types_set:
            return scen_types
        else:
            return (default_scen_type,) + scen_types

    @property
    def name(self) -> str:
        """
        Get the default name of the app.

        Returns
        -------
        name : str
            The default name of the app.

        Notes
        -----
        This property returns the default app name. Use the Insight app interface to get the current app name:
        :fct-ref:`insight.app_name`.

        See Also
        --------
        AppConfig
        AppInterface.app_name
        """
        return self.__name

    @property
    def version(self) -> AppVersion:
        """
        Get the version number of the app.

        Returns
        -------
        version : AppVersion
            The version number of the app.

        See Also
        --------
        AppConfig
        AppVersion
        """
        return self.__version

    @property
    def result_data(self) -> ResultData:
        """
        Get the result data configuration of the app.

        Returns
        -------
        result_data : ResultData
            The result data configuration of the app.

        See Also
        --------
        AppConfig
        ResultData
        """
        return self.__result_data

    @property
    def scen_types(self) -> Tuple[str]:
        """
        Get the scenario types of the app.

        Returns
        -------
        scen_types : Tuple[str]
            The scenario types of the app.

        See Also
        --------
        AppConfig
        """
        return self.__scen_types

    @property
    def _data_connector_cls(self) -> Type[DataConnector]:
        """ Property for the type of the data connector. For FICO internal use only. """
        return self.__data_connector_cls

    def __init_entity_names(self):
        """ Assign a name to all entities (except for Columns).
            The name assignment also checks whether the names are valid the identifiers. """
        for entity_name, entity in self.__entities.items():
            entity.name = entity_name

    #
    def __init_entity_indices(self):
        for entity in self.__entities.values():
            if isinstance(entity, (Series, DataFrame)):
                #
                entity._init(self.__entities)

    @staticmethod
    def __get_exec_modes(app_cls):
        exec_modes = {}

        for attrName, attr in inspect.getmembers(app_cls):
            if hasattr(attr, 'exec_mode') and isinstance(attr.exec_mode, ExecMode):
                if isinstance(attr, types.FunctionType):
                    if exec_modes.get(attr.exec_mode.name) is not None:
                        raise KeyError('The {} execution mode cannot be defined twice.'.format(attr.exec_mode.name))

                    exec_modes[attr.exec_mode.name] = attr.exec_mode
                else:
                    raise TypeError('The ExecMode() decorator can only be used to decorate a method. ' +
                                    'The attribute "{}" is not a method.'.format(attrName))

        for mode_name, mode_cls in {ExecMode.LOAD: ExecModeLoad, ExecMode.RUN: ExecModeRun}.items():
            if mode_name not in exec_modes:
                print('WARNING: Class {} does not define a {} execution mode. It is necessary to decorate a method '
                      'with the @{}() decorator. If a method is already decorated with this decorator, then check '
                      'whether the function has a unique name.'
                      .format(app_cls.__name__, mode_name, mode_cls.__name__), file=sys.stderr)

        return exec_modes

    @staticmethod
    def __get_old_syntax_entity_annotation_strings(annotations: Dict[str, Any]) -> Dict[str, str]:
        """
        Return the dictionary of entities from the supplied annotation dictionary that use the 'old syntax'
        annotations such as "xi.Scalar" instead of "xi.types.Scalar", provided the annotation dictionary is string-based
        (ie Python 3.11+ or forward annotations is activated)
        """
        old_syntax_entities = {}

        for (name, ann) in annotations.items():
            #
            #
            #
            #
            if isinstance(ann, str) and (ann.startswith("xi.") or ann.startswith("xpressinsight.")):
                #
                ann_without_package = ann.split('.', 1)[1]

                if any(ann_without_package.startswith(ent_cls_name) for ent_cls_name in ENTITY_CLASS_NAMES):
                    old_syntax_entities[name] = ann

        return old_syntax_entities

    @staticmethod
    def __get_old_syntax_entity_annotations(annotations: Dict[str, Any]) -> Dict[str, EntityBase]:
        """
        Return the list of entity names from the supplied annotation dictionary that use the 'old syntax' annotations
        such as "xi.Scalar" instead of "xi.types.Scalar", provided the annotation dictionary is nor-based (ie
        Python <=3.10 with forward annotations not activated)
        """
        return {name: entity for (name, entity) in annotations.items() if isinstance(entity, EntityBase)}

    @staticmethod
    def __get_entities_from_type_hints(app_type_hints: Dict[str, type]) -> Dict[str, EntityBase]:
        """
        Given the type hints for a class, extract the entities from annotations
        """
        entities = {}
        for (name, type_hint) in app_type_hints.items():
            #
            if get_origin(type_hint) is Annotated:
                #
                entities_from_annotated = [arg for arg in get_args(type_hint) if isinstance(arg, EntityBase)]
                if len(entities_from_annotated) > 1:
                    raise TypeError(
                        'Entity {} has multiple Insight entity annotations; an entity must have only a\n'
                        'single annotation argument with type subclassing EntityBase'.format(name)
                    )
                elif len(entities_from_annotated) == 1:
                    entity = entities_from_annotated[0]
                    entities[name] = entity

                    #
                    #
                    actual_type_hint = get_args(type_hint)[0]

                    if (not issubclass(actual_type_hint, entity.type_hint)) or\
                            (issubclass(actual_type_hint, bool) and entity.type_hint == int):
                        raise TypeError("Entity {} has type hint {} but should be {}.".format(
                            name, actual_type_hint, entity.type_hint))
        return entities

    @staticmethod
    def __get_entities(app_cls) -> Dict[str, EntityBase]:
        """
        Get the entities for the given class
        """
        #
        annotations = getattr(app_cls, '__annotations__', {})

        #
        try:
            app_type_hints = get_type_hints(app_cls, include_extras=True)

        except TypeError as e:
            #
            #
            #
            old_syntax_entities = AppConfig.__get_old_syntax_entity_annotation_strings(annotations)
            if old_syntax_entities:
                raise TypeError(
                    "The Insight app is using an old syntax for specifying entities, which is not supported\n"
                    "in Python versions which store type hints as strings (Python 3.11+ or earlier versions with\n"
                    "`from __future__ import annotations`). Please update the annotations of entities {} as\n"
                    "follows:\n"
                    "    xi.Param becomes xi.types.Param\n"
                    "    xi.Scalar becomes xi.types.Scalar\n"
                    "    xi.Index becomes xi.types.Index\n"
                    "    xi.Series becomes xi.types.Series\n"
                    "    xi.DataFrame becomes xi.types.DataFrame".format(', '.join(old_syntax_entities.keys()))
                )
            else:
                #
                raise e

        else:
            entities = AppConfig.__get_entities_from_type_hints(app_type_hints)

            #
            #
            #
            if entities and AppConfig.__get_old_syntax_entity_annotations(annotations):
                raise TypeError(
                    'The Insight app is declaring entities using inconsistent syntax; when some entities are\n'
                    'annotated with either "xi.types.EntityType" or "Annotated[type, xi.EntityType]", the\n'
                    'entities {} cannot be annotated as "xi.EntityType" (where EntityType is one of: Param,\n'
                    'Scalar, Index, Series, DataFrame)'.format(
                        ', '.join(AppConfig.__get_old_syntax_entity_annotations(annotations).keys())
                    ))

            #
            #
            #
            if not entities:
                entities = AppConfig.__get_old_syntax_entity_annotations(annotations)

        return entities

    @property
    def entities(self) -> ValuesView[EntityBase]:
        """
        Get the list of all Insight entities of the app.

        Returns
        -------
        entities : ValuesView[EntityBase]
            The Insight app entities.

        See Also
        --------
        AppConfig.get_entity
        AppConfig
        EntityBase
        """
        return self.__entities.values()

    def get_entity(self, name: str) -> Optional[EntityBase]:
        """
        Get an Insight entity by name.

        Parameters
        ----------
        name : str
            The name of the entity.

        Returns
        -------
        entity : Optional[EntityBase]
            The Insight entity or `None` if not found.

        See Also
        --------
        AppConfig.entities
        AppConfig
        EntityBase
        """
        return self.__entities.get(name)

    @property
    def exec_modes(self) -> ValuesView[ExecMode]:
        """
        Get the list of all execution modes of the app.

        Returns
        -------
        exec_modes : ValuesView[ExecMode]
            The execution modes of the app.

        See Also
        --------
        AppConfig.get_exec_mode
        AppConfig
        ExecMode
        """
        return self.__exec_modes.values()

    def get_exec_mode(self, name: str) -> Optional[ExecMode]:
        """
        Get an execution mode object by name.

        Parameters
        ----------
        name : str
            The name of the execution mode.

        Returns
        -------
        exec_mode : Optional[ExecMode]
            The execution mode object or `None` if not found.

        See Also
        --------
        AppConfig.exec_modes
        AppConfig
        ExecMode
        """
        return self.__exec_modes.get(name)

    def __call__(self, app_cls=None):
        if not issubclass(app_cls, AppBase):
            raise TypeError('The Insight app {} must be a subclass of xpressinsight.AppBase.'
                            .format(app_cls.__name__))

        self.__entities = self.__get_entities(app_cls)
        self.__exec_modes = self.__get_exec_modes(app_cls)
        self.__init_entity_names()
        self.__init_entity_indices()
        #
        app_cls._app_cfg = self
        return app_cls


class AppBase(ABC):
    """
    The `AppBase` class. An Insight application must be a subclass of `AppBase`.

    Examples
    --------

    >>> import xpressinsight as xi
    ...
    ... @xi.AppConfig("My App")
    ... class MyApp(xi.AppBase):
    ...     pass
    """

    #
    _app_cfg: AppConfig = None

    #
    __data_connector: DataConnector
    __insight: AppInterface

    @classmethod
    def get_app_cfg(cls) -> AppConfig:
        """
        Gets the application configuration object of the Insight app.
        This class method is equivalent to the instance property `AppBase.app_cfg`.

        Returns
        -------
        app_cfg : AppConfig
            The application configuration object.

        See Also
        --------
        AppConfig.app_cfg
        """
        if not cls._app_cfg:
            raise AttributeError(
                "Cannot access the application configuration!\n"
                "    Please make sure that the Insight application class is decorated with the AppConfig decorator.\n"
                "    Please access the application configuration through self.app_cfg, where self is an instance\n"
                "    of the Insight application.")

        return cls._app_cfg

    def __new__(cls, *args, **kwargs):
        if cls is AppBase:
            raise TypeError(f"Only children of {cls.__name__} may be instantiated.\n"
                            f"   Correct:  class InsightApp(xi.AppBase): ...\n"
                            f"   Wrong:    class InsightApp(xi.AppBase()): ...")

        #
        return object.__new__(cls, *args, **kwargs)

    def __init__(self):
        """ Initialization function of the base class of an Insight application. """

        test_mode = getattr(self.app_cfg, "_test_mode", True)
        work_dir = getattr(self.app_cfg, "_work_dir", os.path.join("work_dir", "insight"))

        if test_mode:
            self.__insight = AppTestInterface(work_dir=work_dir, test_mode=test_mode, app=self)
        else:
            #
            rest_port = 8083
            rest_token = "TOKEN_ABC"
            self.__insight = AppRestInterface(rest_port, rest_token, work_dir=work_dir, test_mode=test_mode,
                                              app=self)

        #
        self.__data_connector = self.app_cfg._data_connector_cls(self)

    @property
    def app_cfg(self) -> AppConfig:
        """
        Property for the application configuration object of the Insight app.

        Returns
        -------
        app_cfg : AppConfig
            The application configuration object.

        Examples
        --------
        Demonstration of using the application configuration for getting the application version number:

        >>> import xpressinsight as xi
        ...
        ... @xi.AppConfig("My App", version=xi.AppVersion(1, 0, 0))
        ... class InsightApp(xi.AppBase):
        ...     @xi.ExecModeLoad()
        ...     def load(self):
        ...         print(f"Version number: {self.app_cfg.version}")

        See Also
        --------
        AppConfig
        AppConfig.__init__
        """
        return self.__class__.get_app_cfg()

    @property
    def data_connector(self) -> DataConnector:
        return self.__data_connector

    @property
    def insight(self) -> AppInterface:
        """
        Property for the application interface of the Insight app.

        Returns
        -------
        insight : AppInterface
            The application interface.

        Examples
        --------
        Demonstration of using the application interface for getting the current scenario name:

        >>> import xpressinsight as xi
        ...
        ... @xi.AppConfig("My App")
        ... class InsightApp(xi.AppBase):
        ...     @xi.ExecModeLoad()
        ...     def load(self):
        ...         print(f"Scenario name: {self.insight.scenario_name}")

        See Also
        --------
        AppInterface
        """
        return self.__insight

    def call_exec_mode(self, name: str) -> int:
        exec_mode = self.app_cfg.get_exec_mode(name)

        if exec_mode is None:
            print(f'ERROR: The {self.__class__.__name__} class does not have the {name} execution mode.',
                  file=sys.stderr)
            return 1

        return exec_mode.call(self)

    def call_exec_modes(self, exec_modes: List[str]) -> int:
        for exec_mode in exec_modes:
            result = self.call_exec_mode(exec_mode)

            if result != 0:
                print('ERROR: The {} execution mode failed. Exit code: {}.'.format(exec_mode, result),
                      file=sys.stderr)
                return result

        return 0

    def load_and_run(self, delete_work_dir: bool = True) -> int:
        if delete_work_dir:
            self.insight.delete_work_dir()

        return self.call_exec_modes([ExecMode.LOAD, ExecMode.RUN])
