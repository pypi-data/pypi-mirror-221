import codefast as cf
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="premium",
    version=cf.generate_version(),
    author="sK9xTFBq0H",
    author_email="google@gmail.com",
    description="Python AI toolkits",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/",
    packages=setuptools.find_packages(),
    include_package_data=True,
    package_data={
     # And include any *.msg files found in the "hello" package, too:
        "premium": [
            'localdata/*.txt', 'localdata/*.pickle', 'localdata/*.mp3',
            'localdata/*.wav'
        ],
    },
    install_requires=[
        'smart-open', 'optuna', 'jieba', 'matplotlib', 'scikit-learn',
        'transformers', 'fasttext', 'classifiercluster', 'codefast', 'jiwer',
        'pandas', 'numpy', 'pytorch-lightning==1.7.7'
    ],
    entry_points={
        'console_scripts': ['demo=premium.demo:entry', 'zz=premium.zz:main'],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
