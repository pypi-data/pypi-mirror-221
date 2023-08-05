from pydantic import BaseModel
from typing import List

from .TrackingId import TrackingId

from .OperationalDetail import OperationalDetail


class CompletedPackageDetail(BaseModel):
    sequenceNumber: int
    trackingIds: List[TrackingId]
    groupNumber: int
    signatureOption: str
    operationalDetail: OperationalDetail