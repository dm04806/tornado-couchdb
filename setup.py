from setuptools import setup

setup(name='tornado-couchdb',
      version='0.1.0',
      description="Blocking and non-blocking (asynchronous) clients for CouchDB using Tornado's httpclient",
      author='Jacob Sondergaard',
      author_email='jacob@nephics.com',
      license="MIT License",
      url='https://bitbucket.org/nephics/tornado-couchdb',
      packages=['couch'],
      requires=['tornado(>=2.4)']
)