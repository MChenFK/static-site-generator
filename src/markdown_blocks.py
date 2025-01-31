def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    new_blocks = []
    for block in blocks:
        block = block.strip()
        if len(block) == 0:
            continue
        new_blocks.append(block)
    return new_blocks
