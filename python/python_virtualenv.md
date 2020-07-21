Virtual env allows you to install "local" python libraries without
having them affect your "global" python libraries. This allows you
to have different versions of the same library in different projects.

> Note: virtual env basically creates a "library folder" that you can
  use to loadup an environment. You **do not** want to add source
  files to the "library folder"

- `virtualenv $PROJECT_NAME`
    - Creates a new virtual environment directory

- `virtualenv -p requirements.txt $PROJECT_NAME`
    - Creates a new virtual environment directory based off existing
      list of python libs

- `source $PROJECT_NAME/bin/activate`
    - Load python environment into shell.  Know this b/c `pip list`
      will only contain ~3 python libraries
    - Prompt will change to show "inside"/"using" virtual env

- `pip freeze --local > requirements.txt`
    - Save libraries associated with particular virtual environment

- `deactivate`
    - Exit virtual environment

- `rm -rf $PROJECT_NAME`
    - Delete virtual environment
