from fastapi import FastAPI, APIRouter, status



app = FastAPI()
router = APIRouter()


@router.get("/")
def get_risk_justifications():
    return "return all of the risk justification items"

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_risk_justification():
    return "create risk justification item"

@router.patch("/{risk_justificationId}")
def update_risk_justification(risk_justificationId: str):
    return f"update risk justification item with id: {risk_justificationId}"

@router.get('/{risk_justificationId}')
def get_risk_justification(risk_justificationId: str):
    return f"get risk justification item with id {risk_justificationId}"

@router.delete('/{risk_justificationId}')
def delete_risk_justification(risk_justificationId: str):
    return f"delete risk justification item with id {risk_justificationId}"


app.include_router(router, tags=['risk_justification'], prefix="/api/risk_justifications")


@app.get("/api/healthchecker")
def root():
    return {"message": "Healthly"}