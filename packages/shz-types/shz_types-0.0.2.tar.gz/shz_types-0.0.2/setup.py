from setuptools import setup, find_packages

with open("README.md", "r") as arq:
    readme = arq.read()

project_name = 'shz_types'

setup(name=project_name,
      version='0.0.2',
      license='MIT License',
      author='Eliseu Brito',
      long_description=readme,
      long_description_content_type="text/markdown",
      author_email='eliseubrito776@gmail.com',
      keywords='shz types shztypes shz_types',
      description=u'Personal types for my projects',
      packages=find_packages(),
      install_requires=['numpy==1.25.1', 'pandas==2.0.3'], )
