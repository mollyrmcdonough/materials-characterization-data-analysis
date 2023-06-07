import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='mcda',
    author='Molly McDonough',
    author_email='mrm6464@psu.edu',
    description='Materials Characterization Data Analysis',
    keywords='materials science, data analysis',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='',
    project_urls={
        'Documentation': '',
        'Bug Reports':
        '',
        'Source Code': '',
        # 'Funding': '',
        # 'Say Thanks!': '',
    },
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    classifiers=[
        # see https://pypi.org/classifiers/
        'Development Status :: 2 - Pre-Alpha',

        'Intended Audience :: Scientists and Engineers',
        'Topic :: Materials Science :: Data Analysis',
        'Programming Language :: Python :: 3.11.3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    # install_requires=['Pillow'],
    extras_require={
        'dev': ['check-manifest'],
        # 'test': ['coverage'],
    },
    # entry_points={
    #     'console_scripts': [  # This can provide executable scripts
    #         'run=mcda:main',
    # You can execute `run` in bash to run `main()` in src/mcda/__init__.py
    #     ],
    # },
)
