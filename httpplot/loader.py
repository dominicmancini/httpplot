import importlib.resources


def load_resource_text(filename: str) -> str | None:
    """Load a resource text file from the package.
    Args:
        filename (str): The name of the resource file to load.
    Returns:
        str | None: The contents of the resource file, or None if not found.
    """
    anchor = importlib.resources.files("httpplot.resources")
    content = ""
    
    file = anchor.joinpath(filename)
    # return none if file does not exist
    # if not file.is_file():
    #     return None
    try:
        with importlib.resources.as_file(file) as f:
            content = f.read_text()
    except Exception as e:
        pass
    return content


if __name__ == "__main__":
    ex = load_resource_text("httpgd.html")
    if ex is not None:
        print(f"Loaded {len(ex)} bytes")
    else:
        print("File not found")
