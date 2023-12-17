from db.base_class import Base
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Date
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String)
    password = Column(String)
    name = Column(String)
    age = Column(Integer)
    gender = Column(String)
    height = Column(Float)
    weight = Column(Float)


class Cluster(Base):
    __tablename__ = 'clusters'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    description = Column(String)
    name = Column(String)


class UserClusterAssignment(Base):
    __tablename__ = 'user_cluster_assignments'

    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    cluster_id = Column(Integer, ForeignKey('clusters.id'), primary_key=True)
    assignment_date = Column(Date)

    user = relationship("UserModel", back_populates="cluster_assignments")
    cluster = relationship("ClusterModel", back_populates="users")


class Friends(Base):
    __tablename__ = 'friends'

    user_id_1 = Column(Integer, ForeignKey('users.id'), primary_key=True)
    user_id_2 = Column(Integer, ForeignKey('users.id'), primary_key=True)
    status = Column(String)
    start_date = Column(Date)


class Activity(Base):
    __tablename__ = 'activities'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    steps = Column(Integer)
    calories_burned = Column(Integer)
    date = Column(Date)


class UserChallengeStatus(Base):
    __tablename__ = 'user_challenge_statuses'

    unique_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    challenge_id = Column(Integer)
    status = Column(String)


class DailyChallenge(Base):
    __tablename__ = 'daily_challenges'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    description = Column(String)
    difficulty_level = Column(String)
    reward_points = Column(Integer)
    required_activity = Column(String)


class UserRewards(Base):
    __tablename__ = 'user_rewards'

    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    reward_id = Column(Integer, primary_key=True)
    date_earned = Column(Date)


class Achievements(Base):
    __tablename__ = 'achievements'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    description = Column(String)
    points = Column(Integer)