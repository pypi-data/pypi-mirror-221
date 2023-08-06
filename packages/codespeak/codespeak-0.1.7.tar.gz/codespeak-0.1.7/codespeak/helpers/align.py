import textwrap


def align(s: str):
    return textwrap.dedent(s).strip("\n")
