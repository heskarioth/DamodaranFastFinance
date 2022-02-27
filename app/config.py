import os, sys

#import sys
#sys.path.append(".")
from pydantic import BaseSettings
from typing import List
class etlSettings(BaseSettings):
    inshold : str #= 'https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/inshold.html'
    histretSP : str
    histimpl : str
    wcdata : str
    roe : str
    fundgr : str
    histgr : str
    fundgrEB : str
    finflows : str
    margin : str
    goodwill : str
    r_d : str
    capex: str
    divfcfe : str
    divfund : str
    macro : str
    dbtfund : str
    debtdetails : str
    leaseeffect : str
    wacc : str
    totalbeta : str
    ctryprem : str
    betas : str
    countrytaxrates : str
    taxrate : str
    ref_industry_names : str
    ref_bonds : str

    class Config:
        env_file = "etl.env"


etl_settings = etlSettings()


class databaseSettings(BaseSettings):
    database_hostname: str
    database_port : str
    database_username : str
    database_password : str
    database_name : str
    secret_key : str 
    access_token_expire_minutes : int 
    class Config:
        env_file = "./db.env"

database_settings = databaseSettings()

class otherSettings(BaseSettings):
    algorithm : str
    secret_key : str
    access_token_expire_minutes  : int

    class Config:
        env_file = "./db.env"

other_settings = otherSettings()



