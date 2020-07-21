from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory

while True:
    input_ = prompt(
        "> ",
        history=FileHistory(".prompt_ex.rc"),
    )

    print(input_)
