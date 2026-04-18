import PyPDF2
import os

def extract_pdf_text(pdf_path):
    """提取PDF文本内容"""
    text = ""
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)
        print(f"PDF总页数: {num_pages}")
        
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text += f"\n--- 第 {page_num + 1} 页 ---\n"
            text += page.extract_text()
    
    return text

# 读取PDF文件
pdf_path = r'd:\Desktop\全文档\教材\大二下\大二下\软件工程\作业\《软件开发实践》报告-刘君南、覃富镇、包桂德(1).pdf'

if os.path.exists(pdf_path):
    content = extract_pdf_text(pdf_path)
    
    # 保存到文本文件
    output_path = r'd:\Desktop\全文档\教材\大二下\大二下\软件工程\作业\pdf_content.txt'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"\n内容已保存到: {output_path}")
    print(f"内容长度: {len(content)} 字符")
    print("\n前3000字符预览:")
    print(content[:3000])
else:
    print(f"文件不存在: {pdf_path}")
