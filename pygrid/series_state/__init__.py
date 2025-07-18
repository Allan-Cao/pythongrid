# Generated by ariadne-codegen

from .base_client import BaseClient
from .base_model import BaseModel, Upload
from .client import Client
from .enums import ErrorDetail, ErrorType, GameType, ParticipationStatus
from .exceptions import (
    GraphQLClientError,
    GraphQLClientGraphQLError,
    GraphQLClientGraphQLMultiError,
    GraphQLClientHttpError,
    GraphQLClientInvalidResponseError,
)
from .input_types import GameStateFilter
from .series_draft_state import (
    SeriesDraftState,
    SeriesDraftStateSeriesState,
    SeriesDraftStateSeriesStateGames,
    SeriesDraftStateSeriesStateGamesDraftActions,
    SeriesDraftStateSeriesStateGamesDraftActionsDraftable,
    SeriesDraftStateSeriesStateGamesDraftActionsDrafter,
    SeriesDraftStateSeriesStateGamesTeams,
    SeriesDraftStateSeriesStateGamesTeamsPlayers,
    SeriesDraftStateSeriesStateGamesTeamsPlayersCharacter,
    SeriesDraftStateSeriesStateGamesTeamsPlayersRoles,
    SeriesDraftStateSeriesStateGamesTitleVersion,
)
from .series_games import (
    SeriesGames,
    SeriesGamesSeriesState,
    SeriesGamesSeriesStateGames,
)
from .series_state import (
    SeriesState,
    SeriesStateSeriesState,
    SeriesStateSeriesStateGames,
    SeriesStateSeriesStateGamesClock,
    SeriesStateSeriesStateGamesExternalLinks,
    SeriesStateSeriesStateGamesExternalLinksDataProvider,
    SeriesStateSeriesStateGamesExternalLinksExternalEntity,
    SeriesStateSeriesStateGamesMap,
    SeriesStateSeriesStateGamesMapBounds,
    SeriesStateSeriesStateGamesMapBoundsMax,
    SeriesStateSeriesStateGamesMapBoundsMin,
    SeriesStateSeriesStateGamesNonPlayerCharacters,
    SeriesStateSeriesStateGamesStructures,
    SeriesStateSeriesStateGamesTeams,
    SeriesStateSeriesStateGamesTeamsKillAssistsReceivedFromPlayer,
    SeriesStateSeriesStateGamesTeamsMultikills,
    SeriesStateSeriesStateGamesTeamsObjectives,
    SeriesStateSeriesStateGamesTeamsPlayers,
    SeriesStateSeriesStateGamesTeamsUnitKills,
    SeriesStateSeriesStateGamesTitleVersion,
    SeriesStateSeriesStateTeams,
    SeriesStateSeriesStateTitle,
)
from .series_state_legacy import (
    SeriesStateLegacy,
    SeriesStateLegacySeriesState,
    SeriesStateLegacySeriesStateGames,
    SeriesStateLegacySeriesStateGamesClock,
    SeriesStateLegacySeriesStateGamesExternalLinks,
    SeriesStateLegacySeriesStateGamesExternalLinksDataProvider,
    SeriesStateLegacySeriesStateGamesExternalLinksExternalEntity,
    SeriesStateLegacySeriesStateGamesMap,
    SeriesStateLegacySeriesStateGamesMapBounds,
    SeriesStateLegacySeriesStateGamesMapBoundsMax,
    SeriesStateLegacySeriesStateGamesMapBoundsMin,
    SeriesStateLegacySeriesStateGamesNonPlayerCharacters,
    SeriesStateLegacySeriesStateGamesStructures,
    SeriesStateLegacySeriesStateGamesTeams,
    SeriesStateLegacySeriesStateGamesTeamsKillAssistsReceivedFromPlayer,
    SeriesStateLegacySeriesStateGamesTeamsMultikills,
    SeriesStateLegacySeriesStateGamesTeamsObjectives,
    SeriesStateLegacySeriesStateGamesTeamsPlayers,
    SeriesStateLegacySeriesStateGamesTeamsUnitKills,
    SeriesStateLegacySeriesStateTeams,
    SeriesStateLegacySeriesStateTitle,
)

