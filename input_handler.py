import sys

try: 
    # for Windows
    import msvcrt

    def get_key():
        return msvcrt.getch().decode("utf-8")

except ImportError:
    # for Unix/macOS/Linux
    import tty
    import termios

    def get_key():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            return sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)