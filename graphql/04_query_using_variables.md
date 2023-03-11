# Query using variables

You can create the equivalent of a query "function" where you fill in the
parameters for the query using query variables. In the example below, we
do two things.

1. We create a query "function" named `PetByName` that takes as its input
a status.
2. That query "function" forwards the status to the `allPets` query.

When combined with setting the query "variable" elsewhere, this allows me
to query for all pets based on status in a resuable way.

Query:

```
query PetByName($status: PetStatus) {
  allPets(status: $status) {
    weight
  }
}
```

Query Variables:

```
{
  "status": "AVAILABLE"
}
```
