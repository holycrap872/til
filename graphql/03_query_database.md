## Querying a GraphQL database

```
query {
  totalCustomers
  allPets {
    weight
    category
  }
  totalPets
}
```

yields

```
{
    "data": {
        "totalCustomers": 903,
        "allPets": [
            {
                "weight": 10.2
            },
            {
                "weight": 9.7
            },
            ...
        ],
        "totalPets": 25
    }
}
```
