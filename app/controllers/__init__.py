def blueprints():
    from .dashboards import bp as dashboards_bp
    from .exames import bp as exames_bp
    from .questoes import bp as questoes_bp
    from .professor import bp as professor_bp
    return [dashboards_bp, exames_bp, professor_bp, questoes_bp]
