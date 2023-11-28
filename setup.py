import setuptools

setuptools.setup(
    name="Translator for 2048 game",
    version="0.0.1",
    author="Kamil",
    description="Translator for 2048 game",
    packages=setuptools.find_packages(),
    python_requires=">=3.10",
    py_modules=["translator"],
    install_requires=open("requirements.txt").read().splitlines(),
    package_dir={"": "."},
)