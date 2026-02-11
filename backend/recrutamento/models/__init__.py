from recrutamento.models.resposta_candidato_skill_diferencial import RepostaCandidatoSkillDiferencial
from .area_atuacao import AreaAtuacao
from .beneficio import Beneficio
from .candidato import Candidato
from .curso import Curso
from .formacao_candidato import FormacaoCandidato
from .instituicao import Instituicao
from .pergunta_aberta import PerguntaAberta
from .peso_skill import PesoSkill
from .resposta_aberta import RespostaAberta
from .skill import Skill
from .skill_candidato import SkillCandidato
from .vaga import Vaga

__all__ = [
    AreaAtuacao,
    Beneficio,
    Skill,
    SkillCandidato,
    Candidato,
    Curso,
    FormacaoCandidato,
    Instituicao,
    PerguntaAberta,
    PesoSkill,
    RespostaAberta,
    Vaga, 
    RepostaCandidatoSkillDiferencial
]