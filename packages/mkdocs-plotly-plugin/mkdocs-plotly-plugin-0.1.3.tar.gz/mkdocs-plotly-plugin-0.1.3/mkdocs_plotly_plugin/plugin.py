import os

from mkdocs.plugins import BasePlugin
from mkdocs import utils
from mkdocs.exceptions import PluginError
from bs4 import BeautifulSoup
from mkdocs.config import config_options
from flatten_dict import flatten
import json

from mkdocs_plotly_plugin.fences import fence_plotly

base_path = os.path.dirname(os.path.abspath(__file__))
print(base_path)

CUSTOM_FENCES = [
    {"name": "plotly", "class": "plotly-chart", "format": fence_plotly}]

TEMPLATES = ["plotly", "plotly_min", "plotly_dark_min", "plotly_white", "plotly_dark",
                        "ggplot2", "seaborn", "simple_white", "none"]


class PlotlyChartsPlugin(BasePlugin):
    config_scheme = (
        ("lib_path", config_options.Type(str, default='')),
        ("template_default", config_options.Type(str, default='plotly_min')),
        ("template_slate", config_options.Type(str, default='plotly_dark_min')),
        ("enable_template", config_options.Type(bool, default=True))
    )

    def on_config(self, config, **kwargs):
        # Make sure custom fences are configured.
        custom_fences = (
            config.get("mdx_configs", {})
            .get("pymdownx.superfences", {})
            .get("custom_fences", {})
        )
        if not custom_fences:
            raise PluginError(
                "[mkdocs_plotly_plugin]: You have not configured any custom fences, please see the setup instructions."
            )

    def on_post_page(self, output, page, config, **kwargs):
        """Add javascript script tag, javascript code, and template json to initialize Plotly"""
        soup = BeautifulSoup(output, "html.parser")
        if not soup.find("div", class_="mkdocs-plotly"):
            return output

        lib_link = soup.new_tag("script")
        if self.config['lib_path'] == "":
            lib_url = "https://cdn.plot.ly/plotly-latest.min.js"
        else:
            lib_url = utils.get_relative_url(
                utils.normalize_url("assets/javascripts/plotly.min.js"),
                page.url
            )
        lib_link.attrs['src'] = lib_url
        soup.head.append(lib_link)
        docs_dir = config['docs_dir']

        if self.config['enable_template']:
            if self.config['template_default'] in TEMPLATES:
                template_default_file = os.path.join(
                    base_path, "templates", f"{self.config['template_default']}.json")
            else:
                template_default_file = os.path.join(
                    docs_dir, self.config['template_default'])
            if self.config['template_slate'] in TEMPLATES:
                template_slate_file = os.path.join(
                    base_path, "templates", f"{self.config['template_slate']}.json")
            else:
                template_slate_file = os.path.join(
                    docs_dir, self.config['template_slate'])

            def create_template_span(span_id, template_file):
                """
                Create a span element which holds the default templates for plotly charts.
                We flatten the template so that plotly only updates specified attributes
                only and doesn't replace the entire sub-object.
                https://plotly.com/javascript/plotlyjs-function-reference/#plotlyrestyle
                The template json file can be nested to improve readability.
                """
                template_span = soup.new_tag('span')
                template_span.attrs['id'] = span_id
                template_span.attrs['hidden'] = True
                with open(template_file) as f:
                    template_dict = json.load(f)

                template_dict = flatten(template_dict, reducer='dot')
                # json dumps will make the json str short to reduce size of html doc
                template_span.string = json.dumps(template_dict)
                return template_span

            template_default = create_template_span('default-template-settings', template_default_file)
            soup.body.append(template_default)

            template_slate = create_template_span('slate-template-settings', template_slate_file)
            soup.body.append(template_slate)

        js_code = soup.new_tag("script")
        js_code.attrs['src'] = utils.get_relative_url(
            utils.normalize_url("assets/javascripts/mkdocs-plotly-plugin.js"),
            page.url
        )
        soup.body.append(js_code)

        return str(soup)

    def on_page_content(self, html, page, config, **kwargs):
        """Update datapath to be relative to the docs dir
        """
        soup = BeautifulSoup(html, "html.parser")
        charts = soup.find_all("div", class_="mkdocs-plotly")
        for chart in charts:
            if chart.attrs.get('data-jsonpath'):
                chart.attrs['data-jsonpath'] = utils.get_relative_url(
                    utils.normalize_url(
                        chart.attrs['data-jsonpath']),
                    page.url
                )
        return str(soup)

    def on_post_build(self, config, **kwargs):
        """
        Copy javascript lib and init code to assets
        """
        output_base_path = os.path.join(config["site_dir"], "assets")
        utils.copy_file(
            os.path.join(base_path, "javascripts", "mkdocs-plotly-plugin.js"),
            os.path.join(output_base_path, "javascripts",
                         "mkdocs-plotly-plugin.js"),
        )
        docs_dir = config['docs_dir']
        if self.config['lib_path'] != '':
            utils.copy_file(
                os.path.join(docs_dir, self.config['lib_path']),
                os.path.join(output_base_path, "javascripts", "plotly.min.js"),
            )
