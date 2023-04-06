# Processo seletivo para Engenheiro de Dados Junior - Geofusion

Olá, seja bem vinde ao processo seletivo de Engenharia de Dados Junior da Geofusion!

### Contexto

A equipe de produtos da Geofusion tem recebido feedbacks da equipe comercial e eles dizem que alguns clientes do setor de alimentação (restaurantes, pizzarias, bares, etc.) estão procurando soluções que os ajudem a entender melhor seus concorrentes. Eles gostariam de saber qual é a faixa de preço praticada pelos concorrentes, como é o fluxo de pessoas nesses locais, qual é a população e a densidade demográfica dos bairros onde os concorrentes estão, e etc.

### Desafio

Atualmente, um dos nossos desafios é criar serviços de dados escaláveis, otimizados para o armazenamento e para o acesso aos dados.

Nossos Analistas analisaram os dados de fluxo de pessoas e concluíram que a melhor forma de apresentar essa informação seria segmentando o fluxo por dias da semana e períodos do dia (manhã, tarde e noite), ou seja, os clientes precisam saber quantas pessoas em média frequentam seus concorrentes em cada dia da semana e em cada período do dia.

A densidade demográfica de um bairro é uma informação muito importante para nossos clientes e é uma informação que precisa ser calculada. A densidade demográfica de um bairro é o resultado da divisão da população  pela área do bairro.


### Dataset

São 4 arquivos:
1) [Bairros](https://s3.sa-east-1.amazonaws.com/geofusion-data-engineer-files/bairros.csv)
  a) Contém dados sobre bairros com código do município.
2) [Concorrentes](https://s3.sa-east-1.amazonaws.com/geofusion-data-engineer-files/concorrentes.csv)
  a) Contém dados sobre os concorrentes do meu estabelecimento.
3) [Eventos de Fluxo](https://s3.sa-east-1.amazonaws.com/geofusion-data-engineer-files/eventos_de_fluxo.csv.gz)
  a) Contém dados de eventos de visitas aos concorrentes com código do cliente, data da visita e código do concorrente.
4) [População](https://s3.sa-east-1.amazonaws.com/geofusion-data-engineer-files/populacao.json)
  a) Contém dados sobre a população dos bairros.

Os arquivos também constam na pasta `./dados` desse projeto.


### Modelagem

* Prepare os dados e os tipos corretos. Não assuma nada no dataset que você recebeu (cheque se tudo esta preenchido, se não tem um inteiro no meio da string, etc).
* Desenvolva as consultas abaixo com o pandas (utilizando merges e joins) utilizando o Notebook em anexo  Essas consultas precisam ser capaz de responder as seguintes perguntas:
  * qual é a faixa de preço praticada pelos concorrentes;
  * como é o fluxo de pessoas nesses locais (média por dia, maximo e minimo por dia, etc);
  * qual é a população e a densidade demográfica dos bairros onde os concorrentes estão;
* Sugira um schema de saída, com nome das colunas, tipos dos dados e uma sugestão de tipo de arquivo (CSV, Parquet, JSON, etc) e justifique. 
* Exemplifique com algumas queries em SQL como seria possivel nossos analistas extrairem as informações acima.
  * Opcional: crie visualizações dos dados (gráficos).

#### Entrega
* **Entregue o relatório acima em qualquer formato (Word, Markdown, etc).**
* **Comprima seu projeto com tudo que você utilizou e envie para nós.**
* **[plus] Comente sobre possíveis dificuldades que você tenha encontrado ao realizar o case.**


Boa sorte!