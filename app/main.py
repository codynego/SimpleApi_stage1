from fastapi import FastAPI, HTTPException, Query
from datetime import datetime
import pytz

app = FastAPI()

@app.get("/api")
async def get_info(
    slack_name: str = Query(..., title="Slack Name"),
    track: str = Query(..., title="Track"),
):
    # Get the current UTC time with a UTC timezone object
    utc_time = datetime.now(pytz.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    # Determine the current day of the week
    current_day = datetime.now(pytz.utc).strftime("%A")

    # Define GitHub URLs
    github_file_url = "https://github.com/username/repo/blob/main/file_name.ext"
    github_repo_url = "https://github.com/codynego/SimpleApi_stage1"

    # Create the JSON response
    response = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200,
    }
    return response

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
