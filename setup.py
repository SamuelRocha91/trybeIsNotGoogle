from setuptools import setup

setup(
    name="ting",
    description="Projeto ting",
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    packages=["ting_file_management", "ting_word_searches"],
)
