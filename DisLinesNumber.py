import os
import glob
import argparse
import fitz  # pip install PyMuPDF

def process_pdf(file_path, width):
    """处理PDF文件，应用红线遮盖效果"""
    try:
        doc = fitz.open(file_path)
    except Exception as e:
        print(f"无法打开文件 {file_path}：{e}")
        return

    for page in doc:
        # 定义遮盖区域：从页面左侧(0,0)到(width,页面高度)
        margin_rect = fitz.Rect(0, 0, width, page.rect.height)
        # 应用红线，彻底删除该区域内的内容
        page.add_redact_annot(margin_rect, fill=None)
        page.apply_redactions()

    # 修改后的PDF文件名为: 原文件名_output.pdf
    base, ext = os.path.splitext(file_path)
    output_path = f"{base}_output.pdf"
    try:
        doc.save(output_path)
        print(f"处理完成，已生成 {output_path}")
    except Exception as e:
        print(f"保存文件 {output_path} 时出错：{e}")
    finally:
        doc.close()

def main():
    parser = argparse.ArgumentParser(description="PDF文件遮盖处理工具")
    parser.add_argument("--width", type=int, default=50, help="遮盖区域的宽度，默认50")
    parser.add_argument("--file", help="指定输入的PDF文件路径")
    args = parser.parse_args()

    width = args.width

    if args.file:
        # 如果指定了PDF文件，则处理该文件
        process_pdf(args.file, width)
    else:
        # 没有指定PDF文件，则自动搜索当前文件夹内所有PDF文件
        pdf_files = glob.glob("*.pdf")

        if not pdf_files:
            print("当前文件夹内没有找到PDF文件，请将待处理文件复制到当前目录")
            return
        
        # 排除已处理的pdf文件
        pdf_files = [pdf for pdf in pdf_files if not pdf.endswith("_output.pdf")]
        if not pdf_files:
            print("所有PDF文件都已处理或没有可处理的PDF文件。注：脚本会自动屏蔽以_output.pdf结尾的已处理文件")
            return

        for pdf in pdf_files:
            process_pdf(pdf, width)

if __name__ == "__main__":
    main()
