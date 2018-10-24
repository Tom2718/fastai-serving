# Serving Fastai Models

The aim of this project was to develop a minimal Django webapp that will allow you to serve a fastai model.

## Get started

Install dependencies using conda environment:

```sh
conda create -n "myEnv" python=3.6
conda activate myEnv
conda install -- file requirements.txt
```

Then run the webapp:

```sh
python manage.py runserver
```

## Structure

Put trained `.pth` models in `models/models`

Put dummy categories into `models/train` and `models/validate`. Test is not required.

Create `tmp` directory to store uploaded photos.