import requests
from bs4 import BeautifulSoup
import time
import os
import re

# 配置区
BLOG_URLS = [
    "https://blog.csdn.net/realwangpu",      # 优先这个
    "https://blog.csdn.net/weixin_39938069", # 第二个
]

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

# 关键字筛选设置
KEYWORD = "TongWeb"

# 安全文件名
def safe_filename(title):
    # 去掉非法字符，并确保文件名不会因为太长被系统拒绝
    return re.sub(r'[<>:"/\\|?*]', '_', title)[:100]

def get_article_list(blog_url, max_pages=30):
    articles = []
    for page in range(1, max_pages + 1):
        url = f"{blog_url}/article/list/{page}"
        try:
            resp = requests.get(url, headers=HEADERS, timeout=10)
            resp.raise_for_status()
            soup = BeautifulSoup(resp.text, 'lxml')
            
            items = soup.select('div.article-item-box')
            if not items:
                break
                
            for item in items:
                a_tag = item.select_one('h4 a')
                if a_tag:
                    title = a_tag.get_text(strip=True).replace('原文', '').strip()
                    
                    # 仅保留包含关键字的文章
                    if KEYWORD.lower() not in title.lower():
                        continue 
                    
                    link = a_tag['href']
                    if link.startswith('/'):
                        link = 'https://blog.csdn.net' + link
                    articles.append({'title': title, 'url': link})
            
            print(f"扫描第{page}页... 当前已发现 {len(articles)} 篇相关文章")
            time.sleep(1) 
        except Exception as e:
            print(f"列表页{page}出错：{e}")
            break
    return articles

def get_article_content(url):
    try:
        resp = requests.get(url, headers=HEADERS, timeout=10)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, 'lxml')
        
        # CSDN常见的正文ID
        content = soup.find('div', id='article_content') or soup.find('div', class_='article-content')
        if content:
            # 清洗掉干扰元素
            for bad in content(['script', 'style', 'iframe', 'aside', 'nav']):
                bad.decompose()
            return content.get_text(separator='\n', strip=True)
        return "内容解析失败"
    except Exception as e:
        return f"内容抓取失败：{e}"

# 创建输出文件夹
output_dir = 'csdn_tongweb'
os.makedirs(output_dir, exist_ok=True)

# 主流程
readme_lines = ["# TongWeb 相关博客合集\n\n"]

for blog in BLOG_URLS:
    print(f"\n 正在筛选博主文章: {blog}")
    target_articles = get_article_list(blog)
    
    print(f" 筛选完成！共有 {len(target_articles)} 篇关于 {KEYWORD} 的文章待下载。")
    
    for i, art in enumerate(target_articles):
        print(f" 正在爬取({i+1}/{len(target_articles)}): {art['title'][:40]}...")
        
        content = get_article_content(art['url'])
        
        # 拼接Markdown
        md_text = f"# {art['title']}\n\n> 原文地址: {art['url']}\n\n---\n\n{content}"
        
        # 保存文件
        file_name = f"{safe_filename(art['title'])}.md"
        with open(os.path.join(output_dir, file_name), 'w', encoding='utf-8') as f:
            f.write(md_text)
        
        readme_lines.append(f"- [{art['title']}]({file_name})\n")
        
        # 合理爬取，防止被CSDN封IP
        time.sleep(3)

# 生成索引
with open(os.path.join(output_dir, 'README.md'), 'w', encoding='utf-8') as f:
    f.writelines(readme_lines)

print(f"\n 全部完成！文章已保存至文件夹: {output_dir }")