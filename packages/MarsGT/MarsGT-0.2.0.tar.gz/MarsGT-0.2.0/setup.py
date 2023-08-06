from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
setup(
    name="MarsGT",
    version='0.2.0',
    packages=find_packages(),
    install_requires=[
        'anndata==0.8.0',
        'dill==0.3.4',
        'matplotlib==3.5.1',
        'numpy==1.22.3',
        'pandas==1.4.2',
        'scipy==1.9.1',
        'seaborn==0.11.2',
        'scikit-learn==1.1.2',
        'torch-geometric==2.1.0.post1',
        'torchmetrics==0.9.3',
        'xlwt==1.3.0',
        'tqdm==4.64.0',
        'scanpy==1.9.1',
        'leidenalg==0.8.10',
        'ipywidgets==8.0.6'
    ],
    extras_require={
        # The following packages are not available on PyPI as binary wheels with CPU support.
        # Users must manually install them using the appropriate command:
        # "torch_sparse": ["torch-sparse==0.6.12+cpu"],
        # "torch_scatter": ["torch-scatter==2.0.9+cpu"],
        # "torch_cluster": ["torch-cluster==1.5.9+cpu"],
    },
    python_requires='>=3.8.0, <3.9',
    description="MarsGT: A Python library for rare cell identification (Internal testing only)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "License :: OSI Approved :: MIT License"
    ]
)