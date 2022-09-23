import re
import socket
from zeroconf import ServiceBrowser, ServiceListener, Zeroconf
from shelly.shelly import Shelly

class Listener():
  def __init__(self, services: []):
    self.services = services
    pass

  def update_service(self, zc: Zeroconf, type_: str, name: str) -> None:
    pass

  def remove_service(self, zc: Zeroconf, type_: str, name: str) -> None:
    pass

  def add_service(self, zc: Zeroconf, type_: str, name: str) -> None:
      match = re.search("[sS]helly", name)
      if match:
        splitted_name = name.split(".")
        shelly_name = splitted_name[0]
        service_info = zc.get_service_info(type_, name)
        service_address = service_info.server
        shelly = Shelly(shelly_name, service_address)
        shelly.get_device_info()
        self.services.append(shelly)
