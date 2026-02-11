# 🔐 Gerenciamento de Secrets

Este documento explica como lidar com secrets e credenciais no projeto.

## ⚠️ NUNCA Commite Secrets!

**Arquivos que NUNCA devem ser commitados:**

- `backend/k8s/*/secrets.yaml` - Secrets do Kubernetes
- `.env` - Variáveis de ambiente locais
- Chaves API, tokens, senhas em código

## 📁 Arquivos de Secrets

### Kubernetes Secrets

Os secrets do Kubernetes estão em `.gitignore`:

```
backend/k8s/dev/secrets.yaml  ❌ NÃO commitar!
backend/k8s/prod/secrets.yaml ❌ NÃO commitar!
```

**Use os arquivos `.example`:**

```bash
# Criar seu arquivo de secrets local
cp backend/k8s/dev/secrets.yaml.example backend/k8s/dev/secrets.yaml

# Editar com suas credenciais reais
# Lembre-se: valores devem estar em base64
echo -n "seu-valor" | base64
```

### Django Settings

**NO CÓDIGO:**
```python
# ❌ NUNCA faça isso
EMAIL_HOST_PASSWORD = "SG.abc123xyz..."

# ✅ SEMPRE use variáveis de ambiente
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', '')
```

**NO MODELO:**
```python
# ✅ Configure via Django Admin
email_host_password = models.CharField(
    default="",  # Configurar no Admin
)
```

## 🔧 Workflow Correto

### 1. Desenvolvimento Local

```bash
# Frontend
cp frontend/.env.example frontend/.env
# Edite frontend/.env com seus tokens

# Backend K8s (se usar)
cp backend/k8s/dev/secrets.yaml.example backend/k8s/dev/secrets.yaml
# Edite com suas credenciais
```

### 2. Codificar Valores em Base64

```bash
# Codificar
echo -n "minha-senha-secreta" | base64
# Resultado: bWluaGEtc2VuaGEtc2VjcmV0YQ==

# Decodificar (para verificar)
echo "bWluaGEtc2VuaGEtc2VjcmV0YQ==" | base64 -d
```

### 3. Deploy no Replit

Configure via **Secrets** do Replit:
- `API_SECRET`
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- etc.

### 4. Deploy no Kubernetes

```bash
# Aplicar secrets (arquivo NÃO está no git!)
kubectl apply -f backend/k8s/dev/secrets.yaml
```

## 🚨 Se Você Commitou Um Secret

**PARE IMEDIATAMENTE!**

1. **Não faça push** se ainda não fez
2. **Revogue o secret** (regenere a chave/token)
3. **Limpe o histórico git**:

```bash
# Remover arquivo do histórico
git filter-branch --force --index-filter \
  'git rm --cached --ignore-unmatch caminho/para/arquivo-com-secret.yaml' \
  --prune-empty --tag-name-filter cat -- --all

# Forçar push (CUIDADO!)
git push origin main --force
```

4. **Adicione ao .gitignore**
5. **Crie arquivo .example** sem secrets

## ✅ Checklist Antes de Commitar

- [ ] Nenhum `.env` no commit
- [ ] Nenhum `secrets.yaml` no commit
- [ ] Nenhuma senha/token em código Python
- [ ] Verificou com `git diff` antes de commit
- [ ] Arquivos `.example` atualizados (se necessário)

## 📚 Referências

- [GitHub Secret Scanning](https://docs.github.com/en/code-security/secret-scanning)
- [12 Factor App - Config](https://12factor.net/config)
- [Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)

## 🔑 Secrets Usados no Projeto

| Secret | Onde Usar | Como Obter |
|--------|-----------|------------|
| `API_SECRET` | Django Token | Django Admin → Auth Tokens |
| `AWS_ACCESS_KEY_ID` | Storage S3 | AWS IAM Console |
| `AWS_SECRET_ACCESS_KEY` | Storage S3 | AWS IAM Console |
| `EMAIL_HOST_PASSWORD` | SendGrid | SendGrid Dashboard |
| `SECRET_KEY` | Django | `python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'` |
| `DATABASE_URL` | PostgreSQL | Provider do database |

## 💡 Dicas

1. **Use gerenciadores de secrets** em produção (AWS Secrets Manager, Vault, etc.)
2. **Rotacione secrets** periodicamente
3. **Limite permissões** - princípio do menor privilégio
4. **Monitore acessos** - configure alertas
5. **Documente** qual secret precisa de quais permissões

---

**Lembre-se: Um secret commitado é um secret comprometido!**

Sempre revogue e regenere credentials que foram expostas acidentalmente.
