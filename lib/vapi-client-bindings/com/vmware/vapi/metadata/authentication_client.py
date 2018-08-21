# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vapi.metadata.authentication.
#---------------------------------------------------------------------------

"""
The ``com.vmware.vapi.metadata.authentication_client`` module provides classes
that expose authentication information for operation elements across all the
service elements. 

To calculate the effective authentication information for an operation element,
you should first see if there is an authentication scheme specified for the
operation element. If it is not specified, then authentication scheme for the
service element that contains this operation element is used. If it is not
specified for the service element as well, then the authentication scheme for
the package element that contains this service element is used.

"""

__author__ = 'VMware, Inc.'
__docformat__ = 'restructuredtext en'

import sys

from vmware.vapi.bindings import type
from vmware.vapi.bindings.converter import TypeConverter
from vmware.vapi.bindings.enum import Enum
from vmware.vapi.bindings.error import VapiError
from vmware.vapi.bindings.struct import VapiStruct
from vmware.vapi.bindings.stub import (
    ApiInterfaceStub, StubFactoryBase, VapiInterface)
from vmware.vapi.bindings.common import raise_core_exception
from vmware.vapi.data.validator import (UnionValidator, HasFieldsOfValidator)
from vmware.vapi.exception import CoreException
from vmware.vapi.lib.constants import TaskType
from vmware.vapi.lib.rest import OperationRestMetadata


class AuthenticationInfo(VapiStruct):
    """
    The ``AuthenticationInfo`` class describes the authentication information.
    Authentication information could be specified for a package element,
    service elenent or an operation element. 
    
    Using the authentication scheme information, a client invoking an API call
    from any class can figure out what kind of credentials are needed for that
    API call.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """

    _validator_list = [
        UnionValidator(
            'scheme_type',
            {
                'SESSION_AWARE' : [('session_manager', True)],
                'SESSIONLESS' : [],
            }
        ),
    ]



    def __init__(self,
                 scheme_type=None,
                 session_manager=None,
                 scheme=None,
                ):
        """
        :type  scheme_type: :class:`AuthenticationInfo.SchemeType`
        :param scheme_type: The type of the authentication scheme.
        :type  session_manager: :class:`str`
        :param session_manager: In a session aware authentication scheme, a session manager is
            required that supports ``create``, ``delete`` and ``keepAlive``
            methods. The fully qualified class name of the session manager is
            provided in :attr:`AuthenticationInfo.session_manager` attribute.
            This class is responsible for handling sessions.
            This attribute is optional and it is only relevant when the value
            of ``schemeType`` is
            :attr:`AuthenticationInfo.SchemeType.SESSION_AWARE`.
        :type  scheme: :class:`str`
        :param scheme: String identifier of the authentication scheme. 
            
            Following are the supported authentication schemes by the
            infrastructure: 
            
            * The identifier ``com.vmware.vapi.std.security.saml_hok_token``
              for SAML holder of key token based authentication mechanism.
            * The identifier ``com.vmware.vapi.std.security.bearer_token`` for
              SAML bearer token based authentication mechanism.
            * The identifier ``com.vmware.vapi.std.security.session_id`` for
              session based authentication mechanism.
            * The identifier ``com.vmware.vapi.std.security.user_pass`` for
              username and password based authentication mechanism.
        """
        self.scheme_type = scheme_type
        self.session_manager = session_manager
        self.scheme = scheme
        VapiStruct.__init__(self)

    class SchemeType(Enum):
        """
        The ``AuthenticationInfo.SchemeType`` class provides class attributes for
        the set of valid authentication scheme types.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        SESSIONLESS = None
        """
        Indicates that the scheme is a session less authentication scheme, the user
        is authenticated on every method. There is no explicit session
        establishment.

        """
        SESSION_AWARE = None
        """
        Indicates that the scheme is a session aware authentication scheme. It
        requires an explicit login before executing a method and logout when a
        session terminates. A class might choose to have a session aware scheme if
        it wants to associate some state corresponding to the user until the user
        logs out or if it wants to mitigate the cost of authenticating the user on
        every method.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`SchemeType` instance.
            """
            Enum.__init__(string)

    SchemeType._set_values([
        SchemeType('SESSIONLESS'),
        SchemeType('SESSION_AWARE'),
    ])
    SchemeType._set_binding_type(type.EnumType(
        'com.vmware.vapi.metadata.authentication.authentication_info.scheme_type',
        SchemeType))

AuthenticationInfo._set_binding_type(type.StructType(
    'com.vmware.vapi.metadata.authentication.authentication_info', {
        'scheme_type': type.ReferenceType(__name__, 'AuthenticationInfo.SchemeType'),
        'session_manager': type.OptionalType(type.StringType()),
        'scheme': type.StringType(),
    },
    AuthenticationInfo,
    False,
    None))



class ComponentData(VapiStruct):
    """
    The ``ComponentData`` class contains the authentication information of the
    component along with its fingerprint.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 info=None,
                 fingerprint=None,
                ):
        """
        :type  info: :class:`ComponentInfo`
        :param info: Authentication information of the component. This includes
            information about all the modules in the component.
        :type  fingerprint: :class:`str`
        :param fingerprint: Fingerprint of the metadata of the component. 
            
            Authentication information could change when there is an
            infrastructure update. Since the data present in
            :attr:`ComponentData.info` could be quite large, ``fingerprint``
            provides a convenient way to check if the data for a particular
            component is updated. 
            
            You should store the fingerprint associated with a component. After
            an update, by invoking the :func:`Component.fingerprint` method,
            you can retrieve the new fingerprint for the component. If the new
            fingerprint and the previously stored fingerprint do not match,
            clients can then use the :func:`Component.get` to retrieve the new
            authentication information for the component.
        """
        self.info = info
        self.fingerprint = fingerprint
        VapiStruct.__init__(self)

