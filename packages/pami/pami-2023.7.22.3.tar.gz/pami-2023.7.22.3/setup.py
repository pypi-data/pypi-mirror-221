import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='pami',
    version='2023.07.22.3',
    url='https://github.com/udayLab/PAMI',
    license='GPLv3',
    install_requires=[            # All necessary packages utilized by our PAMI software
        'psutil',
        'pandas',
        'plotly',
        'matplotlib',
        'resource',
        'validators',
        'urllib3',
        'Pillow',
        'numpy',
    ],
    extras_require={
        'gpu':  ['cupy', 'pycuda'],
        'spark': ['pyspark'],
    },
    classifiers=[
        'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.5',
)
