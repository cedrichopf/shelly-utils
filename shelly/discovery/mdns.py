import time
import requests
from zeroconf import ServiceBrowser, Zeroconf
from shelly.shelly import Shelly
from shelly.mdns.listener import Listener

class MDNSDiscovery():
  def __init__(self) -> None:
    self.services = []
    self.zeroconf = Zeroconf()
    self.listener = Listener(self.services)
    pass

  def run(self, wait_time: int) -> []:
    browser = ServiceBrowser(self.zeroconf, "_http._tcp.local.", self.listener)
    time.sleep(wait_time)
    self.zeroconf.close()
    return self.services
