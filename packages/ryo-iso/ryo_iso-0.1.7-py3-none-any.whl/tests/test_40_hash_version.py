import pytest
import os
import delegator
import shutil
import tempfile
import importlib
from pathlib import Path

def test_init(pytestconfig,request,data_path):
    import ryo_iso.cli

    with (data_path/'iso.yml').open('w') as f:
        f.write("""# test config file
image: ubuntu/22.04
arch: amd64
variant: desktop
apt:
  install:
    - git
    - python3-pip

pip:
  install:
    - doit
""")

    importlib.reload(ryo_iso.cli)
    ryo_iso.cli.cli(['_hash_version'])

    with (data_path/'.release_version').open('r') as f:
        image_version = f.read()
    assert(image_version == '22.04.2')

    with (data_path/'.hash').open('r') as f:
        image_hash = f.read()
    assert(image_hash == 'b98dac940a82b110e6265ca78d1320f1f7103861e922aa1a54e4202686e9bbd3')
