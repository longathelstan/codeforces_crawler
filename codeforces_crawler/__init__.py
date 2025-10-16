import json
import os
import scrapy
import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin


class CodeforcesGroupSpider(scrapy.Spider):
    name = "codeforces_group"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # đọc file config.json
        config_path = os.path.join(os.path.dirname(__file__), "..", "config.json")
        with open(config_path, "r", encoding="utf-8") as f:
            config = json.load(f)

        self.username = config["username"]
        self.password = config["password"]
        self.group_id = config["group_id"]

        self.login_url = "https://codeforces.com/enter"
        self.start_urls = [f"https://codeforces.com/group/{self.group_id}/contests"]

