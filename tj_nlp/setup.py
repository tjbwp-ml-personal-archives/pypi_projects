from setuptools import setup, find_packages

setup(
    name='tj_preproc',
    version='0.0.2',
    license='MIT',
    author="Tariq Jamil",
    author_email='tariqjamil.bwp@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/pypi_projects/tj_nlp/',
    keywords='tjtext_preproc_ds',
    install_requires=[
          'unidecode',
          'nltk',
          'autocorrect',
          'bs4',
          'pandas',
          'numpy',
          'tqdm',
      ],
)