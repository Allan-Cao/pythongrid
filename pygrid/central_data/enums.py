# Generated by ariadne-codegen
# Source: https://api.grid.gg/central-data/graphql

from enum import Enum


class ContentCatalogEntityType(str, Enum):
    CHARACTER = "CHARACTER"
    ITEM = "ITEM"
    MAP = "MAP"


class ContentCatalogVersionOrderField(str, Enum):
    PUBLISHED_ON = "PUBLISHED_ON"
    TITLE = "TITLE"


class ErrorDetail(str, Enum):
    DEADLINE_EXCEEDED = "DEADLINE_EXCEEDED"
    ENHANCE_YOUR_CALM = "ENHANCE_YOUR_CALM"
    FIELD_NOT_FOUND = "FIELD_NOT_FOUND"
    INVALID_ARGUMENT = "INVALID_ARGUMENT"
    INVALID_CURSOR = "INVALID_CURSOR"
    MISSING_RESOURCE = "MISSING_RESOURCE"
    SERVICE_ERROR = "SERVICE_ERROR"
    TCP_FAILURE = "TCP_FAILURE"
    THROTTLED_CONCURRENCY = "THROTTLED_CONCURRENCY"
    THROTTLED_CPU = "THROTTLED_CPU"
    TOO_MANY_REQUESTS = "TOO_MANY_REQUESTS"
    UNIMPLEMENTED = "UNIMPLEMENTED"
    UNKNOWN = "UNKNOWN"


class ErrorType(str, Enum):
    BAD_REQUEST = "BAD_REQUEST"
    FAILED_PRECONDITION = "FAILED_PRECONDITION"
    INTERNAL = "INTERNAL"
    NOT_FOUND = "NOT_FOUND"
    PERMISSION_DENIED = "PERMISSION_DENIED"
    UNAUTHENTICATED = "UNAUTHENTICATED"
    UNAVAILABLE = "UNAVAILABLE"
    UNKNOWN = "UNKNOWN"


class OrderDirection(str, Enum):
    ASC = "ASC"
    DESC = "DESC"


class PlayerType(str, Enum):
    ESPORTS = "ESPORTS"
    REGULAR = "REGULAR"


class SeriesOrderBy(str, Enum):
    ID = "ID"
    StartTimeScheduled = "StartTimeScheduled"
    UpdatedAt = "UpdatedAt"


class SeriesType(str, Enum):
    COMPETITIVE = "COMPETITIVE"
    ESPORTS = "ESPORTS"
    LOOPFEED = "LOOPFEED"
    SCRIM = "SCRIM"


class ServiceLevel(str, Enum):
    FULL = "FULL"
    LIMITED = "LIMITED"
    NONE = "NONE"


class TournamentVenueType(str, Enum):
    HYBRID = "HYBRID"
    LAN = "LAN"
    ONLINE = "ONLINE"
    UNKNOWN = "UNKNOWN"
