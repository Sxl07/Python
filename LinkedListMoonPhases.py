from colorama import Fore, Style, init

init()


class Month:

  def __init__(self, name=None, days=0):
    self.next = None
    self.name = name
    self.days = days
    dic = [{'dia': i + 1, 'faseLunar': " "} for i in range(days)]
    self.dictDay = dic
    if self.name == "Enero":
      self.numberMonth = 1
    if self.name == "Febrero":
      self.numberMonth = 2
    if self.name == "Marzo":
      self.numberMonth = 3
    if self.name == "Abril":
      self.numberMonth = 4
    if self.name == "Mayo":
      self.numberMonth = 5
    if self.name == "Junio":
      self.numberMonth = 6
    if self.name == "Julio":
      self.numberMonth = 7
    if self.name == "Agosto":
      self.numberMonth = 8
    if self.name == "Septiembre":
      self.numberMonth = 9
    if self.name == "Octubre":
      self.numberMonth = 10
    if self.name == "Noviembre":
      self.numberMonth = 11
    if self.name == "Diciembre":
      self.numberMonth = 12


class LinkedList:

  def __init__(self):
    self.head = None

  def append(self, name, days, year):
    new_node = Month(name, days)
    new_node.year = year
    if self.head is None:
      self.head = new_node
    else:
      cur_node = self.head
      while cur_node.next is not None:
        cur_node = cur_node.next
      cur_node.next = new_node

  def lunarPhase(self, year, month, day) -> str:
    a = (14 - month) // 12
    y = year + 4800 - a
    m = month + 12 * a - 3
    jdn = day + (
        (153 * m + 2) // 5) + 365 * y + y // 4 - y // 100 + y // 400 - 32045

    new_moon_jdn = 2451550.1
    lunar_cycle = 29.53
    days_since_new_moon = jdn - new_moon_jdn
    lunar_phase = (days_since_new_moon % lunar_cycle) / lunar_cycle * 8
    rounded_phase = round(lunar_phase) % 8

    phases = [
        "Luna Nueva🌑", "Luna Nueva Visible🌒", "Luna Cuarto Creciente🌓",
        "Luna Gibada Creciente🌔", "Luna Llena🌕", "Luna Gibada Menguante🌖",
        "Cuarto Menguante🌗", "Luna Menguante🌘"
    ]
    return (phases[rounded_phase])

  def colorPhase(self, year, month, day) -> str:
    a = (14 - month) // 12
    y = year + 4800 - a
    m = month + 12 * a - 3
    jdn = day + (
        (153 * m + 2) // 5) + 365 * y + y // 4 - y // 100 + y // 400 - 32045

    new_moon_jdn = 2451550.1
    lunar_cycle = 29.53
    days_since_new_moon = jdn - new_moon_jdn
    lunar_phase = (days_since_new_moon % lunar_cycle) / lunar_cycle * 8
    rounded_phase = round(lunar_phase) % 8
    phases = [
        Fore.LIGHTWHITE_EX, Fore.CYAN, Fore.MAGENTA,Fore.LIGHTBLACK_EX ,Fore.YELLOW, Fore.BLUE,Fore.RED,Fore.GREEN]
    
    return (phases[rounded_phase])

  def displayPhase(self, year, month, day):
    cur_node = self.head
    siguiente = cur_node.next
    while ((cur_node is not None) and (siguiente.numberMonth != month + 1)):
      for i in range(0, len(cur_node.dictDay)):
        cur_node.dictDay[i]["faseLunar"] = self.lunarPhase(
            cur_node.year, cur_node.numberMonth, cur_node.dictDay[i]["dia"])

        if ((day == cur_node.dictDay[i]["dia"])
            and (cur_node.numberMonth == month)):
          fecha = (day, month, year)
          print("La fase Lunar en el hemisferio Norte para la fecha:",
                '{:02d}/{:02d}/{:04d}'.format(*fecha), "es:",
                cur_node.dictDay[i]["faseLunar"])
      cur_node = cur_node.next

  def displayCalendar(self, start_day, year):
    days_of_week = ["Do", "Lu", "Ma", "Mi", "Ju", "Vi", "Sa"]
    cur_node = self.head
    print(Fore.LIGHTWHITE_EX+" Luna Nueva🌑\n",Fore.CYAN +"Luna Nueva Visible🌒\n",Fore.MAGENTA + "Luna Cuarto Creciente🌓\n",
       Fore.LIGHTBLACK_EX + "Luna Gibada Creciente🌔\n", Fore.YELLOW+"Luna Llena🌕\n",Fore.BLUE+ "Luna Gibada Menguante🌖\n", Fore.RED+"Cuarto Menguante🌗\n",Fore.GREEN+ "Luna Menguante🌘\n"+Style.RESET_ALL)
    print(str(cur_node.year).center(21, "-") + "+")
    print(" " * 21 + "|")
    while cur_node is not None:
      print((cur_node.name).center(20, "-"), "+")
      print(" ".join(days_of_week), "|")
      day = 1
      for i in range(0, len(cur_node.dictDay)):
        cur_node.dictDay[i]["faseLunar"] = self.lunarPhase(cur_node.year, cur_node.numberMonth, cur_node.dictDay[i]["dia"])
        color= self.colorPhase(cur_node.year, cur_node.numberMonth, cur_node.dictDay[i]["dia"])
        
        if cur_node.dictDay[i]["dia"] == 1:
          print("   " * start_day, end="")
        
        print(color + "{:>2}".format(cur_node.dictDay[i]["dia"]) +
              Style.RESET_ALL,
              end=" ")
        if (day + start_day) % 7 == 0:
          print("|")
        if cur_node.dictDay[i]["dia"] == len(cur_node.dictDay):
          print("   " * (7 - ((start_day + cur_node.days) % 7)), end="|")
        day += 1
      print()
      print(" " * 20, "|")
      start_day = (start_day + cur_node.days) % 7
      cur_node = cur_node.next
    print("-" * 21 + "+")

  def remove_month_days(self):
    self.head = None


months = LinkedList()


def set_month_days(year):
  months.append("Enero", 31, year)
  months.append(
      "Febrero", 28 if not year % 4 == 0 or
      (year % 100 == 0 and not year % 400 == 0) else 29, year)
  months.append("Marzo", 31, year)
  months.append("Abril", 30, year)
  months.append("Mayo", 31, year)
  months.append("Junio", 30, year)
  months.append("Julio", 31, year)
  months.append("Agosto", 31, year)
  months.append("Septiembre", 30, year)
  months.append("Octubre", 31, year)
  months.append("Noviembre", 30, year)
  months.append("Diciembre", 31, year)


def get_first_day_of_year(year):
  day = (1 + 5 * ((year - 1) % 4) + 4 * ((year - 1) % 100) + 6 *
         ((year - 1) % 400)) % 7
  days = [0, 1, 2, 3, 4, 5, 6]
  return days[day]


yearCalendar = int(input("Digite el año del Calendario a imprimir\n"))
set_month_days(yearCalendar)
x = 0
while (x != 4):
  x = int(
      input(
          "---------elige la opcion a ejecutar---------\n1)Imprimir Calendario\n2)Buscar la Fase Lunar en una fecha especifica\n3)Cambiar el año a ejecutar\n4)Salir\n"
      ))
  if (x == 1):
    print("\n===========================================\n")
    months.displayCalendar(get_first_day_of_year(yearCalendar), yearCalendar)
    print("\n===========================================\n")
  elif (x == 2):
    mesFase = int(input("Ingresa el mes a buscar(1-12)\n"))
    diaFase = int(input("Ingresa el dia a buscar\n"))
    print("\n===========================================\n")
    months.displayPhase(yearCalendar, mesFase, diaFase)
    print("\n===========================================\n")
  elif (x == 3):
    months.remove_month_days()
    yearCalendar = int(input("Digite el año del Calendario a imprimir\n"))
    set_month_days(yearCalendar)
  elif (x == 4):
    print("\nEl programa fue finalizado con exito.\n")
  else:
    x = int(
        input(
            "---------elige la opcion a ejecutar---------\n1)Imprimir Calendario\n2)Buscar la Fase Lunar en una fecha especifica\n3)Cambiar el año a ejecutar\n4)Salir\n"
        ))
