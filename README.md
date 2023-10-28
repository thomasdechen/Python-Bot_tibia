🤖 Bot para o Jogo Tibia - Automatizando com Python

Neste projeto, desenvolvi um bot para o jogo Tibia que passou por várias versões. O principal objetivo por trás desses bots foi me divertir enquanto aprendia programação em Python e me familiarizava com várias bibliotecas. Uma biblioteca crucial que utilizei foi o pyautogui para reconhecimento de imagem.

Esses projetos serviram como excelentes oportunidades para praticar o raciocínio lógico, explorar conceitos de programação e entender a importância de algoritmos na prática.

🎮 Interação com o Jogo e Automatização

Os bots que criei são projetados para interagir com o ambiente do jogo e automatizar certas ações. Os movimentos do personagem são facilitados usando o minimap, e os bots incluem opções para atacar monstros sob condições específicas. Por exemplo, o personagem pode enfrentar monstros ao alcançar uma posição designada no minimap ou quando um número predefinido de monstros é detectado na tela. Essa detecção de monstros é realizada por meio do menu de 'batalha' do jogo, utilizando técnicas de reconhecimento de imagem e a cor de um pixel específico.

📊 Gestão de Recursos e Capacidade de fazer 'Resupply'

Um recurso notável dos bots é sua capacidade de gerenciar recursos e atuar de maneira 100% autônoma. O bot é programado para monitorar os suprimentos restantes, tomando decisões inteligentes sobre quando iniciar um processo de 'recarga'. Essa 'recarga' envolve armazenar itens coletados e comprar os suprimentos necessários para permitir uma próxima caçada. A implementação desse mecanismo de gerenciamento de recursos depende de uma biblioteca chamada Pytesseract. Essa biblioteca permite que o bot leia imagens do jogo, extraia informações numéricas de regiões específicas e, posteriormente, atualize variáveis. Consequentemente, o bot pode acompanhar com precisão a contagem de poções de cura do personagem, garantindo que o personagem não fique sem suplimentos.

Através desses projetos, não apenas aprimorei minhas habilidades de programação, mas também compreendi a importância dos algoritmos na otimização do programa e redução de funções gigantes para funções menores.

📂Sobre os arquivos do programa
all_images: Todas imagens além das marcações do minimap, imagens de monstros, portas, bancos de depósitos, poções, etc;
refill_map: Marcações do mapa utilizadas para fazer o refill do personagem.
tibiamap: Marcações do mapa utilizadas para o personagem se movimentar dentro do local de caça.

Obs: O programa incorpora dois loops distintos: o loop principal é ativado quando o personagem está na área de caça; já o segundo loop é acionado quando o personagem necessita reabastecer seus suprimentos. Nesse cenário, o programa entra em um loop específico que utiliza a pasta "refill_map" para orientar os movimentos pelo minimap.

| 🗺️ Funções                          | Status |
|------------------------------------|--------|
| Alertas                            | ✔️     |
| Auto ring                          | ✔️     |
| Cavebot                            | ✔️     |
| Combinação de Ataques              | ✔️     |
| Descarte de Frascos                | ✔️     |
| Depósito de Itens Não Empilhados   | ✔️     |
| Depósito de Itens Empilhados       | ✔️     |
| Consumidor de Comida               | ✔️     |
| Cura                               | ✔️     |
| Seleção Inteligente de Alvos       | ✔️     |
| Recarga                            | ✔️     |
| Coleta Rápida                      | ✔️     |
| Venda de Frascos                   | ✔️     |

