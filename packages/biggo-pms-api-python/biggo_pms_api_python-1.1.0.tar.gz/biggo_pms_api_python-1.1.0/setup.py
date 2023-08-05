from distutils.core import setup
from pathlib import Path
from setuptools import find_packages

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='biggo_pms_api_python',
    version='1.1.0',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    requires=['requests', 'base64', 'time', 'json', 'os', 'datetime'],
)
