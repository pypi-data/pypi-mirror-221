# messages needed to construct an analysis request
from .analysis_pb2 import AnalyzeRequest, AnalyzeResponse
from .analysis_pb2_grpc import AnalysisServiceStub
from ...common.v1.fileblob_pb2 import FileBlob  # noqa

import os
import grpc

from typing import Iterable

# the default kerfed API URL
api_url = os.getenv('KERFED_URL', 'api.kerfed-gke-dev.kerfed.dev:443')
api_key = os.getenv('KERFED_API_KEY', None)

# cache service stubs
_cache = {}


def Analyze(request: AnalyzeRequest) -> Iterable[AnalyzeResponse]:
    """
    A helper wrapper for creating a gRPC channel and stub for the
    `AnalysisService.Analyze` method using default values.

    Parameters
    -----------
    request
      Analysis request

    Yields
    ------------
    result
      As results are returned from the server.
    """
    global api_key, api_url

    # use a cached default stub and channel
    # they aren't expensive and don't expire
    key = f'{api_url}-{api_key}-Analysis'
    stub = _cache.get(key, None)
    if stub is None:
        # secure the connection with default server-side TLS
        stub = AnalysisServiceStub(grpc.secure_channel(
            api_url, grpc.ssl_channel_credentials()))
        _cache.clear()
        _cache[key] = stub

    # add the API key to the request headers
    auth = [('authorization',  f'bearer {api_key}')]
    # run the remote procedure call
    for result in stub.Analyze(request, metadata=auth):
        yield result
