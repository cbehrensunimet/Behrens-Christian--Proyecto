from datetime import datetime


now = datetime.now()

day = now.day

year = now.year


if now.month ==1:
    month = 'Enero'
elif now.month ==2:
    month = 'Febrero'
elif now.month ==3:
    month = 'Marzp'
elif now.month ==4:
    month = 'Abril'
elif now.month ==5:
    month = 'Mayo'
elif now.month ==6:
    month = 'Junio'
elif now.month ==7:
    month = 'Julio'
elif now.month ==8:
    month = 'Agosto'
elif now.month ==9:
    month = 'Septiembre'
elif now.month ==10:
    month = 'Octubre'
elif now.month ==11:
    month = 'Noviembre'
elif now.month ==12:
    month = 'Diciembre'