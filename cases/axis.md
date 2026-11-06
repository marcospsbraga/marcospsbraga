# AXIS — Visão do produto e alinhamento estratégico

**Data do alinhamento:** 06/11/2026  
**Responsável pelo produto:** IMPROVE  
**Estágio:** exploração e concepção (sem desenvolvimento iniciado neste alinhamento)  
**Natureza deste documento:** registro do que foi conversado em 06/11/2026. Não equivale à homologação de escopo, arquitetura, preço ou cronograma.

> **Princípio de trabalho:** discutir e validar o produto antes de desenhar telas ou programar. Distinguir direção inicial, hipótese e decisão ainda aberta. Este registro substitui o conteúdo conceitual anterior do AXIS; não incorpora definições de conversas antigas que não tenham sido retomadas neste alinhamento.

## 1. Visão geral

O **AXIS** é uma proposta de **plataforma SaaS própria da IMPROVE para academias**, com dois pilares de valor igualmente importantes:

1. **Centro de Operações:** simplificar e profissionalizar a administração da academia, oferecendo ferramentas realmente úteis para a equipe.
2. **Experiência do aluno:** aplicativo tecnológico e integrado à rotina de treinos, acompanhamento de evolução, relacionamento e recursos de inteligência artificial.

Um terceiro conjunto de experiências atende **professores e personal trainers**; a IMPROVE terá uma **administração interna da plataforma**. O equilíbrio pretendido é de qualidade e valor entregue, não necessariamente de número de telas nem de horas de implementação.

A entrada inicial imaginada é **academia tradicional/musculação**, com estrutura preparada para evoluir, se validado, para pilates, CrossFit, lutas e outros negócios fitness. A operação pode variar por modalidade, sem exigir produtos inteiramente separados.

## 2. Público, distribuição e foco inicial

- **Cliente pagante principal:** academia/estabelecimento que contrata uma assinatura do AXIS.
- **Usuários da academia:** proprietário, gestores, recepção, professores, personal trainers e outros profissionais, com funções e acessos apropriados.
- **Alunos:** recebem acesso ao aplicativo por meio da academia contratante, **sem pagamento obrigatório adicional ao AXIS**.
- **Descoberta inicial:** a própria academia apresenta o aplicativo aos seus alunos; não se pressupõe que o público geral conheça ou procure espontaneamente o AXIS.
- **Marketplace aberto para qualquer pessoa procurar/contratar personal independente:** **fora do foco inicial**, após ter sido explorado e temporariamente descartado por aumentar a complexidade.
- Uma área com academias participantes é uma possibilidade futura, mas a aquisição orgânica de alunos não será pressuposta como principal motor do lançamento.

**Piloto possível:** academia do tio do fundador. Ainda não houve conversa com ele; ele não foi apresentado à IMPROVE, e seus sistemas, dores reais e interesse são desconhecidos. A hipótese é oferecer uso como cliente-piloto, talvez gratuitamente ou cobrindo custos operacionais; **condições, propriedade intelectual, suporte e expectativas precisam ser combinados antes de qualquer parceria**.

## 3. Experiências e permissões

### Centro de Operações da academia
Possibilidades a investigar: cadastro e matrículas, planos e contratos, pagamentos, inadimplência, presença/acesso, agenda e aulas, organização da equipe, indicadores e comunicação com alunos. O objetivo é reduzir esforço administrativo e dar clareza à gestão.

### Ambiente profissional
Professores e personal trainers podem ter experiências próprias para seus alunos, treinos, avaliações, acompanhamento e alertas. Foi defendida a **separação conceitual entre professor vinculado à academia e personal trainer**, porque suas relações e permissões podem ser diferentes. Um personal independente, sem vínculo com academia, foi considerado como possibilidade, mas **não transforma automaticamente o AXIS em marketplace nesta fase**.

### Aplicativo do aluno
Acompanhar treinos, evolução, cargas, frequência, metas e comunicação com a academia, conforme recursos disponíveis e autorizações aplicáveis. A experiência deve ser excelente mesmo quando a academia não contrata os módulos administrativos mais caros.

### Administração da IMPROVE
Ambiente interno para clientes/academias, assinaturas, planos, módulos, suporte e monitoramento da operação SaaS; **não deve significar acesso indiscriminado aos dados internos das academias**.

### Base compartilhada, contextos separados
A direção conceitual é **uma plataforma com dados coerentes e experiências personalizadas por perfil**, e não quatro sistemas desconectados. A mesma pessoa pode ter papéis distintos em academias distintas.

- A identidade de um usuário é distinta de seu vínculo e de suas permissões em cada academia.
- Cada academia deve ter seus dados empresariais isolados das demais.
- As permissões precisam ser efetivamente conferidas no servidor, não apenas escondendo botões.
- Identidade visual, módulos e regras podem ser configurados por academia.

**Não há tecnologia, banco, infraestrutura ou arquitetura detalhada homologados.**

## 4. Aplicativo único e continuidade da jornada

**Preferência inicial:** um **único aplicativo AXIS para alunos de várias academias**, personalizado com identidade e serviços do estabelecimento com o qual o aluno possui vínculo.

**Outra direção inicial:** a pessoa mantém sua conta e uma **trajetória fitness pessoal permitida**, inclusive ao mudar de academia. Dados de contratos, pagamentos, avaliações profissionais e demais registros da academia permanecem segregados. A continuidade ou transferência de informações exige regras de finalidade, responsabilidade, acesso, retenção e privacidade; dados de uma academia não aparecem automaticamente em outra.

