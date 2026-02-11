#!/bin/bash

# Verifica se o Git está presente
if ! [ -x "$(command -v git)" ]; then
  echo "Erro: Git não está instalado." >&2
  exit 1
fi

# Verifica se o Docker está presente
if ! [ -x "$(command -v docker)" ]; then
  echo "Erro: Docker não está instalado." >&2
  exit 1
fi

# Obter o SHA do commit atual (primeiros 7 caracteres)
GIT_COMMIT_SHA=$(git rev-parse --short HEAD)

# Verificar se estamos em um repositório Git
if [ -z "$GIT_COMMIT_SHA" ]; then
  echo "Erro: Não foi possível obter o SHA do commit. Verifique se você está em um repositório Git." >&2
  exit 1
fi

# Obter a data e a hora atual no formato YYYYMMDD-HHMM
BUILD_DATE=$(date +"%Y%m%d-%H%M")

# Nome do repositório Docker (substitua pelo seu nome de usuário/nome de repositório no Docker Hub ou outro registro)
DOCKER_REPO="timenovadata/conecta"

# Nome completo da imagem com o SHA do commit e a data/hora
IMAGE_TAG="${DOCKER_REPO}:${GIT_COMMIT_SHA}-${BUILD_DATE}"

# Tag `latest` para a imagem
LATEST_TAG="${DOCKER_REPO}:latest"

# Construir a imagem Docker com a tag personalizada
echo "Construindo a imagem Docker com a tag: ${IMAGE_TAG}"
docker build -t ${IMAGE_TAG} .

# Verificar se a imagem foi criada com sucesso
if [ $? -eq 0 ]; then
  echo "Imagem Docker criada com sucesso: ${IMAGE_TAG}"
else
  echo "Erro: Falha ao criar a imagem Docker." >&2
  exit 1
fi

# Tag adicional `latest`
echo "Aplicando a tag 'latest' para a imagem: ${LATEST_TAG}"
docker tag ${IMAGE_TAG} ${LATEST_TAG}

# Fazer push da imagem com a tag do commit e data/hora
echo "Fazendo push da imagem para o repositório: ${IMAGE_TAG}"
docker push ${IMAGE_TAG}

# Fazer push da tag 'latest'
echo "Fazendo push da tag 'latest' para o repositório: ${LATEST_TAG}"
docker push ${LATEST_TAG}

# Verificar se o push foi bem-sucedido
if [ $? -eq 0 ]; then
  echo "Push realizado com sucesso para ${IMAGE_TAG} e ${LATEST_TAG}"
else
  echo "Erro: Falha ao realizar o push da imagem Docker." >&2
  exit 1
fi

# Exibir as imagens Docker disponíveis localmente
docker images | grep ${DOCKER_REPO}