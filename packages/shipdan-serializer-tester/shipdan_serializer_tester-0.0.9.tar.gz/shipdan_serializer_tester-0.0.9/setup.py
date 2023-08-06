from setuptools import setup, find_packages

setup(
    name='shipdan_serializer_tester',
    version='0.0.9',
    description='for shipdan_application, shipdan_operation basic ModelSerializer field test',
    author='dare',
    author_email='gdare1999@gmail.com',
    url='https://github.com/G-D4R3/shipdan_serializer_tester.git',
    install_requires=['django',],
    packages=find_packages(exclude=[]),
    keywords=['dare', 'darever', 'bunkerkids', 'shipdan', 'pypi'],
    python_requires='>=3.9',
    package_data={},
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)