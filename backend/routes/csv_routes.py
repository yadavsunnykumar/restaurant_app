from fastapi import APIRouter, HTTPException
from services.csv_services import get_csv_data,get_single_data_with_category,get_single_data_without_category
from utils.response_handler import handle_exception

router = APIRouter()

@router.get("/data", summary="Get CSV data", tags=["CSV"])
async def read_csv():
    """
    Reads CSV file and returns its contents as a list of dictionaries.
    """
    try:
        return get_csv_data()
    except Exception as e:
        raise HTTPException(status_code=500, detail=handle_exception(e))

@router.get("/data/{name}")
async def get_specific_data_without_category(name:str):
    return get_single_data_without_category(name)


@router.get("/data/")
async def get_specific_data_with_category(region:str):
    return get_single_data_with_category(region)