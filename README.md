<meta name="qrichtext" content="1">

<style type="text/css"> p, li { white-space: pre-wrap; } </style>

<span style=" font-family:'Segoe UI'; font-size:14pt; font-weight:600;">Descrição:</span>

<br>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Ahand (Give me a hand) é um programa para otimização de processos que envolvam arquivos PDF.</span>

<br>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Com Ahand é possível:</span>

<br>

<span style=" font-family:'Segoe UI'; font-size:11pt;">- Unir arquivos PDF.</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">- Extrair páginas de arquivos PDF.</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">- Dividir arquivos PDF.</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">- Escanear arquivos PDF através do reconhecimento óptico de caracteres (OCR), transformando em um PDF pesquisável.</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">- Organizar arquivos PDF de acordo com as frases ou palavras encontradas dentro do arquivo.</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">- Compactar arquivos PDF contidos em subpastas de uma pasta raiz.</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">¨NBSP;</span>

<span style=" font-family:'Segoe UI'; font-size:14pt; font-weight:600;">Nomenclatura dos arquivos:</span>

<br>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Dentro do programa, existem tags, elas são variáveis que abrangem alguns padrões bastante usados na hora de renomear um arquivo. As tags são indicadas por #.</span>

<br>

<span style=" font-family:'Segoe UI'; font-size:11pt; font-weight:600;">#origin</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;"> = Nome original do arquivo.</span>

<span style=" font-family:'Segoe UI'; font-size:11pt; font-weight:600;">#year</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;"> = Ano atual.</span>

<span style=" font-family:'Segoe UI'; font-size:11pt; font-weight:600;">#month</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;"> = Mês atual.</span>

<span style=" font-family:'Segoe UI'; font-size:11pt; font-weight:600;">#day</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;"> = Dia atual.</span>

<span style=" font-family:'Segoe UI'; font-size:11pt; font-weight:600;">#hour</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;"> = Hora atual.</span>

<span style=" font-family:'Segoe UI'; font-size:11pt; font-weight:600;">#minutes</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;"> = Minutos atuais.</span>

<span style=" font-family:'Segoe UI'; font-size:11pt; font-weight:600;">#seconds</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;"> = Segundos atuais</span>

<span style=" font-family:'Segoe UI'; font-size:11pt; font-weight:600;">#time</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;"> = Hora, minutos e segundos atuais.</span>

<span style=" font-family:'Segoe UI'; font-size:11pt; font-weight:600;">#pages</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;"> = Página(s) exportadas do arquivo. Disponível apenas para as funções Separar/Dividir e Organizar(caso a caixa de seleção "Mover apenas páginas esteja marcada").</span>

<br>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Por padrão, caso o campo de nome esteja vazio, os arquivos são salvos com a tag #origin, com exceção da função Separar/Dividir, que utiliza as tags #origin,#pages.</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Para utilizar um conjunto de tags, é necessário delimitar por vírgulas.</span>

<br>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Veja um exemplo de nomenclatura de um arquivo:</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Arquivos de entrada: </span>

<span style=" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;">C:\Downloads\file1.pdf, C:\Downloads\file2.pdf</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Extrair página indicada: </span>

<span style=" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;">3</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Diretório de saída: </span>

<span style=" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;">C:\Downloads</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Nome do arquivo: </span>

<span style=" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;">#origin,#pages,Contas a pagar,#year,#month,#day</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Resultado: </span>

<span style=" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;">C:\Downloads\file1_3_Contas a pagar_2020_10_14, C:\Downloads\file2_3_Contas a pagar_2020_10_14</span>

<br>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Note que você pode utilizar tags e texto em conjunto, mas eles devem ser delimitados por vírgula.</span>

<br>

<span style=" font-family:'Segoe UI'; font-size:14pt; font-weight:600;">Unir arquivos PDF:</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Exemplo:</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Arquivos de entrada: </span>

<span style=" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;">C:\Downloads\file1.pdf, C:\Downloads\file2.pdf</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Diretório de saída: </span>

<span style=" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;">C:\Downloads\</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Nome do arquivo: </span>

<span style=" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;">merged</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Resultado: </span>

<span style=" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;">C:\Downloads\merged.pdf</span>

<br>

<span style=" font-family:'Segoe UI'; font-size:14pt; font-weight:600;">Extrair páginas ou dividir arquivos PDF:</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Lista - Páginas indicadas: Extrair ou dividir nas páginas indicadas.</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Lista - A cada n páginas: Extrair ou dividir a cada "n" páginas.</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Caixa de seleção - Dividir arquivo: Através de um arquivo, outros são gerados, os dividindo nas páginas indicadas.</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Caixa de seleção - Extrair no mesmo arquivo: As páginas indicadas são extraídas em um mesmo arquivo.</span>

<br>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Exemplos:</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Arquivo de entrada:</span>

