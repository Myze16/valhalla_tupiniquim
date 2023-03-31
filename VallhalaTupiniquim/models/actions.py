class Acoes:
    def atacar(player, alvo):

    


    def ataca(self, alvo, ataque, dano):
        ataque.randint(1,6)
        if ataque <= 2:
            dano.alvo = 0
        elif ataque > 2 <= 5:
            dano.alvo = 2
        else:
            dano.alvo = 4
        alvo.dano(dano)
        mensagem = f"{self.nome} atacou {alvo.nome} causando {dano: .2f} de dano!"
        self.mensagem(mensagem)