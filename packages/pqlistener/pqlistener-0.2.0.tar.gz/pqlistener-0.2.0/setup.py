from distutils.core import setup

setup(
    name='pqlistener',
    version='0.2.0',
    author='cordely',
    packages=['pqlistener'],
    package_dir={'': '.'},
    package_data={'': ['sub.dll', 'sub.so', 'sub-linux.so', 'sub-mac-m1.so']},
    description='python sub golang postgresql pub',
)