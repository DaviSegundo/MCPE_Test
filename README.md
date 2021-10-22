# Sistema de Visualização de Processos
<hr>

#### Autor:  Davi Segundo Pinheiro

## Funcionalidades Backend:
- Consultar.
- Cadastrar.
- Buscar.
- Excluir.
- Editar.
- Controle de Admin.

A aplicação tem persistência dos dados no Banco de dados. Para esse projeto foi utilizado o **SQLite3**.

## Funcionalidades Frontend:
- Interface responsiva.
- Estilização para boa aparência.

Foi utilizado **Bootstrap** para acelerar o processo de estilização.
<hr>

## Telas

#### Tela Inicial:
Tela de visualização geral de processos.
<p align='center'>
    <img src='./docs/tela_inicial.png' height=450 style="border-radius: 10px;">
</p>
Mostra algumas informações gerais dos processos, sendo possível acessar cada processo para ter mais detalhes.
<hr>

#### Tela de Busca:
É possível fazer busca pelo nome do processo.
<p align='center'>
    <img src='./docs/tela_busca.png' height=450 style="border-radius: 10px;">
</p>
É retornado de maneira bem generalista, com o intuito de facilitar a busca mesmo sem saber o nome exato do processo em questão.
<hr>

#### Tela do Processo:
Tela de vizualização mais específica de cada processo.
<p align='center'>
    <img src='./docs/tela_processo.png' height=450 style="border-radius: 10px;">
</p>
Nessa tela podemos editar ou excluir aquele processe que está sendo exibido.
<hr>

#### Tela de Cadastro/Editar:
Aqui é possível fazer o cadastro de um novo processo informando os dados dele ou ir a partir de um processo específico e editar os dados dele.
<p align='center'>
    <img src='./docs/tela_cadastro.png' height=450 style="border-radius: 10px;">
</p>
<p align='center'>
    <img src='./docs/tela_editar.png' height=450 style="border-radius: 10px;">
</p>
A categoria do processo foi criada com um select field para aparecer apenas as categorias já cadastradas.

Na tela de editar os dados do processo que está sendo mofificado já vão para os campos por default, assim facilitando a alteração só nos campos desejados.
<hr>

### Tela de Administração do Site:
<p align='center'>
    <img src='./docs/admin_geral.png' height=450 style="border-radius: 10px;">
</p>
Aqui é possível ver todos os Models registrados no site, além de ser possível observar as mudanças feitas.

#### Tela de Administração dos Processos:
Aqui temos a tela de administração dos processos, onde podemos ver alguns detalhes e gerenciar os dados.
<p align='center'>
    <img src='./docs/admin_processos.png' height=450 style="border-radius: 10px;">
</p>
Foram feitas algumas alterações para melhorar a vizualização dessa página, como a implementação de uma tabela mais informativa, uma barra de pesquisa e uma filtro por categoria.

#### Tela de Administação das Categorias:
Por aqui adicionamos as categorias possíveis que os processos podem receber.
<p align='center'>
    <img src='./docs/admin_categorias.png' height=450 style="border-radius: 10px;">
</p>
<hr>