def blueprints():
    from .dashboards import bp as dashboards_bp
    return [dashboards_bp]