import requests
from datetime import datetime

# GitHub 仓库信息
REPO_OWNER = "W1ndys"
REPO_NAME = "Easy-QFNU"

# 获取仓库信息
repo_url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}"
response = requests.get(repo_url)
response.raise_for_status()
repo_info = response.json()

# 获取最后一次提交信息
commits_url = repo_info["commits_url"]
last_commit_url = f"{commits_url.split('{/sha}')[0]}?per_page=1"
response = requests.get(last_commit_url)
response.raise_for_status()
last_commit = response.json()[0]

# 格式化日期为 yyyy-mm-dd 格式
commit_date = datetime.strptime(last_commit['commit']['committer']['date'], "%Y-%m-%dT%H:%M:%SZ")
formatted_date = commit_date.strftime("%Y-%m-%d")

# 提取提交哈希值的前七位
commit_sha_short = last_commit['sha'][:7]

# # 获取本页面更新日期
# current_date = datetime.now().strftime("%Y-%m-%d")

# 构建提交的链接
commit_url = last_commit['html_url']

# 构建 HTML 内容
html_content = f"""更新日期: {formatted_date}
更新哈希值: <a href="{commit_url}">{commit_sha_short}</a>
"""

# 将 HTML 内容写入 index.html 文件
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

