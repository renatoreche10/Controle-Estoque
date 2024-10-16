use cadastro_produtos;
create table produtos(
id int not null auto_increment primary key,
produto varchar (100) not null,
preco float not null,
estoque int not null 
);
use cadastro_produtos;
select * from produtos


