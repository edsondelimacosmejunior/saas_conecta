from recrutamento.serializers.resposta_candidato_skill_diferencial_serializers import RepostaCandidatoSkillDiferencialSerializer
from .area_atuacao_serializers import AreaAtuacaoSerializer
from .beneficio_serializers import BeneficioSerializer
from .candidato_serializers import CandidatoSerializer
from .candidato_serializers import CandidatoCreateSerializer
from .curso_serializers import CursoSerializer
from .formacao_candidato_serializers import FormacaoCandidatoSerializer
from .instituicao_serializers import InstituicaoSerializer
from .pergunta_aberta_serializers import PerguntaAbertaSerializer
from .resposta_aberta_serializers import RespostaAbertaSerializer
from .skill_candidato_serializers import SkillCandidatoSerializer
from .skill_serializers import SkillSerializer
from .vaga_serializers import VagaSerializer

__all__ = [
    AreaAtuacaoSerializer,
    BeneficioSerializer,
    CandidatoSerializer,
    CandidatoCreateSerializer,
    CursoSerializer,
    FormacaoCandidatoSerializer,
    InstituicaoSerializer,
    PerguntaAbertaSerializer,
    RespostaAbertaSerializer,
    SkillCandidatoSerializer,
    SkillSerializer,
    VagaSerializer,
    RepostaCandidatoSkillDiferencialSerializer
]
