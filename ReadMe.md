Author: 林子宸(Emol)
Date:   2026.1.19 ~ 2026.2.13

# 1. 文件结构（不含脚本）
```bash
TONGWEB8知识库 
    ├── 通道日志数据源参数问答对   `主要针对通道，日志，数据源三个维度设计的QA对`
        ├── 通道日志数据参数说明.csv     `关于通道、日志、数据源三个维度的参数说明`
        ├── tongweb8.csv                `NotebookLM关于参数调优的问答对，整理成csv版本`
        ├── tongweb8.xlsx               `NotebookLM关于参数调优的问答对，整理成xlsx版本`
    ├── 用户手册                  `将原有的PDF格式的用户手册整理成易读的csv/markdown文档`
        ├── TongWeb_00.csv              `000_TongWeb_V8.0产品对比手册的csv格式`
        ├── TongWeb_01.csv              `001_TongWeb_V8.0产品介绍手册的csv格式`
        ├── TongWeb_02.csv              `002_TongWeb_V8.0安装与使用指引的csv格式`
        ├── TongWeb_04.csv              `004_TongWeb_V8.0命令行工具手册的csv格式`
        ├── TongWeb_05.csv              `005_TongWeb_V8.0REST API手册的csv格式`
        ├── TongWeb_06.csv              `006_TongWeb_V8.0常见问题手册的csv格式`
        ├── TongWeb_07.csv              `007_TongWeb_V8.0安全加固手册的csv格式`
        ├── TongWeb_08.csv              `008_TongWeb_V8.0容器化部署手册的csv格式`
        ├── TongWeb8_00.md              `000_TongWeb_V8.0产品对比手册的markdown`
        ├── TongWeb8_01.md              `001_TongWeb_V8.0产品介绍手册的markdown`
        ├── TongWeb8_02.md              `002_TongWeb_V8.0安装与使用指引的markdown`
        ├── TongWeb8_03A.md             `003_TongWeb_V8.0安装与使用指引的markdown（第1~344页）` 
        ├── TongWeb8_03B.md             `003_TongWeb_V8.0安装与使用指引的markdown（第345~末页）`
        ├── TongWeb8_04.md              `004_TongWeb_V8.0命令行工具手册的markdown`
        ├── TongWeb8_05.md              `005_TongWeb_V8.0REST API手册的markdown`
        ├── TongWeb8_06.md              `006_TongWeb_V8.0常见问题手册的markdown`
        ├── TongWeb8_07.md              `007_TongWeb_V8.0安全加固手册的markdown`
        ├── TongWeb8_08.md              `008_TongWeb_V8.0容器化部署手册的markdown`
    ├── CSDN 爬虫                 `将CSDN链接的文章爬虫得到markdown文档，并合并成txt文档`
        ├── csdn_tongweb                 `从 CSDN 链接上爬下来的原始markdown格式的文档` 
        ├── tongweb_csdn_combined.txt    `将爬下来的所有有效的markdown文档合并成一个txt文件`
    ├── Dify                      `Dify平台上的智能体相关配置文件`
        ├── 工具插件配置                  `针对Dify配置了Word和Markdown文档生成工具`
        ├── prompt.md                    `Dify平台的智能体Prompt配置`
        ├── TongWeb8人工智障.yml          `Dify平台的智能体源文件，可直接在Dify上打开`
    ├── Prompt                     `提示词原文`
        ├── Prompt01.md~Prompt04.md      `4款提示词，已经上传至智能体网站172.16.80.85的模板`
    ├── 整理好的其他知识库          `针对同事整理的QA对做了一些优化`
        ├── BK_plus.csv                  `针对同事的QA对使用NotebookLM设计的25个问题`
        ├── BK_plus.xlsx                 `针对同事的QA对使用NotebookLM设计的25个问题，xlsx格式` 
        ├── tongweb_csdn_final.csv       `CSDN上的整理出的问题对，爬虫后合并成csv文档格式`
        ├── TongWeb_Final_Table.csv      `针对同事的QA对，整理成的csv文档`
        ├── TongWeb_Knowledge_Base.csv   `针对同事的QA对，整理成的csv文档`
        ├── TW8_Expert_Knowledge_Clean.csv`针对同事的QA对，整理成的csv文档`
    ├── 总结文档                    `两次会议的总结文档，开会时间2026.1.28和2026.2.6`
        ├── 第二次总结2.pdf               `主要介绍Dify智能体搭建，PDF转换等方面的设计思路`
        ├── 第一次总结1.pdf               `主要介绍平台智能体测试情况，以及提示词配置的思路` 
```

