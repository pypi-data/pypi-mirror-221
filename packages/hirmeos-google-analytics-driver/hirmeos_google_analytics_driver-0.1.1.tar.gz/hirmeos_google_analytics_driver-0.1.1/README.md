# Google Analytics Driver
[![Build Status](https://travis-ci.org/hirmeos/google_analytics_driver.svg?branch=master)](https://travis-ci.org/hirmeos/google_analytics_driver) [![Release](https://img.shields.io/github/release/hirmeos/google_analytics_driver.svg?colorB=58839b)](https://github.com/hirmeos/google_analytics_driver/releases) [![License](https://img.shields.io/github/license/hirmeos/google_analytics_driver.svg?colorB=ff0000)](https://github.com/hirmeos/google_analytics_driver/blob/master/LICENSE)

- Documentation: https://metrics.operas-eu.org/docs/google-analytics

This driver allows programmatic retrieval of Google Analytics stats reports in order to generate normalised publication-level usage reports.

The driver is made of two modules: the first one obtains statistics from GA's API and stores them in a directory (`CACHEDIR`); the second reads from cache, normalises the reports, and outputs to a different directory (`OUTDIR`). We recommend running this driver in a docker container and mapping both `CACHEDIR` and `OUTDIR` to persistent volumes.

## Setup
### Requirements
Identifier normalisation is performed using an instance of [hirmeos/identifier_translation_service][1] - you must first setup this API.

### API Service Account Key
Obtain the private key of a service account linked to your google analytics views: https://developers.google.com/analytics/devguides/reporting/core/v4/quickstart/service-py

The private key will be inside a json file. We must provide the path to this file using the env variable `KEY_PATH` (see "Environment variables" below). If you are running the driver using docker you will need to map the local json file to the `KEY_PATH` location in the container (see "Run via crontab" below).

### Environment variables
The following environment variables must be set. You can find a template in `./config/config.env.example`.

| Variable                | Description                                                                                        |
| ----------------------- | -------------------------------------------------------------------------------------------------- |
| `MODES`                 | A JSON array containing further configuration (see below).                                         |
| `EXCLUDED_URLS`         | An array of URLs that are reported on GA but should be ignored.                                    |
| `KEY_PATH`              | The path to the json file containing Google Analytics API private key.                             |
| `OUTDIR`                | The path to the directory where the driver will store its output.                                  |
| `CACHEDIR`              | The path to the directory where the driver will store the raw reports.                             |
| `URI_API_ENDP`          | The URL to the translation service.                                                                |
| `API_DEBUG`             | Whether to use JWT to authenticate to the translation service (true/false).                        |
| `AUTH_API_ENDP`         | The URL to the tokens API. Optional if `API_DEBUG=false`                                           |
| `URI_API_USER`          | The email address of the user with access to the translation service. Optional if `API_DEBUG=false`|
| `URI_API_PASS`          | The password of the above user. Optional if `API_DEBUG=false`                                      |
| `URI_SCHEME`            | The desired URI scheme to normalise identifiers to (we recommend DOI, info:doi).                   |
| `COUNTRY_URI_SCHEME`    | The URI scheme of the country coulmn ('urn:iso:std:3166:-2' for iso2).                             |
| `URI_STRICT`            | Whether to output errors with ambiguous translation queries.                                       |
| `CUTOFF_DAYS`           | The driver will get reports until today minus `CUTOFF_DAYS`.                                       |


### Example `config.env` file

```
MODES=["measure":"https://metrics.operas-eu.org/obp-pdf/sessions/v1","name":"obp-htmlreader","prefix":"https://www.openbookpublishers.com/htmlreader","startDate":"2014-02-26","config":[{"name":"view-id","value":"012345678"},{"name":"metric","value":"ga:uniquePageViews"},{"name":"dimension","value":"ga:pagePathLevel2"},{"name":"dimension","value":"ga:countryIsoCode"},{"name":"filter","value":"^/htmlreader/"}],"regex":["https:\\/\\/www\\.openbookpublishers\\.com\\/htmlreader\\/(?:[0-9]{3}-)?[0-9]{1,5}-[0-9]{1,7}-[0-9]{1,6}-[0-9]"]}]
EXCLUDED_URLS=[]
OUTDIR=/usr/src/app/output
CACHEDIR=/usr/src/app/cache
KEY_PATH=/usr/src/app/config/key.json
URI_API_ENDP=https://identifier.translation.service/translate
AUTH_API_ENDP=https://authentication.service/tokens
URI_API_USER=admin_user@openbookpublishers.com
URI_API_PASS=some_secret_password
URI_SCHEME=info:doi
COUNTRY_URI_SCHEME=urn:iso:std:3166:-2
URI_STRICT=false
CUTOFF_DAYS=1
```

### The `MODES` env variable
You must define a JSON array in`MODES`, with at least one record. The driver will iterate through the array, performing its task once per mode; in a typical case there will only be one entry in the array, however this configuration allows one single driver to query reports from multiple google analytics accounts.

Each entry of the `MODES` array must contain values for `measure`, `name`, `startDate`, and `config`.

| Attribute   | Description                                                                                                     |
| ----------- | --------------------------------------------------------------------------------------------------------------- |
| `measure`   | A URI identifying the type of measure. Similar to other drivers, the name should reflect the platform; in the case of GA, your own platofrm, e.g. https://metrics.operas-eu.org/obp-html/sessions/v1 to measure sessions in Open Book Publisher's HTML online reader. |
| `name`      | The name of this mode. This is not too important, though it is used as the prefix of cache files, so if you run multiple MODES you should use unique names. |
| `startDate` | The first date in which your account has usage data available in Google Analytics (YYYY-MM-DD format).                                                      |
| `config`    | An array containing various parameters needed to pass onto GA's API (e.g. view ID) (see below).                                                             |
| `regex`     | The regular expression needed to retrieve data for a specific URL structure. For example, Open Book Publishers's HTML reader uses /htmlreader/{book_isbn} hence our regex would be "https:\\/\\/www\\.openbookpublishers\\.com\\/htmlreader\\/(?:[0-9]{3}-)?[0-9]{1,5}-[0-9]{1,7}-[0-9]{1,6}-[0-9]" |

#### The `config` attribute
| Attribute   | Description                                                                                                                                      |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `view-id`   | The ID of the GA view that you wish to access. You can use https://ga-dev-tools.appspot.com/account-explorer to find a View ID.                  |
| `metric`    | The main metric we're interested in. We like to use "ga:uniquePageViews" (this would be sessions when applied to a parent directory). You may find the full list in https://developers.google.com/analytics/devguides/reporting/core/dimsmets |
| `dimension` | The dimensions related to metric that we want to obtain. We recommend including two of these, "ga:pagePathLevel2" (the path) and "ga:countryIsoCode" (country in iso-2 format - prefixed after with `COUNTRY_URI_SCHEME`). Again, you may find the full list in https://developers.google.com/analytics/devguides/reporting/core/dimsmets |
| `filter`    | What filter to use so that you don't get all data for the whole website. In our example this would be "^/htmlreader/" (starts with 'htmlreader') |

Example:
```
MODES=[{"measure":"https://metrics.operas-eu.org/obp-pdf/sessions/v1","name":"obp-htmlreader","prefix":"https://www.openbookpublishers.com/htmlreader","startDate":"2015-01-01","config":[{"name":"view-id","value":"012345678"},{"name":"metric","value":"ga:uniquePageViews"},{"name":"dimension","value":"ga:pagePathLevel2"},{"name":"dimension","value":"ga:countryIsoCode"},{"name":"filter","value":"^/htmlreader/"}],"regex":["https:\\/\\/www\\.openbookpublishers\\.com\\/htmlreader\\/(?:[0-9]{3}-)?[0-9]{1,5}-[0-9]{1,7}-[0-9]{1,6}-[0-9]"]}]
```

## Run via crontab
```
0 0 * * 0 docker run --rm --name "google_analytics_driver" --env-file /path/to/config.env -v google_analytics_cache:/usr/src/app/cache -v metrics:/usr/src/app/output openbookpublishers/google_analytics_driver:2
```
- `--rm` is used to delete the container once it exists;
- `--name` is completely optional (it will get receive a random name otherwise);
- `--env-file` is the path to the config file (in the local machine);
- `-v` is to add a volume (to persist data). We have three of these: google_analytics_cache will store the results of the API queries to GA; metrics stores the output of the driver (the normalised CSV files); and the last one (`key.json`) is a mapping of the local json file containing the API credentials, to the location in the container specified in `KEY_PATH`.


[1]: https://github.com/hirmeos/identifier_translation_service "Identifier Translation Service"
