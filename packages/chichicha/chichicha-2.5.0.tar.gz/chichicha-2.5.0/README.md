
## Installation
Open your own environment. (e.g. `myenv310` under miniconda)

Install `setuptools` & `wheel` & `twine` using `pip`:

```
$ pip install setuptools wheel twine
```

## Register PyPI account

Link: [https://pypi.org/](https://pypi.org/)

## Build .gz file

```
$ python setup.py sdist build
```

## Build .whl file

Build *.whl file in `\dist` folder by using setup.py

```
$ python setup.py bdist_wheel
```

## Upload whl file to PyPI

Upload *.whl file from `\dist` folder to PyPI platfrom. 

```
$ twine upload dist/*
```

## Log in PyPI platform.

WPC systems offical account
 
```
>>> User name: chungleepeople
>>> User password: wpc16071240
```

## Basic structure

#### File directory (before)
```
├── LICENSE
├── README.rst
├── chichicha
│   └── __init__.py
└── setup.py
```

## Add pyd file structure

You have to manually add all of pyd file from folder **chichicha** in `MANIFEST.in`.  

```
recursive-include chichicha *.pyd
```
#### File directory (after)
```
├── LICENSE
├── README.rst
├── chichicha
│   └── __init__.py
│   └── pywpc.pyd
└── setup.py
└── MANIFEST.in
```

## References

[Package python modules in PyPI ](https://medium.com/%E8%B3%87%E5%B7%A5%E7%AD%86%E8%A8%98/%E6%89%93%E5%8C%85python-module-%E5%88%B0pypi-%E4%B8%8A-aef1f73e1774)

[Include pyd files in Python Packages](https://stackoverflow.com/questions/37031456/include-pyd-files-in-python-packages)

