def blueprints():
    from .dashboards import bp as dashboards_bp
    from .exames import bp as exames_bp
    from .resposta_aluno import resposta_aluno_bp
    from .questoes import bp as questoes_bp
    return [dashboards_bp, exames_bp, resposta_aluno_bp, questoes_bp]