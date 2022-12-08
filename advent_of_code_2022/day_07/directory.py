def parse_inputs(inputs: list) -> tuple[dict, dict]:
    parent_directories = {}
    current_directory = ""
    previous_directory = ""

    files = dict()
    directories = dict()

    for input in inputs:
        if input.startswith("$ cd"):
            previous_directory = current_directory
            current_directory = (
                parent_directories[current_directory]
                if input.endswith("..")
                else f"""{current_directory}/{input.split(" ")[-1]}""".replace(
                    "//", "/"
                )
            )
            if not parent_directories.get(current_directory):
                parent_directories[current_directory] = previous_directory

        elif input.startswith("$ ls"):
            files[current_directory] = []
            directories[current_directory] = []
        elif input.startswith("dir "):
            directories[current_directory].append(
                f"""{current_directory}/{input.split(" ")[-1]}""".replace(
                    "//", "/"
                )
            )
        else:
            file = input.split(" ")
            files[current_directory].append(
                [
                    file[0],
                    f"""{current_directory}/{file[1]}""".replace("//", "/"),
                ]
            )

    return files, directories


def get_size_of_directory(
    directory: str, files: dict, directories: dict
) -> int:
    size_of_files = sum([int(x[0]) for x in files.get(directory, [])])
    inner_directories = directories.get(directory, [])
    if not inner_directories:
        return size_of_files
    else:
        return size_of_files + sum(
            [
                get_size_of_directory(y, files, directories)
                for y in inner_directories
            ]
        )


def print_directory(
    directory: str, files: dict, directories: dict, level=0
) -> int:
    prefix = ""
    for _ in range(level):
        prefix += "\t"
    print(f"{prefix}- {directory} (dir)")
    for file in files.get(directory, []):
        print(f"{prefix}\t- {file[1]} (file, size={file[0]})")
    inner_directories = directories.get(directory, [])
    if not inner_directories:
        return
    else:
        for y in inner_directories:
            print_directory(y, files, directories, level + 1)
