from shelly.discovery.mdns import MDNSDiscovery
from shelly.shelly import Shelly

WAIT_TIME = 20

def main():
  discovery = MDNSDiscovery()
  print(f'Fetching Shelly devices for {WAIT_TIME} seconds')
  shellies: [] = discovery.run(WAIT_TIME)
  print(f'Found {len(shellies)} Shelly devices')
  shelly: Shelly
  for shelly in shellies:
    print(f'Rebooting Shelly {shelly.name}')
    shelly.reboot()
  print(f'Triggered reboot for {len(shellies)} Shelly devices')
  pass

main()
