#!/usr/bin/env python3
"""
Local live preview generator for GitHub Profile README.md
Generates a styled GitHub Dark Mode HTML file and opens it in your default browser.
"""

import os
import sys
import webbrowser
from pathlib import Path

REPO_DIR = Path(__file__).resolve().parent
README_PATH = REPO_DIR / "README.md"
OUTPUT_HTML = REPO_DIR / ".preview.html"

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en" data-color-mode="dark" data-dark-theme="dark">
<head>
  <meta charset="utf-8">
  <title>GitHub Profile Preview - amritkr1999</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.5.1/github-markdown-dark.min.css">
  <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
  <style>
    body {{
      box-sizing: border-box;
      margin: 0;
      padding: 30px 15px;
      background-color: #0d1117;
      color: #c9d1d9;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
    }}
    .container {{
      max-width: 900px;
      margin: 0 auto;
      background-color: #0d1117;
      border: 1px solid #30363d;
      border-radius: 8px;
      padding: 32px;
    }}
    .markdown-body {{
      background-color: transparent !important;
    }}
    .preview-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 24px;
      padding-bottom: 12px;
      border-bottom: 1px solid #30363d;
      font-size: 14px;
      color: #8b949e;
    }}
    .badge {{
      background: #238636;
      color: #ffffff;
      padding: 4px 10px;
      border-radius: 12px;
      font-weight: 600;
      font-size: 12px;
    }}
  </style>
</head>
<body>
  <div class="container">
    <div class="preview-header">
      <div><strong>amritkr1999</strong> / README.md</div>
      <div class="badge">Local Profile Preview</div>
    </div>
    <div id="content" class="markdown-body"></div>
  </div>
  <script>
    const markdownSource = {markdown_json};
    document.getElementById('content').innerHTML = marked.parse(markdownSource);
  </script>
</body>
</html>
"""

def main():
    if not README_PATH.exists():
        print(f"Error: Could not find {README_PATH}", file=sys.stderr)
        sys.exit(1)

    import json
    markdown_content = README_PATH.read_text(encoding="utf-8")
    html_content = HTML_TEMPLATE.format(markdown_json=json.dumps(markdown_content))

    OUTPUT_HTML.write_text(html_content, encoding="utf-8")
    print(f"Preview generated at: {OUTPUT_HTML}")
    webbrowser.open(OUTPUT_HTML.as_uri())

if __name__ == "__main__":
    main()
