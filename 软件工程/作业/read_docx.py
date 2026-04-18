import zipfile
import xml.etree.ElementTree as ET
import re

def read_docx(file_path):
    """读取docx文件内容"""
    with zipfile.ZipFile(file_path, 'r') as z:
        # 读取document.xml
        xml_content = z.read('word/document.xml')
        
        # 解析XML
        tree = ET.fromstring(xml_content)
        
        # 定义命名空间
        ns = {
            'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
        }
        
        # 提取所有文本
        texts = []
        for elem in tree.iter():
            if elem.tag == '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t':
                if elem.text:
                    texts.append(elem.text)
        
        return ''.join(texts)

# 读取文件
file_path = r'd:\Desktop\全文档\教材\大二下\大二下\软件工程\作业\《软件开发实践》报告-刘君南、覃富镇、包桂德(1).docx'
content = read_docx(file_path)

# 保存到文本文件
output_path = r'd:\Desktop\全文档\教材\大二下\大二下\软件工程\作业\report_content.txt'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"内容已保存到: {output_path}")
print(f"内容长度: {len(content)} 字符")
print("\n前2000字符预览:")
print(content[:2000])
