from setuptools import setup, find_packages
from platform import python_version

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

## --- get release version ---
release_version = "unknown"
with open("chichicha/version.py") as f:
    line = f.read().strip()
    release_version = line.replace("version = ", "").replace('"', '')


setup(
    name="chichicha",
    version= release_version,
    author="chunglee_people",
    author_email="lschung@wpc.com.tw",
    url="https://github.com/WPC-Systems-Ltd/WPC_PyPI",
    packages=['chichicha'],
    include_package_data=True, ## True means it need MANIFEST.in files
    install_requires=['pyusb>=1.2.1', 'numpy>=1.23.0',
                      'qasync>=0.23.0', 'matplotlib>=3.5.2', 'qasync>=0.23.0',
                      'PyQt5>=5.15.4', 'PyQt5-Qt5>=5.15.2', 'PyQt5-sip>=12.10.1', 'wpcEXEbuild>=0.0.1'],

)
