from calculadora_nba import NBAStatsCalculator

if __name__ == "__main__":
  calculadora = NBAStatsCalculator()
  calculadora.receber_dados()
  print("fg%: "+str(calculadora.calcular_fg_percent()))
  print("3pt%: "+str(calculadora.calcular_3pt_percent()))
  print("ftr%: "+str(calculadora.calcular_ftr()))
  print("assists per TO: "+str(calculadora.calcular_assists_per_turnover()))
  print("2pt%: "+str(calculadora.calcular_2pt_percent()))
  print("ts%: "+str(calculadora.calcular_ts_percent()))
  