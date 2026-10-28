#!/usr/bin/env python3

def secure_archive(
    m_filename: str, mode: str, cont: str = ""
) -> tuple[bool, str]:
    try:
        if mode == "read":
            with open(m_filename, "r") as file:
                text = file.read()
                return True, text
        elif mode == "write":
            with open(m_filename, "w") as file:
                file.write(cont)
                return True, "Content succesfully written to file"
        else:
            return False, "Incorrect 'mode', try again."
    except OSError as error:
        return False, str(error)


if __name__ == "__main__":
    print(
        "=== Cyber Archives Security ===\n\n"
        "Using 'secure_archive' to read from a nonexistent file:\n"
        f"{secure_archive('/not/existing/file', 'read', '')}"
        "\n\nUsing 'secure_archive' to read from an inaccessible file:\n"
        f"{secure_archive('/etc/master.passwd', 'read')}"
        "\n\nUsing 'secure_archive' to read from a regular file:\n"
        f"{secure_archive('ancient.txt', 'read')}"
        "\n\nUsing 'secure_archive' to write previous content to a new file:\n"
        f"{secure_archive('new.txt', 'write', 'Hello World')}"
    )
