import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='s1280247_learn2',
    version='2023.07.27',
    author='Tsubasa Yamauchi',
    author_email='s1280247@u-aizu.ac.jp',
    description='This ssoftware is being developd in the Python Class, University of Aizu.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    url='https://github.com/s1280247/s1280247_learn.git',
    license='GPLv3',
    install_requires=[
        'pandas',
        'plotly',
    ],
    extras_require={
        'gpu': ['cupy', 'pycuda'],
        'spark': ['pyspark'],
        'dev': ['twine', 'setuptools', 'build'],
        'all': ['cupy', 'pycuda', 'pyspark', 'twine', 'setuptools', 'build']
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    python_requiers='>=3.5',
)
