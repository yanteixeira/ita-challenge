# Dados Disponíveis

Foram disponibilizados diversas base de dados relacionadas à geolocalização, satélites, estações meteorológicas e preditores climáticos. 


* **bimtra.csv**
Versão resumida da base de dados do BIMTRA (Banco de Informações de Movimento de Tráfego Aéreo). Essa base possui informações dos movimentos nos aeródromos do Brasil.
	* flightid: identificador único de um voo
	* origem: Código do Aeroporto de origem do voo
	* destino: Código do Aeroporto de destino do voo
	* dt_dep: data e Hora de Decolagem do voo
	* dt_arr: data e Hora do Pouso do voo. Essa variável que deve ser estimada pelo modelo.


* **espera.csv**
Histórico de ocorrências de espera em voo por hora e aeródromo. 
	* esperas: ocorrência de espera para determinada hora em determinado aeroporto
	* hora: hora referência para determinado registro
	* aero: aeroporto em que ocorreu a espera


* **tc_prev.csv**
Previsões por hora de troca de cabeceira nos aeroportos.
	* hora: hora referência para determinado registro
	* troca: variável booleana indicando se ocorreu a troca ou não
	* aero: aeroporto em que ocorreu o registro


* **tc_real.csv**
Previsões por hora de troca de cabeceira nos aeroportos.
	* hora: hora referência para determinado registro
	* troca: variável booleana indicando se ocorreu a troca ou não
	* aero: aeroporto em que ocorreu o registro


* **metar.csv**
Base de dados METAR (Meteorological Aerodrome Report). Apresenta dados de telemetria de estações meteorológicas da região dos aeródromos, como temperatura, velocidade do vento, umidade, etc.
	* hora: hora referência para determinado registro
	* metar: código METAR
	* aero: aeroporto em que ocorreu o registro


* **metaf.csv**
Base de dados METAF (Terminal Aerodrome Forecast). Apresenta dados de previsão de registros metereológicos na região dos aeródromos, como temperatura, velocidade do vento, umidade, etc.
	* hora: hora referência para determinado registro
	* metaf: código METAF
	* aero: aeroporto em que ocorreu o registro


* **cat_62.csv**
A base de dados CAT-62 consiste na síntese radar do espaço aéreo brasileiro. A cada 4 segundos é gerado um registro para cada aeronave. Essa base não está disponível no repositório devido ao seu tamanho.


* **test.xlsx**
Dados que deverão ser usados para teste do modelo preditivo. 

