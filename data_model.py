from dataclasses import dataclass
from typing import Optional

@dataclass
class PerformanceRecord:
    """Data model for performance metrics.

    Predictor and target variables for linear regression.
    """
    # Predictor variables
    entry_id: str
    account: str
    count: int
    committi: float
    dbprocti: Optional[float] = None
    readdirti: Optional[float] = None
    readseqti: Optional[float] = None
    chngti: Optional[float] = None
    procti: Optional[float] = None
    cputi: Optional[float] = None
    queueti: Optional[float] = None
    rollwaitti: Optional[float] = None
    generateti: Optional[float] = None
    reploadti: Optional[float] = None
    cualoadti: Optional[float] = None
    dynploadti: Optional[float] = None
    queti: Optional[float] = None
    ddicti: Optional[float] = None
    cpicti: Optional[float] = None
    lockti: Optional[float] = None
    insti: Optional[float] = None
    updti: Optional[float] = None
    delti: Optional[float] = None
    rollinti: Optional[float] = None
    rolloutti: Optional[float] = None
    firstrecti: Optional[int] = None
    lastrecti: Optional[int] = None
    elapsedti: Optional[float] = None
    rollti: Optional[float] = None
    loadgenti: Optional[float] = None
    dbti: Optional[float] = None
    execution_ti: Optional[float] = None
    data_send_ti: Optional[float] = None
    data_receive_ti: Optional[float] = None
    logon_ti: Optional[float] = None
    authorization_ti: Optional[float] = None

    # Target variable
    respti: float
