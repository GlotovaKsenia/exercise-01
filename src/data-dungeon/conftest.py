import subprocess
import sys

import pytest


@pytest.fixture
def here(request):
    return request.node.path.parent


@pytest.fixture
def run_script():
    def run(script, inputs=()):
        result = subprocess.run(
            [sys.executable, str(script)],
            input="\n".join(inputs) + ("\n" if inputs else ""),
            capture_output=True,
            check=True,
            cwd=script.parent,
            text=True,
        )
        return result.stdout

    return run
