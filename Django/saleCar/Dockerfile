# Define a imagem base
FROM python:3.9

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o arquivo de requirements.txt para o diretório de trabalho
COPY ./requirements.txt .

# Instala as dependências do projeto
RUN pip install -r requirements.txt

# Copia o conteúdo da pasta 'app_car' do host para o diretório de trabalho do container
COPY / .

# Define o comando padrão para executar o servidor do Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
