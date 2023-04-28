# a = user input (price)             k = remainder of division 1
# b = amount of two euro coins       l = remainder of division 2
# c = amount of one euro coins       m = remainder of division 3
# d = amount of 50 cent coins        n = remainder of division 4
# e = amount of 20 cent coins        o = remainder of division 5
# f = amount of 10 cent coins        p = remainder of division 6
# g = amount of 5 cent coins         q = remainder of division 7
# h = amount of 2 cent coins
# i = amount of 1 cent coins




active = True

while active:


    print("\nEnter a price in cents to see how you can pay")
    print("in the most efficient way possible.\n")
    prompt = input("type 's' to start \ntype 'q' to quit\n\n")

    if prompt.lower() == 'q':
        
        active = False

    elif prompt.lower() == 's':

        amount = input("\nPlease enter price(in cents): ")


        a=int(amount)
        b=int(a)//200
        k=int(a)-int(b)*200
        c=int(k)//100
        l=int(k)-int(c)*100
        d=int(l)//50
        m=int(l)-int(d)*50
        e=int(m)//20
        n=int(m)-int(e)*20
        f=int(n)//10
        o=int(n)-int(f)*10
        g=int(o)//5
        p=int(o)-int(g)*5
        h=int(p)//2
        q=int(p)-int(h)*2
        i=int(q)//1  

            

        print(  "\n\tamount of coins:\n")
        print(          "2euros: \t",b)
        print(         "1euros: \t", c)
        print(        "50cents: \t", d)
        print(        "20cents: \t", e)
        print(        "10cents: \t", f)
        print(         "5cents: \t", g)
        print(         "2cents: \t", h)
        print(         "1cents: \t", i, "\n")
