from .admin.area_atuacao_admin_tests import AreaAtuacaoAdminTest
from .admin.beneficio_admin_tests import BeneficioAdminTest
from .admin.candidato_admin_tests import CandidatoAdminTest
from .admin.curso_admin_tests import CursoAdminTest
from .admin.instituicao_admin_tests import InstituicaoAdminTest
from .admin.skill_admin_tests import SkillAdminTest
from .admin.vaga_admin_tests import VagaAdminTest
from .models.area_atuacao_model_tests import AreaAtuacaoModelTest
from .models.beneficio_model_tests import BeneficioModelTest
from .models.candidato_model_tests import CandidatoModelTest
from .models.curso_model_tests import CursoModelTest
from .models.formacao_candidato_model_tests import FormacaoCandidatoModelTest
from .models.instituicao_model_tests import InstituicaoModelTest
from .models.pergunta_aberta_model_tests import PerguntaAbertaModelTest
from .models.resposta_aberta_model_tests import RespostaAbertaModelTest
from .models.skill_candidato_model_tests import SkillCandidatoModelTest
from .models.skill_model_tests import SkillModelTest
from .models.vaga_model_tests import VagaModelTest
from .viewsets.area_atuacao_viewset_tests import TestAreaAtuacaoViewSet
from .viewsets.beneficio_viewset_tests import TestBeneficioViewSet
from .viewsets.candidato_viewset_tests import TestCandidatoViewSet
from .viewsets.curso_viewset_tests import TestCursoViewSet
from .viewsets.formacao_candidato_viewset_tests import TestFormacaoCandidatoViewSet
from .viewsets.instituicao_viewset_tests import TestInstituicaoViewSet
from .viewsets.pergunta_aberta_viewset_tests import TestPerguntaAbertaViewSet
from .viewsets.resposta_aberta_viewset_tests import TestRespostaAbertaViewSet
from .viewsets.skill_candidato_viewset_tests import TestSkillCandidatoViewSet
from .viewsets.skill_viewset_tests import TestSkillViewSet
from .viewsets.vaga_viewset_tests import TestVagaViewSet

__all__ = [
    # Testes de admin
    AreaAtuacaoAdminTest,
    BeneficioAdminTest,
    CandidatoAdminTest,
    CursoAdminTest,
    InstituicaoAdminTest,
    SkillAdminTest,
    VagaAdminTest,
    # Testes de model
    AreaAtuacaoModelTest,
    BeneficioModelTest,
    CandidatoModelTest,
    CursoModelTest,
    FormacaoCandidatoModelTest,
    InstituicaoModelTest,
    PerguntaAbertaModelTest,
    RespostaAbertaModelTest,
    SkillCandidatoModelTest,
    SkillModelTest,
    VagaModelTest,
    # Testes de viewsets
    TestAreaAtuacaoViewSet,
    TestBeneficioViewSet,
    TestCandidatoViewSet,
    TestCursoViewSet,
    TestFormacaoCandidatoViewSet,
    TestInstituicaoViewSet,
    TestPerguntaAbertaViewSet,
    TestRespostaAbertaViewSet,
    TestSkillCandidatoViewSet,
    TestSkillViewSet,
    TestVagaViewSet,
]