ComponentData._set_binding_type(type.StructType(
    'com.vmware.vapi.metadata.authentication.component_data', {
        'info': type.ReferenceType(__name__, 'ComponentInfo'),
        'fingerprint': type.StringType(),
    },
    ComponentData,
    False,
    None))



class ComponentInfo(VapiStruct):
    """
    The ``ComponentInfo`` class contains authentication information of a
    component element. 
    
    For an explanation of authentication information contained within component
    elements, see :class:`Component`.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 packages=None,
                ):
        """
        :type  packages: :class:`dict` of :class:`str` and :class:`PackageInfo`
        :param packages: Authentication information of all the package elements. The key in
            the :class:`dict` is the identifier of the package element and the
            value in the :class:`dict` is the authentication information for
            the package element. 
            
            For an explanation of authentication information containment within
            package elements, see :class:`Package`.
            When clients pass a value of this class as a parameter, the key in
            the attribute :class:`dict` must be an identifier for the resource
            type: ``com.vmware.vapi.package``. When methods return a value of
            this class as a return value, the key in the attribute
            :class:`dict` will be an identifier for the resource type:
            ``com.vmware.vapi.package``.
        """
        self.packages = packages
        VapiStruct.__init__(self)

ComponentInfo._set_binding_type(type.StructType(
    'com.vmware.vapi.metadata.authentication.component_info', {
        'packages': type.MapType(type.IdType(), type.ReferenceType(__name__, 'PackageInfo')),
    },
    ComponentInfo,
    False,
    None))



class OperationInfo(VapiStruct):
    """
    The ``OperationInfo`` class contains authentication information of an
    operation element.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 schemes=None,
                ):
        """
        :type  schemes: :class:`list` of :class:`AuthenticationInfo`
        :param schemes: List of authentication schemes used by an operation element. The
            authentication scheme specified on the service element
            corresponding to this operation element is ignored.
        """
        self.schemes = schemes
        VapiStruct.__init__(self)

OperationInfo._set_binding_type(type.StructType(
    'com.vmware.vapi.metadata.authentication.operation_info', {
        'schemes': type.ListType(type.ReferenceType(__name__, 'AuthenticationInfo')),
    },
    OperationInfo,
    False,
    None))



