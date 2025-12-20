from pydantic import BaseModel , Field

class ip_features(BaseModel):
    Weight_kg: float
    Distance_km: float
    Provider_Blue_Dart: bool = False
    Provider_DTDC: bool = False
    Provider_Delhivery: bool = False
    Provider_India_Post: bool = False
    Provider_Private_Avg: bool = False


class output(BaseModel):
    Rate_per_kg_Rs : float


