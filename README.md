multi stage residual BCR-Net for microscopy deconvolution
==============================

# mrBCR-Net for microscopy deconvolution
## Solving the inverse problem of microscopy deconvolution with a residual Beylkin-Coifman-Rokhlin neural network

## Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------
## Paper link
this repo contains the code for the paper
(https://arxiv.org/abs/2407.03239)

## model pipeline
the pipeline of the proejct works as below:
![img](https://github.com/leeroyhannover/m-rBCR/blob/main/figs/pipe.png)

## test results
### biosr
test results on biosr:
![img](https://github.com/leeroyhannover/m-rBCR/blob/main/figs/biosr.png)

### simulated imagenet 
test results on simulated imagenet microscopy dataset
<div align=center>
<img src="https://github.com/leeroyhannover/m-rBCR/blob/main/figs/imn.png">
</div>

### real microscopy dataset dSTORM 
test results on real dSTORM microscopy dataset
![img](https://github.com/leeroyhannover/m-rBCR/blob/main/figs/dSTORM.png)

### real microscopy dataset confocal-widefield 
test results on real widefield-confocal micrscopy dataset
![img](https://github.com/leeroyhannover/m-rBCR/blob/main/figs/widefield_confocal.png)

all dataset is public avaibable online. please go to their original work to download the dataset.
For the widefield-confocal dataset we generated, please refer to this:
(https://rodare.hzdr.de/record/2668)