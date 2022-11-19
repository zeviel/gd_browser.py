import requests

class GDBrowser:
	def __init__(self) -> None:
		self.api = "https://gdbrowser.com/api"
		self.headers = {
			"server": "nginx/1.14.0 (Ubuntu)",
			"content-type": "application/json; charset=utf-8",
			"connection": "keep-alive"
		}

	def get_level(
			self, 
			level_id: int,
			download: bool = False) -> dict:
		url = f"{self.api}/level/{level_id}"
		if download:
			url += "?download"
		return requests.get(url, headers=self.headers).json()

	def get_user_profile(self, username: str) -> dict:
		return requests.get(
			f"{self.api}/profile/{username}",
			headers=self.headers).json()

	def search(
			self,
			query: str,
			count: int = 10,
			demon_filter: int = None,
			page: int = 0,
			gauntlet: int = None,
			type: str = "trending") -> dict:
		url = f"{self.api}/search/{query}?count={count}"
		if demon_filter:
			url += f"&demonFilter={demon_filter}"
		if page:
			url += f"&page={page}"
		if gauntlet:
			url += f"&gauntlet={gauntlet}"
		if type:
			url += f"&type={type}"
		return requests.get(url, headers=self.headers).json()

	def get_leaderboard(
			self,
			count: int = 100, 
			is_creator: bool = False) -> dict:
		url = f"{self.api}/leaderboard?count={count}"
		if is_creator:
			url += "&creator"
		return requests.get(url, headers=self.headers).json()

	def get_map_packs(self) -> dict:
		return requests.get(
			f"{self.api}/mappacks",
			headers=self.headers).json()

	def get_gauntlets_list(self) -> dict:
		return requests.get(
			f"{self.api}/gauntlets",
			headers=self.headers).json()

	def get_level_leaderboard(
			self,
			level_id: int,
			count: int = 100) -> dict:
		return requests.get(
			f"{self.api}/leaderboardLevel/{level_id}?count={count}",
			headers=self.headers).json()

	def get_user_posts(
			self,
			user_id: int,
			page: int = 0,
			count: int = 10,
			type: str = "profile") -> dict:
		return requests.get(
			f"{self.api}/comments/{user_id}?page={page}&count={count}&type={type}",
			headers=self.headers).json()

	def get_user_comments(
			self,
			user_id: int,
			page: int = 0,
			count: int = 10,
			type: str = "commentHistory") -> dict:
		return requests.get(
			f"{self.api}/comments/{user_id}?page={page}&count={count}&type={type}",
			headers=self.headers).json()

	def get_level_comments(
			self,
			level_id: int,
			page: int = 0,
			is_top: bool = False,
			count: int = 10,
			type: str = "commentHistory") -> dict:
		url = f"{self.api}/comments/{level_id}?page={page}&count={count}&type={type}"
		if is_top:
			url += "&top"
		return requests.get(url, headers=self.headers).json()

	def check_song_verification(self, song_id: int) -> dict:
		return requests.get(
			f"{self.api}/song/{song_id}",
			headers=self.headers).text

	def analyze_level(self, level_id: int) -> dict:
		return requests.get(
			f"{self.api}/analyze/{level_id}",
			headers=self.headers).json()

	def get_user_icon(
			self,
			username: str,
			form: str = "cube",
			size: str = "auto") -> dict:
		return requests.get(
			f"{self.api}/icon/{username}?form={form}&size={size}",
			headers=self.headers).json()
