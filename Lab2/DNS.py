import dns.resolver

def dns_lookup():
    try:
        d = "example.com"

        print("A Records:")
        for r in dns.resolver.resolve(d, "A"):
            print(r)

        print("\nMX Records:")
        for r in dns.resolver.resolve(d, "MX"):
            print(r)

        print("\nCNAME Records:")
        try:
            for r in dns.resolver.resolve(d, "CNAME"):
                print(r)
        except:
            print("No CNAME found")

    except Exception as e:
        print("Error:", e)

dns_lookup()
