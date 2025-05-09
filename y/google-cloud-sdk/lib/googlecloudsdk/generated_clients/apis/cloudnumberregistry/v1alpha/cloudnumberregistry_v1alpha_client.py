"""Generated client library for cloudnumberregistry version v1alpha."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from googlecloudsdk.generated_clients.apis.cloudnumberregistry.v1alpha import cloudnumberregistry_v1alpha_messages as messages


class CloudnumberregistryV1alpha(base_api.BaseApiClient):
  """Generated client library for service cloudnumberregistry version v1alpha."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://cloudnumberregistry.googleapis.com/'
  MTLS_BASE_URL = 'https://cloudnumberregistry.mtls.googleapis.com/'

  _PACKAGE = 'cloudnumberregistry'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
  _VERSION = 'v1alpha'
  _CLIENT_ID = 'CLIENT_ID'
  _CLIENT_SECRET = 'CLIENT_SECRET'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'CloudnumberregistryV1alpha'
  _URL_VERSION = 'v1alpha'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new cloudnumberregistry handle."""
    url = url or self.BASE_URL
    super(CloudnumberregistryV1alpha, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.projects_locations_operations = self.ProjectsLocationsOperationsService(self)
    self.projects_locations_registryBooks_historicalEvents = self.ProjectsLocationsRegistryBooksHistoricalEventsService(self)
    self.projects_locations_registryBooks_nodeEvents = self.ProjectsLocationsRegistryBooksNodeEventsService(self)
    self.projects_locations_registryBooks_registryNodes = self.ProjectsLocationsRegistryBooksRegistryNodesService(self)
    self.projects_locations_registryBooks_resourceImports = self.ProjectsLocationsRegistryBooksResourceImportsService(self)
    self.projects_locations_registryBooks = self.ProjectsLocationsRegistryBooksService(self)
    self.projects_locations = self.ProjectsLocationsService(self)
    self.projects = self.ProjectsService(self)

  class ProjectsLocationsOperationsService(base_api.BaseApiService):
    """Service class for the projects_locations_operations resource."""

    _NAME = 'projects_locations_operations'

    def __init__(self, client):
      super(CloudnumberregistryV1alpha.ProjectsLocationsOperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Cancel(self, request, global_params=None):
      r"""Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. Clients can use Operations.GetOperation or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an Operation.error value with a google.rpc.Status.code of `1`, corresponding to `Code.CANCELLED`.

      Args:
        request: (CloudnumberregistryProjectsLocationsOperationsCancelRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Cancel')
      return self._RunMethod(
          config, request, global_params=global_params)

    Cancel.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}:cancel',
        http_method='POST',
        method_id='cloudnumberregistry.projects.locations.operations.cancel',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha/{+name}:cancel',
        request_field='cancelOperationRequest',
        request_type_name='CloudnumberregistryProjectsLocationsOperationsCancelRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a long-running operation. This method indicates that the client is no longer interested in the operation result. It does not cancel the operation. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`.

      Args:
        request: (CloudnumberregistryProjectsLocationsOperationsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}',
        http_method='DELETE',
        method_id='cloudnumberregistry.projects.locations.operations.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha/{+name}',
        request_field='',
        request_type_name='CloudnumberregistryProjectsLocationsOperationsDeleteRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

      Args:
        request: (CloudnumberregistryProjectsLocationsOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}',
        http_method='GET',
        method_id='cloudnumberregistry.projects.locations.operations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha/{+name}',
        request_field='',
        request_type_name='CloudnumberregistryProjectsLocationsOperationsGetRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`.

      Args:
        request: (CloudnumberregistryProjectsLocationsOperationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListOperationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/operations',
        http_method='GET',
        method_id='cloudnumberregistry.projects.locations.operations.list',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1alpha/{+name}/operations',
        request_field='',
        request_type_name='CloudnumberregistryProjectsLocationsOperationsListRequest',
        response_type_name='ListOperationsResponse',
        supports_download=False,
    )

  class ProjectsLocationsRegistryBooksHistoricalEventsService(base_api.BaseApiService):
    """Service class for the projects_locations_registryBooks_historicalEvents resource."""

    _NAME = 'projects_locations_registryBooks_historicalEvents'

    def __init__(self, client):
      super(CloudnumberregistryV1alpha.ProjectsLocationsRegistryBooksHistoricalEventsService, self).__init__(client)
      self._upload_configs = {
          }

    def Show(self, request, global_params=None):
      r"""Shows HistoricalEvents in a given registry book.

      Args:
        request: (CloudnumberregistryProjectsLocationsRegistryBooksHistoricalEventsShowRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ShowHistoricalEventsResponse) The response message.
      """
      config = self.GetMethodConfig('Show')
      return self._RunMethod(
          config, request, global_params=global_params)

    Show.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/registryBooks/{registryBooksId}/historicalEvents:show',
        http_method='GET',
        method_id='cloudnumberregistry.projects.locations.registryBooks.historicalEvents.show',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'orderBy', 'pageSize', 'pageToken'],
        relative_path='v1alpha/{+parent}/historicalEvents:show',
        request_field='',
        request_type_name='CloudnumberregistryProjectsLocationsRegistryBooksHistoricalEventsShowRequest',
        response_type_name='ShowHistoricalEventsResponse',
        supports_download=False,
    )

  class ProjectsLocationsRegistryBooksNodeEventsService(base_api.BaseApiService):
    """Service class for the projects_locations_registryBooks_nodeEvents resource."""

    _NAME = 'projects_locations_registryBooks_nodeEvents'

    def __init__(self, client):
      super(CloudnumberregistryV1alpha.ProjectsLocationsRegistryBooksNodeEventsService, self).__init__(client)
      self._upload_configs = {
          }

    def Show(self, request, global_params=None):
      r"""Shows NodeEvents related to an IP range in a given registry book.

      Args:
        request: (CloudnumberregistryProjectsLocationsRegistryBooksNodeEventsShowRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ShowNodeEventsResponse) The response message.
      """
      config = self.GetMethodConfig('Show')
      return self._RunMethod(
          config, request, global_params=global_params)

    Show.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/registryBooks/{registryBooksId}/nodeEvents:show',
        http_method='GET',
        method_id='cloudnumberregistry.projects.locations.registryBooks.nodeEvents.show',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'ipRange', 'orderBy', 'pageSize', 'pageToken'],
        relative_path='v1alpha/{+parent}/nodeEvents:show',
        request_field='',
        request_type_name='CloudnumberregistryProjectsLocationsRegistryBooksNodeEventsShowRequest',
        response_type_name='ShowNodeEventsResponse',
        supports_download=False,
    )

  class ProjectsLocationsRegistryBooksRegistryNodesService(base_api.BaseApiService):
    """Service class for the projects_locations_registryBooks_registryNodes resource."""

    _NAME = 'projects_locations_registryBooks_registryNodes'

    def __init__(self, client):
      super(CloudnumberregistryV1alpha.ProjectsLocationsRegistryBooksRegistryNodesService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a new RegistryNode in a given project and location.

      Args:
        request: (CloudnumberregistryProjectsLocationsRegistryBooksRegistryNodesCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/registryBooks/{registryBooksId}/registryNodes',
        http_method='POST',
        method_id='cloudnumberregistry.projects.locations.registryBooks.registryNodes.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['registryNodeId', 'requestId'],
        relative_path='v1alpha/{+parent}/registryNodes',
        request_field='registryNode',
        request_type_name='CloudnumberregistryProjectsLocationsRegistryBooksRegistryNodesCreateRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a single RegistryNode.

      Args:
        request: (CloudnumberregistryProjectsLocationsRegistryBooksRegistryNodesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/registryBooks/{registryBooksId}/registryNodes/{registryNodesId}',
        http_method='DELETE',
        method_id='cloudnumberregistry.projects.locations.registryBooks.registryNodes.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['requestId'],
        relative_path='v1alpha/{+name}',
        request_field='',
        request_type_name='CloudnumberregistryProjectsLocationsRegistryBooksRegistryNodesDeleteRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets details of a single RegistryNode.

      Args:
        request: (CloudnumberregistryProjectsLocationsRegistryBooksRegistryNodesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (RegistryNode) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/registryBooks/{registryBooksId}/registryNodes/{registryNodesId}',
        http_method='GET',
        method_id='cloudnumberregistry.projects.locations.registryBooks.registryNodes.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha/{+name}',
        request_field='',
        request_type_name='CloudnumberregistryProjectsLocationsRegistryBooksRegistryNodesGetRequest',
        response_type_name='RegistryNode',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists RegistryNodes in a given project and location.

      Args:
        request: (CloudnumberregistryProjectsLocationsRegistryBooksRegistryNodesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListRegistryNodesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/registryBooks/{registryBooksId}/registryNodes',
        http_method='GET',
        method_id='cloudnumberregistry.projects.locations.registryBooks.registryNodes.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'orderBy', 'pageSize', 'pageToken'],
        relative_path='v1alpha/{+parent}/registryNodes',
        request_field='',
        request_type_name='CloudnumberregistryProjectsLocationsRegistryBooksRegistryNodesListRequest',
        response_type_name='ListRegistryNodesResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates the parameters of a single RegistryNode.

      Args:
        request: (CloudnumberregistryProjectsLocationsRegistryBooksRegistryNodesPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/registryBooks/{registryBooksId}/registryNodes/{registryNodesId}',
        http_method='PATCH',
        method_id='cloudnumberregistry.projects.locations.registryBooks.registryNodes.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['requestId', 'updateMask'],
        relative_path='v1alpha/{+name}',
        request_field='registryNode',
        request_type_name='CloudnumberregistryProjectsLocationsRegistryBooksRegistryNodesPatchRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Search(self, request, global_params=None):
      r"""Search registry nodes in a given registry book.

      Args:
        request: (CloudnumberregistryProjectsLocationsRegistryBooksRegistryNodesSearchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (SearchRegistryNodesResponse) The response message.
      """
      config = self.GetMethodConfig('Search')
      return self._RunMethod(
          config, request, global_params=global_params)

    Search.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/registryBooks/{registryBooksId}/registryNodes:search',
        http_method='GET',
        method_id='cloudnumberregistry.projects.locations.registryBooks.registryNodes.search',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['attributeKeys', 'ipRange', 'keywords', 'orderBy', 'pageSize', 'pageToken', 'source'],
        relative_path='v1alpha/{+parent}/registryNodes:search',
        request_field='',
        request_type_name='CloudnumberregistryProjectsLocationsRegistryBooksRegistryNodesSearchRequest',
        response_type_name='SearchRegistryNodesResponse',
        supports_download=False,
    )

  class ProjectsLocationsRegistryBooksResourceImportsService(base_api.BaseApiService):
    """Service class for the projects_locations_registryBooks_resourceImports resource."""

    _NAME = 'projects_locations_registryBooks_resourceImports'

    def __init__(self, client):
      super(CloudnumberregistryV1alpha.ProjectsLocationsRegistryBooksResourceImportsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates an resource import to import data from a source.

      Args:
        request: (CloudnumberregistryProjectsLocationsRegistryBooksResourceImportsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/registryBooks/{registryBooksId}/resourceImports',
        http_method='POST',
        method_id='cloudnumberregistry.projects.locations.registryBooks.resourceImports.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['requestId', 'resourceImportId'],
        relative_path='v1alpha/{+parent}/resourceImports',
        request_field='resourceImport',
        request_type_name='CloudnumberregistryProjectsLocationsRegistryBooksResourceImportsCreateRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a single ResourceImport.

      Args:
        request: (CloudnumberregistryProjectsLocationsRegistryBooksResourceImportsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/registryBooks/{registryBooksId}/resourceImports/{resourceImportsId}',
        http_method='DELETE',
        method_id='cloudnumberregistry.projects.locations.registryBooks.resourceImports.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['requestId'],
        relative_path='v1alpha/{+name}',
        request_field='',
        request_type_name='CloudnumberregistryProjectsLocationsRegistryBooksResourceImportsDeleteRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets details of a single ResourceImport.

      Args:
        request: (CloudnumberregistryProjectsLocationsRegistryBooksResourceImportsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ResourceImport) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/registryBooks/{registryBooksId}/resourceImports/{resourceImportsId}',
        http_method='GET',
        method_id='cloudnumberregistry.projects.locations.registryBooks.resourceImports.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha/{+name}',
        request_field='',
        request_type_name='CloudnumberregistryProjectsLocationsRegistryBooksResourceImportsGetRequest',
        response_type_name='ResourceImport',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists ResourceImports in a given project and location.

      Args:
        request: (CloudnumberregistryProjectsLocationsRegistryBooksResourceImportsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListResourceImportsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/registryBooks/{registryBooksId}/resourceImports',
        http_method='GET',
        method_id='cloudnumberregistry.projects.locations.registryBooks.resourceImports.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'orderBy', 'pageSize', 'pageToken'],
        relative_path='v1alpha/{+parent}/resourceImports',
        request_field='',
        request_type_name='CloudnumberregistryProjectsLocationsRegistryBooksResourceImportsListRequest',
        response_type_name='ListResourceImportsResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates the parameters of a single ResourceImport.

      Args:
        request: (CloudnumberregistryProjectsLocationsRegistryBooksResourceImportsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/registryBooks/{registryBooksId}/resourceImports/{resourceImportsId}',
        http_method='PATCH',
        method_id='cloudnumberregistry.projects.locations.registryBooks.resourceImports.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['requestId', 'updateMask'],
        relative_path='v1alpha/{+name}',
        request_field='resourceImport',
        request_type_name='CloudnumberregistryProjectsLocationsRegistryBooksResourceImportsPatchRequest',
        response_type_name='Operation',
        supports_download=False,
    )

  class ProjectsLocationsRegistryBooksService(base_api.BaseApiService):
    """Service class for the projects_locations_registryBooks resource."""

    _NAME = 'projects_locations_registryBooks'

    def __init__(self, client):
      super(CloudnumberregistryV1alpha.ProjectsLocationsRegistryBooksService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a new RegistryBook in a given project and location.

      Args:
        request: (CloudnumberregistryProjectsLocationsRegistryBooksCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/registryBooks',
        http_method='POST',
        method_id='cloudnumberregistry.projects.locations.registryBooks.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['registryBookId', 'requestId'],
        relative_path='v1alpha/{+parent}/registryBooks',
        request_field='registryBook',
        request_type_name='CloudnumberregistryProjectsLocationsRegistryBooksCreateRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a single RegistryBook.

      Args:
        request: (CloudnumberregistryProjectsLocationsRegistryBooksDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/registryBooks/{registryBooksId}',
        http_method='DELETE',
        method_id='cloudnumberregistry.projects.locations.registryBooks.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['force', 'requestId'],
        relative_path='v1alpha/{+name}',
        request_field='',
        request_type_name='CloudnumberregistryProjectsLocationsRegistryBooksDeleteRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets details of a single RegistryBook.

      Args:
        request: (CloudnumberregistryProjectsLocationsRegistryBooksGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (RegistryBook) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/registryBooks/{registryBooksId}',
        http_method='GET',
        method_id='cloudnumberregistry.projects.locations.registryBooks.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha/{+name}',
        request_field='',
        request_type_name='CloudnumberregistryProjectsLocationsRegistryBooksGetRequest',
        response_type_name='RegistryBook',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists RegistryBooks in a given project and location.

      Args:
        request: (CloudnumberregistryProjectsLocationsRegistryBooksListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListRegistryBooksResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/registryBooks',
        http_method='GET',
        method_id='cloudnumberregistry.projects.locations.registryBooks.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'orderBy', 'pageSize', 'pageToken'],
        relative_path='v1alpha/{+parent}/registryBooks',
        request_field='',
        request_type_name='CloudnumberregistryProjectsLocationsRegistryBooksListRequest',
        response_type_name='ListRegistryBooksResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates the parameters of a single RegistryBook.

      Args:
        request: (CloudnumberregistryProjectsLocationsRegistryBooksPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/registryBooks/{registryBooksId}',
        http_method='PATCH',
        method_id='cloudnumberregistry.projects.locations.registryBooks.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['requestId', 'updateMask'],
        relative_path='v1alpha/{+name}',
        request_field='registryBook',
        request_type_name='CloudnumberregistryProjectsLocationsRegistryBooksPatchRequest',
        response_type_name='Operation',
        supports_download=False,
    )

  class ProjectsLocationsService(base_api.BaseApiService):
    """Service class for the projects_locations resource."""

    _NAME = 'projects_locations'

    def __init__(self, client):
      super(CloudnumberregistryV1alpha.ProjectsLocationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets information about a location.

      Args:
        request: (CloudnumberregistryProjectsLocationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Location) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}',
        http_method='GET',
        method_id='cloudnumberregistry.projects.locations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha/{+name}',
        request_field='',
        request_type_name='CloudnumberregistryProjectsLocationsGetRequest',
        response_type_name='Location',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists information about the supported locations for this service.

      Args:
        request: (CloudnumberregistryProjectsLocationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListLocationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations',
        http_method='GET',
        method_id='cloudnumberregistry.projects.locations.list',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['extraLocationTypes', 'filter', 'pageSize', 'pageToken'],
        relative_path='v1alpha/{+name}/locations',
        request_field='',
        request_type_name='CloudnumberregistryProjectsLocationsListRequest',
        response_type_name='ListLocationsResponse',
        supports_download=False,
    )

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = 'projects'

    def __init__(self, client):
      super(CloudnumberregistryV1alpha.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }
