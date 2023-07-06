Sometimes rows in SQL can be "nested". You can break out these rows by
"unnesting" them and joining them with the original query. For example,
given the table:

```
Row 1:
  - bindle:
    {name=AWSMary, description=null, guid=bindle.resource.vwvf}
  - aws_accounts:
    [{account_id=8757, aws_region=us-east-1}, {account_id=0996, aws_region=us-west-2}]
```

Running the query:

```
SELECT bindle.guid, aws_account.account_id, aws_account.aws_region
FROM "mapilicious_raw_sources_v2"."latest_pipelines"
CROSS JOIN UNNEST(aws_accounts) as t(aws_account)
LIMIT 10;
```

Will result in:

```
bindle.resource.vwvf, 8757, us-west-2
bindle.resource.vwvf, 0996, us-west-2
```

