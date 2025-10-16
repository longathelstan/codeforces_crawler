# Scrapy settings for codeforces_crawler project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "codeforces_crawler"

SPIDER_MODULES = ["codeforces_crawler.spiders"]
NEWSPIDER_MODULE = "codeforces_crawler.spiders"

ADDONS = {}

ROBOTSTXT_OBEY = False
DOWNLOAD_DELAY = 1.0
COOKIES_ENABLED = True
FEED_EXPORT_ENCODING = "utf-8"
USER_AGENT = "Mozilla/5.0"