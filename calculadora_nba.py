class NBAStatsCalculator:
    def __init__(self):
      self.minutes_played = 0
      self.points = 0
      self.field_goal_attempted = 0
      self.field_goal_made = 0
      self.three_point_shot_attempted = 0
      self.three_point_shot_made = 0
      self.freethrow_made = 0
      self.freethrow_attempted = 0
      self.assists = 0
      self.turnovers = 0
      self.steals = 0
      self.blocks = 0

    def calcular_fg_percent(self):
      if self.field_goal_attempted == 0:
        return 0
      return float(self.field_goal_made)/float(self.field_goal_attempted)
    
    def calcular_3pt_percent(self):
      if self.three_point_shot_attempted == 0:
        return 0
      return float(self.three_point_shot_made)/float(self.three_point_shot_attempted)
    
    def calcular_ftr(self):
      if self.freethrow_attempted == 0:
        return 0
      return float(self.freethrow_made)/float(self.freethrow_attempted)
    
    def calcular_assists_per_turnover(self):
      if self.turnovers == 0:
        return 0
      return float(self.assists)/float(self.turnovers)
    
    def calcular_2pt_percent(self):
      numero_cestas_2pt_tentadas = self.field_goal_attempted - self.three_point_shot_attempted
      numero_cestas_2pt_acertadas = self.field_goal_made - self.three_point_shot_made
      if numero_cestas_2pt_tentadas == 0:
        return 0
      return float(numero_cestas_2pt_acertadas)/float(numero_cestas_2pt_tentadas)

    def calcular_ts_percent(self):
      if self.field_goal_attempted == 0 and self.freethrow_attempted == 0:
        return 0
      ts = (self.points/2)/(self.field_goal_attempted + 0.475*self.freethrow_attempted)
      return ts
    
    def receber_dados(self):
      self.minutes_played = int(input("Digite o numero de minutos jogados: "))
      self.points = int(input("Digite o numero de pontos: "))
      self.field_goal_attempted = int(input("Digite o numero de fga: "))
      self.field_goal_made = int(input("Digite o numero de fgm: "))
      self.three_point_shot_attempted = int(input("Digite o numero de 3pa: "))
      self.three_point_shot_made = int(input("Digite o numero de 3pm: "))
      self.freethrow_made = int(input("Digite o numero de ftm: "))
      self.freethrow_attempted = int(input("Digite o numero de fta: "))
      self.assists = int(input("Digite o numero de assistências: "))
      self.turnovers = int(input("Digite o numero de turnovers: "))
      self.steals = int(input("Digite o numero de steals: "))
      self.blocks = int(input("Digite o numero de blocks: "))
