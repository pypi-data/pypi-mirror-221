from pathlib import Path
import tomllib as tl
import subprocess as sub

from typing import Self, List, Dict
from rich.console import Console
from rich.tree import Tree
from copy import copy
from zipfile import ZipFile as ZF
import os.path
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
import signal
import shutil
import requests as req
from zipfile import ZipFile as ZF
from io import BytesIO
from collections import OrderedDict
from functools import partial
from threading import Event
from typing import Iterable
from urllib.request import urlopen

from rich.progress import (
    BarColumn,
    DownloadColumn,
    Progress,
    TaskID,
    TextColumn,
    TimeRemainingColumn,
    TransferSpeedColumn,
    SpinnerColumn,
    TimeElapsedColumn
)

cout = Console()
cerr = Console(stderr=True)

__all__ = ['Config', 'error', 'log', 'ConfigFile', 'powershell', 'download', 'get_each']

Pkg = Path(__file__).parent
Root = Pkg.parent
Assets = Pkg / 'assets'
ConfigFile = Pkg / 'config.toml'



class Config:
    def __new__(cls) -> Self:
        cls.data = None
        cls.load()
        return cls
    @classmethod
    def load(cls):
        cls.data = tl.loads(ConfigFile.read_text())
    
    @classmethod        
    def render(cls):
        config = cls.data
        root = Tree("[bold red]🛠️ Configuration File[/bold red]")
        projects = root.add("[bold yellow]📦 Projects:[/bold yellow]")
        
        alias_list = config['aliases']
        
        for proot in config['projects']:
            node = projects.add(f"[magenta]🚀 {proot}[/magenta]")
            for project, aliases in alias_list.items():
                if project == proot:
                    for al in aliases:
                        node_alias = node.add(al)
                        node_alias.add(f"[underline yellow]Alias for `{proot}`.[/underline yellow]\n [dim]Use `[cyan]fr-pol-lots serve --project [red]{al}[/red][/cyan]` to launch")
        return root
    
    @classmethod
    def aliases(cls, include_name: bool = True):
        for name in cls.data['projects']:
            if include_name:
                yield name,name
            if name in cls.data['aliases']:
                for alias in cls.data['aliases'][name]:
                    yield name, alias
    
    @classmethod
    def find_project(cls, name: str) -> str:
        for project, alias in cls.aliases():
            if alias == name.lower():
                return project


def powershell(cmd: str):
    completed = sub.run(["powershell", "-Command", cmd], shell=True)

log = cout.log
error = cerr.log





progress = Progress(
    TextColumn("[bold blue]{task.fields[filename]}", justify="right"),
    BarColumn(bar_width=None),
    "[progress.percentage]{task.percentage:>3.1f}%",
    "•",
    DownloadColumn(),
    "•",
    TransferSpeedColumn(),
    "•",
    TimeRemainingColumn(),
)



spinner = Progress(
    SpinnerColumn(),
    TextColumn("[bold blue]{task.description}", justify="right"),
    BarColumn(bar_width=None),
    "[progress.percentage]{task.percentage:>3.1f}%",
    "•",
    TimeElapsedColumn(),
    "•",
    TimeRemainingColumn(),
)


done_event = Event()


def handle_sigint(signum, frame):
    done_event.set()


signal.signal(signal.SIGINT, handle_sigint)


def copy_url(task_id: TaskID, url: str, path: str, unpack: bool = True) -> None:
    """Copy data from a url to a local file."""
    response = urlopen(url)
    # This will break if the response doesn't contain content length
    progress.update(task_id, total=int(response.info()["Content-length"]))
    with open(path, "wb") as dest_file:
        progress.start_task(task_id)
        for data in iter(partial(response.read, 32768), b""):
            dest_file.write(data)
            
            progress.update(task_id, advance=len(data))
            if done_event.is_set():
                return
    if unpack:
        os.system(f'unzip {path}')
    progress.remove_task(task_id)
    return path

def download(urls: Iterable[str], dest_dir: str, workers: int = 10, unpack: bool = True):
    """Download multiple files to the given directory."""
    futures = []
    with progress:
        with ThreadPoolExecutor(max_workers=workers) as pool:
            for url in urls:
                filename = url.split("/")[-1]
                dest_path = os.path.join(dest_dir, filename)
                task_id = progress.add_task("download", filename=filename, start=True, total=None)
                ft = pool.submit(copy_url, task_id, url, dest_path, unpack)
                futures += [ft]
    
    for f in as_completed(futures):
        yield Path(f.result())
        
def get_url(task_id: TaskID, url:str):
    files = []
    res = req.get(url).content
    with ZF(BytesIO(res)) as zf:
        for f in zf.filelist:
            with zf.open(f.orig_filename) as extf:
                files += [extf.read()]
    spinner.remove_task(task_id)
    return files   
    

def get_each(urls: Iterable[str],  workers: int = 10):
    futures = []
    with spinner:
        with ThreadPoolExecutor(max_workers=workers) as pool:
            for url in urls:
                filename = url.split("/")[-1]
                task_id = spinner.add_task(f"Downloading {filename} ..", start=True)
                ft = pool.submit(get_url, task_id, url)
                futures += [ft]
    
    for f in as_completed(futures):
        yield from f.result()