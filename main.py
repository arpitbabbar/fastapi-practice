from fastapi import FastAPI, Path

app = FastAPI()


players = {
    1: {
        "name": "Virat Kohli",
        "country": "India",
        "ipl_team": "RCB"
    },
    2: {
        "name": "Rohit Sharma",
        "country": "India",
        "ipl_team": "MI"
    }
}


@app.get("/")
def hello_world():
    return {"Hello World"}


@app.get("/get-all-players")
def get_all_players():
    return players


@app.get("/get-player/{player_id}")
def get_player_by_id(player_id: int):
    return players[player_id]
