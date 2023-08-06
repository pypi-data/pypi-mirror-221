from setuptools import setup, find_packages

setup(
    name='mcptbr',
    version='0.1.6',
    packages=find_packages(),
    install_requires=[
        "mcpi", # Dependências necessárias para sua biblioteca (se houver).
    ],
    author='Lucas Pereira',
    author_email='lucasthe2@gmail.com',
    description='Biblioteca para manipular o Minecraft através do python.',
    readme = "README.md",
    #url='https://github.com/seu_usuario/minha_biblioteca',
    license='MIT',  # Substitua pela licença adequada.
)
