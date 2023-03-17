from typer import *  # Import typer.
from typing import *  # Import typing.
from prettytable import PrettyTable
import colorama  # Import the colorama.
import secrets
import time
import glob
import json
import subprocess
import os as cmd
import platform

colorama.init()  # Initialize colorama.
app = Typer()  # Initialize application.

config = {
    "config": {},
    "running": [],
    "ids": []
}

os = platform.system()
python = 'python' if os == 'Windows' else 'python3'


class Config:  # Configuration of the application.
    files = glob.glob('*')

    def __init__(self):  # Initializes the configuration.
        global config
        if 'productivePy.json' in self.files:
            with open('productivePy.json', 'r') as f:
                config = json.load(f)
                f.close()
        else:
            with open('productivePy.json', 'w') as f:
                f.write('{\n\t"config": {},\n\t"running": [],\n\t"ids": []\n}')
                f.close()

    def update(self, data):
        try:
            with open('productivePy.json', 'w') as f:
                f.write(json.dumps(data, indent=4))
                f.close()
        except:
            pass

    def get(self):
        data = None
        while True:
            try:
                with open('productivePy.json', 'r') as f:
                    data = json.load(f)
                    f.close()
                break
            except:
                pass
        return data


setup = Config()  # Config.


def cls():
    global os
    cmd.system(f'cls' if os == 'Windows' else f'clear')
    return


@app.command()
# Main entry point.
def main(
        version: Optional[bool] = Option(None, metavar='version',
                                         show_default=False, help='Get version of productivePy.'),
        command: Optional[str] = Argument(
            None, show_default=False, metavar='[ run/re-run/status/stop/stopAll ]', rich_help_panel='Commands', help='Commands.'),
        file: Optional[str] = Argument(None, show_default=False, rich_help_panel='Commands',
                                       metavar='file', help='Config file, to perform tasks.'),
        dealy: Optional[int] = Option(0, show_default=False, metavar='time',
                                      rich_help_panel='Commands', help='Time out for running file after updating.'),
        args: Optional[str] = Option('', show_default=False, metavar='args',
                                     rich_help_panel='Commands', help='Add args => \'$ python $file $args\''),
        clear: Optional[bool] = Option(0, show_default=False, metavar='clear-screen',
                                       rich_help_panel='Commands', help='Clear screen before re-run.'),
        autoStart: Optional[bool] = Option(0, show_default=False, metavar='auto-restart',
                                       rich_help_panel='Commands', help='Auto restart after program ende`s.'),
):
    global config, os, python
    if version:
        print('1.0.0')
        raise Exit()
    elif command:
        if command in ['run', 're-run']:
            if file:
                file = file if '.py' in file else config['config'][file][0]
                id = secrets.token_hex(5) if '.py' in file else file
                config['running'].append(str(id))
                config['ids'].append(str(id))
                config['config'][str(id)] = [file, 'running']
                setup.update(config)
                print(f'{colorama.Fore.LIGHTYELLOW_EX}[productivePy] 1.0.0')
                print(
                    f'{colorama.Fore.LIGHTYELLOW_EX}[productivePy] to restart at any time, fire `productivePy re-run $id` command in terminal')
                print(
                    f'{colorama.Fore.LIGHTYELLOW_EX}[productivePy] watching path(s): *.*')
                print(
                    f'{colorama.Fore.LIGHTYELLOW_EX}[productivePy] watching extensions: py')
                print(
                    f'{colorama.Fore.LIGHTGREEN_EX}[productivePy] starting ` {python} "{file}" `{colorama.Fore.WHITE}')
                try:
                    exe = subprocess.Popen([python, file, args])
                    code = open(file, 'r').read()
                    repeat = 0
                    rs = 0

                    while id in config['running']:
                        time.sleep(dealy)
                        newCode = open(file, 'r').read()
                        config = setup.get()

                        if code != newCode:
                            code = newCode
                            del newCode

                            if clear:
                                cls()
                            if repeat == 0:
                                repeat += 1
                            else:
                                repeat -= 1
                                rs -= 1
                                print(
                                    f'{colorama.Fore.LIGHTGREEN_EX}[productivePy] restarting due to changes...')
                                print(
                                    f'{colorama.Fore.LIGHTGREEN_EX}[productivePy] starting ` {python} "{file}" `{colorama.Fore.LIGHTWHITE_EX}')
                                exe.terminate()
                                exe = subprocess.Popen([python, file, args])
                        elif exe.poll() == 0 and rs == 0:
                            rs += 1
                            print(
                                f'{colorama.Fore.LIGHTGREEN_EX}[productivePy] clean exit - waiting for changes before restart...')
                            if autoStart:
                                repeat -= 1
                                rs -= 1
                                print(
                                    f'{colorama.Fore.LIGHTGREEN_EX}[productivePy] restarting due to changes...')
                                print(
                                    f'{colorama.Fore.LIGHTGREEN_EX}[productivePy] starting ` {python} "{file}" `{colorama.Fore.LIGHTWHITE_EX}')
                                exe.terminate()
                                exe = subprocess.Popen([python, file, args])
                        else:
                            pass

                    print(
                        f'{colorama.Fore.LIGHTGREEN_EX}[productivePy] clean exit...')
                except:
                    config['running'].remove(id)
                    config['config'][id] = [file, 'stoped']
                    setup.update(config)
                    print(
                        f'{colorama.Fore.LIGHTGREEN_EX}[productivePy] clean exit...')

            else:
                raise Exception("Invalid file.")
        elif command == 'status':
            if clear:
                config = {
                    "config": {},
                    "running": [],
                    "ids": []
                }
                setup.update(config)
            else:
                table = PrettyTable()
                table.field_names = ['No.', 'ID', 'File', 'Status']
                no = 0
                for out in config['ids']:
                    no += 1
                    table.add_row([no, out, config['config'][out]
                                   [0], config['config'][out][1]])
                print(table)
        elif command == 'stop':
            config['running'].remove(file)
            setup.update(config)
        elif command == 'stopAll':
            config['running'] = []
            setup.update(config)
        else:
            raise Exception("Invalid command.")


if __name__ == '__main__':  # Initialize.
    app()  # Initialize the application.
 
