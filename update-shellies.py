from shelly.discovery.mdns import MDNSDiscovery
from shelly.shelly import Shelly

WAIT_TIME = 20

def main():
  discovery = MDNSDiscovery()
  print(f'Fetching Shelly devices for {WAIT_TIME} seconds')
  shellies: [] = discovery.run(WAIT_TIME)
  print(f'Found {len(shellies)} Shelly devices')
  update_counter = 0
  shelly: Shelly
  for shelly in shellies:
    print(f'Checking update for Shelly {shelly.name}')
    update_version = shelly.update_available()
    if len(update_version) == 0:
      print(f'No update available for Shelly {shelly.name}')
    else:
      print(f'Updating Shelly {shelly.name} to version {update_version}')
      shelly.update_device()
      update_counter = update_counter + 1
      print(f'Successfully triggered update for Shelly {shelly.name}')
  print(f'Triggered update for {update_counter} Shelly devices')
  pass

main()
