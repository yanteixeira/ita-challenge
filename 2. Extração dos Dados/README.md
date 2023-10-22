# Extração dos dados de treino

Essa pasta contem scripts que extraem automaticamente as bases de dados bimtra, espera, metar, metaf, cat_62 e tc_prev.

Para rodar os scripts:

```
#Extração dos dados principais
%run data_extraction.py
```

```
#Extração dos dados de satelite
%run cat62_extraction.py
```