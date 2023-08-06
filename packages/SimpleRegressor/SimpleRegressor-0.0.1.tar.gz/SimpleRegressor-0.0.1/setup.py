from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

with open('HISTORY.md') as history_file:
    HISTORY = history_file.read()


setup_args = dict(
    name='SimpleRegressor',
    version='0.0.1',
    description='Simple Forest model',
    long_description_content_type="text/markdown",
    long_description=README + '\n\n' + HISTORY,
    packages=find_packages(),
    package_data={'': ['*.pkl']},
    author='Kishore',
    author_email='kishore.k.22032002@gmail.com',
    url='https://github.com/kishorekaruppusamy/SimpleRegressor',
    download_url='https://pypi.org/project/SimpleRegressor/'
)

if __name__ == '__main__':
    setup(**setup_args)