<span style=" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;"> C:\Downloads\file.pdf</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Diretório de saída: </span>

<span style=" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;">C:\Downloads\</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Nome do arquivo: </span>

<span style=" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;">#origin,#pages</span>

<br>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Exemplo 1:</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Lista = </span>

<span style=" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;">Páginas indicadas</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Caixa de seleção = </span>

<span style=" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;">Dividir arquivo</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Páginas = </span>

<span style=" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;">3,7-8,11-16</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Resultado: </span>

<span style=" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;">C:\Downloads\file_3.pdf, C:\Downloads\file_7-8.pdf, C:\Downloads\file_11-16.pdf</span>

<br>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Exemplo 2:</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Lista = </span>

<span style=" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;">Páginas indicadas</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Caixa de seleção = </span>

<span style=" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;">Extrair no mesmo arquivo</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Páginas = </span>

<span style=" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;">3,7-8,11-16</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Resultado: </span>

<span style=" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;">C:\Downloads\file_3,7-8,11-16.pdf</span>

<br>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Exemplo 3:</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Lista = </span>

<span style=" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;">A cada n páginas</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Caixa de seleção = </span>

<span style=" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;">Dividir arquivo</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Páginas = </span>

<span style=" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;">4</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Resultado: </span>

<span style=" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;">C:\Downloads\file_1-4.pdf, C:\Downloads\file_5-8.pdf, C:\Downloads\file_9-12.pdf, C:\Downloads\file_13-16.pdf</span>

<br>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Exemplo 4:</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Lista = </span>

<span style=" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;">A cada n páginas</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Caixa de seleção = </span>

<span style=" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;">Extrair no mesmo arquivo</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Páginas = </span>

<span style=" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;">4</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Resultado: </span>

<span style=" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;">C:\Downloads\file_4,8,12,16.pdf</span>

<br>

<span style=" font-family:'Segoe UI'; font-size:14pt; font-weight:600;">Escanear arquivos PDF (OCR):</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Exemplo:</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Arquivos de entrada: </span>

<span style=" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;">C:\Downloads\file1.pdf, C:\Downloads\file2.pdf</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Diretório de saída: </span>

<span style=" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;">C:\Downloads\</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Nome do arquivo: </span>

<span style=" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;">#origin,OCR</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">DPI: </span>

<span style=" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;">200</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Resultado: </span>

<span style=" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;">C:\Downloads\file1_OCR.pdf, C:\Downloads\file2_OCR.pdf</span>

<br>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Note que quanto maior o DPI, maior o tamanho da imagem.</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Caso o reconhecimento óptico de caracteres (OCR) não atinja um resultado satisfatório, experimente alterar o DPI.</span>

<br>

<span style=" font-family:'Segoe UI'; font-size:14pt; font-weight:600;">Organizar arquivos PDF:</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Você pode organizar arquivos PDF de acordo com as frases ou palavras encontradas dentro do arquivo.</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Suponhamos que você seja um professor e queira organizar os trabalhos enviados por seus alunos por escola, turma, ano atual, matéria, tema do trabalho e nome do aluno:</span>

<br>

<span style=" font-family:'Segoe UI'; font-size:11pt;">- Primeiro, certifique-se de que o documento PDF seja pesquisável, isto é, contenha texto. Caso seja uma imagem escaneada, utilize a função "Escanear arquivos PDF" antes de proceder.</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">- Importe os arquivos PDF que você deseja organizar.</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">- Selecione o diretório de saída. Como exemplo será "</span>

<span style=" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;">C:Desktop\</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">"</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">- Importe um ou mais arquivos CSV com a tabela que contém as palavras a pesquisar (você pode gerar o arquivo com um editor de planilhas, como o Excel).</span>

<br>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Alunos.csv</span>

|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |

<br>

<span style=" font-family:'Segoe UI'; font-size:11pt;">(Todos os dados referentes a alunos foram gerados aleatoriamente).</span>

<br>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Matérias.csv</span>

|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |

<br>

<br>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Iremos procurar pelo nome de todos os alunos, que se encontra na tabela </span>

<span style=" font-family:'Segoe UI'; font-size:11pt; color:#a0a0a0;">Alunos</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;"> coluna </span>

<span style=" font-family:'Segoe UI'; font-size:11pt; color:#a0a0a0;">1</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">, junto a todos os temas de trabalho, que se encontra na tabela </span>

<span style=" font-family:'Segoe UI'; font-size:11pt; color:#a0a0a0;">Matérias</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;"> coluna </span>

<span style=" font-family:'Segoe UI'; font-size:11pt; color:#a0a0a0;">1</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">.</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Então temos a definição </span>

<span style=" font-family:'Segoe UI'; font-size:11pt; color:#a0a0a0;">tabela:coluna</span>

<br>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Sendo assim, o campo "</span>

<span style=" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;">Procurar por expressões</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">" recebe o seguinte valor: </span>

