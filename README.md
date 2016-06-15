# Personalize-Your-SublimeText-for-Latex
This repo aims at creating an efficient environment for Latex writing using Sublime Text 2/3 with LaTeXtools and Bracket Highlighter on OSX and Windows

## Features:
1. Almost all frequently used packages are included: ams* for math-typing, tikz/pgf for drawing and plotting, algorithm2e for algorithm.
2. All kinds for brackets are outline highlighted by different color, there are several useful shortcuts:

    | shortcut        |              function              |
    |-----------------|:----------------------------------:|
    | super+alt+up    | select contents in current bracket |
    | super+alt+left  |     move cursor to left bracket    |
    | super+alt+right |    move cursor to right bracket    |

3. Useful short macros for math-typping: adaptive-size brackets, frequently used operators, all theorem environments
4. Auto completion for short macros: for more detail see LaTeXTools/LaTeX math.sublime-completions and LaTeXTools/LaTeX math.sublime-completions and LaTeXTools/LaTeX.sublime-completions

    | snippet trigger     | environment or macro              | description                                        |
    |---------------------|-----------------------------------|----------------------------------------------------|
    | eq/eqn              | equation/equation*                | single line equation without/with numbering        |
    | al/aln              | IEEEeqnarray/IEEEeqnarray*        | multiline equation without/with numbering          |
    | eqnhead             | IEEEeqnarraymulticol              | used for multiline case when LHS too long          |
    | item/enum           | itemize/enumerate                 | itemization/enumeration environment                |
    | thm/pps/crl/lem/def | all kinds of theorem environment  | theorem/proposition/corollary/lemma/definition     |
    | prf/sln             | proof environment                 | proof/solution                                     |
    | rd/sq/cl/ag         | \rd(sq/cl/ag)brs{  }              | round/square/curly/angle brace                     |
    | rdv/sqv/clv/agv     | \rd(sq/cl/ag)brsv{  }             |  round/square/curly/angle brace with "|" delimiter |
    | fr/fd/fp            | \frac{}{}, \fracd{}{}, \fracp{}{} | fraction, derivative, partial derivative           |
    | lim/amax/amin       | \limit{}, \argmax{}, \argmin{}    | limit, argmax, argmin                              |
5. Templates for frequently used figures with snippets: tree, markov chain, graph, factor graph, algebra diagram and plot. Shortcuts for the snippets:

    | snippet trigger | template                                     |
    |-----------------|----------------------------------------------|
    | plot            | pgfplots for function and sequence of points |
    | tikz-diag       | algebra diagram                              |
    | tikz-markov     | Markov chain                                 |
    | tikz-fg         | factor graph                                 |
    | tikz-tree       | probability tree                             |
    | tikz-graph      | graph                                        |


### Reason for using IEEEeqnarray instead align for multiline equations:
There are several environments for multiline equations, I prefer the environment which satisfies
* have full control on every line of equation
* backward search for SyncTex jumps to correct line
* consistency of indentation with other math environments, no overlapping between equation and numbering, etc. For more details refer to http://moser-isi.ethz.ch/docs/typeset_equations.pdf

Here is a simple table for comparison among several environments:

| environment      | equation numbering | SyncTex support      | remark              |
|------------------|--------------------|----------------------|---------------------|
| align            | every line         | jump to end          |                     |
| equation+aligned | only one           | jump to correct line |                     |
| eqnarray         | every line         | jump to correct line | have many drawbacks |
| IEEEeqnarray     | every line         | jump to correct line |                     |

# Installation:
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
7. When you write a new tex file, put tex_macros.tex at same directory and type "\input{tex_macros}" before importing any other packages.
