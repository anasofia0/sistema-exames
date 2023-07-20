def blueprints():
    from .dashboards import bp as dashboards_bp
    from .exames import bp as exames_bp
    from .preencher import bp as preencher_bp
    return [dashboards_bp, exames_bp, preencher_bp]