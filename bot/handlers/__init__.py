from .start import router as start_router
from .help import router as help_router
from .team import router as team_router
from .next_game import router as next_game_router

routers = [
    start_router,
    help_router,
    team_router,
    next_game_router
]
