def extract_title(markdown):
    if len(markdown) == 0:
        raise Exception("Markdown must not be empty")
    lines = markdown.split("\n")
    for line in lines:
        if line[:2] == "# ":
            return line.strip("# ")
    raise Exception("Markdown must have title)")