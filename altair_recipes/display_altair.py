from IPython.core.display import display, HTML


def display_html(x):
    return display(HTML(x))


display_html("""
<script src="https://cdn.jsdelivr.net/npm/vega@3"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-lite@2"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-embed@3"></script>
""")


def display_altair_chart(x):
    display_html("""
 <div id="vis"></div>
  <script type="text/javascript">
    var spec = """ + x.to_json() + """;
    var opt = {"renderer": "canvas", "actions": false};
    vegaEmbed("#vis", spec, opt);
  </script>
  """)
