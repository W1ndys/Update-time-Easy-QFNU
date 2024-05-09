import requests
from datetime import datetime, timedelta

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
commit_date_utc = datetime.strptime(last_commit['commit']['committer']['date'], "%Y-%m-%dT%H:%M:%SZ")
commit_date_utc8 = commit_date_utc + timedelta(hours=8)  # 转换为 UTC+8 时间
formatted_date = commit_date_utc8.strftime("%Y-%m-%d")

# 提取提交哈希值的前七位
commit_sha_short = last_commit['sha'][:7]

# 构建提交的链接
commit_url = last_commit['html_url']

# 构建 HTML1 内容
html_content1 = f"""<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Easy-QFNU 最后一次更新</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <h1>Easy-QFNU 更新记录</h1>
        <p>更新日期: {formatted_date} | 更新哈希值: <a href="{commit_url}">{commit_sha_short}(该数据有十分钟以内的延迟)</a></p>
        <p>相关链接: <a href="https://github.com/W1ndys/Easy-QFNU">GitHub 仓库</a>、<a href="https://Easy-QFNU.top">Easy-QFNU官网</a></p>
    </div>
</body>
</html>
"""

# 构建 HTML2 内容
html_content2 = f"""更新日期: {formatted_date} | 更新哈希值: <a href="{commit_url}">{commit_sha_short}(该数据有十分钟以内的延迟)</a>
"""

# 将 HTML 内容写入 更新日期主页文件
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content1)

# 将 HTML 内容写入 update-time-Easy-QFNU.html 文件
with open("update-time-Easy-QFNU.html", "w", encoding="utf-8") as f:
    f.write(html_content2)