__all__ = [
    "BaseClient",
    "BaseModel",
    "Client",
    "ErrorDetail",
    "ErrorType",
    "GameStateFilter",
    "GameType",
    "GraphQLClientError",
    "GraphQLClientGraphQLError",
    "GraphQLClientGraphQLMultiError",
    "GraphQLClientHttpError",
    "GraphQLClientInvalidResponseError",
    "ParticipationStatus",
    "SeriesDraftState",
    "SeriesDraftStateSeriesState",
    "SeriesDraftStateSeriesStateGames",
    "SeriesDraftStateSeriesStateGamesDraftActions",
    "SeriesDraftStateSeriesStateGamesDraftActionsDraftable",
    "SeriesDraftStateSeriesStateGamesDraftActionsDrafter",
    "SeriesDraftStateSeriesStateGamesTeams",
    "SeriesDraftStateSeriesStateGamesTeamsPlayers",
    "SeriesDraftStateSeriesStateGamesTeamsPlayersCharacter",
    "SeriesDraftStateSeriesStateGamesTeamsPlayersRoles",
    "SeriesDraftStateSeriesStateGamesTitleVersion",
    "SeriesGames",
    "SeriesGamesSeriesState",
    "SeriesGamesSeriesStateGames",
    "SeriesState",
    "SeriesStateLegacy",
    "SeriesStateLegacySeriesState",
    "SeriesStateLegacySeriesStateGames",
    "SeriesStateLegacySeriesStateGamesClock",
    "SeriesStateLegacySeriesStateGamesExternalLinks",
    "SeriesStateLegacySeriesStateGamesExternalLinksDataProvider",
    "SeriesStateLegacySeriesStateGamesExternalLinksExternalEntity",
    "SeriesStateLegacySeriesStateGamesMap",
    "SeriesStateLegacySeriesStateGamesMapBounds",
    "SeriesStateLegacySeriesStateGamesMapBoundsMax",
    "SeriesStateLegacySeriesStateGamesMapBoundsMin",
    "SeriesStateLegacySeriesStateGamesNonPlayerCharacters",
    "SeriesStateLegacySeriesStateGamesStructures",
    "SeriesStateLegacySeriesStateGamesTeams",
    "SeriesStateLegacySeriesStateGamesTeamsKillAssistsReceivedFromPlayer",
    "SeriesStateLegacySeriesStateGamesTeamsMultikills",
    "SeriesStateLegacySeriesStateGamesTeamsObjectives",
    "SeriesStateLegacySeriesStateGamesTeamsPlayers",
    "SeriesStateLegacySeriesStateGamesTeamsUnitKills",
    "SeriesStateLegacySeriesStateTeams",
    "SeriesStateLegacySeriesStateTitle",
    "SeriesStateSeriesState",
    "SeriesStateSeriesStateGames",
    "SeriesStateSeriesStateGamesClock",
    "SeriesStateSeriesStateGamesExternalLinks",
    "SeriesStateSeriesStateGamesExternalLinksDataProvider",
    "SeriesStateSeriesStateGamesExternalLinksExternalEntity",
    "SeriesStateSeriesStateGamesMap",
    "SeriesStateSeriesStateGamesMapBounds",
    "SeriesStateSeriesStateGamesMapBoundsMax",
    "SeriesStateSeriesStateGamesMapBoundsMin",
    "SeriesStateSeriesStateGamesNonPlayerCharacters",
    "SeriesStateSeriesStateGamesStructures",
    "SeriesStateSeriesStateGamesTeams",
    "SeriesStateSeriesStateGamesTeamsKillAssistsReceivedFromPlayer",
    "SeriesStateSeriesStateGamesTeamsMultikills",
    "SeriesStateSeriesStateGamesTeamsObjectives",
    "SeriesStateSeriesStateGamesTeamsPlayers",
    "SeriesStateSeriesStateGamesTeamsUnitKills",
    "SeriesStateSeriesStateGamesTitleVersion",
    "SeriesStateSeriesStateTeams",
    "SeriesStateSeriesStateTitle",
    "Upload",
]
