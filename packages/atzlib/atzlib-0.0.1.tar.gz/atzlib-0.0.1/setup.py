from setuptools import setup, find_packages

setup(
    name='atzlib',
    version='0.0.1',
    description='Bunch of small python tools.',
    author='jhlee29',
    author_email='leejinha829@gmail.com',
    url='https://github.com/xinagand/atzlib.git',
    install_requires=[],
    packages=find_packages(exclude=[]),
    keywords=['jhlee29', 'python'],
    python_requires='>=3.6',
    package_data={},
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)