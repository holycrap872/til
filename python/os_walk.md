#OS Walk

I've always found `os.walk` a little confusing.  I used it but never really
bothered to try to understand it.  That time is not (to understand it that is).
`os.walk` takes a path of a file struture to exploreand returns a
*triple* of every directory within the structure. This runs a little bit counter
to what I've always thought so I'll provide an example.

Consider the following snippit of code:

```
for dir, sub_dirs, files in os.walk(path_to_file_structure):
    print("Exploring directory located at " + str(dir))

    print("Sub-directories in directory:")
    for sub_dir in sub_dirs:
        print(sub_dir)

        print("Full path to above sub-directory:")
        print(os.path.join(dir, sub_dir))

    print("Files within in directory:")
    for file in files:
        print(file)

        print("Full path to the above file:")
        print(os.path.join(dir, file))
```

Put another way, we are iterating through each `dir` within the file structure
and we are given a list of files and sub-directories that are within the `dir`.

[thanks!](http://pythoncentral.io/how-to-traverse-a-directory-tree-in-python-guide-to-os-walk/)
