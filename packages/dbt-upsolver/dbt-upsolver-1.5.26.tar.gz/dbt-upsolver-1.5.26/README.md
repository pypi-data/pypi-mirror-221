# dbt-upsolver
# Using Upsolver udapter for dbt

- [What is Upsolver](#what_is_upsolver)
- [SQLake](#SQLake)
- [What is dbt](#what_is_dbt)
- [What is dbt Core](#what_is_dbt_core)
- [Getting started](#getting_started)
    - [Install dbt-upsolver adapter](#install_dbt_upsolver)
    - [Register Upsolver account](#register_upsolver)
    - [Create API token](#create_api_token)
    - [Create new dbt-upsolver project](#create_new_project)
- [Supported dbt commands](#supported_dbt)
- [Supported Upsolver SQLake functionality](#supported_upsolver)
- [Further reading](#further_reading)

## What is Upsolver

[Upsolver](https://upsolver.com) enables you to use familiar SQL syntaxto quickly build and deploy data pipelines, powered by a stream processing engine designed for cloud data lakes.

## SQLake

[SQLake](https://docs.upsolver.com/sqlake) is Upsolvers new UI and SQL console allowing to execute commands and monitor pipelines in the UI. It also includes freee trial and access to variety of examples and tutorials.

## What is dbt
[dbt](https://docs.getdbt.com/) is a transformation workflow that helps you get more work done while producing higher quality results.

## What is dbt Core
dbt Core is an open-source tool that enables data teams to transform data using analytics engineering best practices. You can install and use dbt Core on the command line.

## Getting started  

### Install dbt-upsolver adapter :

```sh
 pip install  dbt-upsolver
```
### Make sure the adapter is installed:
```sh
dbt --version
```
#### Expect to see:
```
Core:
  - installed: <version>
  - latest:    <version>
Plugins:
  - upsolver: <version>
```
### Register Upsolver account

To register just navigate to [SQL Lake Sign Up form](https://sqlake.upsolver.com/signup). You'll have access to SQL workbench with examples and tutorials after completing the registration.

### Create API token

After login navigate to "[Settings](https://sqlake.upsolver.com/Settings)" and then to "[API Tokens](https://sqlake.upsolver.com/Settings/api-tokens)"

You will need API token and API Url to access Upsolver programatically.

![API Tokens screen](https://github.com/Upsolver/upsolver-sdk-python/raw/build_package/doc/img/APITokens-m.png)

Then click "Generate" new token and save it for future use.

### Get your user name, database and schema
For **user name** navigate to **Settings** -> **User details** and copy user name
For **database** and **schema** navigate to **Worksheets** and click **New**.
You will find **database name** and **schema(catalog) name** under **Entities panel**

###  Create new dbt-upsolver project
```sh
dbt init <project_name>
```
Prompt:

Which database would you like to use?
[1] upsolver

```sh
Enter a number:
api_url (your api_url): https://mt-api-prod.upsolver.com
token (your token): <token>
user (dev username): <username>
database (default database): <database>
schema (default schema): <schema>
threads (1 or more) [1]: <number>
```

####  profiles.yml should look like this:
###### profiles.yml location is something like /Users/<user>/.dbt/profiles.yml
```yml
project_name:
  target: dev
  outputs:
    dev:
      api_url: https://mt-api-prod.upsolver.com
      database: ...
      schema: ...
      threads: 1
      token: ...
      type: upsolver
      user: ...
```

### Check connection
```sh
dbt debug
```
#### - To run all models
```sh
dbt run
```
#### - To run the specific model
```sh
dbt run --select <model name>
```
### Supported dbt commands:

| COMMAND | STATE |
| ------ | ------ |
| docs| supported |
| source | supported |
| init | supported |
| clean | supported |
| debug | supported |
| deps | supported |
| list| not supported |
| ls | not supported |
| build | supported |
| snapshot | not supported |
| run | supported |
| compile | supported |
| parse | supported |
| test | not supported |
| seed | not supported |
| run-operation | supported |

### Supported Upsolver SQLake functionality:
| FUNCTION | STATE | MATERIALIZED | CONFIGURATION PROPERTIES
| ------ | ------ | ------ | ------ |
| Create compute cluster| not supported | - | - |
| [Create connection](https://docs.upsolver.com/sqlake/sql-command-reference/sql-connections/create-connection) | supported | connection | connection_type(S3/Kafka/Snowflake ...), [connection_options](https://docs.upsolver.com/sqlake/sql-command-reference/sql-connections/create-connection#connection-options) |
| [Create copy job](https://docs.upsolver.com/sqlake/sql-command-reference/sql-jobs/create-job/copy-from) | supported | incremental, incremental_strategy: 'copy' | source(S3/Kafka/Snowflake ...) , target_type(Datalake/Snowflake), [options](https://docs.upsolver.com/sqlake/sql-command-reference/sql-jobs/create-job/copy-from#job-options) |
| [Create merge job](https://docs.upsolver.com/sqlake/sql-command-reference/sql-jobs/create-job/sql-transformation-jobs/merge) | supported | incremental, incremental_strategy: 'merge'| target_type(S3/Datalake/Snowflake ...), target_connection, target_table_alias, target_schema, [options](https://docs.upsolver.com/sqlake/sql-command-reference/sql-jobs/create-job/sql-transformation-jobs/merge#job-options) |
| [Create insert job](https://docs.upsolver.com/sqlake/sql-command-reference/sql-jobs/create-job/sql-transformation-jobs/insert) | supported | incremental, incremental_strategy: 'insert'| target_type(S3/Datalake/Snowflake ...), target_connection, target_table_alias, target_schema, [options](https://docs.upsolver.com/sqlake/sql-command-reference/sql-jobs/create-job/sql-transformation-jobs/insert#job-options) |
| [Create materialized views](https://docs.upsolver.com/sqlake/sql-command-reference/sql-jobs/sql-materialized-views) | supported | materializedview |
| [Expectations](https://docs.upsolver.com/sqlake/how-to-guides/managing-data-quality-ingesting-data-with-expectations) | supported | incremental, incremental_strategy: 'copy' | model constraints and column constraints [in the yml file](https://docs.getdbt.com/reference/resource-properties/constraints) |
| [MAP_COLUMNS_BY_NAME](https://docs.upsolver.com/sqlake/sql-command-reference/sql-jobs/create-job/sql-transformation-jobs/insert/map_columns_by_name) | supported | incremental, incremental_strategy: ‘insert’ | map_columns_by_name(True/False) |
| [Upsert with INSERT](https://docs.upsolver.com/sqlake/quickstarts/upsert-data-to-your-target-table#upsert-with-insert) | supported | incremental, incremental_strategy: ‘insert’ | primary_key|
| [Upsert with MERGE](https://docs.upsolver.com/sqlake/quickstarts/upsert-data-to-your-target-table#upsert-with-insert)| supported | incremental, incremental_strategy: ‘merge’ | primary_key |
| [PARTITIONED BY](https://docs.upsolver.com/sqlake/sql-command-reference/sql-tables/create-table#partition-clause) | supported | incremental | partition_by |


## SQL connections
Connections are used to provide Upsolver with the proper credentials to bring your data into SQLake as well as to write out your transformed data to various services. More details on ["Upsolver SQL connections"](https://docs.upsolver.com/sqlake/sql-command-reference/sql-connections)
As a dbt model connection is a model with materialized='connection'
```sql
{{ config(
        materialized='connection',
        connection_type={ 'S3' | 'GLUE_CATALOG' | 'KINESIS' | 'KAFKA'| 'SNOWFLAKE' },
        connection_options={}
    	)
}}
```
Running this model will compile CREATE CONNECTION(or ALTER CONNECTION if exists) SQL and send it to Upsolver engine. Name of the connection will be name of the model.

## SQL copy job
A COPY FROM job allows you to copy your data from a given source into a table created in a metastore connection. This table then serves as your staging table and can be used with SQLake transformation jobs to write to various target locations. More details on ["Upsolver SQL copy-from"](https://docs.upsolver.com/sqlake/sql-command-reference/sql-jobs/create-job/copy-from)

As a dbt model copy job is model with materialized='incremental'
```sql
{{ config(  materialized='incremental',
            sync=True|False,
            source = 'S3'| 'KAFKA' | ... ,
        	options={
              	'option_name': 'option_value'
            },
        	partition_by=[{}]
      	)
}}
SELECT * FROM {{ ref(<model>) }}
```
Running this model will  compile CREATE TABLE SQL(or ALTER TABLE if exists) and CREATE COPY JOB(or ALTER COPY JOB if exists) SQL and send it to Upsolver engine. Name of the table will be name of the model. Name of the job will be name of the model plus '_job'

## SQL insert job
An INSERT job defines a query that pulls in a set of data based on the given SELECT statement and inserts it into the designated target. This query is then run periodically based on the RUN_INTERVAL defined within the job. More details on ["Upsolver SQL insert"](https://docs.upsolver.com/sqlake/sql-command-reference/sql-jobs/create-job/sql-transformation-jobs/insert).

As a dbt model insert job is model with materialized='incremental' and incremental_strategy='insert'
```sql
{{ config(  materialized='incremental',
            sync=True|False,
            map_columns_by_name=True|False,
            incremental_strategy='insert',
            options={
              	'option_name': 'option_value'
            },
            primary_key=[{}]
          )
}}
SELECT ...
FROM {{ ref(<model>) }}
WHERE ...
GROUP BY ...
HAVING COUNT(DISTINCT orderid::string) ...
```
Running this model will compile CREATE TABLE SQL(or ALTER TABLE if exists) and CREATE INSERT JOB(or ALTER INSERT JOB if exists) SQL and send it to Upsolver engine. Name of the table will be name of the model. Name of the job will be name of the model plus '_job'

## SQL merge job
A MERGE job defines a query that pulls in a set of data based on the given SELECT statement and inserts into, replaces, or deletes the data from the designated target based on the job definition. This query is then run periodically based on the RUN_INTERVAL defined within the job. More details on ["Upsolver SQL merge"](https://docs.upsolver.com/sqlake/sql-command-reference/sql-jobs/create-job/sql-transformation-jobs/merge).

As a dbt model merge job is model with materialized='incremental' and incremental_strategy='merge'
```sql
{{ config(  materialized='incremental',
            sync=True|False,
            map_columns_by_name=True|False,
            incremental_strategy='merge',
            options={
              	'option_name': 'option_value'
            },
            primary_key=[{}]
          )
}}
SELECT ...
FROM {{ ref(<model>) }}
WHERE ...
GROUP BY ...
HAVING COUNT ...
```
Running this model will compile CREATE TABLE SQL(or ALTER TABLE if exists) and CREATE MERGE JOB(or ALTER MERGE JOB if exists) SQL and send it to Upsolver engine. Name of the table will be name of the model. Name of the job will be name of the model plus '_job'

## SQL materialized views
When transforming your data, you may find that you need data from multiple source tables in order to achieve your desired result.
In such a case, you can create a materialized view from one SQLake table in order to join it with your other table (which in this case is considered the main table). More details on ["Upsolver SQL materialized views"](https://docs.upsolver.com/sqlake/sql-command-reference/sql-jobs/create-job/sql-transformation-jobs/sql-materialized-views).

As a dbt model materialized views  is model with materialized='materializedview'.
```sql
{{ config(  materialized='materializedview',
            sync=True|False,
            options={'option_name': 'option_value'}
        )
}}
SELECT ...
FROM {{ ref(<model>) }}
WHERE ...
GROUP BY ...
```
Running this model will compile CREATE MATERIALIZED VIEW SQL(or ALTER MATERIALIZED VIEW if exists) and send it to Upsolver engine. Name of the materializedview  will be name of the model.

## Projects examples

> projects examples link: [github.com/dbt-upsolver/examples/](https://github.com/Upsolver/dbt-upsolver/tree/main/examples)

## Further reading

[Projects examples](https://github.com/Upsolver/dbt-upsolver/tree/main/examples)

[Upsolver sqlake documentation](https://docs.upsolver.com/sqlake/)

[DBT documentation](https://docs.getdbt.com/docs/introduction)

[Upsolver Comunity Slack](https://join.slack.com/t/upsolvercommunity/shared_invite/zt-1zo1dbyys-hj28WfaZvMh4Z4Id3OkkhA)
