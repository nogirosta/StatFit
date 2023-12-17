from datetime import date
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from datetime import date
from typing import Optional, Generic, TypeVar
from pydantic.generics import GenericModel
from pydantic import BaseModel


T = TypeVar('T')


class Request(GenericModel, Generic[T]):
	parameter: Optional[T] = Field(...)


class Response(GenericModel, Generic[T]):
	code: str
	status: str
	message: str
	result: Optional[str]


# Define Pydantic models for the database
class User(BaseModel):
	id: int = Field(..., alias='UserID')
	name: str
	age: Optional[int]
	gender: Optional[str]
	height: Optional[float]
	weight: Optional[float]

	class Config:
		orm_mode = True


class Cluster(BaseModel):
	id: int = Field(..., alias='ClusterID')
	description: Optional[str]
	name: str

	class Config:
		orm_mode = True


class UserClusterAssignment(BaseModel):
	user_id: int = Field(..., alias='UserID')
	cluster_id: int = Field(..., alias='ClusterID')
	assignment_date: date

	class Config:
		orm_mode = True


class Friends(BaseModel):
	user_id_1: int = Field(..., alias='UserID_1')
	user_id_2: int = Field(..., alias='UserID_2')
	status: Optional[str]
	start_date: Optional[date]

	class Config:
		orm_mode = True


class Activity(BaseModel):
	id: int = Field(..., alias='ActivityID')
	user_id: int = Field(..., alias='UserID')
	steps: Optional[int]
	calories_burned: Optional[int]
	date: Optional[date]

	class Config:
		orm_mode = True


class UserChallengeStatus(BaseModel):
	unique_id: int = Field(..., alias='UniqueID')
	user_id: int = Field(..., alias='UserID')
	challenge_id: int = Field(..., alias='ChallengeID')
	status: Optional[str]

	class Config:
		orm_mode = True


class DailyChallenge(BaseModel):
	id: int = Field(..., alias='ChallengeID')
	description: str
	difficulty_level: Optional[str]
	reward_points: Optional[int]
	required_activity: Optional[str]

	class Config:
		orm_mode = True


class UserRewards(BaseModel):
	user_id: int = Field(..., alias='UserID')
	reward_id: int = Field(..., alias='RewardID')
	date_earned: date

	class Config:
		orm_mode = True


class Achievements(BaseModel):
	unique_id: int = Field(..., alias='UniqueID')
	name: str
	rarity: Optional[str]
	description: Optional[str]

	class Config:
		orm_mode = True
