def atm(request):
    while request>0:
        while request>=100:
            print 100
            request-=100
        while request>=50:
            print 50
            request-=50
        while request>=10:
            print 10
            request-=10
        while request>=5:
            print 5
            request-=5
        if request>0:
            print request
        request-=request
atm()