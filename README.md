# Personalize-Your-SublimeText-for-Latex
This repo aims at creating an efficient environment for Latex writing using Sublime Text 2/3 with LaTeXtools and Bracket Highlighter on OSX and Windows

# How to use:
1. Your computer should have Latex support, you can install MiKTeX or Tex Live
2. Install PDF viewer supprting SyncTex, I recommend Skim for OSX and Sumatra for Windows
  * For Skim, go to Preference --> Sync, uncheck "Check for changes", for PDF-Tex Sync Support choose "Sublime Text 2" for ST2, and "Sublime Text" for ST3.
  * For Sumatra, go to Settings|Options, and enter "C:\Program Files\Sublime Text 2\sublime_text.exe" "%f:%l" for ST2, and "C:\Program Files\Sublime Text 3\sublime_text.exe" "%f:%l" for ST3
3. Install Sublime Text on your computer, install Package Control, refer https://packagecontrol.io/installation#st3
4. After installing Package Control, press cmd+shift+P, type "Package Control: Install Package", install "LaTeXtools" and "Bracket Highlighter"
5. If you are using Sublime Text 2, skip this step, otherwise 
  * Install "Package Resource Viewer" from Package Control
  * Press ctrl+shift+P, type "Package Resource Viewer: Extract Package", extract "LaTeXtools", "Bracket Highlighter", "LaTeX" and "Color Scheme - Default"
6. On Menu Preference --> Browse Packages, backup the original "Package" folder, merge the "Package" folder in this repo with the original one, (For sublime Text 2, use the folder "Package for Sublime 2")
