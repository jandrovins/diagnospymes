from django.apps import AppConfig


class MmEvaluationConfig(AppConfig):
    name = 'mm_evaluation'

    # Register signals for models when starting app
    def ready(self):
        import mm_evaluation.signals
