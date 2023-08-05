**Installation 📦**

Install LumaCLI via pip:

```bash
pip install lumaCLI
```

# `lumaCLI`

**Usage**:

```console
$ lumaCLI [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `dbt`
* `postgres`

## `lumaCLI dbt`

**Usage**:

```console
$ lumaCLI dbt [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `ingest`: Sends a bundle of JSON files...
* `send-test-results`: Sends the run_results.json file located in...

### `lumaCLI dbt ingest`

Sends a bundle of JSON files (manifest.json, catalog.json, sources.json, run_results.json) to a Luma endpoint. If 'metadata_dir' is not specified, the current working directory is used.

Args:
    metadata_dir (str, optional): Directory path containing all the metadata files. Defaults to current working directory if not provided.
    endpoint (str): The endpoint URL for ingestion.

Returns:
    response: The HTTP response obtained from the endpoint.

**Usage**:

```console
$ lumaCLI dbt ingest [OPTIONS] [METADATA_DIR]
```

**Arguments**:

* `[METADATA_DIR]`: Path to the directory with dbt metadata files. If not provided, current working directory will be used.

**Options**:

* `-e, --endpoint TEXT`: URL of the ingestion endpoint.  [env var: LUMA_DBT_INGEST_ENDPOINT; required]
* `--help`: Show this message and exit.

### `lumaCLI dbt send-test-results`

Sends the run_results.json file located in the specified directory to a Luma endpoint. If 'metadata_dir' is not specified, the current working directory is used.

Args:
    metadata_dir (str, optional): Directory path containing the run_results.json file. Defaults to current working directory if not provided.
    endpoint (str): The endpoint URL for ingestion.

Returns:
    response: The HTTP response obtained from the endpoint.

**Usage**:

```console
$ lumaCLI dbt send-test-results [OPTIONS] [METADATA_DIR]
```

**Arguments**:

* `[METADATA_DIR]`: Path to the directory with the run_results.json file. If not provided, current working directory will be used.

**Options**:

* `-e, --endpoint TEXT`: URL of the ingestion endpoint.  [env var: LUMA_DBT_SEND-TEST-RESULTS_ENDPOINT; required]
* `--help`: Show this message and exit.

## `lumaCLI postgres`

**Usage**:

```console
$ lumaCLI postgres [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `ingest`: Creates dictionary with Postgres Metadata...

### `lumaCLI postgres ingest`

Creates dictionary with Postgres Metadata Information and sends it to the Luma Postgres ingest endpoint.

**Usage**:

```console
$ lumaCLI postgres ingest [OPTIONS] ENDPOINT
```

**Arguments**:

* `ENDPOINT`: URL of the Luma Postgres ingestion endpoint.  [env var: LUMA_POSTGRES_INGEST_ENDPOINT;required]

**Options**:

* `-u, --username TEXT`: PostgreSQL username.  [env var: LUMA_POSTGRES_USERNAME; required]
* `-d, --database TEXT`: PostgreSQL database.  [env var: LUMA_POSTGRES_DATABASE; required]
* `-h, --host TEXT`: PostgreSQL host.  [env var: LUMA_POSTGRES_HOST; default: localhost]
* `-p, --port TEXT`: PostgreSQL port.  [env var: LUMA_POSTGRES_PORT; default: 5432]
* `-P, --password TEXT`: PostgreSQL password.  [env var: LUMA_POSTGRES_PASSWORD; required]
* `-D, --dry-run`: Whether to do a dry run. Print but not send the payload
* `--help`: Show this message and exit.