class PackageInfo(VapiStruct):
    """
    The ``PackageInfo`` class contains authentication information of a package
    element. 
    
    For an explanation of authentication information contained within package
    elements, see :class:`Package`.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 schemes=None,
                 services=None,
                ):
        """
        :type  schemes: :class:`list` of :class:`AuthenticationInfo`
        :param schemes: List of authentication schemes to be used for all the operation
            elements contained in this package element. If a particular service
            or operation element has no explicit authentications defined in the
            authentication defintion file, these authentication schemes are
            used for authenticating the user.
        :type  services: :class:`dict` of :class:`str` and :class:`ServiceInfo`
        :param services: Information about all service elements contained in this package
            element that contain authentication information. The key in the
            :class:`dict` is the identifier of the service element and the
            value in the :class:`dict` is the authentication information for
            the service element. 
            
            For an explanation of authentication information containment within
            service elements, see :class:`Service`.
            When clients pass a value of this class as a parameter, the key in
            the attribute :class:`dict` must be an identifier for the resource
            type: ``com.vmware.vapi.service``. When methods return a value of
            this class as a return value, the key in the attribute
            :class:`dict` will be an identifier for the resource type:
            ``com.vmware.vapi.service``.
        """
        self.schemes = schemes
        self.services = services
        VapiStruct.__init__(self)

PackageInfo._set_binding_type(type.StructType(
    'com.vmware.vapi.metadata.authentication.package_info', {
        'schemes': type.ListType(type.ReferenceType(__name__, 'AuthenticationInfo')),
        'services': type.MapType(type.IdType(), type.ReferenceType(__name__, 'ServiceInfo')),
    },
    PackageInfo,
    False,
    None))



class ServiceInfo(VapiStruct):
    """
    The ``ServiceInfo`` class contains authentication information of a service
    element. 
    
    For an explanation of authentication information contained within service
    elements, see :class:`Service`.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 schemes=None,
                 operations=None,
                ):
        """
        :type  schemes: :class:`list` of :class:`AuthenticationInfo`
        :param schemes: List of authentication schemes to be used for all the operation
            elements contained in this service element. The authentication
            scheme specified on the package element corresponding to this
            service element is ignored.
        :type  operations: :class:`dict` of :class:`str` and :class:`OperationInfo`
        :param operations: Information about all operation elements contained in this service
            element that contain authentication information. The key in the
            :class:`dict` is the identifier of the operation element and the
            value in the :class:`dict` is the authentication information for
            the operation element. 
            
            For an explanation of containment of authentication information
            within operation elements, see
            :class:`com.vmware.vapi.metadata.authentication.service_client.Operation`.
            When clients pass a value of this class as a parameter, the key in
            the attribute :class:`dict` must be an identifier for the resource
            type: ``com.vmware.vapi.operation``. When methods return a value of
            this class as a return value, the key in the attribute
            :class:`dict` will be an identifier for the resource type:
            ``com.vmware.vapi.operation``.
        """
        self.schemes = schemes
        self.operations = operations
        VapiStruct.__init__(self)

ServiceInfo._set_binding_type(type.StructType(
    'com.vmware.vapi.metadata.authentication.service_info', {
        'schemes': type.ListType(type.ReferenceType(__name__, 'AuthenticationInfo')),
        'operations': type.MapType(type.IdType(), type.ReferenceType(__name__, 'OperationInfo')),
    },
    ServiceInfo,
    False,
    None))



class Component(VapiInterface):
    """
    The ``Component`` class provides methods to retrieve authentication
    information of a component element. 
    
    A component element is said to contain authentication information if any
    one of package elements contained in it has authentication information.
    """
    RESOURCE_TYPE = "com.vmware.vapi.component"
    """
    Resource type for component.

    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ComponentStub)


    def list(self):
        """
        Returns the identifiers for the component elements that have
        authentication information.


        :rtype: :class:`list` of :class:`str`
        :return: The list of identifiers for the component elements that have
            authentication information.
            The return value will contain identifiers for the resource type:
            ``com.vmware.vapi.component``.
        """
        return self._invoke('list', None)

    def get(self,
            component_id,
            ):
        """
        Retrieves authentication information about the component element
        corresponding to ``component_id``. 
        
        The :class:`ComponentData` contains the authentication information
        about the component element and it's fingerprint. It contains
        information about all the package elements that belong to this
        component element.

        :type  component_id: :class:`str`
        :param component_id: Identifier of the component element.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vapi.component``.
        :rtype: :class:`ComponentData`
        :return: The :class:`ComponentData` instance that corresponds to
            ``component_id``
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the component element associated with ``component_id`` does not
            have any authentication information.
        """
        return self._invoke('get',
                            {
                            'component_id': component_id,
                            })

    def fingerprint(self,
                    component_id,
                    ):
        """
        Retrieves the fingerprint computed from the authentication metadata of
        the component element corresponding to ``component_id``. 
        
        The fingerprint provides clients an efficient way to check if the
        metadata for a particular component has been modified on the server.
        The client can do this by comparing the result of this operation with
        the fingerprint returned in the result of :func:`Component.get`.

        :type  component_id: :class:`str`
        :param component_id: Identifier of the component element.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vapi.component``.
        :rtype: :class:`str`
        :return: The fingerprint computed from the authentication metadata of the
            component.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the component element associated with ``component_id`` does not
            have any authentication information.
        """
        return self._invoke('fingerprint',
                            {
                            'component_id': component_id,
                            })
class Package(VapiInterface):
    """
    The ``Package`` class provides methods to retrieve authentication
    information of a package element. 
    
    A package element is said to contain authentication information if there is
    a default authentication assigned to all service elements contained in the
    package element or if one of the service element contained in this package
    element has authentication information.
    """
    RESOURCE_TYPE = "com.vmware.vapi.package"
    """
    Resource type for package.

    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _PackageStub)


    def list(self):
        """
        Returns the identifiers for the package elements that have
        authentication information.


        :rtype: :class:`list` of :class:`str`
        :return: The list of identifiers for the package elements that have
            authentication information.
            The return value will contain identifiers for the resource type:
            ``com.vmware.vapi.package``.
        """
        return self._invoke('list', None)

    def get(self,
            package_id,
            ):
        """
        Retrieves authentication information about the package element
        corresponding to ``package_id``.

        :type  package_id: :class:`str`
        :param package_id: Identifier of the package element.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vapi.package``.
        :rtype: :class:`PackageInfo`
        :return: The :class:`PackageInfo` instance that corresponds to
            ``package_id``
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the package element associated with ``package_id`` does not have
            any authentication information.
        """
        return self._invoke('get',
                            {
                            'package_id': package_id,
                            })
