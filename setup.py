from distutils.core import setup

with open('README.rst') as f:
    readme = f.read()

import os 

def copy_dir(path="./languages"):
    dir_path = path
    base_dir = os.path.join(path, dir_path)
    for (dirpath, dirnames, files) in os.walk(base_dir):
        for f in files:
            yield os.path.join(dirpath.split('/', 1)[1], f)

# folders_to_include = ["src", "languages", "samples"]

setup(
    name='urdu_python',
    version='1.1',
    packages=['urdu_python', 'urdu_python/src', 'urdu_python/src/filters'],
    # package_data = {
    #     '' : [f for f in copy_dir()]
    # },
    package_data={'':['languages/*/*.yaml']},
    # package_data = {'languages': './languages'},
    description='Simple example kernel for Jupyter',
    long_description=readme,
    author='Jupyter Development Team',
    author_email='jupyter@googlegroups.com',
    url='https://github.com/saadbazaz/UrduPython',
    install_requires=[
        'jupyter_client', 'IPython', 'ipykernel',

        # Custom dependencies
        'ply',
        'PyYAML',
        'Unidecode',
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
    ],
)
