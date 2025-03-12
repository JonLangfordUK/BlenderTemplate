import sys
from pathlib import Path
import toml

ROOT_DIR = Path(__file__).parent.parent.absolute()
SRC_DIR = ROOT_DIR / "src"

with open(ROOT_DIR / "pyproject.toml", "r", encoding="utf-8") as f:
    pyproject = toml.load(f)

print(pyproject)

project = pyproject["project"]["name"]

project_name = pyproject["project"]["name"]
authors = ", ".join(f"{author['name']} <{author['email']}>" for author in pyproject["project"]["authors"])
version = pyproject["project"]["version"]

print (authors)

extensions = [
    'sphinx.ext.autodoc',
    'sphinx_autodoc_typehints',
]

sys.path.insert(0, str(SRC_DIR))

templates_path = ['_templates']

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

variables_to_export = [
    "project_name",
    "authors",
    "version",
]

frozen_locals = dict(locals())
rst_epilog = '\n'.join(map(lambda x: f".. |{x}| replace:: {frozen_locals[x]}", variables_to_export))
del frozen_locals