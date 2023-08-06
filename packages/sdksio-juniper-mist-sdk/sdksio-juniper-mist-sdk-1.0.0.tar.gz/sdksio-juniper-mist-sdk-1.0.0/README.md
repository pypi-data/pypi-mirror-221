
# Getting Started with Mist API

## Introduction

> Version: **2306.2.8**
> 
> Date: **July 10, 2023**

---


### Available Documentation

* [Postman](https://documenter.getpostman.com/view/224925/SzYgQufe)
* [Open API](https://doc.mist-lab.fr/)

---


### Useful links

* [Mist Homepage](https://www.mist.com)
* [Mist Documentation](https://www.mist.com/documentation)
* [Official API Documentation](https://api.mist.com/api/v1/docs/Home) (Mist account required)
* [Mist Blog](https://www.mist.com/news/?md_post_type=post)
* [Mist Updates](https://www.mist.com/documentation/category/product-updates/)

## Install the Package

The package is compatible with Python versions `3 >=3.7, <= 3.11`.
Install the package from PyPi using the following pip command:

```python
pip install sdksio-juniper-mist-sdk==1.0.0
```

You can also view the package at:
https://pypi.python.org/pypi/sdksio-juniper-mist-sdk/1.0.0

## Test the SDK

You can test the generated SDK and the server with test cases. `unittest` is used as the testing framework and `pytest` is used as the test runner. You can run the tests as follows:

Navigate to the root directory of the SDK and run the following commands

```
pip install -r test-requirements.txt
pytest
```

## Initialize the API Client

**_Note:_** Documentation for the client can be found [here.](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/client.md)

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| `environment` | Environment | The API environment. <br> **Default: `Environment.PRODUCTION`** |
| `http_client_instance` | `HttpClient` | The Http Client passed from the sdk user for making requests |
| `override_http_client_configuration` | `bool` | The value which determines to override properties of the passed Http Client from the sdk user |
| `http_call_back` | `HttpCallBack` | The callback value that is invoked before and after an HTTP call is made to an endpoint |
| `timeout` | `float` | The value to use for connection timeout. <br> **Default: 60** |
| `max_retries` | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 0** |
| `backoff_factor` | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 2** |
| `retry_statuses` | `Array of int` | The http statuses on which retry is to be done. <br> **Default: [408, 413, 429, 500, 502, 503, 504, 521, 522, 524]** |
| `retry_methods` | `Array of string` | The http methods on which retry is to be done. <br> **Default: ['GET', 'PUT']** |
| `authorization` | `string` | Auth Header. Replace {x-auth-key} with your Auth Key.<br>*Default*: `'Token {x-auth-key}'` |

The API client can be initialized as follows:

```python
from mistapi.mistapi_client import MistapiClient
from mistapi.configuration import Environment

client = MistapiClient(
    authorization='Token {x-auth-key}'
)
```

## Environments

The SDK can be configured to use a different environment for making API calls. Available environments are:

### Fields

| Name | Description |
|  --- | --- |
| production | **Default** Mist Global 01 |
| environment2 | Mist Global 02 |
| environment3 | Mist Global 03 |
| environment4 | Mist Global 04 |
| environment5 | Mist Europe 01 |

## Authorization

This API uses `Custom Header Signature`.

## List of APIs

* [Login With O Auth 2](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/login-with-o-auth-2.md)
* [API Token](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/api-token.md)
* [Msps Admins](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/msps-admins.md)
* [Msps Inventory](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/msps-inventory.md)
* [Msps Invites](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/msps-invites.md)
* [Msps Logo](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/msps-logo.md)
* [Msps Logs](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/msps-logs.md)
* [Msps Licenses](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/msps-licenses.md)
* [Msps Marvis](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/msps-marvis.md)
* [Msps Org Groups](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/msps-org-groups.md)
* [Msps Orgs](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/msps-orgs.md)
* [Msps SL Es](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/msps-sl-es.md)
* [Msps SSO Roles](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/msps-sso-roles.md)
* [Msps SSO](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/msps-sso.md)
* [Msps Stats](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/msps-stats.md)
* [Msps Tickets](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/msps-tickets.md)
* [Orgs Admins](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/orgs-admins.md)
* [Sites Alarms](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/sites-alarms.md)
* [Sites Applications](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/sites-applications.md)
* [Sites Anomaly](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/sites-anomaly.md)
* [Sites Asset Filters](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/sites-asset-filters.md)
* [Sites Assets](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/sites-assets.md)
* [Sites Beacons](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/sites-beacons.md)
* [Sites Calls](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/sites-calls.md)
* [Sites Clients-Wan](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/sites-clients-wan.md)
* [Sites Clients-Wired](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/sites-clients-wired.md)
* [Sites Clients-Wireless](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/sites-clients-wireless.md)
* [Sites Devices](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/sites-devices.md)
* [Sites Devices-Wireless](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/sites-devices-wireless.md)
* [Sites Devices Others](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/sites-devices-others.md)
* [Sites Devices-Wired](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/sites-devices-wired.md)
* [Sites Devices-Wired Virtual Chassis](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/sites-devices-wired-virtual-chassis.md)
* [Sites Devices-WAN](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/sites-devices-wan.md)
* [Sites Devices-WANHA](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/sites-devices-wanha.md)
* [Sites Devices Stats](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/sites-devices-stats.md)
* [Sites Devices Upgrades](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/sites-devices-upgrades.md)
* [Sites Devices Utilities](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/sites-devices-utilities.md)
* [Sites Events](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/sites-events.md)
* [Sites EVPN Topologies](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/sites-evpn-topologies.md)
* [Sites Guests](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/sites-guests.md)
* [Sites Insights](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/sites-insights.md)
* [Sites Licenses](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/sites-licenses.md)
* [Sites Location](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/sites-location.md)
* [Sites Maps](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/sites-maps.md)
* [Sites Maps Auto-Orientation](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/sites-maps-auto-orientation.md)
* [Sites Maps Auto-Placement](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/sites-maps-auto-placement.md)
* [Sites Mx Edges](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/sites-mx-edges.md)
* [Sites Mx Tunnels](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/sites-mx-tunnels.md)
* [Sites Networks](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/sites-networks.md)
* [Sites Pcaps](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/sites-pcaps.md)
* [Sites Psks](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/sites-psks.md)
* [Sites Rfdiags](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/sites-rfdiags.md)
* [Sites Rogues](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/sites-rogues.md)
* [Sites RRM](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/sites-rrm.md)
* [Sites Rssizones](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/sites-rssizones.md)
* [Sites Services](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/sites-services.md)
* [Sites Service Policies](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/sites-service-policies.md)
* [Sites Setting](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/sites-setting.md)
* [Sites Skyatp](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/sites-skyatp.md)
* [Sites SL Es](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/sites-sl-es.md)
* [Sites Stats](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/sites-stats.md)
* [Sites Subscriptions](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/sites-subscriptions.md)
* [Sites Synthetic Tests](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/sites-synthetic-tests.md)
* [Sites UI Settings](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/sites-ui-settings.md)
* [Sitesv Beacons](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/sitesv-beacons.md)
* [Sites VP Ns](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/sites-vp-ns.md)
* [Sites Webhooks](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/sites-webhooks.md)
* [Sites Wlans](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/sites-wlans.md)
* [Sites Wx Rules](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/sites-wx-rules.md)
* [Sites Wx Tags](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/sites-wx-tags.md)
* [Sites Wx Tunnels](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/sites-wx-tunnels.md)
* [Sites Zones](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/sites-zones.md)
* [Webhook Samples](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/webhook-samples.md)
* [Orgs Admin](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/orgs-admin.md)
* [Login](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/login.md)
* [Installer](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/installer.md)
* [Admin](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/admin.md)
* [Mobile](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/mobile.md)
* [Msps](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/msps.md)
* [Sites](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/sites.md)
* [Constants](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/constants.md)
* [Self](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/controllers/self.md)

## Classes Documentation

* [Utility Classes](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/utility-classes.md)
* [HttpResponse](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/http-response.md)
* [HttpRequest](https://www.github.com/sdks-io/juniper-mist-python-sdk/tree/1.0.0/doc/http-request.md)