class Service(VapiInterface):
    """
    The ``Service`` class provides methods to retrieve authentication
    information of a service element. 
    
    A service element is said to contain authentication information if there is
    a default authentication assigned to all operation elements contained in a
    service element or if one of the operation elements contained in this
    service element has authentication information.
    """
    RESOURCE_TYPE = "com.vmware.vapi.service"
    """
    Resource type for service.

    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ServiceStub)


    def list(self):
        """
        Returns the identifiers for the service elements that have
        authentication information.


        :rtype: :class:`list` of :class:`str`
        :return: The list of identifiers for the service elements that have
            authentication information.
            The return value will contain identifiers for the resource type:
            ``com.vmware.vapi.service``.
        """
        return self._invoke('list', None)

    def get(self,
            service_id,
            ):
        """
        Retrieves authentication information about the service element
        corresponding to ``service_id``.

        :type  service_id: :class:`str`
        :param service_id: Identifier of the service element.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vapi.service``.
        :rtype: :class:`ServiceInfo`
        :return: The :class:`ServiceInfo` instance that corresponds to
            ``service_id``
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the service element associated with ``service_id`` does not have
            any authentication information.
        """
        return self._invoke('get',
                            {
                            'service_id': service_id,
                            })
class _ComponentStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {})
        list_error_dict = {}
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = None

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'component_id': type.IdType(resource_types='com.vmware.vapi.component'),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = None

        # properties for fingerprint operation
        fingerprint_input_type = type.StructType('operation-input', {
            'component_id': type.IdType(resource_types='com.vmware.vapi.component'),
        })
        fingerprint_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        fingerprint_input_value_validator_list = [
        ]
        fingerprint_output_validator_list = [
        ]
        fingerprint_rest_metadata = None

        operations = {
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.IdType()),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'ComponentData'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'fingerprint': {
                'input_type': fingerprint_input_type,
                'output_type': type.StringType(),
                'errors': fingerprint_error_dict,
                'input_value_validator_list': fingerprint_input_value_validator_list,
                'output_validator_list': fingerprint_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'list': list_rest_metadata,
            'get': get_rest_metadata,
            'fingerprint': fingerprint_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vapi.metadata.authentication.component',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _PackageStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {})
        list_error_dict = {}
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = None

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'package_id': type.IdType(resource_types='com.vmware.vapi.package'),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = None

        operations = {
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.IdType()),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'PackageInfo'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'list': list_rest_metadata,
            'get': get_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vapi.metadata.authentication.package',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _ServiceStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {})
        list_error_dict = {}
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = None

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'service_id': type.IdType(resource_types='com.vmware.vapi.service'),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = None

        operations = {
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.IdType()),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'ServiceInfo'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'list': list_rest_metadata,
            'get': get_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vapi.metadata.authentication.service',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Component': Component,
        'Package': Package,
        'Service': Service,
        'service': 'com.vmware.vapi.metadata.authentication.service_client.StubFactory',
    }

