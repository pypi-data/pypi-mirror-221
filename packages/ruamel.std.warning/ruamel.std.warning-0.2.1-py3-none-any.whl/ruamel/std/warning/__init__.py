# coding: utf-8

from typing import Dict, Any

_package_data: Dict[str, Any] = dict(
    full_package_name='ruamel.std.warning',
    version_info=(0, 2, 1),
    __version__='0.2.1',
    version_timestamp='2023-07-26 14:07:05',
    author='Anthon van der Neut',
    author_email='a.van.der.neut@ruamel.eu',
    description='extend warnings.warn with callee parameter',
    keywords='pypi statistics',
    entry_points='warning=ruamel.std.warning.__main__:main',
    # entry_points=None,
    license='Copyright Ruamel bvba 2007-2023',
    since=2023,
    # status='α|β|stable',  # the package status on PyPI
    # data_files="",
    # universal=True,  # py2 + py3
    # install_requires=['ruamel.std.pathlib', ],
    tox=dict(env='3',),  # *->all p->pypy
    python_requires='>=3',
    mypy=False,
)  # NOQA


version_info = _package_data['version_info']
__version__ = _package_data['__version__']

########

import warnings as org_warnings  # NOQA


class CalleeWarning(Warning):
    pass


class ExtendedWarn:
    warn = org_warnings.warn

    def __call__(self, message, category=None, stacklevel=1, source=None, callee=None):
        if callee:
            assert stacklevel == 1
            if category is not None:
                filename = callee.__func__.__code__.co_filename
                lineno = callee.__func__.__code__.co_firstlineno
                message = CalleeWarning((message, filename, lineno, category))
        else:
            stacklevel += 1
        self.warn(message, category, stacklevel, source)  # NOQA


org_warnings.warn = ExtendedWarn()

_org_formatwarning = org_warnings.formatwarning


def my_formatwarning(message, category, filename, lineno, line):
    if isinstance(message, CalleeWarning):
        try:
            message, filename, lineno, category = message.args[0]
        except ValueError:  # in case there was no tuple provided
            pass
    return _org_formatwarning(message, category, filename, lineno, line)


org_warnings.formatwarning = my_formatwarning
