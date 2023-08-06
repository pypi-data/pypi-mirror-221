from setuptools import setup


setup(
    name='salure_helpers_maxxton',
    version='0.0.2',
    description='Maxxton wrapper from Salure',
    long_description='Maxxton wrapper from Salure',
    author='D&A Salure',
    author_email='support@salureconnnect.com',
    packages=["salure_helpers.maxxton"],
    package_data={'salure_helpers.maxxton': ['templates/*']},
    license='Salure License',
    install_requires=[
        'salure-helpers-salureconnect>=1'
    ],
    zip_safe=False,
)