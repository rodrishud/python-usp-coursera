x = int(input('Por favor, entre com o número de segundos que deseja converter: '))

dias = x // 86400
s1 = x % 86400
horas = s1 // 3600
s2 = s1 % 3600
minutos = s2 // 60
s3 = s2 % 60

print(dias, 'dias,', horas, 'horas,', minutos, 'minutos e', s3, 'segundos.')
