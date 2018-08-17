from setuptools import setup

setup(
    name="timi-uuid",
    version="0.0.1",
    url='http://github.com/lxl0928/timi_uuid',
    author='Timi long',
    author_email='lixiaolong@smuer.cn',
    description='A sensible class for dealing with random UUID5 str',
    long_description=
"""
timi_uuid is a lightweight Python library for sensibly dealing with random UUID5. It allows you to create random UUID5 str in a variety of different ways. Take a look at `the docs <http://packages.python.org/timi-uuid>`_ for the interface.
""",
    packages=['timi_uuid'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)
