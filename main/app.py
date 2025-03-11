from fastapi import FastAPI, File, UploadFile, HTTPException
from typing import List, Dict

from .services import load_ad_platforms, search_ad_platforms

app = FastAPI()

# In-memory storage для рекламных площадок
ad_platforms: Dict[str, List[str]] = {}


@app.post("/upload/", summary="Загрузить данные о рекламных площадках", description="Загружает данные из файла и обновляет in-memory коллекцию.")
async def upload_file(file: UploadFile = File(..., description="Файл с данными о рекламных площадках.")):
    """
    Загружает данные из файла и обновляет in-memory коллекцию.
    """
    global ad_platforms
    content = await file.read()
    ad_platforms = load_ad_platforms(content.decode('utf-8'))
    return {"message": "File uploaded successfully"}


@app.get("/search/", summary="Поиск рекламных площадок", description="Ищет рекламные площадки для заданной локации.")
async def search(location: str = "Локация для поиска рекламных площадок."):
    """
    Ищет рекламные площадки для заданной локации.

    :param location: Локация, для которой нужно найти площадки.
    :return: Список рекламных площадок для заданной локации.
    """

    if not ad_platforms:
        raise HTTPException(status_code=400, detail="No data loaded. Please upload a file first.")
    platforms = search_ad_platforms(ad_platforms, location)
    return {"platforms": platforms}
