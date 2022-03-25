# coleta-e-analise-de-fundos-imobiliarios
Author: Jackson Pertusatti
Projeto criado para ministrar a aula de Python para a turma de Análise de Decisões 1 da Universidade de Brasília - UnB do prof. Edu Prista.

# ROTEIRO DE AULA 

## "Estudar programação = Estudar idiomas"
> **Contexto:** Falar isso pode parecer clichê mas é bem próximo a realidade. Da mesma forma que, ao viajar para o USA se estuda inglês e para o Japão, japonês, para diferentes situações no computador se estudam diferentes linguagens de programação. E conforme a evolução das empresas para a nova realidade, o python vem se tornando a linguagem de programação curinga para inserir a pessoas de fora da tecnologia ao computador, pela sua facilidade de sintaxe e semântica e facilidade de instalação e execução. Assim como no passado as pessoas aprenderam a utilizar o Windows, o Word, o Excel, depois utilizaram e-mail, Powerpoint e smartphones, agora a realidade cada vez mais exige que as pessoas entendam um pouco mais de Ciência de Dados, Cybersegurança, Estatística e Automatizações. E o Python tem se tornado a "Caixa de ferramentas" para os profissionais a essas novas competências. Por isso na aula de hoje vamos aprender um pouco de automatização e ciência de dados.

🎯 **Objetivo da aula**: Realizar uma busca automática na internet, coletando dados sobre Fundos de Investimento Imobiliários (**FIIs**). Filtrar esses dados segundo diversos critérios e apresentar os FIIs que atenderam aos critérios propostos.

🐱 Github: https://github.com/pertusatti22/coleta-e-analise-de-fundos-imobiliarios

📘 **Etapas**

1. [ ] Instalar Dependências
2. [ ] Carregar Bibliotecas
3. [ ] Configurar WebScrapping
4. [ ] Coletar lista de Ticker dos FIIs
5. [ ] Capturar dados
  a. Valor Patrimonial(**VP**)
  b. Cotação(**Cot**)
  c. Patrimônio Líquido(**PL**)
  d. Último Rendimento(**Rend**)
  e. Dividend Yield(**DY**)
6. [ ] Aplicar filtros
  a. Valor patrimonial maior que a cotação
  b. Patrimônio líquido maior que 1 Bi
  c. Último rendimento maior que 0,70 centavos
  d. Dividend Yield maior que 0.6%
7. [ ] Apresentar resultados

🧭 **Propostas de melhorias**

*   Utilizar input para receber um valor de aporte mensal e distribuir esse aporte entre os ativos listados.
*   Buscar outras informações sobre os Fundos como quantidade de ativos.
*   Criar funções para melhorar a organização do código
