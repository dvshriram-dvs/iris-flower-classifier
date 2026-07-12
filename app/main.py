from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request

from app.schemas import IrisInput
from app.model import model, class_names

app = FastAPI()

# Static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# HTML templates
templates = Jinja2Templates(directory="app/templates")


from fastapi import Request

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@app.get("/health")
def health():
    return {"status":"healthy"}


@app.post("/predict")
def predict(data: IrisInput):

    features=[[
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]]

    prediction=model.predict(features)[0]
    probability=model.predict_proba(features)[0]

    return {
        "prediction":class_names[prediction],
        "confidence":round(max(probability)*100,2)
    }