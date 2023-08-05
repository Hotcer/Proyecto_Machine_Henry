
from fastapi import FastAPI, Response

app = FastAPI()

@app.get("/")
async def root():
    """
    Root endpoint for the Steam Games API.
    Returns a HTML response with a centered heading.
    """
    content = '<h2 align="center">Steam Games API</h2>'
    media_type = 'text/html'
    return Response(content=content, media_type=media_type)



