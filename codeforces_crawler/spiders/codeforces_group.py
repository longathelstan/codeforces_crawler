import scrapy
import re
import os
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import json


class CodeforcesGroupSpider(scrapy.Spider):
    name = "codeforces_group"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # đọc file config.json
        config_path = os.path.join(os.path.dirname(__file__), "..", "..", "config.json")
        with open(config_path, "r", encoding="utf-8") as f:
            config = json.load(f)

        self.username = config["username"]
        self.password = config["password"]
        self.group_id = config["group_id"]
        self.cookies = config.get("cookies", {}) # Load cookies from config

        self.login_url = "https://codeforces.com/enter"

    def start_requests(self):
        # Use pre-obtained cookies to directly access the group contests page
        contests_url = f"https://codeforces.com/group/{self.group_id}/contests"
        yield scrapy.Request(
            url=contests_url,
            cookies=self.cookies, # Pass the loaded cookies
            callback=self.parse_contests,
            dont_filter=True # Important to allow re-requesting the same URL if needed
        )

    def parse_contests(self, response):
        """Lấy danh sách contest trong group"""
        if "Codeforces" not in response.text and "login" in response.url.lower():
            self.logger.error("❌ Failed to access group contests page. Cookies might be invalid or expired.")
            return

        for row in response.css(".contests-table tr"):
            link_el = row.css("a::attr(href)").get()
            name_el = row.css("a::text").get()

            if link_el and name_el:
                contest_name = name_el.strip()
                contest_url = urljoin(response.url, link_el)
                
                # Extract contest_id from the contest_url
                match = re.search(r'/contest/(\d+)', contest_url)
                if not match:
                    self.logger.warning(f"⚠️ Could not extract contest ID from URL: {contest_url}")
                    continue
                contest_id = match.group(1)

                group_folder = f"output/{self.group_id}"
                # Use contest_id for the folder name
                contest_output_folder = os.path.join(group_folder, contest_id)

                if os.path.exists(contest_output_folder):
                    self.logger.info(f"⏭️ Skipping already crawled contest (ID: {contest_id}, Name: {contest_name})")
                    continue

                self.logger.info(f"✨ Crawling new contest (ID: {contest_id}, Name: {contest_name})")
                yield scrapy.Request(
                    contest_url,
                    callback=self.parse_contest,
                    cb_kwargs={
                        "contest_name": contest_name, # Keep contest_name for problem details
                        "contest_id": contest_id # Pass contest_id for folder structure
                    },
                    cookies=self.cookies
                )

    def parse_contest(self, response, contest_name, contest_id):
        """Lấy danh sách problem trong contest"""
        for problem in response.css(".problems tr"):
            link = problem.css("a::attr(href)").get()
            if link:
                problem_url = urljoin(response.url, link)
                yield scrapy.Request(
                    problem_url,
                    callback=self.parse_problem,
                    cb_kwargs={
                        "contest_name": contest_name,
                        "contest_id": contest_id # Pass contest_id
                    },
                    cookies=self.cookies
                )

    def parse_problem(self, response, contest_name, contest_id):
        """Parse chi tiết đề bài và xuất ra Markdown"""
        soup = BeautifulSoup(response.text, "html.parser")
        problem_div = soup.select_one(".problemindexholder")
        if not problem_div:
            self.logger.warning(f"⚠️ No problem div found for {response.url}")
            return

        title_el = problem_div.select_one(".title")
        title = title_el.get_text(strip=True) if title_el else "Unknown Problem"

        # Extract time and memory limits
        time_limit = ""
        memory_limit = ""
        info_div = problem_div.select_one(".problem-statement .header")
        if info_div:
            for p_tag in info_div.find_all('p', recursive=False):
                text = p_tag.get_text(strip=True)
                if "time limit" in text.lower():
                    time_limit = text.replace("time limit per test", "Time limit:").strip()
                elif "memory limit" in text.lower():
                    memory_limit = text.replace("memory limit per test", "Memory limit:").strip()

        markdown = self.html_to_markdown(problem_div, title, time_limit, memory_limit)

        # Build file path
        group_folder = f"output/{self.group_id}"
        # Use contest_id for the output folder
        contest_output_folder = os.path.join(group_folder, contest_id)
        os.makedirs(contest_output_folder, exist_ok=True)

        file_name = f"{title}.md"
        # Sanitize file name
        file_name = re.sub(r'[\/:*?"<>|]', '', file_name)
        file_path = os.path.join(contest_output_folder, file_name)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(markdown)

        self.logger.info(f"✅ Saved: {file_path}")

    # --- Utility ---

    def html_to_markdown(self, problem_div_soup, title, time_limit, memory_limit):
        """Chuyển HTML Codeforces -> Markdown đẹp"""
        out = []

        # Title
        out.append(f"# {title}\n")

        # Time and Memory limits
        if time_limit or memory_limit:
            out.append(f"**{time_limit}**")
            out.append(f"**{memory_limit}**\n")
            out.append("---\n")

        # Problem Statement
        problem_statement_div = problem_div_soup.select_one(".problem-statement")
        if problem_statement_div:
            if problem_statement_div.select_one(".header"):
                problem_statement_div.select_one(".header").decompose()
            
            problem_content_div = problem_statement_div.find('div', class_=False, recursive=False)
            if problem_content_div:
                out.append("## 📖 Problem\n")
                out.append(self.convert_element_to_markdown(problem_content_div))
                out.append("\n")

        # Input Specification
        input_spec = problem_div_soup.select_one(".input-specification")
        if input_spec:
            out.append("## 🧩 Input\n")
            out.append(self.convert_element_to_markdown(input_spec))
            out.append("\n")

        # Output Specification
        output_spec = problem_div_soup.select_one(".output-specification")
        if output_spec:
            out.append("## 💡 Output\n")
            out.append(self.convert_element_to_markdown(output_spec))
            out.append("\n")

        # Examples
        sample_tests = problem_div_soup.select(".sample-tests .sample-test")
        if sample_tests:
            out.append("## 🧠 Example\n")
            for i, example in enumerate(sample_tests):
                input_block = example.select_one(".input pre")
                output_block = example.select_one(".output pre")
                if input_block:
                    out.append("### Input\n")
                    out.append("```text\n" + input_block.get_text(strip=True) + "\n```\n")
                if output_block:
                    out.append("### Output\n")
                    out.append("```text\n" + output_block.get_text(strip=True) + "\n```\n")
            out.append("\n")

        # Note
        note = problem_div_soup.select_one(".note")
        if note:
            out.append("## 📝 Note\n")
            out.append(self.convert_element_to_markdown(note))
            out.append("\n")

        return "\n".join(out)

    def convert_element_to_markdown(self, element):
        """Convert a BeautifulSoup element to Markdown, handling LaTeX and images."""
        
        # Handle images
        for img_tag in element.find_all('img'):
            alt = img_tag.get('alt', '')
            src = img_tag.get('src', '')
            if src.startswith("//"):
                src = "https:" + src # Fix protocol-relative URLs
            markdown_img = f"![{alt}]({src})"
            img_tag.replace_with(BeautifulSoup(markdown_img, 'html.parser'))

        # Handle LaTeX
        for tex_span in element.find_all(class_='tex-span'):
            tex_content = tex_span.get_text(strip=True)
            tex_span.replace_with(f"${tex_content}$")
        
        # Handle <i>, <sub>, <sup> for mathematical expressions
        for i_tag in element.find_all('i'):
            i_content = i_tag.get_text(strip=True)
            i_tag.replace_with(f"${i_content}$") # Assume <i> mostly for math variables

        for sub_tag in element.find_all('sub'):
            sub_content = sub_tag.get_text(strip=True)
            sub_tag.replace_with(f"_{{{sub_content}}}") # _{content} for markdown subscript

        for sup_tag in element.find_all('sup'):
            sup_content = sup_tag.get_text(strip=True)
            sup_tag.replace_with(f"^{{{sup_content}}}") # ^{content} for markdown superscript


        # Convert remaining HTML to markdown
        # This is a simplified approach, a full HTML-to-Markdown library would be more robust
        # but for specific Codeforces HTML, this should be sufficient.
        
        # Convert paragraphs
        for p_tag in element.find_all('p'):
            p_tag.insert_after('\n\n') # Add newlines after paragraphs
        
        # Convert lists
        for ul_tag in element.find_all('ul'):
            for li_tag in ul_tag.find_all('li'):
                li_tag.insert_before('* ')
                li_tag.insert_after('\n')
            ul_tag.insert_after('\n')
        
        # Convert strong/bold
        for strong_tag in element.find_all('strong'):
            strong_tag.insert_before('**')
            strong_tag.insert_after('**')
        
        # Convert code blocks
        for pre_tag in element.find_all('pre'):
            pre_tag.insert_before('\n```\n')
            pre_tag.insert_after('\n```\n')

        # Get text, preserving newlines from original processing
        # Use .encode and .decode to handle special characters correctly
        return element.get_text(separator='\n', strip=True)
