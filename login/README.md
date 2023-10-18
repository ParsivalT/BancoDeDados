## Armazenamento de Senhas

É muito importante não armazenar senhas diretamente no banco de dados por questões de segurança. Vou explicar isso com um exemplo hipotético para facilitar a compreensão:

Imagine que você tem uma caixa de tesouros (seu banco de dados) onde guarda informações preciosas, como senhas. Agora, você quer proteger essa caixa contra ladrões (pessoas mal-intencionadas).

**Cenário 1: Senhas armazenadas diretamente no banco de dados**
Se você colocar as senhas diretamente na caixa de tesouros, qualquer pessoa que acesse o banco de dados terá acesso a essas senhas. Isso é como se você deixasse a caixa trancada, mas deixasse a chave pendurada ao lado dela. Se alguém conseguir entrar no banco de dados, todas as senhas estarão à disposição, o que é uma ameaça grave à segurança.

**Cenário 2: Armazenamento seguro das senhas**
A abordagem segura é não guardar as senhas na caixa de tesouros, mas sim guardar algo que seja difícil de ser revertido para as senhas reais. Em vez de senhas, você guarda o equivalente a uma receita de bolo. Por exemplo, se a senha for "12345", você guarda uma versão codificada dela, como "A2D3F5G1". Isso é chamado de "hashing".

Quando alguém tentar fazer login, você pega a senha inserida, aplica o mesmo "hashing" e compara o resultado com o que está na caixa. Se eles combinarem, o acesso é concedido. Dessa forma, mesmo que alguém acesse o banco de dados, eles não encontrarão senhas reais, apenas as versões codificadas, que são muito difíceis de serem revertidas para as senhas originais.

Resumindo, a importância de não armazenar senhas diretamente no banco de dados é proteger a privacidade e segurança dos seus usuários. Se as senhas vazarem, os dados pessoais e contas dos usuários estarão em risco. Portanto, é fundamental adotar práticas seguras de armazenamento, como o "hashing", para garantir a segurança das senhas.
