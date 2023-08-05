# Typography

* **Bold**
* _Italic_
* **_Bold italic_**.
* Super^script^
* Sub~script~

# Numbers

* Normal: 0123456789
* Math: $0123456789$


# Acronyms

\acrodef{CMU}{Carnegie Mellon University}
\acrodef{USA}{United States of America}
\acrodef{SSN}{social security number}

* Default (short+long): \ac{CMU}
* Repeated (short): \ac{CMU}
* Forced short: \acs{USA}
* Repeated after forced short (short+long): \ac{USA}
* Plural: \acp{SSN}


# Math

\newcommand{\PP}[2]{\mathbb{P}_{#1}\left[{#2}\right]}
\newcommand{\XX}{\mathcal{X}}
\newcommand{\EE}[2]{\mathbb{E}_{#1}\left[{#2}\right]}

$$
\int_0^\infty \exp^{-x^2}\,\mathrm{d}x
$$ {#eq:ex1}

$$
a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z,
0, 1, 2, 3, 4, 5, 6, 7, 8, 9
$$ {#eq:ex2}

* Inline: $\int_0^\infty \exp^{-x^2}\,\mathrm{d}x$
* Block: @eq:ex1, @eq:ex2
* Commands defined in body (P[x in X]): $\PP{}{x \in \XX}$
* Aligned:

$$
\begin{aligned}
    x &= 1\\
    x + y &= 10\\
    x + y + z &= 100
\end{aligned}
$$


# Links

* Section: @sec:ex1, @sec:ex1.2
* Appendix section: @sec:app2ex1, @sec:app1ex1.1.1
* Appendix figure: @fig:app1ex1
* Appendix table: @tbl:app2ex1
* Appendix math: @eq:app2ex2
* Pointer to footnote[^1][^2] text

[^1]: Example footnote text.
[^2]: Integer at enim eu tellus malesuada scelerisque. Ut sed rhoncus ipsum, at tempor
      nisl. Vivamus vitae pulvinar leo, at pharetra massa. Ut lobortis odio non nulla
      tincidunt pulvinar.

# Citations

* Short citation[@latex:companion]
* Short citation with pre note[see @latex:companion]
* Short citation with locator[@latex:companion, p. 1]
* Short citation with post note[@latex:companion, for more]
* Short citation with locators and pre/post notes[see @latex:companion, chap. 1-4, for more]
* Long citation: @lesk:1977
* Long citation with locator: @lesk:1977 [chap. 1]
* Long citation with note: @lesk:1977 [for more]
* Multi citation[@lesk:1977; @knuth:1984; @latex:companion]
* Multi citation with pre note[see @lesk:1977; @knuth:1984; @latex:companion]
* Multi citation with locators[@lesk:1977, sec. 1; @knuth:1984; @latex:companion, p. 1-3]
* Multi citation with post note[@lesk:1977; @knuth:1984; @latex:companion, for more]
* Multi citation with locators and pre/post notes[see @lesk:1977, p. 1; @knuth:1984; @latex:companion, chap. 1-2, for more]
