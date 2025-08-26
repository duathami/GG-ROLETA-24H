import random
from datetime import datetime, timedelta
from config import TEXTO_CADASTRO

class Estatisticas:
    def __init__(self):
        # Valores iniciais baseados no seu pedido
        self.vitorias = 75
        self.empates = 6
        self.derrotas = 3
        self.sequencia = 33
        self.ultima_atualizacao = datetime.now()
        
    def calcular_taxa_acerto(self):
        total_jogadas = self.vitorias + self.empates + self.derrotas
        if total_jogadas > 0:
            return (self.vitorias / total_jogadas) * 100
        return 0
    
    def simular_crescimento_realista(self):
        """Simula crescimento orgânico ao longo do tempo"""
        horas_desde_inicio = (datetime.now() - self.ultima_atualizacao).total_seconds() / 3600
        
        # A cada hora, simular algumas jogadas
        jogadas_por_hora = random.randint(1, 3)
        total_jogadas_simuladas = int(horas_desde_inicio * jogadas_por_hora)
        
        for _ in range(total_jogadas_simuladas):
            # 92% de chance de vitória (bem alto)
            if random.random() < 0.92:
                self.vitorias += 1
                self.sequencia += 1
            elif random.random() < 0.06:  # 6% de empate
                self.empates += 1
            else:  # 2% de derrota
                self.derrotas += 1
                self.sequencia = 0
        
        self.ultima_atualizacao = datetime.now()
    
    def gerar_estatistica_diaria(self):
        # Atualizar estatísticas realisticamente
        self.simular_crescimento_realista()
        taxa = self.calcular_taxa_acerto()
        
        # Garantir taxa mínima de 90%
        taxa_ajustada = max(taxa, 90.0)
        
        return f"""
📊 <b>ESTATÍSTICAS EM TEMPO REAL</b>

✅ <b>Vitórias:</b> {self.vitorias}
🟢 <b>Empates:</b> {self.empates}
🚫 <b>Derrotas:</b> {self.derrotas}

🍀 <b>Sequência Atual:</b> {self.sequencia} vitórias
🎯 <b>Taxa de Acerto:</b> {taxa_ajustada:.2f}%

📈 <b>Total de Jogadas:</b> {self.vitorias + self.empates + self.derrotas}
⚡ <b>Próximo Sinal:</b> Em {random.randint(2, 10)} minutos
🕐 <b>Atualizado:</b> {datetime.now().strftime('%H:%M:%S')}

{TEXTO_CADASTRO}

⚠️ Jogue com Responsabilidade. Somente para Maiores de 18 Anos.
"""

    def atualizar_estatisticas(self):
        """Atualiza com nova jogada (chamado a cada comando)"""
        # 92% de chance de vitória - MANTÉM ALTA TAXA
        if random.random() < 0.92:
            self.vitorias += 1
            self.sequencia += 1
        elif random.random() < 0.06:  # 6% de empate
            self.empates += 1
        else:  # 2% de derrota
            self.derrotas += 1
            self.sequencia = 0

# Instância global das estatísticas
stats = Estatisticas()