import urllib

results={}
nf = 'Address not Found'
url = ['https://google.in','https://vmware.com','https://amazon.in','https://google.in','https://adityankn.com']
for link in url:
    try:
        status = urllib.urlopen(link).getcode()
        if link not in results:
            results[link]=[status]
        else:
            results.setdefault(link, []).append(status)
  
    except:
        results.setdefault(link, []).append(nf)

print results

