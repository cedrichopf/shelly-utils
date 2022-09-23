# Shelly Utils

- [Shelly Utils](#shelly-utils)
  - [Requirements](#requirements)
  - [Discovery](#discovery)
  - [Scripts](#scripts)
    - [Update Shellies](#update-shellies)
  - [Known Issues](#known-issues)
  - [Resources](#resources)

---

This repository contains scripts to interact with Shelly devices.

## Requirements

The scripts are written in Python and need Python 3 to run. Additionally, all external dependencies can be found
in the `Pipfile` / `requirements.txt`.

Make sure to install them using the package manager of your choice, e.g.

```sh
$ pipenv install
```

## Discovery

Per default, all scripts are using mDNS to discover Shelly devices in the network. Please make sure mDNS discovery is
configured and available in your network.

Other discovery tools may follow in the future.

## Scripts

### Update Shellies

This script will check if there is an update available for any Shelly device and trigger the update process:

```sh
$ python3 update-shellies.py
```

## Known Issues

- Shellies with enabled Authentication are currently not supported

## Resources

- [Shelly API Docs](https://shelly-api-docs.shelly.cloud/)
- [mDNS](https://en.wikipedia.org/wiki/Multicast_DNS)
