"""Plugin UI views for Secrets Providers."""

from blackdark_nautobot_secrets_providers import secrets
from django.views.generic import TemplateView


class SecretsProvidersHomeView(TemplateView):
    """Plugin home page for Secrets Providers."""

    template_name = "blackdark_nautobot_secrets_providers/home.html"

    def get_context_data(self, **kwargs):
        """Inject `secrets_providers` into template context."""
        ctx = super().get_context_data(**kwargs)
        ctx["secrets_providers"] = secrets.secrets_providers
        return ctx
