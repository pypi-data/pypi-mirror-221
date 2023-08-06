from setuptools import setup

with open('requirements.txt') as requirements:
    required = requirements.read().splitlines()

setup(
    name='stakepy',
    version='1.0.2',
    description='stakeの非公式簡易apiです',
    url='https://github.com/Sn4cy/stakepy',
    author='Sn4cy',
    author_email='info@gg.mail',
    license='GPL-3.0',
    keywords='stake api python',
    packages=[
        "stakepy",
    ],
    install_requires=required,
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.9',
    ],
)