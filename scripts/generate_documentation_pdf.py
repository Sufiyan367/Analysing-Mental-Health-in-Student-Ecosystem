"""
Generate Publication-Grade PDF of Project Development Documentation
Reads docs/project_development_documentation.md, styles it with professional
print CSS, and generates evidence/documentation/Project_Documentation.pdf via Playwright.
"""

import os
import markdown
from playwright.sync_api import sync_playwright

def generate_pdf():
    doc_path = os.path.join('docs', 'project_development_documentation.md')
    output_dir = os.path.join('evidence', 'documentation')
    os.makedirs(output_dir, exist_ok=True)
    pdf_path = os.path.join(output_dir, 'Project_Documentation.pdf')

    with open(doc_path, 'r', encoding='utf-8') as f:
        md_text = f.read()

    # Convert markdown to html with tables support
    html_content = markdown.markdown(md_text, extensions=['tables', 'fenced_code'])

    # Wrap in professional academic styling
    styled_html = f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Analysing Mental Health in Student Ecosystem - Project Documentation</title>
  <style>
    @page {{
      size: A4;
      margin: 20mm 15mm 20mm 15mm;
      @bottom-right {{
        content: counter(page);
      }}
    }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      color: #1e293b;
      line-height: 1.5;
      font-size: 11pt;
    }}
    h1 {{
      color: #0f172a;
      font-size: 20pt;
      border-bottom: 2px solid #2563eb;
      padding-bottom: 6px;
      margin-top: 0;
    }}
    h2 {{
      color: #1e40af;
      font-size: 14pt;
      border-bottom: 1px solid #cbd5e1;
      padding-bottom: 4px;
      margin-top: 18pt;
      page-break-after: avoid;
    }}
    h3 {{
      color: #334155;
      font-size: 12pt;
      margin-top: 12pt;
      page-break-after: avoid;
    }}
    p, li {{
      font-size: 10pt;
      color: #334155;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      margin: 12pt 0;
      font-size: 8.5pt;
      page-break-inside: avoid;
    }}
    th {{
      background-color: #2563eb;
      color: #ffffff;
      font-weight: 600;
      padding: 6pt;
      text-align: left;
      border: 1px solid #1d4ed8;
    }}
    td {{
      padding: 5pt;
      border: 1px solid #cbd5e1;
      vertical-align: top;
    }}
    tr:nth-child(even) td {{
      background-color: #f8fafc;
    }}
    code {{
      background-color: #f1f5f9;
      padding: 1pt 3pt;
      border-radius: 3pt;
      font-family: "Consolas", monospace;
      font-size: 9pt;
      color: #0f172a;
    }}
    pre {{
      background-color: #0f172a;
      color: #f8fafc;
      padding: 8pt;
      border-radius: 4pt;
      font-size: 8pt;
      overflow-x: auto;
    }}
    pre code {{
      background-color: transparent;
      color: #f8fafc;
    }}
    hr {{
      border: none;
      border-top: 1px solid #e2e8f0;
      margin: 16pt 0;
    }}
    blockquote {{
      border-left: 3px solid #2563eb;
      padding-left: 8pt;
      margin: 8pt 0;
      color: #64748b;
    }}
  </style>
</head>
<body>
  {html_content}
</body>
</html>"""

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.set_content(styled_html, wait_until='networkidle')
        page.pdf(
            path=pdf_path,
            format='A4',
            print_background=True,
            margin={'top': '20mm', 'bottom': '20mm', 'left': '15mm', 'right': '15mm'}
        )
        browser.close()

    print(f"Generated printable PDF at: {pdf_path}")
    print(f"PDF file size: {os.path.getsize(pdf_path) / 1024:.2f} KB")

if __name__ == '__main__':
    generate_pdf()
