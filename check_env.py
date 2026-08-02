import sys
import platform
import subprocess


def check_python():
    print("Python version:", sys.version.split()[0])


def check_os():
    print("Platform:", platform.system())


def check_path():
    print("Python executable:", sys.executable)


def check_processor():
    print("Processor:", platform.processor())


def check_machine():
    print("Machine:", platform.machine())


def check_docker():
    try:
        result = subprocess.run(
            ["docker", "--version"],
            capture_output=True,
            text=True,
        )

        print("Docker version:", result.stdout.strip())

        # Uncomment these for debugging:
        # print(result)
        # print("Docker error:", result.stderr.strip())
        # print("Return code:", result.returncode)

    except FileNotFoundError:
        print("Docker is not installed or not found in PATH.")


def check_gpu():
    print("GPU: Not set up yet")


def main():
    check_python()
    check_os()
    check_path()
    check_processor()
    check_machine()
    check_docker()
    check_gpu()


if __name__ == "__main__":
    main()
