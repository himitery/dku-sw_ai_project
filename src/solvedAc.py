from __future__ import annotations

import requests

from interface.interface import *

api: str = "https://solved.ac/api/v3"


class SolvedAc:
	def __init__(self):
		self.univ_ranking: list[UnivRank] | None = None

	# 대학교 랭킹
	def getUnivRanking(self) -> list[UnivRank]:
		if self.univ_ranking is not None:
			return self.univ_ranking

		univ_ranking: list[UnivRank] = list()
		page: int = 1
		while True:
			data = requests.get(
				f"{api}/ranking/organization?type=university&page={page}"
			).json()
			univ_ranking += data["items"]
			if len(data["items"]) == 0:
				break
			page += 1

		univ_ranking = list(filter(lambda x: '대학교' in x['name'], univ_ranking))
		self.univ_ranking = univ_ranking
		return univ_ranking

	# 대학교 유저 랭킹
	def getUnivUserRanking(self, univ_name: str) -> list[UnivUserRank]:
		univ_id: int = self.getUnivId(univ_name)

		ranking: list[UnivUserRank] = list()
		page: int = 1
		while True:
			data = requests.get(
				f"{api}/ranking/in_organization?page={page}&organizationId={univ_id}"
			).json()
			for idx in range(len(data['items'])):
				ranking.append(
					UnivUserRank(
						nickname=data['items'][idx]["handle"],
						bio=data['items'][idx]["bio"],
						organizations=data['items'][idx]["organizations"],
						background=data['items'][idx]['background'],
						badge=data['items'][idx]["badge"],
						profileImageUrl=data['items'][idx]["profileImageUrl"],
						solvedCount=data['items'][idx]["solvedCount"],
						voteCount=data['items'][idx]["voteCount"],
						_class=data['items'][idx]["class"],
						classDecoration=data['items'][idx]["classDecoration"],
						tier=self.getTier(data['items'][idx]["tier"]).name,
						rating=data['items'][idx]["rating"],
						ratingByProblemsSum=data['items'][idx]["ratingByProblemsSum"],
						ratingByClass=data['items'][idx]["ratingByClass"],
						ratingBySolvedCount=data['items'][idx]["ratingBySolvedCount"],
						ratingByVoteCount=data['items'][idx]["ratingByVoteCount"],
						exp=data['items'][idx]["exp"],
						rivalCount=data['items'][idx]["rivalCount"],
						reverseRivalCount=data['items'][idx]["reverseRivalCount"],
						maxStreak=data['items'][idx]["maxStreak"],
						rank=data['items'][idx]["rank"],
						globalRank=data['items'][idx]["globalRank"],
					)
				)

			if len(data["items"]) == 0:
				break
			page += 1

		return ranking

	def getUnivId(self, univ_name: str) -> int:
		univ: list[UnivRank] = self.getUnivRanking()

		return list(filter(lambda x: x['name'] == univ_name, univ))[0]['organizationId']

	def getTier(self, tier_number: int) -> Tier:
		if tier_number == 0:
			return Tier.Unrated
		elif tier_number <= 5:
			return Tier.Bronze
		elif tier_number <= 10:
			return Tier.Silver
		elif tier_number <= 15:
			return Tier.Gold
		elif tier_number <= 20:
			return Tier.Platinum
		elif tier_number <= 25:
			return Tier.Diamond
		elif tier_number <= 30:
			return Tier.Ruby
