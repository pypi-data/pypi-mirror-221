Transformation_options = {
  "s3": {
        "run_interval": {"type": "integer", "editable": False, "optional": True,
            "syntax":"'run_interval': '<N MINUTES/HOURS/DAYS>'",
            "description":"""How often the job runs.
            The runs take place over a set period of time defined by this interval and they must be divisible by the number of hours in a day.
            For example, you can set RUN_INTERVAL to 2 hours (the job runs 12 times per day), but trying to set RUN_INTERVAL to 5 hours would fail since 24 hours is not evenly divisible by 5.RUN_INTERVAL
            Value: <integer> { MINUTE[S] | HOUR[S] | DAY[S] }
            Default: 1 MINUTE"""},
        "start_from": {"type": "value", "editable": False, "optional": True,
            "syntax":"'start_from': '<timestamp>/NOW/BEGINNING'",
            "description":"""Configures the time to start inserting data from. Data before the specified time is ignored.
            If set as a timestamp, it should be aligned to the RUN_INTERVAL.
            For example, if RUN_INTERVAL is set to 5 minutes, then you can set a start time of 12:05 PM but not 12:03 PM. Additionally, the timestamp should be based in UTC and in the following format: TIMESTAMP 'YYYY-MM-DD HH:MM:SS'.
            If set to NOW or BEGINNING, the job runs from the previous full period. For example, if the current time is 12:03 PM, creating the job with a RUN_INTERVAL of 5 minutes starting from NOW means that the first task executed by the job starts from 12:00 PM.
            Values: { NOW | BEGINNING | timestamp }
            Default: BEGINNING"""},
        "end_at": {"type": "value", "editable": True, "optional": True,
            "syntax":"'end_at': '<timestamp>/NOW'",
            "description":"""Configures the time to stop inserting data. Data after the specified time is ignored.
            If set as a timestamp, it should be aligned to the RUN_INTERVAL.
            For example, if RUN_INTERVAL is set to 5 minutes, then you can set an end time of 12:05 PM but not 12:03 PM. Additionally, the timestamp should be based in UTC and in the following format: TIMESTAMP 'YYYY-MM-DD HH:MM:SS'.
            If set to NOW, the job runs up until the previous full period. For example, if the current time is 12:03 PM, creating the job with a RUN_INTERVAL of 5 minutes ending at NOW means that the last task executed by the job ends at 12:00 PM.
            Values: { NOW | timestamp }
            Default: Never"""},
        "compute_cluster": {"type": "identifier", "editable": True, "optional": True,
            "syntax":"'compute_cluster': '<compute_cluster>'",
            "description":"""The compute cluster to run this job.
            This option can only be omitted when there is just one cluster in your environment.
            Once you have more than one compute cluster, you are required to provide which one to use through this option.
            Default: The sole cluster in your environment"""},
        "comment": {"type": "text", "editable": True, "optional": True,
            "syntax":"'comment': '<comment>'",
            "description":"""A description or comment regarding this job."""},
        "allow_cartesian_products": {"type": "boolean", "editable": False, "optional": True,
            "syntax":"'allow_cartesian_products': True/False",
            "description":"""When true, flattening unrelated arrays may lead to Cartesian products in your final result.
            See: UNNEST
            Default: false"""},
        "aggregation_parallelism": {"type": "integer", "editable": True, "optional": True,
            "syntax":"'aggregation_parallelism': <integer>",
            "description":"""Only supported when the query contains aggregations. Formally known as "output sharding."
            Default: 1"""},
        "run_parallelism": {"type": "integer", "editable": True, "optional": True,
            "syntax":"'run_parallelism': <integer>",
            "description":"""Controls how many jobs run in parallel to process a single minute of data from the source table.
            Increasing this can lower the end-to-end latency if you have lots of data per minute.
            Default: 1"""},
        "file_format": {"type": "value", "editable": False, "optional": False,
            "syntax":"'file_format': 'CSV/TSV ...'",
            "description":"""The file format for the output file.
            Values: { CSV | TSV | AVRO | PARQUET | JSON }"""},
        "compression": {"type": "value", "editable": False, "optional": True,
            "syntax":"'compression': 'SNAPPY/GZIP ...'",
            "description":"""The compression for the output files.
            Values: { NONE | GZIP | SNAPPY | ZSTD }
            Default: NONE"""},
        "date_pattern": {"type": "text", "editable": False, "optional": True,
            "syntax":"'date_pattern': '<date_pattern>'",
            "description":"""Upsolver uses the date pattern to partition the output on the S3 bucket. Upsolver supports partitioning up to the minute, for example: 'yyyy/MM/dd/HH/mm'. For more options, see: Java SimpleDateFormat
            Default:  'yyyy/MM/dd/HH/mm'"""},
        "output_offset": {"type": "identifier", "editable": False, "optional": True,
            "syntax":"'output_offset': '<N MINUTES/HOURS/DAYS>'",
            "description":""" By default, the file 2023/01/01/00/01 contains data for 2023-01-01 00:00 - 2023-01-01 00:00.59.999. Setting OUTPUT_OFFSET to 1 MINUTE add to that so a value of the first minute will move the file name to 02, if you want to move it back you can use negative values.
            Value: <integer> { MINUTE[S] | HOUR[S] | DAY[S] }
            Default: 0"""},
        "location": {"type": "text", "editable": False, "optional": False,
            "syntax":"'location': '<location>'",
            "description":"""The target location to write files to, as a full S3 URI. The location URI pattern can include macros referring to data columns, this allows custom partitioning of the data in the target location.
            Supported macros:
            Time: {time:<date-pattern>}
            This macro will be replaced with the job execution time at runtime. The date pattern provided must be in Java's date formatting syntax. Only a single-time macro can be used in the location.
            Column: {col:<column-name>}
            This macro will be replaced with the value of the column provided. The column provided must appear in the select statement of the job.
            Shard: {shard:format}
            This macro will be replaced by the output shard number writing the current file. It is important to use this as part of your pattern if you are using RUN_PARALLELISM, otherwise, each shard will overwrite the file.
            The supported format is a subset of Java's string fromat syntax. The supported options are either:
            1. %0xd - Will result in a shard number padded with x-1 leading 0's.  For example, %05d will result in 00001 for shard number 1.
            2. %d - Will simply use the shard number with no padding.
            Usually, it's recommended to include padding to ensure alphabetical sorting of the output files."""}
  },
  "elasticsearch": {
        "run_interval": {"type": "integer", "editable": False, "optional": True,
            "syntax":"'run_interval': '<N MINUTES/HOURS/DAYS>'",
            "description":"""How often the job runs.
            The runs take place over a set period of time defined by this interval and they must be divisible by the number of hours in a day.
            For example, you can set RUN_INTERVAL to 2 hours (the job runs 12 times per day), but trying to set RUN_INTERVAL to 5 hours would fail since 24 hours is not evenly divisible by 5.RUN_INTERVAL
            Value: <integer> { MINUTE[S] | HOUR[S] | DAY[S] }
            Default: 1 MINUTE"""},
        "start_from": {"type": "value", "editable": False, "optional": True,
            "syntax":"'start_from': '<timestamp>/NOW/BEGINNING'",
            "description":"""Configures the time to start inserting data from. Data before the specified time is ignored.
            If set as a timestamp, it should be aligned to the RUN_INTERVAL.
            For example, if RUN_INTERVAL is set to 5 minutes, then you can set a start time of 12:05 PM but not 12:03 PM. Additionally, the timestamp should be based in UTC and in the following format: TIMESTAMP 'YYYY-MM-DD HH:MM:SS'.
            If set to NOW or BEGINNING, the job runs from the previous full period. For example, if the current time is 12:03 PM, creating the job with a RUN_INTERVAL of 5 minutes starting from NOW means that the first task executed by the job starts from 12:00 PM.
            Values: { NOW | BEGINNING | timestamp }
            Default: BEGINNING"""},
        "end_at": {"type": "value", "editable": True, "optional": True,
            "syntax":"'end_at': '<timestamp>/NOW'",
            "description":"""Configures the time to stop inserting data. Data after the specified time is ignored.
            If set as a timestamp, it should be aligned to the RUN_INTERVAL.
            For example, if RUN_INTERVAL is set to 5 minutes, then you can set an end time of 12:05 PM but not 12:03 PM. Additionally, the timestamp should be based in UTC and in the following format: TIMESTAMP 'YYYY-MM-DD HH:MM:SS'.
            If set to NOW, the job runs up until the previous full period. For example, if the current time is 12:03 PM, creating the job with a RUN_INTERVAL of 5 minutes ending at NOW means that the last task executed by the job ends at 12:00 PM.
            Values: { NOW | timestamp }
            Default: Never"""},
        "compute_cluster": {"type": "identifier", "editable": True, "optional": True,
            "syntax":"'compute_cluster': '<compute_cluster>'",
            "description":"""The compute cluster to run this job.
            This option can only be omitted when there is just one cluster in your environment.
            Once you have more than one compute cluster, you are required to provide which one to use through this option.
            Default: The sole cluster in your environment"""},
        "allow_cartesian_products": {"type": "boolean", "editable": False, "optional": True,
            "syntax":"'allow_cartesian_products': True/False",
            "description":"""When true, flattening unrelated arrays may lead to Cartesian products in your final result.
            See: UNNEST
            Default: false"""},
        "aggregation_parallelism": {"type": "integer", "editable": True, "optional": True,
            "syntax":"'aggregation_parallelism': <integer>",
            "description":"""Only supported when the query contains aggregations. Formally known as "output sharding."
            Default: 1"""},
        "run_parallelism": {"type": "integer", "editable": True, "optional": True,
            "syntax":"'run_parallelism': <integer>",
            "description":"""Controls how many jobs run in parallel to process a single minute of data from the source table.
            Increasing this can lower the end-to-end latency if you have lots of data per minute.
            Default: 1"""},
        "bulk_max_size_bytes": {"type": "integer", "editable": True, "optional": True,
            "syntax":"'bulk_max_size_bytes': <integer>",
            "description":"""The max size of each bulk insert into the index. This option defaults to 9MB.
            Default: 9"""},
        "index_partition_size": {"type": "value", "editable": True, "optional": True,
            "syntax":"'index_partition_size': 'HOURLY/DAILY ...'",
            "description":"""The size of each partition of the index. The default is value is DAILY.
            Values: {  HOURLY | DAILY | MONTHLY | YEARLY }
            Default: DAILY"""},
        "comment": {"type": "text", "editable": True, "optional": True,
            "syntax":"'comment': '<comment>'",
            "description":"""A description or comment regarding this job."""}
  },
  "snowflake": {
        "custom_insert_expressions": {"type": "dict_str", "editable": True, "optional": True,
            "syntax":"'custom_insert_expressions': {'INSERT_TIME' : 'CURRENT_TIMESTAMP()','MY_VALUE': '<value>'}",
            "description":""" Configure a list of custom expression transformations to apply to the value of each column when inserting unmatched (new) rows. Note this is only used in Merge Jobs.
            Note: You can use {} as a placeholder for the mapped value from the select statement.
            Type: array[(column, expression)]
            Default: ()"""},
        "custom_update_expressions": {"type": "dict_str", "editable": True, "optional": True,
            "syntax":"'custom_update_expressions': {'UPDATE_TIME' : 'CURRENT_TIMESTAMP()','MY_VALUE': '<value>'}",
            "description":"""Configure a list of custom expression transformations to apply to the value of each column when updating matched rows. Note this is only used in Merge Jobs.
            Note: You can use {} as a placeholder for the mapped value from the select statement.
            Type: array[(column, expression)]
            Default: ()"""},
        "keep_existing_values_when_null": {"type": "boolean", "editable": True, "optional": True,
            "syntax":"'keep_existing_values_when_null': True/False",
            "description":""" If enabled, updates to the table preserve the previous non-null value. This option is useful if your update events only contain values for modified columns. This works by coalescing the new value with the existing value. If the new value is null the previous value will be preserved. This means that updating values to null is not supported.
            Default: false."""},
        "add_missing_columns": {"type": "boolean", "editable": False, "optional": True,
            "syntax":"'add_missing_columns': True/False",
            "description":"""When true, columns that don't exist in the target table are added automatically when encountered.
            When false, you cannot do SELECT * within the SELECT statement of your transformation job.
            Default: false"""},
        "run_interval": {"type": "integer", "editable": False, "optional": True,
            "syntax":"'run_interval': '<N MINUTES/HOURS/DAYS>'",
            "description":"""How often the job runs.
            The runs take place over a set period of time defined by this interval and they must be divisible by the number of hours in a day.
            For example, you can set RUN_INTERVAL to 2 hours (the job runs 12 times per day), but trying to set RUN_INTERVAL to 5 hours would fail since 24 hours is not evenly divisible by 5.RUN_INTERVAL
            Value: <integer> { MINUTE[S] | HOUR[S] | DAY[S] }
            Default: 1 MINUTE"""},
        "start_from": {"type": "value", "editable": False, "optional": True,
            "syntax":"'start_from': '<timestamp>/NOW/BEGINNING'",
            "description":"""Configures the time to start inserting data from. Data before the specified time is ignored.
            If set as a timestamp, it should be aligned to the RUN_INTERVAL.
            For example, if RUN_INTERVAL is set to 5 minutes, then you can set a start time of 12:05 PM but not 12:03 PM. Additionally, the timestamp should be based in UTC and in the following format: TIMESTAMP 'YYYY-MM-DD HH:MM:SS'.
            If set to NOW or BEGINNING, the job runs from the previous full period. For example, if the current time is 12:03 PM, creating the job with a RUN_INTERVAL of 5 minutes starting from NOW means that the first task executed by the job starts from 12:00 PM.
            Values: { NOW | BEGINNING | timestamp }
            Default: BEGINNING"""},
        "end_at": {"type": "value", "editable": True, "optional": True,
            "syntax":"'end_at': '<timestamp>/NOW'",
            "description":"""Configures the time to stop inserting data. Data after the specified time is ignored.
            If set as a timestamp, it should be aligned to the RUN_INTERVAL.
            For example, if RUN_INTERVAL is set to 5 minutes, then you can set an end time of 12:05 PM but not 12:03 PM. Additionally, the timestamp should be based in UTC and in the following format: TIMESTAMP 'YYYY-MM-DD HH:MM:SS'.
            If set to NOW, the job runs up until the previous full period. For example, if the current time is 12:03 PM, creating the job with a RUN_INTERVAL of 5 minutes ending at NOW means that the last task executed by the job ends at 12:00 PM.
            Values: { NOW | timestamp }
            Default: Never"""},
        "compute_cluster": {"type": "identifier", "editable": True, "optional": True,
            "syntax":"'compute_cluster': '<compute_cluster>'",
            "description":"""The compute cluster to run this job.
            This option can only be omitted when there is just one cluster in your environment.
            Once you have more than one compute cluster, you are required to provide which one to use through this option.
            Default: The sole cluster in your environment"""},
        "allow_cartesian_products": {"type": "boolean", "editable": False, "optional": True,
            "syntax":"'allow_cartesian_products': True/False",
            "description":"""When true, flattening unrelated arrays may lead to Cartesian products in your final result.
            See: UNNEST
            Default: false"""},
        "aggregation_parallelism": {"type": "integer", "editable": True, "optional": True,
            "syntax":"'aggregation_parallelism': <integer>",
            "description":"""Only supported when the query contains aggregations. Formally known as "output sharding."
            Default: 1"""},
        "run_parallelism": {"type": "integer", "editable": True, "optional": True,
            "syntax":"'run_parallelism': <integer>",
            "description":"""Controls how many jobs run in parallel to process a single minute of data from the source table.
            Increasing this can lower the end-to-end latency if you have lots of data per minute.
            Default: 1"""},
        "comment": {"type": "text", "editable": True, "optional": True,
            "syntax":"'comment': '<comment>'",
            "description":"""A description or comment regarding this job."""}
  },
    "datalake": {
        "add_missing_columns": {"type": "boolean", "editable": False, "optional": True,
            "syntax":"'add_missing_columns': True/False",
            "description":""" When true, columns that don't exist in the target table are added automatically when encountered.
            When false, you cannot do SELECT * within the SELECT statement of your transformation job.
            Default: false"""},
        "run_interval": {"type": "integer", "editable": False, "optional": True,
            "syntax":"'run_interval': '<N MINUTES/HOURS/DAYS>'",
            "description":"""How often the job runs.
            The runs take place over a set period of time defined by this interval and they must be divisible by the number of hours in a day.
            For example, you can set RUN_INTERVAL to 2 hours (the job runs 12 times per day), but trying to set RUN_INTERVAL to 5 hours would fail since 24 hours is not evenly divisible by 5.RUN_INTERVAL
            Value: <integer> { MINUTE[S] | HOUR[S] | DAY[S] }
            Default: 1 MINUTE"""},
        "start_from": {"type": "value", "editable": False, "optional": True,
            "syntax":"'start_from': '<timestamp>/NOW/BEGINNING'",
            "description":"""Configures the time to start inserting data from. Data before the specified time is ignored.
            If set as a timestamp, it should be aligned to the RUN_INTERVAL.
            For example, if RUN_INTERVAL is set to 5 minutes, then you can set a start time of 12:05 PM but not 12:03 PM. Additionally, the timestamp should be based in UTC and in the following format: TIMESTAMP 'YYYY-MM-DD HH:MM:SS'.
            If set to NOW or BEGINNING, the job runs from the previous full period. For example, if the current time is 12:03 PM, creating the job with a RUN_INTERVAL of 5 minutes starting from NOW means that the first task executed by the job starts from 12:00 PM.
            Values: { NOW | BEGINNING | timestamp }
            Default: BEGINNING"""},
        "end_at": {"type": "value", "editable": True, "optional": True,
            "syntax":"'end_at': '<timestamp>/NOW'",
            "description":"""Configures the time to stop inserting data. Data after the specified time is ignored.
            If set as a timestamp, it should be aligned to the RUN_INTERVAL.
            For example, if RUN_INTERVAL is set to 5 minutes, then you can set an end time of 12:05 PM but not 12:03 PM. Additionally, the timestamp should be based in UTC and in the following format: TIMESTAMP 'YYYY-MM-DD HH:MM:SS'.
            If set to NOW, the job runs up until the previous full period. For example, if the current time is 12:03 PM, creating the job with a RUN_INTERVAL of 5 minutes ending at NOW means that the last task executed by the job ends at 12:00 PM.
            Values: { NOW | timestamp }
            Default: Never"""},
        "compute_cluster": {"type": "identifier", "editable": True, "optional": True,
            "syntax":"'compute_cluster': '<compute_cluster>'",
            "description":"""The compute cluster to run this job.
            This option can only be omitted when there is just one cluster in your environment.
            Once you have more than one compute cluster, you are required to provide which one to use through this option.
            Default: The sole cluster in your environment"""},
        "allow_cartesian_products": {"type": "boolean", "editable": False, "optional": True,
            "syntax":"'allow_cartesian_products': True/False",
            "description":"""When true, flattening unrelated arrays may lead to Cartesian products in your final result.
            See: UNNEST
            Default: false"""},
        "aggregation_parallelism": {"type": "integer", "editable": True, "optional": True,
            "syntax":"'aggregation_parallelism': <integer>",
            "description":"""Only supported when the query contains aggregations. Formally known as "output sharding."
            Default: 1"""},
        "run_parallelism": {"type": "integer", "editable": True, "optional": True,
            "syntax":"'run_parallelism': <integer>",
            "description":"""Controls how many jobs run in parallel to process a single minute of data from the source table.
            Increasing this can lower the end-to-end latency if you have lots of data per minute.
            Default: 1"""},
        "comment": {"type": "text", "editable": True, "optional": True,
            "syntax":"'comment': '<comment>'",
            "description":"""A description or comment regarding this job."""}
    },
    "redshift": {
        "run_interval": {"type": "integer", "editable": False, "optional": True,
            "syntax":"'run_interval': '<N MINUTES/HOURS/DAYS>'",
            "description":"""How often the job runs.
            The runs take place over a set period of time defined by this interval and they must be divisible by the number of hours in a day.
            For example, you can set RUN_INTERVAL to 2 hours (the job runs 12 times per day), but trying to set RUN_INTERVAL to 5 hours would fail since 24 hours is not evenly divisible by 5.RUN_INTERVAL
            Value: <integer> { MINUTE[S] | HOUR[S] | DAY[S] }
            Default: 1 MINUTE"""},
        "start_from": {"type": "value", "editable": False, "optional": True,
            "syntax":"'start_from': '<timestamp>/NOW/BEGINNING'",
            "description":"""Configures the time to start inserting data from. Data before the specified time is ignored.
            If set as a timestamp, it should be aligned to the RUN_INTERVAL.
            For example, if RUN_INTERVAL is set to 5 minutes, then you can set a start time of 12:05 PM but not 12:03 PM. Additionally, the timestamp should be based in UTC and in the following format: TIMESTAMP 'YYYY-MM-DD HH:MM:SS'.
            If set to NOW or BEGINNING, the job runs from the previous full period. For example, if the current time is 12:03 PM, creating the job with a RUN_INTERVAL of 5 minutes starting from NOW means that the first task executed by the job starts from 12:00 PM.
            Values: { NOW | BEGINNING | timestamp }
            Default: BEGINNING"""},
        "end_at": {"type": "value", "editable": True, "optional": True,
            "syntax":"'end_at': '<timestamp>/NOW'",
            "description":"""Configures the time to stop inserting data. Data after the specified time is ignored.
            If set as a timestamp, it should be aligned to the RUN_INTERVAL.
            For example, if RUN_INTERVAL is set to 5 minutes, then you can set an end time of 12:05 PM but not 12:03 PM. Additionally, the timestamp should be based in UTC and in the following format: TIMESTAMP 'YYYY-MM-DD HH:MM:SS'.
            If set to NOW, the job runs up until the previous full period. For example, if the current time is 12:03 PM, creating the job with a RUN_INTERVAL of 5 minutes ending at NOW means that the last task executed by the job ends at 12:00 PM.
            Values: { NOW | timestamp }
            Default: Never"""},
        "compute_cluster": {"type": "identifier", "editable": True, "optional": True,
            "syntax":"'compute_cluster': '<compute_cluster>'",
            "description":"""The compute cluster to run this job.
            This option can only be omitted when there is just one cluster in your environment.
            Once you have more than one compute cluster, you are required to provide which one to use through this option.
            Default: The sole cluster in your environment"""},
        "allow_cartesian_products": {"type": "boolean", "editable": False, "optional": True,
            "syntax":"'allow_cartesian_products': True/False",
            "description":"""When true, flattening unrelated arrays may lead to Cartesian products in your final result.
            See: UNNEST
            Default: false"""},
        "aggregation_parallelism": {"type": "integer", "editable": True, "optional": True,
            "syntax":"'aggregation_parallelism': <integer>",
            "description":"""Only supported when the query contains aggregations. Formally known as "output sharding."
            Default: 1"""},
        "run_parallelism": {"type": "integer", "editable": True, "optional": True,
            "syntax":"'run_parallelism': <integer>",
            "description":"""Controls how many jobs run in parallel to process a single minute of data from the source table.
            Increasing this can lower the end-to-end latency if you have lots of data per minute.
            Default: 1"""},
        "skip_failed_files": {"type": "boolean", "editable": False, "optional": True,
            "syntax":"'skip_failed_files': True/False",
            "description":"""When true, the job will skip any files in which the job is unsuccessful and continue with the rest of the files.
            Default: true"""},
        "fail_on_write_error": {"type": "boolean", "editable": False, "optional": True,
            "syntax":"'fail_on_write_error': True/False",
            "description":"""When true, the job will fail when an on-write error occurs.
            Default: false"""},
        "comment": {"type": "text", "editable": True, "optional": True,
            "syntax":"'comment': '<comment>'",
            "description":"""A description or comment regarding this job."""}
    }
}
