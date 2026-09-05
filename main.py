from fastapi import FastAPI, HTTPException, Query
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from ntes import NTESClient, NTESError
import os

app = FastAPI(
    title="Indian Railways NTES & PNR Portal",
    description="A responsive API wrapper and portal for Indian Railways Enquiry and PNR status tracking.",
    version="1.0.0"
)

client = NTESClient()

@app.get("/api/search")
def search_train(q: str = Query(..., min_length=1)):
    try:
        res = client.search(q)
        return res
    except NTESError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/train_info")
def train_info(train_no: str = Query(..., min_length=1)):
    try:
        res = client.train_info(train_no)
        return res
    except NTESError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/live_status")
def live_status(train_no: str = Query(...), start_date: str = Query(...)):
    try:
        res = client.live_status(train_no, start_date)
        return res
    except NTESError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/schedule")
def schedule(train_no: str = Query(...), start_date: str = Query("")):
    try:
        res = client.schedule(train_no, start_date)
        return res
    except NTESError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/station_live")
def station_live(station_code: str = Query(...), hours: int = Query(2)):
    try:
        res = client.station_live(station_code, hours)
        return res
    except NTESError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/trains_between")
def trains_between(from_station: str = Query(...), to_station: str = Query(...), train_type: str = Query("XXX")):
    try:
        res = client.trains_between(from_station, to_station, train_type)
        return res
    except NTESError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/pnr_status")
def pnr_status(pnr: str = Query(..., min_length=10, max_length=10)):
    try:
        res = client.pnr_status(pnr)
        return res
    except NTESError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Setup Static Files directory
static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")
if not os.path.exists(static_dir):
    os.makedirs(static_dir)

@app.get("/")
def read_index():
    index_path = os.path.join(static_dir, "index.html")
    if not os.path.exists(index_path):
        return {"message": "Server is running. Frontend static/index.html is not created yet."}
    return FileResponse(index_path)

# Mount the static files directory at /static for caching, images, etc.
app.mount("/static", StaticFiles(directory=static_dir), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)
