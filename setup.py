import os
import setuptools

with open(os.path.join('openvpn_resolver', 'resources', 'README.md')) as f:
    long_description = f.read()

with open(os.path.join('openvpn_resolver', 'resources', 'requirements.txt')) as f:
    install_requires = list(map(lambda s: s.strip(), f.readlines()))


_VERSION = '0.0.1'
_PACKAGE_NAME = 'openvpn_status_resolver'

setuptools.setup(
    name=_PACKAGE_NAME,
    version=_VERSION,
    description="Resolve hostnames to IPs in the input using OpenVPN status data.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[],
    author='Dustin Oprea',
    author_email='dustin@randomingenuity.com',
    packages=setuptools.find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    package_data={
        'ss': [
            'resources/README.md',
            'resources/requirements.txt',
            'resources/requirements-testing.txt',

            'resources/example/*',
        ],
    },
    install_requires=install_requires,
    scripts=[
        'openvpn_resolver/resources/scripts/osr_export',
    ],
)
