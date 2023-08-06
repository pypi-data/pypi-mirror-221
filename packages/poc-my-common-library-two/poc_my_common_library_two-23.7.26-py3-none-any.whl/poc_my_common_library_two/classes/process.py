
class Process:
    def __init__(self):
        print('initiated from process.py')

    def info(self):
        return '/usr/bin/command -param value'

    def print_out(self, info: str):
        print(info)