<span style=" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;">Alunos:1,Matérias:1</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Se houver mais de um conjunto tabela:coluna, eles devem ser delimitados por vírgulas, como no exemplo acima.</span>

<br>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Note que se o valor de uma linha for localizado, temos acesso a todos os valores das outras colunas adjacentes nessa tabela.</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Como por exemplo, se dentro do arquivo conter o nome "Bianca Helena Cavalcanti", podemos pedir para o programa retornar o valor da coluna 3, que para essa linha é "2C".</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Dessa forma, temos acesso a valores que não necessariamente precisam estar dentro do arquivo.</span>

<br>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Com isso em mente:</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Iremos informar o destino que queremos exportar o arquivo caso as condições forem satisfeitas:</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Queremos criar uma árvore de diretório nesse modelo: </span>

<span style=" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;">diretório_de_saída\ano_atual\escola\turma\matéria\tema_do_trabalho\</span>

<br>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Então iremos informar em qual tabela e coluna esses valores se encontram.</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Sendo assim, o campo "</span>

<span style=" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;">Criar subpastas</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">" recebe o seguinte valor: </span>

<span style=" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;">#year,Alunos:4,Alunos:3,Matérias:2,Matérias:1</span>

<br>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Caso as condições não sejam satisfeitas dentro de um arquivo, podemos indicar um diretório para movê-lo.</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Sendo assim, o campo "</span>

<span style=" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;">Se não encontrar mover para pasta</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">" recebe o seguinte valor: </span>

<span style=" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;">Não encontrado</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Caso vazio, os arquivos em que não foram encontradas todas as palavras não serão movidos.</span>

<br>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Agora, iremos informar o nome do arquivo, neste caso queremos o nome do aluno.</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Sendo assim, o campo "</span>

<span style=" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;">Nome do arquivo</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">" recebe o seguinte valor: </span>

<span style=" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;">Alunos:1</span>

<br>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Há ainda algumas caixas de seleção:</span>

<br>

<span style=" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;">Mover apenas páginas:</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;"> Se marcado, irá procurar pelas palavras dentro de cada página e exporta-la caso os requisitos sejam satisfeitos. Útil quando cada página representa um arquivo, como uma nota fiscal. Caso contrário, as palavras serão pesquisadas dentro de todo o arquivo.</span>

<span style=" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;">Ignorar primeira linha:</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;"> Marcar caso a primeira linha seja cabeçalho e você não queira pesquisa-la dentro do arquivo.</span>

<span style=" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;">Ignorar acentos:</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;"> Realizar pesquisa desconsiderando acentos. Marcar para maior precisão.</span>

<span style=" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;">Ignorar pontuação:</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;"> Realizar pesquisa desconsiderando pontuação tais como ".,;/?!". Marcar para maior precisão.</span>

<span style=" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;">Ignorar espaços:</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;"> Realizar pesquisa desconsiderando espaços. Marcar para maior precisão.</span>

<br>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Para este exemplo, iremos desmarcar apenas a opção "Mover apenas páginas".</span>

<br>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Então, como exemplo de resultado, caso ambas as palavras "Bianca Helena Cavalcanti" e "Deslocamento escalar" sejam encontradas no arquivo, temos:</span>

<span style=" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;">C:Desktop\2020\Durvalino Grion Prof\2C\Cinemática\Deslocamento escalar\Bianca Helena Cavalcanti.pdf</span>

<br>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Se em vez de criar uma árvore de diretório </span>

<span style=" font-family:'Segoe UI','sans-serif'; font-size:11pt;">quiséssemos </span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">apenas renomear o arquivo, bastava informar os valores no campo "</span>

<span style=" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;">Nome do arquivo</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">" e deixar o campo "</span>

<span style=" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;">Criar subpastas</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">" vazio.</span>

<br>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Então, como exemplo de resultado, temos:</span>

<span style=" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;">C:Desktop\2020_Durvalino Grion Prof_2C_Cinemática_Deslocamento escalar_Bianca Helena Cavalcanti.pdf</span>

<br>

<span style=" font-family:'Segoe UI'; font-size:14pt; font-weight:600;">Criar ficheiro ZIP de arquivos PDF:</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Exemplo:</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Diretório raiz: </span>

<span style=" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;">C:\Downloads\root\</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Subpastas contidas no diretório raiz: Janeiro,Fevereiro,Março</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Diretório de saída: </span>

<span style=" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;">C:\Downloads\output\</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Nome do arquivo ZIP: </span>

<span style=" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;">#origin,#year</span>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Resultado: </span>

<span style=" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;">C:\Downloads\output\Janeiro_2020.zip, C:\Downloads\output\Fevereiro_2020.zip, C:\Downloads\output\Março_2020.zip</span>

<br>

<span style=" font-family:'Segoe UI'; font-size:11pt;">Portanto, todos os arquivos PDF contidos nas subpastas Janeiro,Fevereiro,Março serão compactados.</span>

