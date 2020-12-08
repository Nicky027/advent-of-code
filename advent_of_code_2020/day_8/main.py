from boot_code import BootCode


def main():
    with open("input.txt", "r") as file:
        input_code = file.readlines()

    code = BootCode(input_code)
    print(code.run())

    code2 = BootCode(input_code)
    print(code2.modified_run())


if __name__ == "__main__":
    main()
