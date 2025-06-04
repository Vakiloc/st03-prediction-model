from dataclasses import dataclass

from typing import Optional, List


PREDICTOR_COLUMNS: List[str] = [
    'ENTRY_ID', 'ACCOUNT', 'COUNT', 'COMMITTI', 'DBPROCTI', 'READDIRTI',
    'READSEQTI', 'CHNGTI', 'PROCTI', 'CPUTI', 'QUEUETI', 'ROLLWAITTI',
    'GENERATETI', 'REPLOADTI', 'CUALOADTI', 'DYNPLOADTI', 'QUETI', 'DDICTI',
    'CPICTI', 'LOCKTI', 'INSTI', 'UPDTI', 'DELTI', 'ROLLINTI', 'ROLLOUTTI',
    'FIRSTRECTI', 'LASTRECTI', 'ELAPSEDTI', 'ROLLTI', 'LOADGENTI', 'DBTI',
    'EXECUTION_TI', 'DATA_SEND_TI', 'DATA_RECEIVE_TI', 'LOGON_TI',
    'AUTHORIZATION_TI',
]

TARGET_COLUMN = 'RESPTI'


@dataclass
class PerformanceRecord:
    """Data model for performance metrics.

    Predictor and target variables for linear regression.
    """
    # Predictor variables
    ENTRY_ID: str
    ACCOUNT: str
    COUNT: int
    COMMITTI: float

    # Target variable
    RESPTI: float

    DBPROCTI: Optional[float] = None
    READDIRTI: Optional[float] = None
    READSEQTI: Optional[float] = None
    CHNGTI: Optional[float] = None
    PROCTI: Optional[float] = None
    CPUTI: Optional[float] = None
    QUEUETI: Optional[float] = None
    ROLLWAITTI: Optional[float] = None
    GENERATETI: Optional[float] = None
    REPLOADTI: Optional[float] = None
    CUALOADTI: Optional[float] = None
    DYNPLOADTI: Optional[float] = None
    QUETI: Optional[float] = None
    DDICTI: Optional[float] = None
    CPICTI: Optional[float] = None
    LOCKTI: Optional[float] = None
    INSTI: Optional[float] = None
    UPDTI: Optional[float] = None
    DELTI: Optional[float] = None
    ROLLINTI: Optional[float] = None
    ROLLOUTTI: Optional[float] = None
    FIRSTRECTI: Optional[int] = None
    LASTRECTI: Optional[int] = None
    ELAPSEDTI: Optional[float] = None
    ROLLTI: Optional[float] = None
    LOADGENTI: Optional[float] = None
    DBTI: Optional[float] = None
    EXECUTION_TI: Optional[float] = None
    DATA_SEND_TI: Optional[float] = None
    DATA_RECEIVE_TI: Optional[float] = None
    LOGON_TI: Optional[float] = None
    AUTHORIZATION_TI: Optional[float] = None
