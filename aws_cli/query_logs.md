## How to query AWS logs

This resulted in a false step down, what I would argue, was the obvious path
followed by sweet redemption thans to dsmrt/query-aws-logs-insights.bash.

### False step

I want to look at the logs, and get some filtered results:

```
aws logs filter-log-events --log-group-name <log_group> --filter-pattern "Seeing if h" --region us-west-2 --start-time 1609503200000
```

Unfortunately, this was super slow. I was thinking to myself, is there a version
of insights for the CLI:

### Proper step

1. Create an insights query

```
aws logs start-query --log-group-name <log_group> --region us-west-2 --start-time 1609503200000 --end-time 1621081962000 --query-string "fields @message | filter @message like /Seeing if h/"
```

2. Download the results

```
aws logs get-query-results --query-id <output_of_prev_command> --region us-west-2 > out.txt
```

> Note: There's a status of the query at the beginning of the output... wait for it
    to "Complete".
