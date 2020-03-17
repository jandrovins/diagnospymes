from django.apps import AppConfig


class MmEvaluationConfig(AppConfig):
    name = 'mm_evaluation'

    def ready(self):
        import mm_evaluation.signals
