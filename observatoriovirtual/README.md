# Observatório Virtual

Observatório Virtual para a execução remota de algoritmos da área de Astronomia.<br>
Desenvolvido em colaboração entre o LABAC-INPE e a Informática-UFSM<br>
Proposta original por Otávio Madalosso: https://github.com/Madalosso/TG/tree/master/Django%20Proj/webfriends

## Execução Local

Recomenda-se o uso de ambiente virtual para instalação isolada dos *software* necessários para o portal. <br>

Instruções para um sistema baseado em Debian:

1. Instale o ambiente virtual [virtualenv](https://pypi.org/project/virtualenv/) e o gerenciador de pacotes em Python [pip](https://pypi.org/project/pip/) (usada a versão 3 do Python).<br> 



2. Instale o Redis, que será usado como um *broker* para o Celery.

```bash 
$ apt install python3-pip virtualenv redis-server
```

3. Crie um ambiente virtual na pasta do projeto:

``` bash 
$ virtualenv myenv -p "/usr/bin/python3" 
```

Ative o ambiente virtual criado:

``` bash 
$ source myvenv/bin/activate
```

4. Clone este projeto dentro do ambiente virtual

5. Instale o restante dos pacotes necessários:

``` bash 
$ pip install django django-registration-redux django-crispy-forms django-jsonview celery redis scikit-image requests
```

ou, utilizando o arquivo *requirements.txt* do projeto, instale tudo com:

``` bash 
$ pip install -r requirements.txt
```

6. Inicie a aplicação:

``` bash 
$ redis-server # Inicia o servidor para o Redis
$ ./manage.py runserver # Inicia o app Django
$ celery -A webfriends worker --loglevel=DEBUG # Inicia o worker do Celery
```

Finalmente, abre o projeto em http://localhost:8000 em um navegador web!

- **Atenção!** Mudanças para configurações locais podem ser necessárias nos arquivos: *settings*, *experiments.py* e *tasks.py*.
