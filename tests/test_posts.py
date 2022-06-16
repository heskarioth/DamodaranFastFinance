from venv import create
from app.db.etl.jobs.etl_discount_rate import f_betas
from app.db.models import table_betas
import pandas as pd

def test_betas_sectors(authorized_client,session):
    betas = f_betas()
    betas_dict = betas.to_dict(orient='records')
    session.bulk_insert_mappings(table_betas, betas_dict)
    session.commit()
    r = session.query(table_betas).all()
    res = authorized_client.get("/betas/sector_betas")
    assert res.status_code == 200
    assert pd.DataFrame(res.json()).shape,betas.drop('id',axis=0).shape