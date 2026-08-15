import json

import azure.functions as func


FUNCTIONS = {
    "/api/invoice": {
        "get": {
            "summary": "Get invoice data",
            "responses": {"200": {"description": "Invoice record"}},
        }
    },
    "/api/shipping": {
        "get": {
            "summary": "Get shipping data",
            "responses": {"200": {"description": "Shipping record"}},
        }
    },
    "/api/product": {
        "get": {
            "summary": "Get product data",
            "responses": {"200": {"description": "Product record"}},
        }
    },
    "/api/vendor": {
        "get": {
            "summary": "Get vendor data",
            "responses": {"200": {"description": "Vendor record"}},
        }
    },
}


def _swagger_spec():
    return {
        "openapi": "3.0.1",
        "info": {
            "title": "github_submodule_demo Functions",
            "version": "1.0.0",
            "description": "Local Swagger page for the sample Azure Functions project.",
        },
        "servers": [{"url": "http://localhost:7071"}],
        "paths": FUNCTIONS,
    }


def _swagger_ui_html():
    return """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Functions Swagger</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css" />
    <style>
      html {
        box-sizing: border-box;
        overflow: -moz-scrollbars-vertical;
        overflow-y: scroll;
      }
      *, *:before, *:after {
        box-sizing: inherit;
      }
      body {
        margin: 0;
        background: #fafafa;
        color: #333;
      }
      #app {
        max-width: 1200px;
        margin: 0 auto;
        padding: 20px;
      }
    </style>
  </head>
  <body>
    <div id="app"></div>
    <script src="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui-bundle.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui-standalone-preset.js"></script>
    <script>
      window.onload = () => {
        SwaggerUIBundle({
          url: location.origin + '/api/swagger/openapi.json',
          dom_id: '#app',
          deepLinking: true,
          layout: 'StandaloneLayout',
          presets: [
            SwaggerUIBundle.presets.apis,
            SwaggerUIStandalonePreset
          ],
          plugins: [
            SwaggerUIBundle.plugins.DownloadUrl
          ]
        });
      };
    </script>
  </body>
</html>
"""


def main(req: func.HttpRequest) -> func.HttpResponse:
    route_path = (req.route_params or {}).get("path", "")
    if route_path == "openapi.json":
        return func.HttpResponse(
            json.dumps(_swagger_spec()),
            mimetype="application/json",
            status_code=200,
        )

    return func.HttpResponse(_swagger_ui_html(), mimetype="text/html", status_code=200)
