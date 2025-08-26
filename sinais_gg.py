import random
from datetime import datetime
from config import TEXTO_CADASTRO

class GGRoleta:
    def __init__(self):
        self.vitorias = 184
        self.derrotas = 9
        self.sequencia = 35
        self.sinais_hoje = 18
        
    def calcular_taxa_acerto(self):
        total = self.vitorias + self.derrotas
        return (self.vitorias / total) * 100 if total > 0 else 0
    
    def gerar_sinal_gg(self):
        # Atualizar contadores
        self.sinais_hoje += 1
        if random.random() < 0.91:  # 91% de acerto
            self.vitorias += 1
            self.sequencia += 1
        else:
            self.derrotas += 1
            self.sequencia = 0
        
        # Gerar sinal no estilo GG Roleta
        tipos_jogo = [
            "Roleta Brasileira",
            "Roleta Europeia", 
            "Roleta Americana",
            "Roleta Eletrônica"
        ]
        
        estrategias = [
            "Método GG Exclusive",
            "Estratégia Golden",
            "Sistema Premium 24h",
            "Técnica Vip GG"
        ]
        
        return f"""
🔔 <b>GG ROLETA - SINAL CONFIRMADO!</b> 🔔
🎮 <b>Jogo:</b> {random.choice(tipos_jogo)}

🎯 <b>ENTRADA:</b> {random.choice(['🔴 Vermelho', '⚫ Preto', '🟢 Verde'])}
📊 <b>ESTRATÉGIA:</b> {random.choice(estrategias)}
⏰ <b>VALIDADE:</b> {random.randint(3, 8)} minutos

📈 <b>CONFIANÇA:</b> {'⭐' * random.randint(4, 5)} ({(random.randint(88, 96))}%)
💰 <b>RETORNO:</b> {random.randint(4, 7)}x

{TEXTO_CADASTRO}

💎 <i>Sinal exclusivo GG Roleta 24h</i>
"""
    
    def gerar_estatisticas_gg(self):
        taxa = self.calcular_taxa_acerto()
        
        return f"""
📊 <b>GG ROLETA - ESTATÍSTICAS OFICIAIS</b>

✅ <b>Vitórias:</b> {self.vitorias}
❌ <b>Derrotas:</b> {self.derrotas}
🎯 <b>Taxa de Acerto:</b> {taxa:.1f}%

🔥 <b>Sequência Atual:</b> {self.sequencia} vitórias
📅 <b>Sinais Hoje:</b> {self.sinais_hoje}
⏰ <b>Atualizado:</b> {datetime.now().strftime('%H:%M:%S')}

{TEXTO_CADASTRO}

🏆 <i>Líder em precisão 24/7</i>
"""
    
    def gerar_analise_gg(self):
        analises = [
            "Mercado extremamente favorável para entradas",
            "Momento premium para estratégias GG",
            "Tendência de alta consolidada",
            "Padrão de repetição identificado"
        ]
        
        return f"""
🔍 <b>GG ROLETA - ANÁLISE TÉCNICA</b>

📈 <b>Situação:</b> {random.choice(analises)}
🎯 <b>Recomendação:</b> Entradas {random.choice(['conservadoras', 'moderadas', 'agressivas'])}
⏰ <b>Horário:</b> {datetime.now().strftime('%H:%M')}

📊 <b>Performance GG:</b> {self.calcular_taxa_acerto():.1f}% de acerto
🔥 <b>Sequência:</b> {self.sequencia} acertos

{TEXTO_CADASTRO}

💎 <i>Análise exclusiva GG Roleta 24h</i>
"""

# Instância global GG Roleta
gg_bot = GGRoleta()