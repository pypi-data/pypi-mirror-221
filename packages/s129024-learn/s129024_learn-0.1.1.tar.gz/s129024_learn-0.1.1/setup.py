import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='s129024_learn',
    version='0.1.1',
    author='Yuga Hanyu',
    author_email='s1290224@u-aizu.ac.jp',
    description='This software is being developed at the University of Aizu, Aizu-Wakamatsu, Fukushima, Japan',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    url='https://github.com/s1290224/s1290224_learn.git',
    license='GPLv3',
    install_requires=[
        'pandas',
        'plotly',
        'pami',
    ],
    extras_require={
        'gpu': ['cupy', 'pycuda'],
        'spark': ['pyspark'],
        'dev': ['twine', 'setuptools'],
        'all': ['cupy', 'pycuda', 'pyspark', 'twine', 'setuptools'],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.5',
)
