# ST03 Prediction Model


This repository contains a minimal example for predicting SAP workload response
time using linear regression. The data model is defined in `data_model.py` and
training logic in `train_model.py`.

## Setup

It is recommended to create a dedicated Python virtual environment before
installing the dependencies. Run the following commands from the repository
root:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Running

The training script expects a SQLite database containing the performance
tables. It automatically selects all predictor columns that exist in the
database table and will one-hot encode any categorical columns. Assuming the
database is called `performance_data.sqlite`, run:

```bash
python train_model.py performance_data.sqlite

```
