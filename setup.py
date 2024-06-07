from setuptools import setup, find_packages

setup(
    name='ScientificDataProcessing',
    version='0.1.0',
    description='A project for processing and analyzing scientific data.',
    author='Yuvraj Singh',
    author_email='rajbro34a@gmail.com',
    url='https://github.com/yourusername/yourproject',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'matplotlib',
        'jupyter',
    ],
    entry_points={
        'console_scripts': [
            'process_data=src.sourcecode:main',
        ],
    },
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)

