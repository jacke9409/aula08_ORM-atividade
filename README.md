-----------------------------------------
Criando o primeiro modelo ORM objetivo
-----------------------------------------
* **criar uma tabela usando SQLAlchemy**
-----------------------------------------
crie uma classe chamada aluno que represente uma tabela no banco de dados.
a tabela deve possuir as seguintes colunas:

Coluna Tipo
Id inteiro(chave primária)
nome texto
idade inteiro
curso texto
requisitos 

Criar a conexão com SQLite (escola.db)
criar a classe Alun
Criar as colunas usando column
Criar a tabela no banco usando Base.metadata.create_all()
Crie 8 alunos
Salve os alunos no banco de dados
Liste todos os alunos cadastrados.