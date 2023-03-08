# ProductivePy

ProductivePy is a productivity tool for Python developers that helps automate repetitive tasks and saves time.

## Installation

To install ProductivePy, run the following command:
- Install required modules.
```sh
$ pip3 install typer typing colorama prettytable secrets
```
- Clone the productivePy Github repository.
```bash
$ git clone "https://github.com/UltronTheAI/productivePy.git"
```
- Copy the productivePy.py file from ./productivePy/productivePy.py in to your project.
```bash
$ cp ./productivePy/productivePy.py "path to your project"
```
- Go to your project.
```bash
$ cd "Your project"
```
- Create new python file, and run it with ProductivePy.
```bash
$ python3 productivePy.py run $fileName
```

## Commands

ProductivePy supports the following commands:

- `run`: Run a Python file
- `re-run`: Re-run the last Python file that was run
- `status`: Show the status of running tasks
- `stop`: Stop a running task
- `stopAll`: Stop all running tasks

## Options

ProductivePy supports the following options:

- `--version`: Get the version of ProductivePy
- `--dealy`: Set a timeout for running a file after updating
- `--args`: Add arguments to the command used to run the file
- `--clear`: Clear the screen before re-running a file
- `--autostart`: Auto-restart a file after it ends

## Command and Options, Examples
- To run a python file.
```bash
$ python3 productivePy.py run $fileName
```
- Status
```bash
$ python3 productivePy.py status
```
- Re-run, you can get id, by running status command, or searching id from productivePy.json, file in your project dir.
```bash
$ python3 productivePy.py re-run $id
```
- Stop, this command takes id, to stop the running process.
```bash
$ python3 productivePy.py stop $id
```
- stopAll, this command will stop all running processes.
```bash
$ python3 productivePy.py stopAll
```
- `--clear` argument, this argument will clear your screen after your code re-runs, when updated.
```bash
$ python3 productivePy.py run $fileName --clear
```
- `--dealy`, this argument set up the dealy, between shifting from running file to re-run it.
```bash
$ python3 productivePy.py run $fileName --dealy 4
```
- `--autostart`, this argument, autostart's your running process, when it is finished.
```bash
$ python3 productivePy.py run $fileName --autostart
```
- `--args`, this argument add the extra args, => `python3 $fileName $args`
```bash
$ python3 productivePy.py run $fileName --args $args
```
## Website
```bash
https://ultrontheai.github.io/productivePy/
```
## Install productivePy, on linux
```bash
chmod +x install_on_linux.sh
```
```bash
./install_on_linux.sh
```
## Authors

- [@UltronTheAI](https://github.com/UltronTheAI)


## License

ProductivePy is released under the MIT License. See `LICENSE` for more information.
