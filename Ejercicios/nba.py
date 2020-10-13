from nba_api.stats.static import  teams
from nba_api.stats.endpoints import leaguegamefinder
import matplotlib.pyplot as plt
import  pandas as pd
nba_teams = teams.get_teams()
df_teams = pd.DataFrame(nba_teams)
df_warriors = df_teams[df_teams["nickname"]=="Warriors"]
id_warriors= df_warriors[["id"]].values[0][0]

game_finder = leaguegamefinder.LeagueGameFinder(team_id_nullable=id_warriors)
game = game_finder.get_data_frames()[0]
games_away = game[game["MATCHUP"]=="GSW vs. TOR"]
games_home = game[game["MATCHUP"]=="GSW @ TOR"]
ax = plt.subplot()
games_away.plot(x='GAME_DATE', y='PLUS_MINUS',ax=ax)
games_home.plot(x='GAME_DATE', y='PLUS_MINUS',ax=ax)
ax.legend(["away","home"])
plt.show()

#print(game)