O modo pessoal gratuito para alguém sem matrícula foi discutido como possibilidade, **não decidido para lançamento**. Também não foram definidos detalhes de portabilidade ou políticas de retenção.

## 5. Inteligência artificial em toda a plataforma

A experiência de IA mais valorizada no alinhamento combina duas formas de atuação:

- **Proativa:** observa dados disponíveis e autorizados, identifica padrões úteis e inicia alertas contextualizados.
- **Conversacional:** campo de perguntas e respostas, com capacidade de explicar dados e apoiar a tomada de decisões.

Exemplos discutidos:

- **Aluno:** aviso sobre queda de frequência, reconhecimento de progressão de carga e conversa sobre evolução.
- **Professor/personal:** identificação de alunos com queda de presença ou evolução estagnada, resumo para acompanhamento e sugestões de revisão profissional.
- **Gestor:** alertas de inadimplência, indicadores operacionais e perguntas em linguagem natural sobre sua academia.

**Agentes que executam tarefas** (ex.: preparar cobranças, relatórios e rotinas) são uma evolução possível, especialmente em planos/módulos mais avançados. Ações relevantes devem ter permissões, registro de execução e aprovação humana quando apropriado.

**Limites essenciais:** a IA deve apoiar, não substituir a responsabilidade de profissionais qualificados. Não prometer precisão inexistente — por exemplo, prever peso futuro exato apenas com dados de esteira. Dados de saúde, desempenho e decisões automatizadas exigem atenção especial à privacidade, ao controle de acesso e à segurança.

## 6. Comercialização — direção recomendada

**Modelo central:** o AXIS pertence à IMPROVE; as academias **assinam** o serviço. A venda definitiva do software a cada cliente **não é o modelo padrão pretendido**.

A recomendação comercial acolhida nesta conversa é um **modelo híbrido**:

1. **Planos progressivos** (nomes ilustrativos: Essencial, Pro e Business).
2. **Faixas de alunos ativos/porte**, para que preço e capacidade acompanhem a operação.
3. **Poucos módulos adicionais relevantes**, especialmente pacotes de automação e agentes de IA, sem cobrar por cada microfuncionalidade.

Um estabelecimento pode escolher um plano e contratar um módulo específico sem necessariamente migrar para outro plano. A composição precisa ser compreensível: se a soma dos extras superar um plano superior equivalente, o AXIS deve sugerir a alternativa mais vantajosa.

Agentes de IA não devem ser precificados apenas por quantidade; importam **tipo de tarefa, volume e custo de uso**. Evitar cobranças excedentes inesperadas e trabalhar com limites claros.

**Não homologados:** nomes e número final de planos, tabelas de preços, faixas de alunos, pacotes, limites de IA e regras de upgrade. Os valores citados durante exemplos foram apenas ilustrativos.

### Vendas e contratação

A **experiência final desejada é autônoma**: a academia conhece a oferta, cadastra-se, escolhe plano e módulos, configura a conta e acompanha contratação e alterações no próprio AXIS. Inicialmente, a IMPROVE provavelmente fará **vendas consultivas e implantação acompanhada**, sem impedir a automação futura.

**Experimentação:** uma demonstração interativa com dados fictícios e um teste gratuito com dados próprios são ideias bem recebidas. O prazo de 14 dias foi apenas sugestão, **não aprovado**. Permanecem em estudo os recursos disponíveis no teste, conversão para planos, limites de uso e prevenção de abuso.

**Antifraude em hipótese:** vincular elegibilidade do teste ao estabelecimento, não só ao e-mail, e adotar verificação e limites proporcionais, sem fricção excessiva.

## 7. O que não vamos assumir como decidido

- Desenvolver todas as modalidades fitness, marketplace ou contratação de personals no primeiro lançamento.
- Tornar o AXIS uma plataforma fitness independente de academias já na V1.
- Cobrar os alunos pelo acesso básico fornecido pela academia.
- Prever resultados físicos exatos por IA ou permitir decisões profissionais automáticas sem controles.
- Definir tecnologias, interfaces, banco de dados, fornecedores ou cronograma.
- Fechar preços, planos definitivos, regras do teste ou custos antes de validação.
- Presumir que o tio já é cliente, investidor ou parceiro; não houve proposta a ele.
- Construir um produto gigantesco antes de validar o valor inicial com uma operação real.

## 8. Continuidade do trabalho

O momento atual é **conversa e alinhamento**, sem desenho de telas ou implementação. Próximas discussões úteis, uma questão de cada vez:

- Como funcionam operações reais de academias e quais dores justificam a assinatura?
- Quais jornadas e permissões são indispensáveis para gestor, recepção, professor, personal e aluno?
- Qual o menor lançamento capaz de entregar valor alto aos dois pilares?
- Quais dados acompanham o aluno entre estabelecimentos e sob quais regras?
- Como medir o impacto do AXIS na rotina e retenção de alunos?
- Quando e como validar os recursos de IA, o consumo e a oferta comercial?

**Resumo da direção:** um SaaS modular de gestão de academias e experiência do aluno, com perfis separados, aplicativo compartilhado personalizável, IA contextual/proativa e comercialização por assinatura; crescimento gradual, baseado em validação real.

---

*Registro exclusivo da conversa de 06/11/2026. Ideias ainda abertas não devem ser tratadas como funcionalidades aprovadas, desenvolvidas ou lançadas.*
