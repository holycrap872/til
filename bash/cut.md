# Cut examples

- Cut from character 2 to 13
  - `cat test.txt | cut -c 2-13`

- Cut from character 5 to end
  - `cat test.txt | cut -c 5-`

- Cut using space as delimiter, select, first and second field, and use ','
  as new delimiter
  - ` cat test.txt | cut -d' ' -f1,2 --output-delimiter=','

- Cut using tab (the default) as delimiter, select, first and second field,
  and use ',' as new delimiter
  - ` cat test.txt | cut -d -f1,2 --output-delimiter=','
