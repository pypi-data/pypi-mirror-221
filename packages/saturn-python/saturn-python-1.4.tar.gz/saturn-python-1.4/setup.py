import re
from setuptools import setup

with open('saturn/version.py') as f:
    match = re.match(r'__version__ = [\'\"](.*?)[\'\"]', f.read())
    __version__ = match.group(1)

def get_long_description():
    with open('README.md') as f:
        return f.read()

setup(
    name='saturn-python',
    version=__version__,
    description="Saturn allows to rerun python scripts skipping some places that were defined in previous runs.",
    author='Alexander Khlebushchev',
    packages=[
        'saturn',
    ],
    url="https://github.com/fomalhaut88/saturn",
    license="MIT",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    zip_safe=False,
    entry_points={
        'console_scripts': ['saturn=saturn.terminal:main'],
    },
)
