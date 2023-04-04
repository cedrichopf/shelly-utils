import requests

class Shelly():
  def __init__(self, name, address) -> None:
    self.protocol = "http"
    self.name = name
    self.address = address
    pass

  def get_device_info(self) -> None:
    url = f'{self.protocol}://{self.address}/rpc/Shelly.GetDeviceInfo'
    response = requests.get(url)
    data = response.json()
    self.version = data["ver"]

  def update_available(self) -> str:
    url = f'{self.protocol}://{self.address}/rpc/Shelly.CheckForUpdate'
    response = requests.get(url)
    response_data = response.json()
    if not 'stable' in response_data:
      return ""
    return response_data["stable"]["version"]

  def update_device(self) -> None:
    url = f'{self.protocol}://{self.address}/rpc'
    response = requests.post(url, json={"id":1,"method":"Shelly.Update", "params":{"stage":"stable"}})

  def reboot(self) -> None:
    url = f'{self.protocol}://{self.address}/rpc/Shelly.Reboot'
    response = requests.get(url)