# 2. 工作总结
# 2.1 针对知识库整理和 Dify 智能体搭建
在本月，我们完成了以下工作内容：
【知识库整理】
1. 我们发现TongWeb智能体平台`172.16.80.85`对csv文档的分片效果最好，针对同事先前的QA对全部整理成csv文档的格式，并且完成切片上传至`172.16.80.85`>`管理中心`->`知识库管理`->`智能体知识库Emol`。
2. 针对不同格式的文档，我们建立出如下的处理方式：
（1） word 文档：直接通过脚本转化成csv，示例脚本如下：
 ```python
        import docx2txt
        import csv
        import os
        import re

        # --- 配置区 ---
        input_docx = "TongWeb一般参数集.docx" 
        output_csv = "TongWeb_Knowledge_With_Images.csv"
        image_folder = "./images"
        if not os.path.exists(image_folder):
            os.makedirs(image_folder)
        # 1. 提取文字和图片
        text = docx2txt.process(input_docx, image_folder)
        # --- 核心修改逻辑：图片编号对齐 ---
        img_counter = 1
        def replace_image_placeholder(match):
            global img_counter
            # 构造带编号的图片标签
            replacement = f" [参考图片: image{img_counter}.png] "
            img_counter += 1
            return replacement
        # 将所有的 <照片路径转换> 替换为带编号的标签
        # 注意：docx2txt 提取的图片命名规则默认就是 image1.png, image2.png...
        text = re.sub(r'<照片路径转换>', replace_image_placeholder, text)
        # 2. 按照“问题：”切分知识点
        chunks = re.split(r'问题：', text)
        # 3. 结构化处理并写入 CSV
        with open(output_csv, 'w', newline='', encoding='utf-8-sig') as f:
            writer = csv.writer(f)
            writer.writerow(['Question', 'Answer']) # 写入表头
            for chunk in chunks:
                if not chunk.strip():
                    continue                  
                if "答案：" in chunk:
                    try:
                        # 以“答案：”为界拆分
                        parts = chunk.split("答案：")
                        q_content = parts[0].strip()
                        
                        # 清理答案内容：
                        # 1. 移除末尾的长横线
                        # 2. 处理可能存在的 ||| 分隔符
                        raw_a_content = parts[1]
                        # 兼容处理：遇到长横线或 ||| 就截断
                        a_content = re.split(r'-{10,}|\|\|\|', raw_a_content)[0].strip()
                        
                        if q_content and a_content:
                            writer.writerow([q_content, a_content])
                    except Exception as e:
                        print(f"⚠️ 跳过一个格式异常的块: {e}")
        print(f"转换完成！")
 ```
（2）excel 文档：可以直接把后缀名称改成`.csv`
（3）PDF 文档：原文可以参见`总结文档`->`第二次总结2.pdf`
    1. PDF解析成Markdown格式的文档通过网站`https://mineru.net/`进行直接转化；
    2. 去掉换行通过Vsocde`正则表达式`替换实现，查找`([^\n])\n+([^\n#])`并替换为`$1\n$2`；
    3. 将去掉换行的Markdown文档进一步删除目录，前言之类的多余的东西；
    4. 整理文档标题，请确保最终的标题格式形如`# 一级序号.二级序号.三级序号`或者`#, ##, ###`来区分不同类型的标题，脚本会根据#的数量或者#和后续编号的数量自动识别标题；
    5. 运行python脚本，填入当前markdown文档名称个转换出来的csv文档名称。
    python脚本路径：`TongWeb8知识库\用户手册\transfer_csv.py`。
    （4）Markdown 文档：可以直接调用PDF文档转换最后一步的脚本，python脚本路径：`TongWeb8知识库\用户手册\transfer_csv.py`。

【提示词设计】
3. 针对TongWeb8的智能体设计了4款提示词，这四款提示词核心使用`ToT`思维树的格式，旨在引导我们的大模型可以像人思考问题时，采用多种不同的思维路径，然后筛选出可行性最高的路径。ToT的灵感来源于Mircosoft推出的`Copilot`大模型中的`Real Talk`模式，他会根据用户的问题，结合用户的性格（通过先前提问形成的短期记忆）给出不同的路径`Fork A, Fork B, Fork C`，然后选出最可能的路径完成整个思考过程。

【Dify智能体搭建】
4. 在 Dify 上搭建了一个智能体，可以实现TongWeb常见运营问题解答，复杂情景的故障排除等，并且通过插件工具生成`word`或者`markdown`文档的报告，且返还一个`URL`下载地址，用户可以直接点击链接完成报告的下载，具体的Dify配置流程可以参加`总结文档`->`第二次总结2.pdf`。
### 相关配置文件说明：
（1）dify_main.py ：这是通过`本机8000端口`接收LLM的数据，并且生成`word文档`和`URL下载地址`；
（2）dify_main2.py：这是通过`本机8001端口`接收LLM的数据，并且生成`markdown文档`和`URL下载地址`；
（3）wordgenerator.jsonc: 这是在 Dify 上配置`word文档下载`工具的json代码；
（4）markdownGenerator.jsonc 这是在 Dify 上配置`markdown文档下载`工具的json代码；

