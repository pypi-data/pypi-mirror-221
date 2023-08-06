import logging
import os
import time
from pathlib import Path

import click
import coloredlogs

coloredlogs.install(level=logging.DEBUG)


def disable_logs():
    logging.getLogger('asyncio').disabled = True
    logging.getLogger('parso.cache').disabled = True
    logging.getLogger('parso.cache.pickle').disabled = True
    logging.getLogger('parso.python.diff').disabled = True
    logging.getLogger('humanfriendly.prompts').disabled = True
    logging.getLogger('blib2to3.pgen2.driver').disabled = True


def tunnel_local_port(port):
    execute(f'python3 -m pymobiledevice3 usbmux forward {port} {port} -d')


def execute(cmd):
    logging.debug(f'executing: {cmd}')
    return os.system(cmd)


@click.group()
def cli():
    pass


def start_remote(debug_port: int, ssh_port: int, process: str, hostname: str, rc_script: str):
    tunnel_local_port(debug_port)
    assert not execute(
        f'ssh -i ~/.ssh/id_rsa -p {ssh_port} root@{hostname} "debugserver 0.0.0.0:{debug_port} --attach={process}"&')

    # wait for it to load
    time.sleep(1)

    # connect local LLDB client
    commands = [f'process connect connect://{hostname}:{debug_port}',
                f'command script import {rc_script}']
    commands = '\n'.join(commands)
    execute(f'lldb --one-line "{commands}"')


@cli.command('remote')
@click.argument('process')
@click.argument('ssh_port', type=click.INT)
@click.option('--debug-port', type=click.INT, default=1234)
@click.option('--hostname', default='localhost')
def remote(process, ssh_port, debug_port, hostname):
    """ Start debugserver at remote device and connect using lldb """
    start_remote(debug_port, ssh_port, process, hostname,
                 os.path.join(Path(__file__).resolve().parent, "lldb_entrypoint.py"))


@cli.command('bare')
def bare():
    """ Just start an lldb shell """
    # connect local LLDB client
    commands = [f'command script import {os.path.join(Path(__file__).resolve().parent, "lldb_entrypoint.py")}']
    commands = '\n'.join(commands)
    execute(f'lldb --one-line "{commands}"')


@cli.command('attach')
@click.option('-n', '--name', help='process name to attach')
@click.option('-p', '--pid', type=click.INT, help='pid to attach')
def attach(name: str, pid: int):
    """ Attach to given process and start an lldb shell """
    # connect local LLDB client
    commands = []
    if name is not None:
        commands.append(f'process attach -n {name}')
    elif pid is not None:
        commands.append(f'process attach -p {pid}')
    else:
        print('missing either process name or pid for attaching')
        return

    commands.append(f'command script import {os.path.join(Path(__file__).resolve().parent, "lldb_entrypoint.py")}')
    commands = '\n'.join(commands)
    execute(f'lldb --one-line "{commands}"')


if __name__ == '__main__':
    disable_logs()
    cli()
