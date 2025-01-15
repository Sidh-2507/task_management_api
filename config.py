import os

class Config:
    # Database configuration
    SQLALCHEMY_DATABASE_URI = 'postgresql://task_user:user123@localhost:5432/task_management_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Secret key for session management
    SECRET_KEY = '29c89d9ee6d47d0271724240f8023e63'
    JWT_SECRET_KEY = 'e82aa9f45c18be53593489ec2e5d24117d0d821c570901013683df5fa5dfad28'
    JWT_ACCESS_TOKEN_EXPIRES = 3600  # 1 hour