# 2.2 针对TongWeb8平台的智能体搭建（补充）
因为Tongweb8平台的智能体背后的LLM没有上下文记忆功能，因此我们很难通过知识库文件直接让他生成一个很好的答案，所以我们在原有知识库的基础上`设计了若干个复杂情景的问答对`，这样在知识库检索时，若检索到相关的分片并且返还给LLM，就可以使得LLM有`参考案例`和`思路借鉴`，从而提升答案的质量。
自己整理的补充知识库遵从QA对的设计原则，涵盖：
1. `关键词描述`：使用1~2个关键术语来概括复杂情景/问题，便于知识库快速检索和精准匹配；
2. `问题描述`  ：设计一个实际生产情景，描述遇到的问题，要求给出一个合理的解决方案；
3. `思考路径`  : 大致的路径为`问题拆分`->`知识库检索（检索哪方面的知识）`->`检索推理（根据检索的内容可以得到什么样的结论，如何得到的）`
4. `最终答案`  : 给出最终的解决方式。
相关文件可以查阅:
1. `TongWeb8知识库\通道日志数据源参数问答对\tongweb8.csv`： 这是从数据源，通道，日志三个维度设计的性能调优问答对，共计`160`个问答对；
2. `TongWeb8知识库\整理好的其他知识库\BK_plus.csv`：这是根据先前同事整理的文档设计的复杂情景下的问答对，核心是要求LLM从多个文件检索相关知识并进行融合，共计`25`个问答对。

