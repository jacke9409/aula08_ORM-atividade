# Criando o primeiro modelo ORM objetivo
# Biblioteca sqlalchemy para criar a conexão com o banco de dados
# criar um ambiente virtual python
from sqlalchemy import create_engine
#importar tipos de dados e estrutura das colunas
from sqlalchemy import Column, Integer, String

# Importar a classe base para criar as classes de modelo
from sqlalchemy.orm import declarative_base
# Importa a ferramenta para criar sessões de banco de dados
from sqlalchemy.orm import sessionmaker

# classe base para ORM (Object-Relational Mapping)
Base = declarative_base()

# crie uma classe chamada aluno que represente uma tabela no banco de dados.
# a tabela deve possuir as seguintes colunas:
class Aluno(Base):
    __tablename__ = "alunos"  # nome da tabela no banco de dados
    id = Column(Integer, primary_key=True)  # coluna de  identificação, chave primária
    nome = Column(String)  # coluna de nome do aluno 
    idade = Column(Integer)  # coluna de idade do aluno
    curso = Column(String)  # coluna de curso do aluno
    requisito = Column(String)  # coluna de requisito do aluno

    def __init__(self, nome, idade, curso, requisito):
        self.nome = nome
        self.idade = idade
        self.curso = curso
        self.requisito = requisito

      
# criar a conexão com o banco de dados
engine = create_engine("sqlite:///alunos.db", echo=True)  # usando SQLite para criar um arquivo de 
# banco de dados local chamado "alunos.db". O parâmetro echo=True
# é usado para exibir as consultas SQL geradas.
  # criar a tabela no banco de dados
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)  # criar uma classe de sessão vinculada ao mecanismo de banco de dados
session = Session() 

# criar 8 alunos
aluno1 = Aluno("Felipe encardido", 17, "Desenvolvimento de Sistemas", "Requisito 1")
aluno2 = Aluno("Maria Joaquina", 18, "Desenvolvimento de Sistemas", "Requisito 2")
aluno3 = Aluno("Gustavo", 17, "Desenvolvimento de Sistemas", "Requisito 3")
aluno4 = Aluno("Ana Clara", 17, "Gestão de Tecnologia da Informação", "Requisito 4")
aluno5 = Aluno("Ana Paula", 21, "Banco de Dados", "Requisito 5")
aluno6 = Aluno("Tia Milena", 22, "Redes de Computadores", "Requisito 6")
aluno7 = Aluno("Juliano", 23, "Segurança da Informação", "Requisito 7")
aluno8 = Aluno("Samira", 24, "Inteligência Artificial", "Requisito 8")

# Salvarve os alunos no banco de dados
session.add_all([aluno1, aluno2, aluno3, aluno4, aluno5, aluno6, aluno7, aluno8])
session.commit()

# liste todos os alunos cadastrados
alunos_cadastrados = session.query(Aluno).all()
for aluno in alunos_cadastrados:
    print(f"ID: {aluno.id}, Nome: {aluno.nome}, Idade: {aluno.idade}, Curso: {aluno.curso}, Requisito: {aluno.requisito}")

# busque o aluno com id == 1
aluno_id1 =  session.query(Aluno).filter_by(id=1).first()
print(f"Aluno com ID 1: {aluno_id1.nome}, Idade: {aluno_id1.idade}, Curso: {aluno_id1.curso}, Requisito: {aluno_id1.requisito}")

# atualize o curso para "Back-end com Gabriel"
gabriel =  session.query(Aluno).filter_by(nome = "Felipe encardido").first()
gabriel.curso = "Back-end com Gabriel"
session.commit()

# Busque um aluno
# remova esse aluno do banco
# aluno_id3 = session.query(Aluno).filter(Aluno.id ==3)

# aluno_remover = session.query(Aluno).filter_by(id=2).first()
# session.delete(aluno_remover)
# session.commit()

# print("ALuno deletado do sistema!", aluno_remover)

# faça as seguintes consultas:
# 1-Buscar alunos com idade maior que 20
# 2-buscar alunos do curso Desenvolvimento de Sistemas

aluno_maiorque = session.query(Aluno).filter(Aluno.idade >=20).all()