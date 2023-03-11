## Rest vs. GraphQL

Rest API's are action oriented in that you define multiple "routes" that
the user can hit. GraphQL is much more data centric by being able to
do complex, dynamic queries all at once.

GraphQL seems like a pain to set up in a lot of ways... but it has a really
nice OOB schema exploration page to help debug.

Flask (or any other webserver) can implement either standard. The main
different is that REST would have multiple routes whereas GraphQL would have
a single `@route("/graphql", POST)` action that everything goes through.

