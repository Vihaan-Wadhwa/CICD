import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parents[1]))

from src.app import appdef 

def test_add():
    assert app.add(2, 3) == 5