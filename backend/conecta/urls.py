from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from recrutamento.viewsets.resposta_candidato_skill_diferencial_viewsets import RepostaCandidatoSkillDiferencialViewSet
from rest_framework import routers

from recrutamento.viewsets import (
    AreaAtuacaoViewSet,
    BeneficioViewSet,
    CandidatoViewSet,
    CursoViewSet,
    FormacaoCandidatoViewSet,
    InstituicaoViewSet,
    PerguntaAbertaViewSet,
    RespostaAbertaViewSet,
    SkillCandidatoViewSet,
    SkillViewSet,
    VagaViewSet,
)

main_router = routers.DefaultRouter()

main_router.register(r"areas-atuacoes", AreaAtuacaoViewSet, basename="areas-atuacoes")
main_router.register(r"beneficios", BeneficioViewSet, basename="beneficios")
main_router.register(r"candidatos", CandidatoViewSet, basename="candidatos")
main_router.register(r"cursos", CursoViewSet, basename="cursos")
main_router.register(
    r"formacoes-candidatos", FormacaoCandidatoViewSet, basename="formacoes-candidatos"
)
main_router.register(r"instituicoes", InstituicaoViewSet, basename="instituicoes")
main_router.register(
    r"perguntas-abertas", PerguntaAbertaViewSet, basename="perguntas-abertas"
)
main_router.register(
    r"respostas-abertas", RespostaAbertaViewSet, basename="respostas-abertas"
)
main_router.register(
    r"respostas-candidato-skill-diferencial", RepostaCandidatoSkillDiferencialViewSet, basename="respostas-candidato-skill-diferencial"
)
main_router.register(
    r"skills-candidatos", SkillCandidatoViewSet, basename="skills-candidatos"
)
main_router.register(r"skills", SkillViewSet, basename="skills")
main_router.register(r"vagas", VagaViewSet, basename="vagas")

urlpatterns = [
    path("admin/docs/", include("django.contrib.admindocs.urls")),
    path("admin/", admin.site.urls),
    path("", include("django.contrib.auth.urls")),
    path("", include("home.urls")),
    path("", include("django_app_novadata.urls")),
    path("avatar/", include("avatar.urls")),
    # path("advanced_filters/", include("advanced_filters.urls")),
    #
    path("api/", include(main_router.urls)),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/docs-swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger",
    ),
    path(
        "api/docs-redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    path("__reload__/", include("django_browser_reload.urls")),
    path("__debug__/", include("debug_toolbar.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler403 = "home.views.error_403"
handler404 = "home.views.error_404"
handler500 = "home.views.error_500"
