from setuptools import setup

setup(name='tecton_utils',
            version='0.0.1',
            description='[private preview] Utils for Tecton',
            author='Tecton',
            packages=['tecton_utils'],
            license="Apache License 2.0",
            install_requires=[
                "pyspark",
                "tecton",
            ],
            setup_requires=["setuptools", "wheel"],
            url="https://tecton.ai",
            python_requires=">=3.7",
           )