上述工作由本人和Google旗下的`NotebookLM`大模型共同完成，`NotebookLM`的网站为：[NotebookLM 官网](https://notebooklm.google.com/)

# 2.3 CSDN文档汇总（补充）
1. 首先我们通过爬虫脚本将`https://blog.csdn.net/realwangpu`和 `https://blog.csdn.net/weixin_39938069`两个CSDN链接的相关`TongWeb`文章爬取下来，整理成`markdown`文档；
爬虫脚本请参考`TongWeb8知识库\CSDN爬虫\main.py`。
2. 使用脚本整理成txt文档，参考脚本如下。
```python
import os
import re
INPUT_DIR = r'file_path'     # 修改成自己的文件夹路径
OUTPUT_TXT = 'tongweb_csdn_combined.txt'
def clean_title(title):
    title = re.sub(r'^原创[|\s]*', '', title)
    title = re.sub(r'^\[原创\]', '', title)
    title = re.sub(r'^原文\s*', '', title)
    return title.strip()
def clean_content(text):
    lines = text.splitlines()
    cleaned_lines = []
    in_code_block = False
    empty_line_count = 0
    
    for line in lines:
        stripped = line.rstrip()
        if stripped.startswith('```'):
            in_code_block = not in_code_block
            cleaned_lines.append(stripped)
            empty_line_count = 0
            continue
        
        if in_code_block:
            if stripped == '':
                if empty_line_count < 1:
                    cleaned_lines.append('')
                    empty_line_count += 1
            else:
                cleaned_lines.append(stripped)
                empty_line_count = 0
        else:
            if stripped == '':
                empty_line_count += 1
                if empty_line_count <= 2:
                    cleaned_lines.append('')
            else:
                cleaned_lines.append(stripped)
                empty_line_count = 0
    
    content = '\n'.join(cleaned_lines).strip()
    content = re.sub(r'\n{4,}', '\n\n', content)
    return content if content else '（正文内容为空）'

# 常见关键词
problem_keywords = ['问题', '简介', '背景', '现象', '描述', '场景', '问题描述', '故障现象']
solution_keywords = ['解决方法', '解决方案', '处理方式', '操作步骤', '配置方法', '应用场景', '解决步骤', '处理步骤']

# 主流程
records = []
skip_files = ['README.md']

for filename in os.listdir(INPUT_DIR):
    if filename.endswith('.md') and filename not in skip_files:
        filepath = os.path.join(INPUT_DIR, filename)
        
        with open(filepath, 'r', encoding='utf-8') as f:
            raw_text = f.read()
        
        full_title = filename.replace('.md', '')
        title_clean = clean_title(full_title)
        
        # 提取原文链接
        url_match = re.search(r'(原文链接|来源|链接)[:：]?\s*(https?://[^\s\n]+)', raw_text, re.IGNORECASE)
        original_url = url_match.group(2).strip() if url_match else ''
        
        # 去除标题行和链接行
        content = re.sub(r'^# .*\n', '', raw_text, count=1, flags=re.MULTILINE)
        content = re.sub(r'原文链接[:：]?.*\n', '', content, flags=re.IGNORECASE)
        content = re.sub(r'来源[:：]?.*\n', '', content, flags=re.IGNORECASE)
        
        # 默认fallback
        problem = title_clean
        solution = clean_content(content)
        
        # 尝试拆分小节
        sections = re.split(r'(^## .*?$)', content, flags=re.MULTILINE)
        sections = [s.strip() for s in sections if s.strip()]
        
        if len(sections) >= 3:
            problem_found = False
            
            for i in range(0, len(sections), 2):
                section_title_raw = sections[i]
                section_title = section_title_raw.replace('##', '').strip()
                section_content = sections[i+1] if i+1 < len(sections) else ''
                
                if not problem_found and any(kw in section_title for kw in problem_keywords):
                    problem = f"{section_title}\n{clean_content(section_content)}"
                    problem_found = True
                    continue
                
                if any(kw in section_title for kw in solution_keywords):
                    remaining_sections = sections[i:]
                    solution_text = []
                    for j in range(0, len(remaining_sections), 2):
                        st = remaining_sections[j].replace('##', '').strip()
                        sc = remaining_sections[j+1] if j+1 < len(remaining_sections) else ''
                        if st:
                            solution_text.append(f"## {st}")
                        if sc:
                            solution_text.append(clean_content(sc))
                    solution = '\n\n'.join(solution_text).strip()
                    break
            
            if problem_found and solution == clean_content(content):
                solution = clean_content('\n\n'.join(sections[i+2:])) if 'i' in locals() else clean_content(content)
        
        records.append({
            '问题': problem,
            '解决方法': solution,
            '关键字': title_clean,
            '文档来源': original_url
        })

# 排序（按关键字）
records.sort(key=lambda x: x['关键字'])

# 写入TXT
with open(OUTPUT_TXT, 'w', encoding='utf-8') as f:
    for idx, rec in enumerate(records, start=1):
        num = f"{idx:03d}"  # 001, 002...
        f.write(f"问题编号: {num}\n")
        f.write(f"问题: {rec['问题']}\n\n")
        f.write(f"解决方法:\n{rec['解决方法']}\n\n")
        f.write(f"关键字: {rec['关键字']}\n")
        f.write(f"文档来源: {rec['文档来源']}\n")
        f.write("-" * 80 + "\n\n")  # 分隔线

print(f"处理完成！共 {len(records)} 条记录")
```
3. 如果还想进一步整理成csv文档并直接上传至知识库，可参考下面的脚本。
```python
import csv
import os
import re

TXT_PATH =   "file_path"         # 填入自己的文件路径
OUTPUT_CSV = 'tongweb_csdn_final_version2.csv'   
# 检查文件是否存在
if not os.path.exists(TXT_PATH):
    print(f"错误：文件 {TXT_PATH} 不存在！请检查路径。")
    exit()
with open(TXT_PATH, 'r', encoding='utf-8') as f:
    text = f.read()
# 分隔符（80个-）
SEPARATOR = '-' * 80
# 拆分记录（去除空块）
blocks = [block.strip() for block in text.strip().split(SEPARATOR) if block.strip()]

rows = []

for block in blocks:
    lines = [line.rstrip() for line in block.split('\n')]
    current = {
        '问题编号': '',
        '问题': '',
        '解决方法': '',
        '关键字': '',
        '文档来源': ''
    } 
    key = None  # 当前正在追加的多行字段 
    for line in lines:
        if line.startswith('问题编号: '):
            current['问题编号'] = line.replace('问题编号: ', '').strip()
            key = None
        elif line.startswith('问题: '):
            current['问题'] = line.replace('问题: ', '').strip()
            key = '问题'  # 问题可能多行
        elif line.startswith('解决方法:'):
            # 解决方法开头，可能有冒号后内容
            value = line.replace('解决方法:', '').lstrip()
            current['解决方法'] = value
            key = '解决方法'  # 开始追加多行
        elif line.startswith('关键字: '):
            current['关键字'] = line.replace('关键字: ', '').strip()
            key = None
        elif line.startswith('文档来源: '):
            current['文档来源'] = line.replace('文档来源: ', '').strip()
            key = None
        elif key and line:  # 多行追加（包括空行，但rstrip已去右空格）
            current[key] += '\n' + line
    # 清理解决方法开头可能的多余空行
    current['解决方法'] = current['解决方法'].strip()

    if current['问题编号']:
        rows.append(current)

# 写入CSV（utf-8-sig防Excel乱码）
with open(OUTPUT_CSV, 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['问题编号', '问题', '解决方法', '关键字', '文档来源'])
    writer.writeheader()
    writer.writerows(rows)

print(f"转化完成！共 {len(rows)} 条记录。")





