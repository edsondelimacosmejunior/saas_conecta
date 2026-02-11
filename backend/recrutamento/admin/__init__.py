from recrutamento.admin.resposta_candidato_skill_diferencial_admin import (
    RepostaCandidatoSkillDiferencialAdmin,
    RepostaCandidatoSkillDiferencialInline)

from .area_atuacao_admin import AreaAtuacaoAdmin
from .beneficio_admin import BeneficioAdmin
from .candidato_admin import CandidatoAdmin
from .curso_admin import CursoAdmin
from .instituicao_admin import InstituicaoAdmin
from .peso_skill_admin import PesoSkillAdmin
from .peso_skill_inline import PesoSkillInline
from .skill_admin import SkillAdmin
from .vaga_admin import VagaAdmin

__all__ = [
    AreaAtuacaoAdmin,
    BeneficioAdmin,
    CursoAdmin,
    CandidatoAdmin,
    InstituicaoAdmin,
    PesoSkillAdmin,
    PesoSkillInline,
    SkillAdmin,
    VagaAdmin,
    RepostaCandidatoSkillDiferencialAdmin,
    RepostaCandidatoSkillDiferencialInline
]
