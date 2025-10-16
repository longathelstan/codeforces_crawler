import scrapy
import re
import os
from bs4 import BeautifulSoup
from urllib.parse import urljoin


class CodeforcesGroupSpider(scrapy.Spider):
    name = "codeforces_group"

    def __init__(self, username, password, group_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.username = username
        self.password = password
        self.group_id = group_id
        self.login_url = "https://codeforces.com/enter"
        self.start_urls = [f"https://codeforces.com/group/{group_id}/contests"]

    def parse(self, response):
        """Đăng nhập trước khi crawl"""
        csrf_token = response.xpath('//meta[@name="X-Csrf-Token"]/@content').get()
        if csrf_token is None:
            yield scrapy.Request(self.login_url, callback=self.login)
        else:
            yield scrapy.Request(self.login_url, callback=self.login)

    def login(self, response):
        csrf_token = response.xpath('//meta[@name="X-Csrf-Token"]/@content').get()
        return scrapy.FormRequest.from_response(
            response,
            formdata={
                'csrf_token': csrf_token,
                'handleOrEmail': self.username,
                'password': self.password,
                '_tta': '176'
            },
            callback=self.after_login
        )

    def after_login(self, response):
        """Sau khi login thành công -> đến danh sách contest"""
        if "Invalid handle or password" in response.text:
            self.logger.error("❌ Login failed")
            return
        contests_url = f"https://codeforces.com/group/{self.group_id}/contests"
        yield scrapy.Request(contests_url, callback=self.parse_contests)

    def parse_contests(self, response):
        """Lấy danh sách contest trong group"""
        for contest in response.css(".contests-table tr"):
            link = contest.css("a::attr(href)").get()
            name = contest.css("a::text").get()
            if link and name:
                contest_url = urljoin(response.url, link)
                yield scrapy.Request(
                    contest_url,
                    callback=self.parse_contest,
                    cb_kwargs={"contest_name": name.strip()}
                )

    def parse_contest(self, response, contest_name):
        """Lấy danh sách problem trong contest"""
        for problem in response.css(".problems tr"):
            link = problem.css("a::attr(href)").get()
            if link:
                problem_url = urljoin(response.url, link)
                yield scrapy.Request(
                    problem_url,
                    callback=self.parse_problem,
                    cb_kwargs={"contest_name": contest_name}
                )

    def parse_problem(self, response, contest_name):
        """Parse chi tiết đề bài"""
        soup = BeautifulSoup(response.text, "html.parser")
        problem_div = soup.select_one(".problemindexholder")
        if not problem_div:
            return

        title = problem_div.select_one(".title").get_text(strip=True)
        content_html = str(problem_div.select_one(".problem-statement"))
        content_html = self.clean_html(content_html)
        markdown = self.html_to_markdown(content_html)

        # Build file path
        group_folder = f"output/{self.group_id}/{contest_name}"
        os.makedirs(group_folder, exist_ok=True)
        file_path = os.path.join(group_folder, f"{title}.md")

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(markdown)

        self.logger.info(f"✅ Saved: {file_path}")

    # --- Utility ---

    def clean_html(self, html):
        """Xử lý HTML trước khi convert"""
        html = re.sub(r'\s+', ' ', html)
        html = html.replace("<br>", "\n").replace("<br/>", "\n")
        return html

    def html_to_markdown(self, html):
        """Chuyển HTML Codeforces -> Markdown đẹp"""
        soup = BeautifulSoup(html, "html.parser")
        out = []

        # Tiêu đề và thuộc tính
        title = soup.select_one(".title")
        if title:
            out.append(f"# {title.get_text(strip=True)}\n")

        def section(title, selector):
            el = soup.select_one(selector)
            if el:
                out.append(f"## {title}\n")
                out.append(self.extract_text_with_latex(el))

        # Phần mô tả
        section("Problem", ".problem-statement > div:nth-of-type(2)")
        section("Input", ".input-specification")
        section("Output", ".output-specification")

        # Examples
        examples = soup.select(".sample-test")
        if examples:
            out.append("## Examples\n")
            for ex in examples:
                input_block = ex.select_one(".input pre")
                output_block = ex.select_one(".output pre")
                if input_block:
                    out.append("**Input:**")
                    out.append("```text\n" + input_block.get_text().strip() + "\n```")
                if output_block:
                    out.append("**Output:**")
                    out.append("```text\n" + output_block.get_text().strip() + "\n```")
                out.append("")

        # Ghi chú
        note = soup.select_one(".note")
        if note:
            out.append("## Note\n")
            out.append(self.extract_text_with_latex(note))

        return "\n".join(out)

    def extract_text_with_latex(self, element):
        """Giữ công thức LaTeX ($...$)"""
        for tex in element.select(".tex-span"):
            tex.replace_with(f"${tex.get_text(strip=True)}$")
        return element.get_text("\n", strip=True)
