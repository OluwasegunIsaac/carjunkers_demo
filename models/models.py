from dataclasses import dataclass
from typing import List, Optional


@dataclass
class VehicleDTO:
    brand: str
    models: List[str]
    manufacturer: str
    years_in_production: Optional[List[str]]
