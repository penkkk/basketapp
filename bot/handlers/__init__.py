from .start import router as start_router
from .help import router as help_router
from .team import router as team_router
from .next_game import router as next_game_router
from .stat import router as stat_router
from .team_stat import router as team_stat_router
from .player_stat import router as player_stat_router

routers = [
    start_router,
    help_router,
    team_router,
    next_game_router,
    stat_router,
    team_stat_router,
    player_stat_router
]
