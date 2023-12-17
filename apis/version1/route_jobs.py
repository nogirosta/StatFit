from fastapi import APIRouter
from fastapi import FastAPI, File, UploadFile
from ml_part.prediction_func import predict_label
import pandas as pd
import io

router = APIRouter()


async def read_csv(upload_file: UploadFile):
	contents = await upload_file.read()
	df = pd.read_csv(io.BytesIO(contents))
	return df


@router.post("/upload-file")
async def upload_file(file: UploadFile = File(...)):
	df = await read_csv(file)
	# Process the file and calculate fitness score
	score, recommendations = predict_label(pure_input_data=df)
	return {"fitness_score": score,
	        "challenge": recommendations}
