from typing import Optional

from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()


players = {
    1: {
        "name": "Virat",
        "country": "India",
        "ipl_team": "RCB"
    },
    2: {
        "name": "Rohit",
        "country": "India",
        "ipl_team": "MI"
    }
}


class Player(BaseModel):
    name: str
    country: str
    ipl_team: str


class UpdatePlayer(BaseModel):
    name: Optional[str] = None
    country: Optional[str] = None
    ipl_team: Optional[str] = None


@app.get("/")
def hello_world():
    return {"Hello World"}


@app.get("/get-all-players")
def get_all_players():
    return players


# Route to demonstrate path variables
@app.get("/get-player/{player_id}")
def get_player_by_id(player_id: int = Path(..., description="ID of player to get data of")):
    return players[player_id]


# route to demonstrate query params
@app.get("/get-player")
def get_player_by_name(name: str):
    for player_id in players:
        if players[player_id]["name"] == name:
            return players[player_id]

    return {"Error": "Player doesn't exist"}


# route to post player in memory
@app.post("/add-player")
def add_player(player: Player):
    player_id = max(players.keys(), default=0)+1
    players[player_id] = player.__dict__
    return player


# route to update players
@app.put("/update-player/{player_id}")
def update_player(player_id: int, player: UpdatePlayer):
    if player_id not in players.keys():
        return {"Error": f"Player with player_id: {player_id} doesn't exist."}

    if player.name is not None:
        players[player_id]["name"] = player.name

    if player.country is not None:
        players[player_id]["country"] = player.country

    if player.ipl_team is not None:
        players[player_id]["ipl_team"] = player.ipl_team

    return players[player_id]


# route to delete players
@app.delete("/delete-player/{player_id}")
def delete_player(player_id: int):
    if player_id not in players.keys():
        return {"Error": f"Player with player_id: {player_id} doesn't exist."}

    del players[player_id]

    return {"Message": f"Player with player_id: {player_id} deleted successfully"}
