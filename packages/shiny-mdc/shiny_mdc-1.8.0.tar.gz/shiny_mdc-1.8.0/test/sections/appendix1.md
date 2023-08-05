# Appendix 1 {#sec:app1ex1}

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam nisi purus,
bibendum non neque sed, lacinia tristique tortor. Vestibulum eu lectus sed velit
luctus varius. Sed sollicitudin ligula ante. Integer porta a erat commodo
dignissim. Duis et lectus diam. Nulla id erat vestibulum nisi placerat
efficitur. Nulla a semper libero. Praesent pharetra ullamcorper massa vel
tincidunt. Sed dignissim magna et tellus efficitur, vitae sollicitudin lorem
tincidunt. Nam non velit et enim rutrum euismod.

## Appendix subsection

### Appendix subsubsection {#sec:app1ex1.1.1}

Proin eleifend lorem semper, commodo tellus nec, porta purus. Nullam commodo
lectus nibh, consequat maximus lorem faucibus in. Nam purus eros, rutrum in
sapien et, condimentum lacinia nibh.

## Appendix figures

![Extra wide figure](figures/densities){#fig:app1ex1 width=7.5in}

<div id="fig:app1ex2">

![Figure with non-default extension](figures/lines.png){width=2in}

![Sub-figure](figures/gaussian2d){width=3in}

![Sub-figure](figures/anscombe){width=4in}

Sub-figures with large combined size.
</div>

* @fig:app1ex1
* @fig:app1ex2

## Appendix includes

* Commands from metadata include (argmin R): <!-- $\argmin$ $\R$ -->
* Include command in body  (there should be text after this):

{% include utils/ext.md %}

## Appendix links

* Appendix section: @sec:app1ex1.1.1, @sec:app2ex1
* Main body section: @sec:ex1
* Main body figure: @fig:ex1
* Main body table: @tbl:ex1
* Main body equation: @eq:ex1
* Citation: @knuth:1984
