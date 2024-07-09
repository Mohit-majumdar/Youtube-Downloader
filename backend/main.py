from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.download import router as DownloadRouter


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(DownloadRouter, prefix="")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", reload=True)
