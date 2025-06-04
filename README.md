# ST03 Prediction Model


This repository contains a minimal example for predicting SAP workload response
time using linear regression. The data model is defined in `data_model.py` and
training logic in `train_model.py`.

The training script expects a SQLite database containing the performance
tables. Assuming the database is called `performance_data.sqlite`, run:

```bash
python train_model.py performance_data.sqlite

```
