texto = 'O Naruto pode ser um pouco duro as vezes, talvez você não saiba disso, mas o Naruto também cresceu sem pai.Na verdade ele nunca conheceu nenhum de seus pais, e nunca teve nenhum amigo em nossa aldeia.Mesmo assim eu nunca vi ele chorar, ficar zangado ou se dar por vencido, ele está sempre disposto a melhorar, ele quer ser respeitado, é o sonho dele e o Naruto daria a vida por isso sem hesitar.Meu palpite é que ele se cansou de chorar e decidiu fazer alguma coisa a respeito!'
#i = contador do while para ir de 40 em 40
i = 40
#j = pegar onde começa o ultimo caracter da linha
j = 39
#k = pegar onde termina o ultimo caracter da linha
k = 40
#l = indice onde vai começar a linha
l = 0

#vai ficar no loop até o i ser maior que o número de caracter do texto
while i<len(texto)+40:
    #defini uma variavel linha para ficar mais facil o controle
    linha = texto
    #se o ultimo caracter for diferente que um espaço(não tiver uma letra)
    if(linha[j:k]!=' '):
        #ira repetir até encontrar um espaço
        while linha[j:k]!=' ':
            #subtrair os indices em -1 para voltar um caracter
            j-=1
            k-=1
    #irá printar a linha
    print(linha[l:k])
    # irá definir o l(onde ira começar a proxima linha) para igual ao k(onde parou a linha)
    l=k
    # irá adcionar um intervalo de 40
    k+=40
    j+=40
    i += 40
#irá printar o resto que sobrou
print(texto[k-40:])
