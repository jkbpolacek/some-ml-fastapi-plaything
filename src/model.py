#!/usr/bin/env python3


from typing import Optional, Literal, List
from pydantic import BaseModel


class Passenger(BaseModel):
    Pclass: Literal[1, 2, 3]
    Name: Optional[str]
    Sex: Literal["male", "female"]
    Age: float
    SibSp: int
    Parch: int
    Fare: float
    Embarked: Optional[Literal["S", "C", "Q"]]


clf = None
