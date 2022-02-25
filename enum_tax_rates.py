from enum import Enum

class Tax_Rates(float, Enum):
    UT = 0.685
    NV = 0.800
    TX = 0.625
    AL = 0.400
    CA = 0.825
