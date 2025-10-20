from typing import Dict
from schemas.dummy_schema import Dummy

_Dummies: Dict[str, Dummy] = {
    "1": Dummy(id="1", name="Sample A", description="A sample item"),
    "2": Dummy(id="2", name="Sample B", description="B sample item"),
    "3": Dummy(id="3", name="Sample C", description="C sample item")
}