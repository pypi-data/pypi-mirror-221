from setuptools import setup

setup(
    name='furs_fiscalization',
    packages=['furs_fiscalization'],
    version='0.8.1',
    license='MIT',
    description='Python library for simplified communication with FURS (Financna uprava Republike Slovenije).',
    author='Hermes d.o.o.',
    author_email='info@hermes-solutions.si ',
    url='https://github.com/HermesGH/furs-fiscalization',
    download_url='https://github.com/HermesGH/furs-fiscalization/archive/v0.7.0.zip',
    keywords=['FURS', 'fiscal', 'fiscal register', 'davcne blagajne'],
    classifiers=[],
    package_data={'furs_fiscalization': ['certs/*.pem']},
    install_requires=[
        'pytz>=2017.2',
        'requests>=2.20.0',
        'python-jose>=3.1.0',
        'pyOpenSSL>=17.5.0',
    ]
)
