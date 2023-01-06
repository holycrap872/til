It's possible to quickly set up a local server for the folder that you are in
using the following command:

```
npx browser-sync start --server --files "./*.html" --no-open --no-notify --directory
```

This serves all .html files in the directory (recursively) so that they can easily be
accessed from the browser by going to localhost:3000. There, all the html files will be
nicely/neatly listed and you can interact with them.

I learned this from the egghead.io tutorial on react.
