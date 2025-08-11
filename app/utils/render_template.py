from pathlib import Path
from jinja2 import Environment, FileSystemLoader, select_autoescape

def email_template(template_name: str, context: dict):
    templates_dir = Path("app/templates/emails").resolve()
    jinja_env = Environment(
        loader=FileSystemLoader(str(templates_dir)),
        autoescape=select_autoescape(
            enabled_extensions=["html"]
        )
    )

    template = jinja_env.get_template(template_name)
    return template.render(context)
