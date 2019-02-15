"""Allow including vega graphics in pweave docs."""
from IPython.core.display import display_html
import hashlib
from enum import Enum


Output = Enum("Output", "pweave_md pweave_html")

has_preamble = False


def to_html(plot):
    """Generate html from plot for inclusion in md or html doc."""
    global has_preamble
    json = plot.to_json()
    id = "A" + hashlib.sha256(json.encode()).hexdigest()
    html = (
        (
            ""
            if has_preamble
            else """
<script src="https://cdn.jsdelivr.net/npm/vega@3"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-lite@2"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-embed@3"></script>
 """
        )
        + """<div id="{id}"></div>
  <script type="text/javascript">
    var spec = {json};
    var opt = {{"renderer": "canvas", "actions": false}};
    vegaEmbed("#{id}", spec, opt);
  </script>
  """.format(
            id=id, json=json
        )
    )
    has_preamble = True
    return html


def show(plot, output=Output.pweave_md):
    """
    Include an Altair (vega) figure in Pweave document.

    Generates html output.
    """
    html = to_html(plot)
    if output == Output.pweave_md:
        display_html(html, raw=True)
    else:
        print(html)


def show_test(f):
    """Display a test decorated with viz_reg_test."""
    show(f(None))
