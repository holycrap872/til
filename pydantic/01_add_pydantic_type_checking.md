## Type checking pydantic models

With the proper settings, VsCode gives you good type checking. In order to turn
on type checking for pydantic, follow the instructions seen
[here](https://docs.pydantic.dev/visual_studio_code/#configure-vs-code). Turning
on the extra "features" in VsCode will give you things like auto-complete and
other niceties. Installation includes:

1. Pylance: "Recommended, next-generation, official VS Code plug-in for Python."
2. Mypy: Gives you "error checks ... alternatively/additionally to Pylance"

> It's still not 100% clear to me how pylance and mypy are related (pylance
seems to have implemented it's own type checking system), but they both seem
to honor the mypy.ini file.