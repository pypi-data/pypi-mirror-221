import click
import os
import yaml
import logging
import requests
import shutil
import traceback
import yaml
import uuid
import json
from io import StringIO
from pylint.lint import Run
from pylint.reporters.text import TextReporter
from zipfile import ZipFile
from typing import List
import zipfile
import glob

import junoplatform
from junoplatform.meta.decorators import auth

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s - %(message)s')
        
class CMDBase(object):
    def __init__(self):
        self.juno_dir = os.path.expanduser('~') + '/.juno'
        self.juno_file = self.juno_dir +  '/config.yaml'

@click.group()
@click.pass_context
def main(ctx, ):
    ctx.obj = CMDBase()

pass_base = click.make_pass_decorator(CMDBase)

@main.command()
@click.argument('name')
@click.argument('plant')
@click.argument('module')
@pass_base
@auth
def init(base, name, plant, module):
    '''create an algo module with project NAME
    '''
    home = os.path.dirname(junoplatform.__file__)
    src = f"{home}/templates/main.py"
    try:
        os.makedirs(name, exist_ok=False)
        shutil.copy2(src, name)
        doc = {"name": name, "version": "0.0.0", "author": os.getlogin(), "description": "template algo project", "plant": plant, "module": module}
        yaml.dump(doc, open(f"{name}/project.yml", "w"), sort_keys=False)
        input = {
            "tags": [
                "PLC1",
                "PLC2"
            ],
            "items": 1440,
            "interval": 5
        }

        json.dump(input, open(f"{name}/input.json", "w"), sort_keys=False)
    except Exception as e:
        msg = traceback.format_exc()
        logging.error(f"failed to create project {name}: {e}")

@main.command()
@click.argument('conf_file', required=False, default="")
@click.option('--input', help = "path of input spec file", default="input.json")
@click.option('--version', help='version')
@pass_base
@auth
def package(base, conf_file, input, version):
    ''' make a package and get a package id
    '''
    try:
        logging.info(f"TODO: package {conf_file} {input} {version}")
        lint = StringIO()  # Custom open stream
        reporter = TextReporter(lint)
        Run(["main.py"], reporter=reporter, exit=False)
        errors = lint.getvalue().split("\n")
        for x in errors:
            if "failed"  in x or "fatal" in x:
                logging.error(x)
                logging.info("fix the error above and redo package")
                exit(1)

        with open('project.yml', 'r') as f:
            s = yaml.safe_load(f)

        id = uuid.uuid4().hex
        s['id'] = id

        def parse_version(s:str) -> List[int]|None:
            v = s.split(".")
            if len(v) != 3:
                return None
            try:
                return [int(x) for x in v]
            except:
                return None

        if version and parse_version(version):
            s["version"] = version
        else: 
            if "version" not in s:
                s["version"] = "0.0.0"
            else:
                # rudelessly limit to 20*20*20 = 8000 versions, wow! my bad or wise?
                v:List[int] = parse_version(s["version"]) # type: ignore
                logging.debug(v)
                try:
                    v.reverse()
                    logging.debug(v)
                    for i in range(len(v)):
                        if v[i] > 20:
                            continue
                        v[i] += 1
                        for j in range(i):
                            v[j] = 0
                        break
                    v.reverse()
                    logging.debug(v)
                    s["version"] = ".".join([str(x) for x in v])
                except:
                    logging.error("invalid version format in project.yml. should be x.y.z and each less than 20")
                    exit(1)

        if conf_file:
            s['conf'] = conf_file
        logging.info(os.getcwd())
            
        with open('project.yml', 'w') as f:
            yaml.safe_dump(s, f, sort_keys=False)

        logging.info(f"pack success(new can be found in project.yml):\n\tplant: {s['plant']}, module: {s['module']}, conf: {conf_file}\n\tid: {id}\n\tversion: {s['version']}")

        # dist
        os.makedirs("dist", exist_ok=True)
        module = s['module']
        plant = s['plant']
        arch = f'dist/{plant}-{module}-{s["id"]}.zip'
        with zipfile.ZipFile(arch, 'w') as f:
            for root, dirs, files in os.walk('./'):
                if root[-4:] == 'dist':
                    continue
                for file in files:
                    p = os.path.join(root, file)
                    f.write(p)
                    logging.info(f"added: {p}")
        logging.info(f"package stored in: {arch}")

    except Exception as e:
        logging.error(e)

@main.command()
@pass_base
@auth
def run(base):
    '''run a package locally for testing
    '''
    os.system("python main.py")


@main.command()
@click.argument('id')
@pass_base
@auth
def deploy(base, id):
    '''deploy package
    '''
    logging.info(f"TODO: deploy {id}")


@main.command()
@click.argument('id')
@pass_base
@auth
def status(base, id):
    ''' check package status
    '''
    logging.info(f"TODO: status {id}")

@main.command()
@click.argument('plant')
@click.argument('module')
@click.argument('id', required=False)
@pass_base
@auth
def rollback(base, plant, module, id):
    '''rollback a package to previous version or specific id[optional]
    '''
    logging.info(f"TODO: rollback {plant} {module} {id}")

@main.command()
@click.argument('plant', required=False)
@pass_base
@auth
def list(base, plant):
    '''list packages and deployed status
    '''
    logging.info(f"TODO: list {plant}")

@main.command()
@click.argument('id')
@pass_base
@auth
def upload(base, id):
    '''upload a package
    '''
    logging.info(f"TODO: upload {id}")
    
@main.command()
@click.argument('username')
@click.argument('password', required=False)
@pass_base
def login(base:CMDBase, username, password):
    '''must login success before all other commands
    '''
    auth = {"username": username, "password": password}
    r = requests.post("https://report.shuhan-juno.com/api/token", data=auth, headers = {'Content-Type': 'application/x-www-form-urlencoded'})
    if r.status_code != 200:
        if 'detail' in r.json():
            detail = r.json()['detail']
            logging.error(f"login error: {detail}")
            return
        else:
            logging.error(f"login error: {r.status_code}")
    token = r.json()['access_token']
    data = {"auth": auth, "token": token}

    with open(base.juno_file, 'w') as f:
        f.write(yaml.dump(data)) 
    logging.info("successfully logged in")