# Problema
# Dada uma fita que contém 4 tipos de base (representada por caracteres), encontrar o maior número de ligações com os pares correspondentes sabendo que a fita pode ser dobrada.

# Observação
# Explorando o fato de que todas as bases envolvidas numa dobra devem efetuar ligações correspondentes, qualquer dobra só é iniciada após duas bases que ligam entre si estarem em sequência.

# Dicas
# Uma dobra somente ocorre quando existe duas bases em sequência que podem ligar-se.
# Quando uma base pode efetuar ligação com outra, essa sempre é uma escolha ótima.
# Já tentou usar uma pilha?


## Solução
#  [Ocultar] A solução fica oculta por padrão. Desencorajamos que você olhe a solução do problema antes de ter tentado.
# Com a observação acima, podemos elaborar uma solução gulosa. Dado uma fita F e um par de bases em sequência que é possível efetuar uma ligação, o número de ligações em F será de uma acrescida ao número de ligações de F′ que nada mais é do que a fita F sem o par de bases ligado. Concluindo, seja S(F) o número de ligações da fita F, e seja P um par de bases em sequência que podem ligar-se, então:
# Se P∉F,S(F)=0

# Senão, S(F)=1+S(F−P)



## Implementação
# Uma maneira bem simples de implementar esta solução é utilizando pilha. A cada base que for inserida na pilha, 
# verifica se esta pode ligar-se com a base do topo da pilha, que em caso positivo, não é inserida e a do topo é removida.
# O número de pares removidos é o máximo de ligações que podem ser realizadas. O custo desta solução é claramente linear, O(n), com n sendo o número de bases presentes na fita.






# link: http://wiki.maratona.dcc.ufmg.br/index.php/ACIDO#
