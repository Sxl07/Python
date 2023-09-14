class Month: 
    def __init__(self, name=None, days=0):
        self.next = None
        self.name = name
        self.days = days 
        list = []
        for i in range(1, days + 1):
            list.append(i)
        self.listDay = list
      
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

    def display(self, start_day, year):
        days_of_week = ["Do", "Lu", "Ma", "Mi", "Ju", "Vi", "Sa"]
        cur_node = self.head
        print(str(cur_node.year).center(21,"-")+"+")
        print(" "*21+"|")
        while cur_node is not None:
            
            print((cur_node.name).center(20,"-"),"+")
            print(" ".join(days_of_week),"|")
            day = 1
            for i in range(0,len(cur_node.listDay)):
                if cur_node.listDay[i] == 1:
                    print("   " * start_day, end="")
                print("{:>2}".format(cur_node.listDay[i]), end=" ")
                if (day + start_day) % 7 == 0:
                    print("|")
                if cur_node.listDay[i]==len(cur_node.listDay):
                    print("   "*(7-((start_day + cur_node.days) % 7)),end="|")
                day += 1  
            print()    
            print(" "*20,"|")
            start_day = (start_day + cur_node.days) % 7
            cur_node = cur_node.next
        print("-"*21+"+")
      
months = LinkedList()
months.append("Enero", 31, 2023)
months.append("Febrero", 28, 2023)
months.append("Marzo", 31, 2023)
months.append("Abril", 30, 2023)
months.append("Mayo", 31, 2023)
months.append("Junio", 30, 2023)
months.append("Julio", 31, 2023)
months.append("Agosto", 31, 2023)
months.append("Septiembre", 30, 2023)
months.append("Octubre", 31, 2023)
months.append("Noviembre", 30, 2023)
months.append("Diciembre", 31, 2023)

months.display(0, 2023)
