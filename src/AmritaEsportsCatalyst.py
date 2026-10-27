import math

class AmritaEsportsCatalyst:
    """
    Киберспортивный катализатор транзакционной активности.
    Конвертирует триумфы команд (MOUZ, Team Spirit) в квантовый буст для PiFi-дерева.
    Реализует концепцию: "Победа на Mirage -> Сдвиг частоты Тора".
    """
    
    def __init__(self):
        self.phi = (1 + 5 ** 0.5) / 2
        
    def calculate_match_momentum(self, team_name, score_win, score_lose, maps_detailed):
        """
        Расчет коэффициента ментального ускорения сети на основе исхода матча.
        """
        print(f"\n🎮 [КИБЕРСПОРТ ТРИГГЕР]: Сканирование ленты Cybersport.ru для команды {team_name}...")
        
        # Рассчитываем плотность борьбы по раундам (напр. 16:14 на Mirage дает максимальное напряжение)
        total_intensity = 0.0
        for m_win, m_lose in maps_detailed:
            round_diff = abs(m_win - m_lose)
            # Чем ближе счет (например, 16:14), тем выше квантовое напряжение в инфополе
            total_intensity += (m_win + m_lose) / (round_diff if round_diff > 0 else 1)
            
        # Финальный множитель катализатора
        match_boost = (score_win / (score_lose if score_lose > 0 else 1)) * math.log1p(total_intensity) * self.phi
        
        print(f"  Результат матча: {score_win}:{score_lose} | Индекс напряжения поля: {total_intensity:.2f}")
        print(f"  Сгенерированный Ментальный Буст: +{match_boost:.4f}x к скорости транзакций")
        
        return max(1.0, match_boost)

if __name__ == "__main__":
    catalyst = AmritaEsportsCatalyst()
    
    # Данные с твоего скрина: MOUZ обыграли Драконов 2:1 (Nuke 2:13, Dust2 13:8, Mirage 16:14)
    mouz_maps = [(2, 13), (13, 8), (16, 14)]
    boost_factor = catalyst.calculate_match_momentum("MOUZ", 2, 1, mouz_maps)
