from poc_my_common_library.classes.shell import Shell
from poc_my_common_library_two.classes.process import Process


def main():
    print('main from poc-my-tool-one')
    shell = Shell()
    _, output = shell.run('du -h')
    process = Process()
    process.print_out(output)


if __name__ == '__main__':
    main()
