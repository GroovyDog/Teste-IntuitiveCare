CREATE TABLE IF NOT EXISTS Operadoras (
	Registro_ANS VARCHAR (6) NOT NULL,
	CNPJ VARCHAR (14) NOT NULL,
	Razao_Social VARCHAR(200) NOT NULL,
	Nome_Fantasia VARCHAR(200),
	Modalidade VARCHAR (50) NOT NULL,
	Logradouro VARCHAR (100) NOT NULL,
	Numero CHAR (15) NOT NULL,
	Complemento VARCHAR (100),
	Bairro VARCHAR (100),
	Cidade VARCHAR (100),
	UF VARCHAR (100),
	CEP CHAR(8),
	DDD INT NOT NULL,
	Telefone CHAR(15) NOT NULL,
	Fax CHAR(15) NOT NULL,
	Endereço_eletronico VARCHAR(100) NOT NULL,
	Representante VARCHAR(100) NOT NULL,
	Cargo_Representante VARCHAR(50) NOT NULL,
	Data_Registro_ANS DATE NOT NULL,
	PRIMARY KEY (Registro_ANS)
);

CREATE TABLE IF NOT EXISTS Despesas(
	Data_despesa DATE NOT NULL,
	Reg_ANS VARCHAR (6) NOT NULL,
	cd_Conta_Contabil CHAR(15) NOT NULL,
	Descricao VARCHAR (100) NOT NULL,
	vl_saldo_final FLOAT NOT NULL,
	FOREIGN KEY (Reg_ANS) REFERENCES Operadoras (Registro_ANS)
);

COPY Despesas FROM '/home/pedro/Público/Teste IntuitiveCare/Teste 3 - Banco de Dados/files/4T2020.csv' DELIMITER ';' CSV HEADER;