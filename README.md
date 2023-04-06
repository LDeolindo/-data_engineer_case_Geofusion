# Case Engenheiro de Dados - Geofusion

Case realizado para o processo seletivo Geofusion.

## Case - Entendendo melhor seus concorrentes

Atualmente, um dos nossos desafios é criar serviços de dados escaláveis, otimizados para o armazenamento e para o acesso aos dados.

Nossos Analistas analisaram os dados de fluxo de pessoas e concluíram que a melhor forma de apresentar essa informação seria segmentando o fluxo por dias da semana e períodos do dia (manhã, tarde e noite), ou seja, os clientes precisam saber quantas pessoas em média frequentam seus concorrentes em cada dia da semana e em cada período do dia.

A densidade demográfica de um bairro é uma informação muito importante para nossos clientes e é uma informação que precisa ser calculada. A densidade demográfica de um bairro é o resultado da divisão da população  pela área do bairro.

Ou seja, responder às seguintes perguntas:

* Qual é a faixa de preço praticada pelos concorrentes?
* Como é o fluxo de pessoas nesses locais (média por dia, maximo e minimo por dia, etc)?
* Qual é a população e a densidade demográfica dos bairros onde os concorrentes estão?

### Pré Requisitos
Para o desenvolvimento foi utilizado a linguagem [Python](https://www.python.org/) com as bibliotecas:
* [Pandas](https://pandas.pydata.org/docs/);
* [Jupyter](https://docs.jupyter.org/en/latest/).

Obs: é fornecido o arquivo: resolucao_requiriments.txt com as bibliotecas e versões utilizadas.

### Começando
Primeiramente, abra o terminal no diretório do teste e instale as dependências:
* `$ pip install -r resolucao_requiriments.txt`

### Entrega
Toda a resolução dos problemas propostos, seja código ou perguntas, foram respondidas no próprio jupyter `Notebook.ipynb`. Para ajudar no desenvolvimento foi criado um arquivo `utils.py`. E por fim, é gerado um arquivo de saída com o nome: `saida/dataset_final.parquet`.

#### Executando
Para rodar a aplicação é só executar o arquivo `Notebook.ipynb`.
