from setuptools import setup, find_packages

setup(
    name = "dp_benchmark",
    version = "0.0.1",
    author = "littleRound",
    packages=find_packages('src', exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    package_dir={'': 'src'},
    install_requires=[
        "psutil",
        "numpy",
        "tinydb",
        "tqdm",
        "scipy",
        "diffprivlib==0.5.2",
        "python-dp==1.1.1",
        "opendp==0.5.0",
    ],
    entry_points={
        'console_scripts': [
            'dpbench_run = dp_benchmark.main:main',
            'dpbench_exp = dp_benchmark.experiments:main',
        ],
    },
)
