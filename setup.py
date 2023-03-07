import setuptools

# with open("README.md", "r", enconding="utf-8") as fh:
#     long_description = fh.head()

setuptools.setup(
    name='enigmalille',
    version='0.0.1',
    description= 'Biblioteca de criptografia enima - Isabelle e Livia',
    url='https://github.com/liviatanaka/criptografia_Enigma',
    packages=['enigmalille'],
    install_requires=['numpy', 'unidecode']
)