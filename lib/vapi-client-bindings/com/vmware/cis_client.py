# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.cis.
#---------------------------------------------------------------------------

"""
The ``com.vmware.cis_client`` module provides VMware common infrastructure
classes.

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


class Session(VapiInterface):
    """
    The ``Session`` class allows API clients to manage session tokens including
    creating, deleting and obtaining information about sessions. 
    
     
    
    * The :func:`Session.create` method creates session token in exchange for
      another authentication token.
    * The :func:`Session.delete` method invalidates a session token.
    * The :func:`Session.get` retrieves information about a session token.
    
     
    
    The call to the :func:`Session.create` method is part of the overall
    authentication process for API clients. For example, the sequence of steps
    for establishing a session with SAML token is: 
    
    * Connect to lookup service.
    * Discover the secure token service (STS) endpoint URL.
    * Connect to the secure token service to obtain a SAML token.
    * Authenticate to the lookup service using the obtained SAML token.
    * Discover the API endpoint URL from lookup service.
    * Call the :func:`Session.create` method. The :func:`Session.create` call
      must include the SAML token.
    
     
    
    See the programming guide and samples for additional information about
    establishing API sessions. 
    
     **Execution Context and Security Context** 
    
    To use session based authentication a client should supply the session
    token obtained through the :func:`Session.create` method. The client should
    add the session token in the security context when using SDK classes.
    Clients using the REST API should supply the session token as a HTTP
    header. 
    
     **Session Lifetime** 
    
    A session begins with call to the :func:`Session.create` method to exchange
    a SAML token for a API session token. A session ends under the following
    circumstances: 
    
    * Call to the :func:`Session.delete` method.
    * The session expires. Session expiration may be caused by one of the
      following situations: 
    
    * Client inactivity - For a particular session identified by client
      requests that specify the associated session ID, the lapsed time since the
      last request exceeds the maximum interval between requests.
    * Unconditional or absolute session expiration time: At the beginning of
      the session, the session logic uses the SAML token and the system
      configuration to calculate absolute expiration time.
    
     
    
    When a session ends, the authentication logic will reject any subsequent
    client requests that specify that session. Any operations in progress will
    continue to completion. 
    
     **Error Handling** 
    
     The :class:`Session` returns the following exceptions: 
    
    * :class:`com.vmware.vapi.std.errors_client.Unauthenticated` exception for
      any exceptions related to the request.
    * :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` exception
      for all exceptions caused by internal service failure.
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _SessionStub)

    class Info(VapiStruct):
        """
        Represents data associated with an API session.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     user=None,
                     created_time=None,
                     last_accessed_time=None,
                    ):
            """
            :type  user: :class:`str`
            :param user: Fully qualified name of the end user that created the session, for
                example Administrator\\\\@vsphere.local. A typical use case for
                this information is in Graphical User Interfaces (GUI) or logging
                systems to visualize the identity of the current user.
            :type  created_time: :class:`datetime.datetime`
            :param created_time: Time when the session was created.
            :type  last_accessed_time: :class:`datetime.datetime`
            :param last_accessed_time: Last time this session was used by passing the session key for
                invoking an API.
            """
            self.user = user
            self.created_time = created_time
            self.last_accessed_time = last_accessed_time
            VapiStruct.__init__(self)

    Info._set_binding_type(type.StructType(
        'com.vmware.cis.session.info', {
            'user': type.StringType(),
            'created_time': type.DateTimeType(),
            'last_accessed_time': type.DateTimeType(),
        },
        Info,
        False,
        None))



    def create(self):
        """
        Creates a session with the API. This is the equivalent of login. This
        method exchanges user credentials supplied in the security context for
        a session identifier that is to be used for authenticating subsequent
        calls. To authenticate subsequent calls clients are expected to include
        the session key.


        :rtype: :class:`str`
        :return: Newly created session identifier to be used for authenticating
            further requests.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the session creation fails due to request specific issues. Due
            to the security nature of the API the details of the error are not
            disclosed. 
            
            Please check the following preconditions if using a SAML token to
            authenticate: 
            
            * the supplied token is delegate-able.
            * the time of client and server system are synchronized.
            * the token supplied is valid.
            * if bearer tokens are used check that system configuration allows
              the API endpoint to accept such tokens.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if session creation fails due to server specific issues, for
            example connection to a back end component is failing. Due to the
            security nature of this API further details will not be disclosed
            in the exception. Please refer to component health information,
            administrative logs and product specific documentation for possible
            causes.
        """
        return self._invoke('create', None)

    def delete(self):
        """
        Terminates the validity of a session token. This is the equivalent of
        log out. 
        
         A session identifier is expected as part of the request. 


        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the session id is missing from the request or the corresponding
            session object cannot be found.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if session deletion fails due to server specific issues, for
            example connection to a back end component is failing. Due to the
            security nature of this API further details will not be disclosed
            in the exception. Please refer to component health information,
            administrative logs and product specific documentation for possible
            causes.
        """
        return self._invoke('delete', None)

    def get(self):
        """
        Returns information about the current session. This method expects a
        valid session identifier to be supplied. 
        
        A side effect of invoking this method may be a change to the session's
        last accessed time to the current time if this is supported by the
        session implementation. Invoking any other method in the API will also
        update the session's last accessed time. 
        
        This API is meant to serve the needs of various front end projects that
        may want to display the name of the user. Examples of this include
        various web based user interfaces and logging facilities.


        :rtype: :class:`Session.Info`
        :return: Information about the session.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the session id is missing from the request or the corresponding
            session object cannot be found.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if session retrieval fails due to server specific issues e.g.
            connection to back end component is failing. Due to the security
            nature of this API further details will not be disclosed in the
            error. Please refer to component health information, administrative
            logs and product specific documentation for possible causes.
        """
        return self._invoke('get', None)
class _SessionStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {})
        create_error_dict = {
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),

        }
        create_input_value_validator_list = [
        ]
        create_output_validator_list = [
        ]
        create_rest_metadata = None

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {})
        delete_error_dict = {
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),

        }
        delete_input_value_validator_list = [
        ]
        delete_output_validator_list = [
        ]
        delete_rest_metadata = None

        # properties for get operation
        get_input_type = type.StructType('operation-input', {})
        get_error_dict = {
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = None

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.SecretType(),
                'errors': create_error_dict,
                'input_value_validator_list': create_input_value_validator_list,
                'output_validator_list': create_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'delete': {
                'input_type': delete_input_type,
                'output_type': type.VoidType(),
                'errors': delete_error_dict,
                'input_value_validator_list': delete_input_value_validator_list,
                'output_validator_list': delete_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'Session.Info'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'create': create_rest_metadata,
            'delete': delete_rest_metadata,
            'get': get_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.cis.session',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Session': Session,
        'task': 'com.vmware.cis.task_client.StubFactory',
    }

