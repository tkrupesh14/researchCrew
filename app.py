from fastapi import FastAPI, Query
from crew import ResearchCrew

app = FastAPI()
crew = ResearchCrew()

@app.get("/analyze")
def analyze(url: str = Query(..., description="URL to analyze")):
    return crew.process(url)
