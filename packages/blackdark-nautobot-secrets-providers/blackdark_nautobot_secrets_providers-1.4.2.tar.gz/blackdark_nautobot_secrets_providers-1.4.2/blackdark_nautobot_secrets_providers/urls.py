"""Django urlpatterns declaration for blackdark_nautobot_secrets_providers plugin."""
from blackdark_nautobot_secrets_providers import views
from django.urls import path

app_name = "blackdark_nautobot_secrets_providers"

urlpatterns = [
    path("", views.SecretsProvidersHomeView.as_view(), name="home"),
]
