import re
import csv
import os

def markdown_to_robust_csv(input_file, output_file):
    if not os.path.exists(input_file):
        print(f"找不到文件: {input_file}")
        return

    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')
    qa_pairs = []
    header_stack = {}  # 存储层级路径
    current_content = []

    for line in lines:
        # 1. 识别标题：支持 # 3. 资料准备 或 # 3.1. 获取安装包
        # 正则解释：开头是#号，后面跟着可选的空格，再跟着数字序号（如3.1.2），最后是标题名
        header_match = re.match(r'^(#+)\s+((?:\d+\.)*\d*\.?)\s*(.*)', line)
        
        if header_match:
            # 保存之前的内容
            if header_stack and current_content:
                q_path = " -> ".join([header_stack[lvl] for lvl in sorted(header_stack.keys())])
                a_text = "\n".join(current_content).strip()
                if a_text:
                    qa_pairs.append([q_path, a_text])
            
            # 2. 确定真实的层级 (Level)
            hashes = header_match.group(1)
            index_num = header_match.group(2).strip('.') # 提取 3.1.2
            title_text = header_match.group(3).strip()
            
            # 鲁棒性逻辑：如果存在 3.1.2 这种序号，按序号的点数决定层级
            if index_num and any(char.isdigit() for char in index_num):
                # "3" 是 1 级, "3.1" 是 2 级, "3.1.2" 是 3 级
                actual_level = index_num.count('.') + 1
            else:
                # 如果没有数字序号，按 # 的数量决定层级
                actual_level = len(hashes)
            
            # 完整的标题名（带上序号更清晰）
            full_title = f"{index_num} {title_text}".strip() if index_num else title_text

            # 清理同级及下级标题
            levels_to_remove = [l for l in header_stack.keys() if l >= actual_level]
            for l in levels_to_remove:
                del header_stack[l]
            
            header_stack[actual_level] = full_title
            current_content = []
        else:
            # 收集内容（包括表格 HTML）
            if line.strip() or (current_content and current_content[-1].strip()):
                current_content.append(line)

    # 处理最后一段
    if header_stack and current_content:
        q_path = " -> ".join([header_stack[lvl] for lvl in sorted(header_stack.keys())])
        a_text = "\n".join(current_content).strip()
        if a_text:
            qa_pairs.append([q_path, a_text])

    # 写入 CSV
    with open(output_file, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Question', 'Answer'])
        writer.writerows(qa_pairs)
    
    print(f"转换成功！")
    print(f"最终生成 QA 对数量: {len(qa_pairs)}")

if __name__ == "__main__":

    markdown_file = 'TongWeb8_08.md'
    output_csv = 'tongweb8_08csv.csv'

    markdown_to_robust_csv(markdown_file, output_csv)