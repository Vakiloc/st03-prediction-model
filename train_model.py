import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from data_model import PerformanceRecord

# Columns used as predictors
PREDICTOR_COLUMNS = [
    'ENTRY_ID', 'ACCOUNT', 'COUNT', 'COMMITTI', 'DBPROCTI', 'READDIRTI',
    'READSEQTI', 'CHNGTI', 'PROCTI', 'CPUTI', 'QUEUETI', 'ROLLWAITTI',
    'GENERATETI', 'REPLOADTI', 'CUALOADTI', 'DYNPLOADTI', 'QUETI', 'DDICTI',
    'CPICTI', 'LOCKTI', 'INSTI', 'UPDTI', 'DELTI', 'ROLLINTI', 'ROLLOUTTI',
    'FIRSTRECTI', 'LASTRECTI', 'ELAPSEDTI', 'ROLLTI', 'LOADGENTI', 'DBTI',
    'EXECUTION_TI', 'DATA_SEND_TI', 'DATA_RECEIVE_TI', 'LOGON_TI',
    'AUTHORIZATION_TI'
]

TARGET_COLUMN = 'RESPTI'

def load_data(csv_path: str) -> pd.DataFrame:
    """Load dataset from a CSV file."""
    df = pd.read_csv(csv_path)
    return df

def train_linear_regression(df: pd.DataFrame) -> LinearRegression:
    """Train a linear regression model for response time prediction."""
    X = df[PREDICTOR_COLUMNS]
    y = df[TARGET_COLUMN]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Test MSE: {mse:.2f}")
    return model

if __name__ == "__main__":
    df = load_data('performance_data.csv')
    model = train_linear_regression(df)
