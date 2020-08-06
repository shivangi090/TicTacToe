from random import randint
import sys
class tictactoe:
    def __init__(self):
        self.l=list(range(1,10))
        self.dashboard(self.l)
        print("Player 1's symbol=x\nCPU's symbol=o")
        print("-------------------------")
        self.playgame(self.li)
    def dashboard(self,ind):
        self.li=ind
        print("""
                {}|{}|{}
                -------
                {}|{}|{}
                -------
                {}|{}|{}""".format(self.li[0],self.li[1],self.li[2],self.li[3],self.li[4],self.li[5],self.li[6],self.li[7],self.li[8]))
        
    def playgame(self,l):
        n=9
        c=None
        while n!=1 and c==None:
            a=int(input("Choose your index or the number that has not been chosen before"))
            print("-------------------------")
            if a in l:
                l[a-1]="x"
                self.dashboard(l)
                c=self.checkmate(l)
                if c==False:
                    print("Player1 is the winner")
                    sys.exit()
                print("Remaining numbers are",l)
                print("-------------------------")
            else:
                continue
            cpu=randint(1,9)
            while cpu not in l or cpu==a:
                cpu=randint(1,9)
            print("CPU chose=",cpu)
            print("-------------------------")
            l[cpu-1]="o"
            self.dashboard(l)
            c=self.checkmate(l)
            if c==False:
                print("CPU is the winner")
                sys.exit()
            print("Remaining numbers are",l)
            print("-------------------------")
            n-=2
    def checkmate(self,l):
        self.l=l
        #horizontal checking
        if self.l[0]==self.l[1]==self.l[2]=="x" or self.l[3]==self.l[4]==self.l[5]=="x" or self.l[6]==self.l[7]==self.l[8]=="x":
            return False
        if self.l[0]==self.l[1]==self.l[2]=="o" or self.l[3]==self.l[4]==self.l[5]=="o" or self.l[6]==self.l[7]==self.l[8]=="o":
            return False
        #vertical
        if self.l[0]==self.l[6]==self.l[3]=="x" or self.l[1]==self.l[4]==self.l[7]=="x" or self.l[2]==self.l[5]==self.l[8]=="x":
            return False
        if self.l[0]==self.l[6]==self.l[3]=="o" or self.l[1]==self.l[4]==self.l[7]=="o" or self.l[2]==self.l[5]==self.l[8]=="o":
            return False
        #left diagonal
        if self.l[0]==self.l[4]==self.l[8]=="x":
            return False
        if self.l[0]==self.l[4]==self.l[8]=="o":
            return False
        #right diagonal
        if self.l[2]==self.l[4]==self.l[6]=="x":
            return False
        if self.l[2]==self.l[4]==self.l[6]=="o":
            return False

        

game=tictactoe()
        
