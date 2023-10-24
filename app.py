import BotNulis
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from typing import Optional
import time

app = FastAPI()
waktuFile = time.strftime("%y%m%d-%H%M%S")


@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("templates/index.html") as f:
        html_content = f.read()
    return html_content


@app.get("/write")
async def write(text: Optional[str] = '', kertas: Optional[int] = 1,
                font: Optional[int] = 1, header: Optional[str] = '',
                tanggal: Optional[str] = ''):
    if text:
        bot = BotNulis.BotNulis(text, kertas, font, header, tanggal)
        result = bot.start()
        return result
    else:
        raise HTTPException(status_code=400, detail="Missing 'text' parameter")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info")
