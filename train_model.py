
import sqlite3
import sys
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from data_model import PerformanceRecord, PREDICTOR_COLUMNS, TARGET_COLUMN

def load_data(db_path: str, table: str = 'HITLIST_RESPTIME') -> pd.DataFrame:
    """Load dataset from a SQLite database.

    Only columns that actually exist in the table will be selected. This makes
    the training script more robust to schema differences across databases.
    """
    conn = sqlite3.connect(db_path)

    # Retrieve column names from the table
    cursor = conn.execute(f"PRAGMA table_info({table})")
    table_columns = {row[1].upper() for row in cursor.fetchall()}

    # Ensure the target column exists
    if TARGET_COLUMN.upper() not in table_columns:
        raise ValueError(f"Target column {TARGET_COLUMN} not found in table {table}")

    selected_predictors = [c for c in PREDICTOR_COLUMNS if c.upper() in table_columns]
    query_columns = selected_predictors + [TARGET_COLUMN]
    query = f"SELECT {', '.join(query_columns)} FROM {table}"
    df = pd.read_sql_query(query, conn)
    conn.close()

    return df

def train_linear_regression(df: pd.DataFrame) -> LinearRegression:
    """Train a linear regression model for response time prediction."""
    feature_columns = [c for c in PREDICTOR_COLUMNS if c in df.columns]
    X = df[feature_columns]
    y = df[TARGET_COLUMN]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Test MSE: {mse:.2f}")
    return model

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python train_model.py <database_path> [table]")
        sys.exit(1)

    db_path = sys.argv[1]
    table = sys.argv[2] if len(sys.argv) > 2 else 'HITLIST_RESPTIME'

    df = load_data(db_path, table)
    model = train_linear_regression(df)
