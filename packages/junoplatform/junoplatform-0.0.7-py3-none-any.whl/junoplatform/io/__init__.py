__all__ = [
    'Storage',
    'InputConfig',
]

from pydantic import BaseModel as BaseModel, Field as Field, root_validator as root_validator
import datetime as datetime
from typing import Optional, Any, List

from junoplatform.io._driver import Pulsar as Pulsar, Opc as Opc, driver_cfg, Redis


class InputConfig(BaseModel):
    '''
    tags: OPC tags
    minutes: last n minutes of data
    items: last n records of data
    inteval: algo schedule interval in seconds
    '''
    tags: List[str]
    minutes: Optional[int] = Field(default=None, description='input data of last n minutes')
    items: Optional[int] = Field(default= None, description='input data of last n items')
    time_from: Optional[datetime.datetime] = Field(default= None, description='input data from time')
    time_to: Optional[datetime.datetime] =Field(default= None, description='input data to time')
    interval: int = Field(description='schedule interval in seconds')

    @root_validator
    def atleast_one(cls, values: 'dict[str, Any]') -> 'dict[str, Any]':
        if all([values.get('minutes'), values.get('items'), values.get('time_from')]):
            raise ValueError("field 'minutes' or 'items' or 'time_to', 'time_from' must be given")
        return values
    

class Storage():
    _cloud = None
    _opc = None
    _local = None

    @property
    def cloud(self):
        if not self._cloud:
            CloudStorage:Pulsar
            if 'pulsar' in driver_cfg:
                CloudStorage = Pulsar(**driver_cfg['pulsar'])
            else:
                CloudStorage = Pulsar(url='pulsar://192.168.101.157:6650')
            self._cloud = CloudStorage

        return self._cloud
    
    @property
    def opc(self):
        if not self._opc:     
            OpcWriter = Opc()
            self._opc = OpcWriter  
        
        return self._opc
    
    @property
    def local(self):
        if not self._local:
            _redis_cfg = {'host': '192.168.101.157', 'port': 6379, 'password': 'myredis', 'db': 0}
            if 'redis' in driver_cfg:
                _redis_cfg = driver_cfg['redis']
            self._local = Redis(**_redis_cfg)
        return self._local
