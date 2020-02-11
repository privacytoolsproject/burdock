# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class DataverseDetails(Model):
    """DataverseDetails.

    :param local_metadata_path:
    :type local_metadata_path: str
    :param token:
    :type token: str
    :param host:
    :type host: str
    """

    _attribute_map = {
        'local_metadata_path': {'key': 'local_metadata_path', 'type': 'str'},
        'token': {'key': 'token', 'type': 'str'},
        'host': {'key': 'host', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(DataverseDetails, self).__init__(**kwargs)
        self.local_metadata_path = kwargs.get('local_metadata_path', None)
        self.token = kwargs.get('token', None)
        self.host = kwargs.get('host', None)
