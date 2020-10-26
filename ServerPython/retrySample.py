import requests
import logging
from retry.api import retry_call

logging_logger = logging.getLogger(__name__)

def request_api(service):
  r = requests.get(service)

  if(r.status_code != requests.codes.ok):
    r.raise_for_status()
  return r.text

  
result = retry_call(request_api, fargs=["http://127.0.0.1:5000/"], tries=-1, delay=3, logger=logging_logger)
print(result)