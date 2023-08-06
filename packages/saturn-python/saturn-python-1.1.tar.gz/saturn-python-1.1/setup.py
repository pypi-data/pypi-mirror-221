import re
from setuptools import setup

with open('saturn/version.py') as f:
    match = re.match(r'__version__ = [\'\"](.*?)[\'\"]', f.read())
    __version__ = match.group(1)

setup(
    name='saturn-python',
    version=__version__,
    description="Saturn allows to rerun python scripts skipping some places that were defined in previous runs.",
    author='Alexander Khlebushchev',
    packages=[
        'saturn',
    ],
    zip_safe=False,
    entry_points={
        'console_scripts': ['saturn=saturn.terminal:main'],
    },
)
