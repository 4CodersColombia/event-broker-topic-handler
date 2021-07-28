from distutils.core import setup
import setuptools


setup(
    name='topic_handler',
    version='0.0.1',
    include_package_data=True,
    description='Library to  management kafka topics with faust',
    author='Andres Gonzalez',
    author_email='andres@4coders.co',
    license="GPLv3",
    # use the URL to the github repo
    url='https://github.com/4CodersColombia/event-broker-topic-handler',
    download_url='https://github.com/4CodersColombia/firesql/tarball/tarball/0.1',
    keywords=['kafka', 'faust'],
    classifiers=['Programming Language :: Python :: 3.9', ],
    packages=setuptools.find_packages(),
    install_requires=[
        'KafkaProducer == 2.8.0',
        'betterproto == 1.2.5',
        'PyJWT == 1.7.1',
        'cryptography == "3.4.7"'
    ],
)
