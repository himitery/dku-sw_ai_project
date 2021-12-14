from enum import Enum
from typing import TypedDict


class Organizations(TypedDict):
	organizationId: int
	name: str
	type: str
	rating: int
	userCount: int
	voteCount: int
	solvedCount: int
	color: str


class Badge(TypedDict):
	badgeId: str
	badgeImageUrl: str
	unlockedUserCount: str
	displayName: str
	displayDescription: str


class Background(TypedDict):
	backgroundId: str
	backgroundImageUrl: str
	author: str
	authorUrl: str
	unlockedUserCount: int
	displayName: str
	displayDescription: str


class Tier(Enum):
	Unrated = 'unrated'
	Bronze = 'bronze'
	Silver = 'silver'
	Gold = 'gold'
	Platinum = 'platinum'
	Diamond = 'diamond'
	Ruby = 'ruby'


class UnivRank(TypedDict):
	organizationId: int
	name: str
	type: str
	ratting: int
	userCount: int
	voteCount: int
	solvedCount: int
	color: str
	rank: int
	globalRank: int


class UnivUserRank(TypedDict):
	nickname: str
	bio: str
	organizations: Organizations
	background: Background
	badge: Badge
	profileImageUrl: str
	solvedCount: int
	voteCount: int
	_class: int
	classDecoration: str
	tier: str
	rating: int
	ratingByProblemsSum: int
	ratingByClass: int
	ratingBySolvedCount: int
	ratingByVoteCount: int
	exp: int
	rivalCount: int
	reverseRivalCount: int
	maxStreak: int
	rank: int
	globalRank: int
